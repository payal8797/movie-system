from Service.MoviesServices import *

class MoviesController:
    @staticmethod
    def getGenres():
        try:
            return MoviesService.getGenres()
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @staticmethod
    def getMovies(request):
        try:
            return MoviesService.getMovies(request)
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
     
    @staticmethod   
    def searchMovie(request):
        try:
            return MoviesService.searchMovie(request)
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @staticmethod
    def top10MoviesByGenre(request):
        try:
            return MoviesService.top10MoviesByGenre(request)
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def similarUsers(request):
        try:
            # return request
            return MoviesService.similarUsers(request)
        except:
            pass    
        
        