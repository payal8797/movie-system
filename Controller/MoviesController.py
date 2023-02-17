from Service.MoviesServices import *

class MoviesController:
    @staticmethod
    def getGenres():
        try:
            cache_key = f"allGenres"
            data = redis_conn.get(cache_key)
            if data is not None:
                genresList = pickle.loads(data)
            else:
                genresList = MoviesService.getGenres(cache_key)
            return genresList
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @staticmethod
    def getMovies(request):
        try:
            page = request.args.get('page', 1, type=int)
            cache_key = f"allMovies:{page}"
            data = redis_conn.get(cache_key)
            if data is not None:
                movieList = pickle.loads(data)
            else:
                movieList = MoviesService.getMovies(page, cache_key)
            return movieList
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
     
    @staticmethod   
    def searchMovie(request):
        try:
            title = request.args.get('title', '')
            page = request.args.get('page', 1, type=int)
            cache_key = f"searchResults:{title}&{page}"
            data = redis_conn.get(cache_key)
            if data is not None:
                searchResults = pickle.loads(data)
            else:
                searchResults = MoviesService.searchMovie(title, page, cache_key)
            return searchResults
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @staticmethod
    def top10MoviesByGenre(request):
        try:
            genresList = request.args.getlist('genresList[]')
            genresList = tuple(genresList)
            cache_key = f"top10MoviesByGenre:{genresList}"
            data = redis_conn.get(cache_key)
            if data is not None:
                top10movies = pickle.loads(data)
            else:
                top10movies = MoviesService.top10MoviesByGenre(genresList, cache_key)
            return top10movies
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @staticmethod
    def similarUsers(request):
        try:
            page = request.args.get('page', 1, type=int)
            group_no = request.args.get('group_no', '')
            cache_key = f"similarUsers:{group_no}&{page}"
            data = redis_conn.get(cache_key)
            if data is not None:
                similarUsers = pickle.loads(data)
            else:
                similarUsers = MoviesService.similarUsers(page, group_no, cache_key)
            return similarUsers
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500    
        
    @staticmethod
    def recommendMovie(request):
        try:
            userid = request.args.get('userid', '')
            cache_key = f"recommendMovie:{userid}"
            data = redis_conn.get(cache_key)
            if data is not None:
                recommendMovie = pickle.loads(data)
            else:
                recommendMovie = MoviesService.recommendMovie(userid, cache_key)
            return recommendMovie
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500    
        
        