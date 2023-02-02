
from flask import Flask,jsonify, render_template
from Database.Database import db
from Controller.MoviesController import *
from Model.MoviesRatingsModel import moviesRatingsModel

# db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@127.0.0.1:5432/movie_recommendation_system'
db.init_app(app)

@app.route("/")
def main():
    try:
        moviesRatings = MoviesController.getMovies()
        # print(moviesRatings)
        # exit()
        return render_template('moviesRatings.html', moviesRatings= moviesRatings)
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/genres")
def genres():
    try:
        genreList = MoviesController.getGenres()
        print(genreList)
        exit()
        # return render_template('genres.html', genres = genreList)
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# @app.route("/movies", methods = ["GET"])
# def movies():
#     try:
#         response  = MoviesController.getMovies(request.args)
#         return response
#     except Exception as e:
#         return e


# @app.route("/searchMovie", methods = ["GET"])
# def searchMovie():
#     try:
#         response  = MoviesController.searchMovie(request.args)
#         return response
#     except Exception as e:
#         return e
    
# @app.route("/top10Movies", methods = ["GET"])
# def top10Movies():
#     try:
#         response  = MoviesController.top10Movies(request.args)
#         return response
#     except Exception as e:
#         return e
    
# @app.route("/similarUsers", methods = ["GET"])
# def similarUsers():
#     try:
#         response  = MoviesController.similarUsers(request.args)
#         return response
#     except Exception as e:
#         return e


