from sqlalchemy import func
from Model.MoviesModel import *
from flask import jsonify, request
from sqlalchemy.orm import joinedload
import pickle
import redis
import json
import pandas as pd
from sklearn.cluster import KMeans
import csv


# Connect to Redis
redis_conn = redis.Redis(host='localhost', port=6379, db=0)


class MoviesService():
    def __init__(self) -> None:
        pass

    def movieListToDict(self, movieList):
        pagination_dict = {}
        pagination_dict['has_prev'] = movieList.has_prev
        pagination_dict['prev_num'] = movieList.prev_num
        pagination_dict['iter_pages'] = list(movieList.iter_pages())
        pagination_dict['page'] = movieList.page
        pagination_dict['has_next'] = movieList.has_next
        pagination_dict['next_num'] = movieList.next_num
        pagination_dict['movieData'] = movieList.items
        return pagination_dict

    def getTopMovies(self, top10movies):
        topMovies = []
        for movieData in top10movies:
            temp = movieData.__dict__
            c = 3.53
            m = 1000
            r = movieData.avg_rating
            v = movieData.count_rating
            calculatedValue = (v / (v + m)) * r + (m / (v + m)) * c
            temp['calculatedValue'] = calculatedValue
            topMovies.append(temp)
        topMovies = sorted(topMovies, key= lambda item: item['calculatedValue'], reverse=True)
        topMovies = topMovies[:10]
        return topMovies
    
    def getMovies(self, page, cache_key):
        try:
            per_page = 20
            movieList  =  movies_ratings_view.query.options(joinedload(movies_ratings_view.movies_genres_mapping_2)).paginate(page = page, per_page = per_page)
            movieList = self.movieListToDict(movieList)
            redis_conn.set(cache_key, pickle.dumps(movieList))
            return movieList
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def searchMovie(self, title, page, cache_key):
        try:            
            per_page = 20
            searchResults = movies_ratings_view.query.filter(movies_ratings_view.title.ilike('%{}%'.format(title))).options(joinedload(movies_ratings_view.movies_genres_mapping_2)).paginate(page = page, per_page = per_page)
            searchResults = self.movieListToDict(searchResults)
            redis_conn.set(cache_key, pickle.dumps(searchResults))
            return searchResults
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def getGenres(self, cache_key):
        try:
            genresList = genres.query.all()
            redis_conn.set(cache_key, pickle.dumps(genresList))
            return genresList
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def top10MoviesByGenre(self, genresList, cache_key):
        try:
            top10movies = movies_ratings_view.query.filter(movies_ratings_view.movies_genres_mapping_2.any(genres.genre_name.in_(genresList)),movies_ratings_view.count_rating >=1000).options(joinedload(movies_ratings_view.movies_genres_mapping_2)).all()
            top10movies = self.getTopMovies(top10movies)
            redis_conn.set(cache_key, pickle.dumps(top10movies))
            return top10movies
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def createDataFrameArray(self, allMovies):
        df_array = []
        if allMovies:
            for item in allMovies:
                df_array.append({
                    "movieid": item.movieid,
                    "userid": item.userid,
                    "title": item.title,
                    "rating": item.rating,
                    "genres": item.genres
                })
        return df_array
    
    def match_genre(self, row, genre):
        return 1 if genre in row['genres'] else 0

    #steps to create csv file with cluster number
    def kmeansImplmentation(self):
        allMovies = movies_user_ratings_view.query.filter(~movies_user_ratings_view.rating.between(1.5,3.5)).all()
        df_array = self.createDataFrameArray(allMovies)
        df = pd.DataFrame(df_array)
        genres_list = list(df['genres'].str.split('|', expand=True).stack().unique())
        for i in genres_list:
            df[i] = df.apply(lambda row: self.match_genre(row, i), axis=1)
        df_for_kmeans = df.drop(columns=['movieid', 'userid', 'title', 'genres']).fillna(0)
        # # Create model for KMeans
        kmeans = KMeans(n_clusters=20)
        # # Use dataset to fit the model
        kmeans.fit(df_for_kmeans)
        # The data must be assigned back to the input df to clearly see the groups
        df_for_kmeans['group'] = kmeans.labels_        
        final_df = df.join(df_for_kmeans.iloc[:,-1])
        final_df = final_df[['userid', 'movieid', 'rating', 'title', 'genres', 'group']]
        final_df.to_csv('cluster_allmovies.csv', index=False)
        
    def similarUsers(self, page, group_no, cache_key):
        try:
            per_page = 50
            similarUsers = movies_cluster_kmeans_view.query.filter(movies_cluster_kmeans_view.group_no == group_no).paginate(page = page, per_page = per_page)
            similarUsers = self.movieListToDict(similarUsers)
            redis_conn.set(cache_key, pickle.dumps(similarUsers))
            return similarUsers
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    def recommendMovie(self, userid, cache_key):
        try:
            top500MoviesOfUser = movies_cluster_kmeans_view.query.with_entities(func.unnest(func.string_to_array(movies_cluster_kmeans_view.genres, '|')).label('genre'), movies_cluster_kmeans_view).filter(movies_cluster_kmeans_view.userid == userid).order_by(movies_cluster_kmeans_view.rating.desc()).limit(500).all()
            # print(top500Movies)
            genre_counts = {}
            for genre, _ in top500MoviesOfUser:
                if genre in genre_counts:
                    genre_counts[genre] += 1
                else:
                    genre_counts[genre] = 1

            # sort the genre counts in descending order and select the top 3
            top_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:3]

            favGenres=[]
            # fetch the top genres
            for genre, _ in top_genres:
                favGenres.append(genre)
            favGenres = tuple(favGenres)
            
            #fetch movieid of that user
            watched=set()
            for movie_id in top500MoviesOfUser:
                watched.add(movie_id[1].movieid)
            # print(watched)

            #filter movies by user's fav genre
            topMovieByGenre = movies_ratings_view.query.filter(movies_ratings_view.movies_genres_mapping_2.any(genres.genre_name.in_(favGenres)), ~movies_ratings_view.movieid.in_(tuple(watched)),movies_ratings_view.count_rating >=1000).options(joinedload(movies_ratings_view.movies_genres_mapping_2)).all()
            recommendMovie = self.getTopMovies(topMovieByGenre)
            redis_conn.set(cache_key, pickle.dumps(recommendMovie))
            return recommendMovie
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
        
MoviesService=MoviesService() 