from Model.MoviesModel import *
from flask import jsonify, request
from sqlalchemy.orm import joinedload
import pickle
import redis
import json
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
        # print("topmovies", topMovies)
        return topMovies
    
    def getMovies(self, request):
        try:
            page = request.args.get('page', 1, type=int)
            cache_key = f"allMovies:{page}"
            per_page = 20
            data = redis_conn.get(cache_key)
            if data is not None:
                movieList = pickle.loads(data)
            else:
                movieList  =  movies_ratings_view.query.options(joinedload(movies_ratings_view.movies_genres_mapping_2)).paginate(page = page, per_page = per_page)
                movieList = self.movieListToDict(movieList)
                redis_conn.set(cache_key, pickle.dumps(movieList))
            return movieList
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def searchMovie(self, request):
        try:
            title = request.args.get('title', '')
            page = request.args.get('page', 1, type=int)
            per_page = 20
            cache_key = f"searchResults:{title}&{page}"
            data = redis_conn.get(cache_key)
            if data is not None:
                searchResults = pickle.loads(data)
            else:
                searchResults = movies_ratings_view.query.filter(movies_ratings_view.title.ilike('%{}%'.format(title))).options(joinedload(movies_ratings_view.movies_genres_mapping_2)).paginate(page = page, per_page = per_page)
                searchResults = self.movieListToDict(searchResults)
                redis_conn.set(cache_key, pickle.dumps(searchResults))
            return searchResults
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def getGenres(self):
        try:
            cache_key = f"allGenres"
            data = redis_conn.get(cache_key)
            if data is not None:
                genresList = pickle.loads(data)
            else:
                genresList = genres.query.all()
                redis_conn.set(cache_key, pickle.dumps(genresList))
            return genresList
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def top10MoviesByGenre(self, request):
        try:
            genresList = request.args.getlist('genresList[]')
            genresList = tuple(genresList)
            cache_key = f"top10MoviesByGenre:{genresList}"
            # data = redis_conn.get(cache_key)
            # if data is not None:
            #     top10movies = pickle.loads(data)
            # else:
            #     redis_conn.set(cache_key, pickle.dumps(top10movies))
            top10movies = movies_ratings_view.query.filter(movies_ratings_view.movies_genres_mapping_2.any(genres.genre_name.in_(genresList)),movies_ratings_view.count_rating >=1000).options(joinedload(movies_ratings_view.movies_genres_mapping_2)).all()
            top10movies = self.getTopMovies(top10movies)
            return top10movies
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    # def similarUsers(self, request):
    #     try:
    #         title = request.get("title")
    #         return MoviesModel.similarUsers(title)
    #     except:
    #         pass
            
        
        
MoviesService=MoviesService() 