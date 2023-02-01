import os
import psycopg2
from psycopg2.extras import RealDictCursor


class Database():
    def __init__(self) -> None:
        pass
    
    def database(self, query):
        try:
            connection = psycopg2.connect(
                host="localhost",
                port="5432",
                database="movie_recommendation_system",
                user='postgres',
                password='root',
                cursor_factory=RealDictCursor
                )

            # Open a cursor to perform database operations
            cur = connection.cursor()
            cur.execute(query)

            return cur.fetchall()

            
        except:
            pass
        
        
Database = Database()