# from Database.Database import db
# from sqlalchemy import Column, String, Integer
# from sqlalchemy.orm import relationship
# from Model.MoviesGenresModel import *

# class genres(db.Model):
#     __tablename__ = "genres"
#     id = Column(Integer, primary_key=True)
#     genres = Column(String)
#     movies_genres_mapping_1 = relationship("moviesRatingsModel", secondary= moviesGenres, back_populates="movies_genres_mapping_2")
#     def __init__(self, id, genres):
#         self.id = id
#         self.genres = genres
