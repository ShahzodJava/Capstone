from datetime import datetime
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String, Column, DateTime
from datetime import date

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()

def drop_and_create():
  db.drop_all()
  db.create_all()
  movie = Movie(
    title = "Iron Man",
    release_date = date(2022,2,25)
  )
  movie2 = Movie(
    title = "Scorpion King",
    release_date = date(2022,3,15)
  )
  movie3 = Movie(
    title = "Terminator",
    release_date = date(2022,4,6)
  )
  movie.insert()
  movie2.insert()
  movie3.insert()

  actor = Actor(
    name = "Dwayne Johnson",
    age = 50,
    gender = "Male",
    movie_id = 2
  )
  actor2 = Actor(
    name = "Scarlett Johansson",
    age = 38,
    gender = "Female",
    movie_id = 1
  )
  actor3 = Actor(
    name = "Robert Downey Jr.",
    age = 57,
    gender = "Male",
    movie_id = 1
  )
  actor4 = Actor(
    name = "Arnold Schwarzenegger",
    age = 75,
    gender = "Male",
    movie_id = 3
  )
  actor.insert()
  actor2.insert()
  actor3.insert()
  actor4.insert()



class Movie(db.Model):
  __tablename__ = "Movies"

  id = Column(Integer,primary_key = True)
  title = Column(String)
  release_date = Column(DateTime)
  actors = db.relationship('Actor', backref='movie')

  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

  def short(self):
    return {
      "id":self.id,
      "title":self.title
    }

  def full(self):
    return {
      "id":self.id,
      "title":self.title,
      "release_date":self.release_date.strftime("%b %d %Y"),
      "actors":[actor.name for actor in self.actors]
    }
# strftime("%b %d %Y %H:%M:%S")

  def insert(self):
    db.session.add(self)
    db.session.commit()
  def delete(self):
    db.session.delete(self)
    db.session.commit()
  def update(self):
    db.session.commit()

class Actor(db.Model):
  __tablename__ = "Actors"

  id  = Column(Integer, primary_key = True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)
  movie_id = Column(Integer, db.ForeignKey('Movies.id'))

  def __init__(self, name, age, gender, movie_id):
    self.name = name
    self.age = age
    self.gender = gender
    self.movie_id = movie_id

  def short(self):
    return {
      "id":self.id,
      "name":self.name
    }

  def full(self):

    return {
      "id":self.id,
      "name":self.name,
      "age":self.age,
      "gender":self.gender,

    }

  def insert(self):
    db.session.add(self)
    db.session.commit()
  def delete(self):
    db.session.delete(self)
    db.session.commit()
  def update(self):
    db.session.commit()
