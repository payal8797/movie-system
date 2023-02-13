from Database.Database import db, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Table

movies_genres = Table('movies_genres', db.metadata,
    Column('movie_id', Integer, db.ForeignKey('movies_ratings.movieid')),
    Column('genre_id', Integer, db.ForeignKey('genres.id'))
)

class genres(db.Model):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    genre_name = Column(String)
    movies_genres_mapping_1 = relationship("movies_ratings_view", secondary= movies_genres, back_populates="movies_genres_mapping_2")
    def __init__(self, id, genre_name):
        self.id = id
        self.genre_name = genre_name
        
movies_ratings = Table('movies_ratings', db.metadata, autoload=True, autoload_with=engine)
class movies_ratings_view(db.Model):
    __table__ = movies_ratings  
    movies_genres_mapping_2 = relationship("genres", secondary= movies_genres,back_populates="movies_genres_mapping_1")
    __mapper_args__ =   {
                        'primary_key' :[movies_ratings.columns.movieid], 
                        }
    
class top10MoviesByGenre():
    pass
