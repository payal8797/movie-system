
from flask import Flask, request
from Database import db
from Controller.MoviesController import *
from Models import genreName, viewModel

# db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@127.0.0.1:5432/movie_recommendation_system'
db.init_app(app)

# def get_engine():
#     return create_engine('postgresql://postgres:root@127.0.0.1:5432/movie_recommendation_system')

@app.route("/")
def main():
    genresList = genreName.query.all()
    viewModelList = viewModel.query.first()
    print(viewModelList)
    # for genres in genresList:
    #     print(genres.genres)
    exit()

@app.route("/movies", methods = ["GET"])
def movies():
    try:
        response  = MoviesController.getMovies(request.args)
        return response
    except Exception as e:
        return e


@app.route("/searchMovie", methods = ["GET"])
def searchMovie():
    try:
        response  = MoviesController.searchMovie(request.args)
        return response
    except Exception as e:
        return e
    
@app.route("/top10Movies", methods = ["GET"])
def top10Movies():
    try:
        response  = MoviesController.top10Movies(request.args)
        return response
    except Exception as e:
        return e
    
@app.route("/similarUsers", methods = ["GET"])
def similarUsers():
    try:
        response  = MoviesController.similarUsers(request.args)
        return response
    except Exception as e:
        return e


