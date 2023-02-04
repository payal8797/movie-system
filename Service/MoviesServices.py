from Model.MoviesGenresModel import moviesGenres
from Model.GenresModel import genres
from Model.MoviesRatingsModel import moviesRatingsModel
from flask import jsonify, request

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
            page = request.args.get('page', 1, type=int)
            per_page = 25
            # print("huh")
            movieList  = moviesRatingsModel.query.all()
            # print("de",movieList)
            # exit()
            return movieList
        except AttributeError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def searchMovie(self, request):
        try:
            page = request.get('page', 1, type=int)
            per_page = 25
            title = request.get("title")
            # print("title", title)
            # exit()
            if (title):
                return moviesRatingsModel.query.filter(moviesRatingsModel.title.ilike('%{}%'.format(title))).paginate(page = page, per_page = per_page)
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