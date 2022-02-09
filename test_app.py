
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie
from datetime import date

class CastingAgencyTestCase(unittest.TestCase):


  def setUp(self):

    self.assistent_token = os.environ['ASSISTENT_TOKEN']
    self.director_token = os.environ['DIRECTOR_TOKEN']
    self.producer_token = os.environ['PRODUCER_TOKEN']
    self.expired_token = os.environ['EXPIRED_TOKEN']
    self.app = create_app()
    self.client = self.app.test_client
    self.database_path = os.environ['TEST_DATABASE_URI']
    setup_db(self.app, self.database_path)

    with self.app.app_context():
      self.db = SQLAlchemy()
      self.db.init_app(self.app)
      self.db.create_all()

    self.new_actor = {
      "name":"Leonardo DiCaprio",
      "age":48,
      "gender":"Male"
    }
    self.new_movie = {
      "title":"Matrisa",
      "release_date":"05-05-2022"
    }

  def tearDown(self):
    pass

  def test_get_actors(self):
    res = self.client().get('/actors', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code,200)
    self.assertEqual(data['success'],True)
    self.assertTrue(data['total_number_of_actors'])

  def test_401_without_header(self):
    res = self.client().get('/actors')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertEqual(data['code'], "authorization_header_missing")
    self.assertEqual(data['description'], "Authorization header is expected.")



  def test_get_actor_by_id(self):
    res = self.client().get('/actors/1', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'],True)
    self.assertTrue(len(data['actor']))

  def test_404_if_actor_does_not_exist(self):
    res = self.client().get('/actors/100', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], "The requested resource doesn't exist.")


  def test_create_actor(self):
    res = self.client().post('/actors', headers={'Authorization': "Bearer {}".format(self.producer_token)}, json=self.new_actor)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['actor']))

  def test_405_if_actor_creation_not_allowed(self):
    res = self.client().post('/actors/100', headers={'Authorization': "Bearer {}".format(self.producer_token)},json=self.new_actor)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 405)
    self.assertEqual(data['success'], False)
    self.assertTrue(data['message'], "Method Not Allowed.")

  def test_403_create_without_permission(self):
    res = self.client().post('/actors', headers={'Authorization': "Bearer {}".format(self.assistent_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 403)
    self.assertEqual(data['code'], "unauthorized")
    self.assertEqual(data['description'], "Permission not found.")


  def test_delete_actor(self):
    res = self.client().delete('/actors/4', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    actor = Actor.query.filter(Actor.id==4).one_or_none()

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['deleted'])
    self.assertEqual(actor, None)

  def test_422_if_actor_does_not_axist(self):
    res = self.client().delete('/actors/1000', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 422)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], "unprocessable")

  def test_update_actor(self):
    res = self.client().patch('/actors/1',headers={'Authorization': "Bearer {}".format(self.producer_token)} ,json={"age":40})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['actor']))

  def test_400_for_failed_update_actor(self):
    res = self.client().patch('/actors/1', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], "Bad Request.")


  #Movies
  def test_get_movies(self):
    res = self.client().get('/movies', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['movies']))

  def test_get_movie_by_id(self):
    res = self.client().get('/movies/1', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'],True)
    self.assertTrue(len(data['movie']))

  def test_404_if_movie_does_not_exist(self):
    res = self.client().get('/movies/100', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], "The requested resource doesn't exist.")

  def test_create_movie(self):
      res = self.client().post('/movies', headers={'Authorization': "Bearer {}".format(self.producer_token)}, json=self.new_movie)
      data = json.loads(res.data)

      self.assertEqual(res.status_code, 200)
      self.assertEqual(data['success'], True)
      self.assertTrue(len(data['movie']))

  def test_405_if_movie_creation_not_allowed(self):
    res = self.client().post('/movies/100',headers={'Authorization': "Bearer {}".format(self.producer_token)} ,json=self.new_movie)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 405)
    self.assertEqual(data['success'], False)
    self.assertTrue(data['message'], "Method Not Allowed.")


  def test_delete_movie(self):
    res = self.client().delete('/movies/3', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    movie = Movie.query.filter(Movie.id==3).one_or_none()

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['deleted'])
    self.assertEqual(movie, None)

  def test_delete_movie_director(self):
    res = self.client().delete('/movies/3', headers={'Authorization': "Bearer {}".format(self.director_token)})
    data = json.loads(res.data)


    self.assertEqual(res.status_code, 403)
    self.assertEqual(data['code'], "unauthorized")
    self.assertEqual(data['description'], "Permission not found.")

  def test_422_if_movie_does_not_axist(self):
    res = self.client().delete('/movies/1000', headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 422)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], "unprocessable")


  def test_update_movie(self):
    res = self.client().patch('/movies/1', headers={'Authorization': "Bearer {}".format(self.producer_token)}, json={"release_date":"3-6-2022"})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['movie']))

  def test_400_for_failed_update_movie(self):
    res = self.client().patch('/movies/1',headers={'Authorization': "Bearer {}".format(self.producer_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], "Bad Request.")

  def test_401_send_request_with_expired_token(self):
    res = self.client().get('/movies',headers={'Authorization': "Bearer {}".format(self.expired_token)})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertEqual(data['code'], "token_expired")
    self.assertEqual(data['description'], "Token expired.")








if __name__=="__main__":
  unittest.main()