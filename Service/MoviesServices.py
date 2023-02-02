from Model.MoviesModel import *
from Model.GenresModel import genres
from Model.MoviesRatingsModel import moviesRatingsModel
from flask import jsonify

class MoviesService():
    def __init__(self) -> None:
        pass
    
    def getGenres(self):
        try:
            genresList = genres.query.all()
            return genresList
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def getMovies(self):
        try:
            movieList = moviesRatingsModel.query.all()
            return movieList
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def searchMovie(self, request):
        try:
            title = request.get("title")
            if (len(title)>0):
                return MoviesModel.searchMovie(title)
            else:
                return MoviesModel.searchMovie('')
        except:
            pass
        
    def top10Movies(self, request):
        try:
            genres = request.get("genres")
            return MoviesModel.top10Movies(genres)
        except:
            pass
    
    def similarUsers(self, request):
        try:
            title = request.get("title")
            return MoviesModel.similarUsers(title)
        except:
            pass
            
        
        
MoviesService=MoviesService() 