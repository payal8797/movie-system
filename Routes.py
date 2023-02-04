from flask import Flask,jsonify, render_template, request
from Database.Database import db
# from Controller.MoviesController import *
from Model.MoviesRatingsModel import moviesRatingsModel
from sqlalchemy.orm import joinedload

# db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@127.0.0.1:5432/movie_recommendation_system'
db.init_app(app)

def to_dict(instance):
    result = {}
    for key in instance.__mapper__.c.keys():
        result[key] = getattr(instance, key)
    return result

def collection_to_dict(collection):
    return [to_dict(item) for item in collection]

@app.route("/movies")
def main():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 25
        header = 'ab'
        # moviesRatings = MoviesController.getMovies()
        moviesRatings  = moviesRatingsModel.query.options(joinedload(moviesRatingsModel.movies_genres_mapping_2)).paginate(page = page, per_page = per_page)
        # for movie in moviesRatings:
        #     for genreItem in movie.movies_genres_mapping_2:
        #         print(genreItem.genres)
        # exit()
        return render_template('moviesRatings.html', moviesRatings= moviesRatings, header = header)
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# @app.route("/genres")
# def genres():
#     try:
#         genreList = MoviesController.getGenres()
#         print(genreList)
#         exit()
#         # return render_template('genres.html', genres = genreList)
#     except AttributeError as e:
#         return jsonify({"error": str(e)}), 500
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route("/searchMovie", methods = ["GET"])
# def searchMovie():
#     try:
#         title = request.args.get('title', '')
#         header = "Search results with title: {}".format(title)
#         searchResults  = MoviesController.searchMovie(request.args)
#         return render_template('moviesRatings.html', moviesRatings = searchResults, header = header)
#     except AttributeError as e:
#         return jsonify({"error": str(e)}), 500
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

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


