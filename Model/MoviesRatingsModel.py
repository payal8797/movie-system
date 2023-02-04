from Database.Database import db, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String, Integer, Table

movies_genres = Table('movies_genres', db.metadata,
    Column('movieid', Integer, db.ForeignKey('movies_ratings.movieid')),
    Column('genres', Integer, db.ForeignKey('genres.id'))
)

class genres(db.Model):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    genres = Column(String)
    movies_genres_mapping_1 = relationship("moviesRatingsModel", secondary= movies_genres, back_populates="movies_genres_mapping_2")
    def __init__(self, id, genres):
        self.id = id
        self.genres = genres
        
movies_ratings = Table('movies_ratings', db.metadata, autoload=True, autoload_with=engine)
class moviesRatingsModel(db.Model):
    __table__ = movies_ratings  
    movies_genres_mapping_2 = relationship("genres", secondary= movies_genres,back_populates="movies_genres_mapping_1")
    __mapper_args__ =   {
                        'primary_key' :[movies_ratings.columns.movieid], 
                        }
