from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
import os
from datetime import datetime

import json
from auth.auth import requires_auth, AuthError
from models import drop_and_create, setup_db, Actor, Movie
from flask_cors import CORS

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

# Uncomment it only the first run
  # drop_and_create()


  @app.route('/')
  def main():
    return "Casting Agency"


  # Endpoints related to Actors (get, create, update, delete)

  @app.route('/actors', methods=['GET'])
  @requires_auth("get:actors")
  def get_actors(jwt):
    actors = Actor.query.all()
    actors_format = [actor.short() for actor in actors]
    return jsonify({
      "success": True,
      "actors":actors_format,
      "total_number_of_actors":len(actors)
    }),200

  @app.route('/actors/<int:id>', methods=['GET'])
  @requires_auth("get:actor-info")
  def get_actor_by_id(jwt,id):

    actor = Actor.query.filter(Actor.id==id).one_or_none()
    if actor is None:
      abort(404)
    movie = Movie.query.filter_by(id=actor.movie_id).one_or_none()
    if movie is None:
      title = ""
    else:
      title = movie.title


    return jsonify({
      "success": True,
      "actor":actor.full(),
      "movie":title
    }),200

  @app.route('/actors', methods=['POST'])
  @requires_auth("post:actor")
  def create_actor(jwt):
    try:
      body = request.get_json()
      name = body.get("name")
      age = body.get("age")
      gender = body.get("gender")
      movie_id = body.get("movie_id")
      actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)
      actor.insert()
      return jsonify({
        "success":True,
        "actor":actor.short()
      }),200
    except:
      abort(422)

  @app.route('/actors/<int:id>', methods=['DELETE'])
  @requires_auth("delete:actor")
  def delete_actor(jwt,id):
    try:

      actor = Actor.query.filter(Actor.id==id).one_or_none()
      if actor is None:
        abort(404)

      actor.delete()
      return jsonify({
        "success":True,
        "deleted":id
      }),200

    except:
      abort(422)


  @app.route('/actors/<int:id>', methods=['PATCH'])
  @requires_auth("patch:actor")
  def update_actor(jwt,id):

    try:
      body = request.get_json()
      name = body.get("name",None)
      age = body.get("age",None)
      gender = body.get("gender",None)
      movie_id = body.get("movie_id", None)

      actor = Actor.query.filter(Actor.id==id).one_or_none()
      if actor is None:
        abort(404)
      if name is not None:
        actor.name = name
      if age is not None:
        actor.age = age
      if gender is not None:
        actor.gender = gender
      if movie_id is not None:
        actor.movie_id = movie_id

      actor.update()
      return jsonify({
        "success":True,
        "actor":actor.full()
      }),200
    except:
      abort(400)




  # Endpoints related to Movies (get, create, update, delete)

  @app.route('/movies', methods=['GET'])
  @requires_auth("get:movies")
  def get_movies(jwt):
    movies = Movie.query.all()
    movies_format = [movie.short() for movie in movies]
    return jsonify({
      "success":True,
      "movies":movies_format,
      "total_number_of_movies":len(movies)
    })

  @app.route('/movies/<int:id>', methods=['GET'])
  @requires_auth("get:movie-info")
  def get_movie_by_id(jwt,id):
    movie = Movie.query.filter(Movie.id==id).one_or_none()
    if movie is None:
      abort(404)
    return jsonify({
      "success":True,
      "movie":movie.full()
    })

  @app.route('/movies', methods=['POST'])
  @requires_auth("post:movie")
  def create_movie(jwt):
    try:
      body = request.get_json()
      title = body.get("title")
      release_date = body.get("release_date")
      movie = Movie(title=title, release_date=datetime.strptime(release_date,'%d-%m-%Y'))
      movie.insert()
      return jsonify({
        "success":True,
        "movie":movie.full()
      }),200
    except:
      abort(422)

  @app.route('/movies/<int:id>', methods=['DELETE'])
  @requires_auth("delete:movie")
  def delete_movie(jwt,id):

    try:
      movie = Movie.query.filter(Movie.id==id).one_or_none()
      if movie is None:
        abort(404)

      movie.delete()
      return jsonify({
        "success":True,
        "deleted":id
      }),200
    except:
      abort(422)

  @app.route('/movies/<int:id>', methods=['PATCH'])
  @requires_auth("patch:movie")
  def update_movie(jwt,id):
    try:
      body = request.get_json()
      title = body.get("title")
      release_date = body.get("release_date")

      movie = Movie.query.filter(Movie.id==id).one_or_none()

      if movie is None:
        abort(404)
      if title is not None:
        movie.title = title
      if release_date is not None:
        movie.release_date = datetime.strptime(release_date,'%d-%m-%Y')

      movie.update()
      return jsonify({
        "success":True,
        "movie":movie.full()
      }),200
    except:
      abort(400)





  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
    }), 422

  @app.errorhandler(404)
  def not_found(error):
    return (jsonify({
      "success":False,
      "error":404,
      "message":"The requested resource doesn't exist."
    }), 404)

  @app.errorhandler(405)
  def not_found(error):
    return (jsonify({
      "success":False,
      "error":405,
      "message":"Method Not Allowed."
    }), 405)

  @app.errorhandler(400)
  def not_found(error):
    return (jsonify({
      "success":False,
      "error":400,
      "message":"Bad Request."
    }), 400)

  @app.errorhandler(AuthError)
  def auth_error(error):
    return (jsonify(error.error), error.status_code)

  return app

app = create_app()

if __name__=="__main__":
  app.debug = True
  app.run()
