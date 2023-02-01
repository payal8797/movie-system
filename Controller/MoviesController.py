from Service.MoviesServices import *

class MoviesController():
    def __init__(self) -> None:
        pass
    
    def getMovies(request):
        try:
            return MoviesService.getMovies(request)
        except:
            pass
        
    def searchMovie(request):
        try:
            # return request
            return MoviesService.searchMovie(request)
        except:
            pass
    
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
        
        