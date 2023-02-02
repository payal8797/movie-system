from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()
engine = create_engine('postgresql://postgres:root@127.0.0.1:5432/movie_recommendation_system')
db.metadata.bind = engine

