# from Database.Database import db
# from sqlalchemy import Column, ForeignKey, String, Integer, Table
# from sqlalchemy.orm import relationship

# # class moviesGenres(db.Model):
# #     __tablename__ = "movies_genres"
# #     id = Column(Integer, primary_key=True)
# #     movieid = Column(String, db.ForeignKey('movies_ratings.movieid'))
# #     genres = Column(String, db.ForeignKey('genres.id'))
# #     def __init__(self, id, genres, movieid):
# #         self.id = id
# #         self.movieid = movieid
# #         self.genres = genres

# moviesGenres = Table('movies_genres', db.metadata,
#     Column('movieid', Integer, db.ForeignKey('movies_ratings.movieid')),
#     Column('genres', Integer, db.ForeignKey('genres.id'))
# )