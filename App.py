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
 
@app.route("/searchSimilarUsers", methods = ["GET"])
def searchSimilarUsers():
    try:
        return render_template('topRated.html')        
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
       
@app.route("/similarUsers", methods = ["GET"])
def similarUsers():
    try:
        group_no = request.args.get('group_no', '')
        header = "Search results with group_no: {}".format(group_no)
        moviesPaginationValue = 'similarUsers'
        searchPath = '&group_no={}'.format(group_no)
        similarUsers  = MoviesController.similarUsers(request)
        return render_template('similarUsers.html', similarUsers = similarUsers, header = header, moviesPaginationValue=moviesPaginationValue, searchPath = searchPath)
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/recommendation", methods = ["GET"])
def recommendation():
    try:
        return render_template('recommendMovie.html')        
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/recommendMovie", methods = ["GET"])
def recommendMovie():
    try:
        userid = request.args.get('userid', '')
        header = "Top recommended movies to userid: {}".format(userid)
        recommendMovie  = MoviesController.recommendMovie(request)
        # return recommendMovie
        return render_template('recommendMovie.html', moviesRatings = {"movieData":recommendMovie}, header = header )        
    except AttributeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500