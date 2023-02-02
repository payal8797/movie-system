from Database.Database import db
from sqlalchemy import Column, String, Integer

class genres(db.Model):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    genres = Column(String)
    def __init__(self, id, genres):
        self.id = id
        self.genres = genres
