from Database import db
from sqlalchemy import Engine, PrimaryKeyConstraint, Column, String, Integer, Double, MetaData, Table
from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import declarative_base
from engine import get_engine

# metadata = MetaData() 
Base = declarative_base()
engine = get_engine()

# view = Table('movies_ratings', Base.metadata, 
#              Column('id',Integer, primary_key=True),
#              Column('movieid', Integer), 
#              Column('title', String), 

#              Column('avg_rating', Double), 
#              Column('count_rating', Double), 
#              Column('sum_rating', Double))

class genreName(db.Model):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    genres = Column(String)
    def __init__(self, id, genres):
        self.id = id
        self.genres = genres

class viewModel(Base):
    # __tablename__ = "movies_ratings"  
    __table__ = Table('movies_ratings', MetaData(), autoload=True, autoload_with=engine)

    # __table__ = view
    # __bind_key__ = None
    # id = Column(Integer)
    # movieid = Column(Integer)
    # title = Column(String)
    # avg_rating = Column(Double)
    # count_rating = Column(Double)
    # sum_rating = Column(Double)
    # def __init__(self, movieid, title,avg_rating, count_rating, sum_rating ):
    #     # self.id = id
    #     self.movieid = movieid
    #     self.title = title        
    #     self.avg_rating = avg_rating  
    #     self.count_rating = count_rating      
    #     self.sum_rating = sum_rating

# registry.map_imperatively(viewModel,view)