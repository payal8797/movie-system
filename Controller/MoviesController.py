from Service.MoviesServices import *

class MoviesController():
    def __init__(self) -> None:
        pass
    
    def getGenres():
        try:
            return MoviesService.getGenres()
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    
    def getMovies():
        try:
            return MoviesService.getMovies()
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def searchMovie(request):
        try:
            return MoviesService.searchMovie(request)
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def top10Movies(request):
        try:
            # return request
            return MoviesService.top10Movies(request)
        except:
            pass
    
    def similarUsers(request):
        try:
            # return request
            return MoviesService.similarUsers(request)
        except:
            pass    
        
        