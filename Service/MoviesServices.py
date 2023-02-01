from Model.MoviesModel import *

class MoviesService():
    def __init__(self) -> None:
        pass
    
    def getMovies(self, request):
        try:
            limit = request.get("limit")
            offset = request.get("offset")
            return MoviesModel.getMovies(limit, offset)
        except:
            pass
        
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