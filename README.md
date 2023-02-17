# movie-system

Resources:
    https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    https://www.postgresql.org/docs/
    https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/
    https://chat.openai.com/chat
    https://www.w3schools.com/bootstrap5/
    https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

Steps to run:
    Setup up database and change db info in database
    Command: flask --app .\App.py --debug run

Queries:
- View a list of movies (ideally paged).
- Search for a movie by title or part of the title.
- Search for the best rated films by genre (eg TOP10 comedies). Consider the number of ratings and the value itself.
- Find users who have the same taste (users who rate the same movies similarly).
- Recommend the movie (according to the similarity in ratings, not rated by the user so far) to the given user