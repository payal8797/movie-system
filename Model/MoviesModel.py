# from Database.Database import *


class MoviesModel():
    def __init__(self) -> None:
        pass
    
    def getMovies(self, limit=50, offset=0):
        try:
            query = "SELECT * FROM MOVIES LIMIT {} OFFSET {}".format(limit, offset)
            return Database.database(query)
        except:
            pass
    
    def searchMovie(self, title):
        try:
            query = "SELECT * FROM MOVIES WHERE title LIKE '%{}%'".format(title)
            return Database.database(query)
        except:
            pass
        
    def top10Movies(self, genres):
        try:
            query = "SELECT m.title, m.genres,  SUM(r.rating)*COUNT(userId) as rating_avg FROM movies m join ratings r ON m.movieId=r.movieId GROUP BY m.title, m.genres HAVING m.genres = '{}' ORDER BY rating_avg DESC LIMIT 10".format(genres)
            return Database.database(query)
        except:
            pass
    
    def similarUsers(self, title):
        try:
            query = "select title, userid, genres, rating from movies m join ratings r on m.movieId=r.movieId where title='{}' and rating > 3 ORDER BY rating DESC LIMIT 20".format(title)
            return Database.database(query)
        except:
            pass    
        
        
MoviesModel=MoviesModel() 