from flask import Flask,jsonify, render_template, request
from Database.Database import db
from Controller.MoviesController import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@127.0.0.1:5432/movie_recommendation_system'
db.init_app(app)

@app.route("/movies")
def main():
    try:
        header = 'List of all movies!!'
        moviesRatings = MoviesController.getMovies(request)
        moviesPaginationValue= 'main'
        searchPath=''
        return render_template('moviesRatings.html', moviesRatings= moviesRatings, header = header, moviesPaginationValue = moviesPaginationValue, searchPath=searchPath)
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/searchMovie", methods = ["GET"])
def searchMovie():
    try:
        title = request.args.get('title', '')
        header = "Search results with title: {}".format(title)
        moviesPaginationValue = 'searchMovie'
        searchResults  = MoviesController.searchMovie(request)
        searchPath = '&title={}'.format(title)
        return render_template('moviesRatings.html', moviesRatings = searchResults, header = header,moviesPaginationValue=moviesPaginationValue, searchPath = searchPath )
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/genres", methods = ["GET"])
def getGenres():
    try:
        genresList  = MoviesController.getGenres()
        return render_template('topRated.html', genresList = genresList)        
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/topMoviesByGenre", methods = ["GET"])
def topMoviesByGenre():
    try:
        genres = request.args.getlist('genresList[]')
        genresList  = MoviesController.getGenres()
        header = "Top 10 movies with genre(s): {}".format(genres)
        topMoviesByGenre  = MoviesController.top10MoviesByGenre(request)
        return render_template('topRated.html', moviesRatings = {"movieData":topMoviesByGenre}, header = header, genresList=genresList )
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# @app.route("/similarUsers", methods = ["GET"])
# def similarUsers():
#     try:
#         response  = MoviesController.similarUsers(request.args)
#         return response
#     except Exception as e:
#         return e


