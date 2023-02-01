from sqlalchemy import create_engine

def get_engine():
    return create_engine('postgresql://postgres:root@127.0.0.1:5432/movie_recommendation_system')
