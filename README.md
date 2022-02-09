# Casting Agency API
### Description
This is project is the final project for the Udacity Full Stack Wev Developer Nanodegree. The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. In this API I implemented third-party authentication with Role Based Access Control using Auth0.

### URL location for the hosted API
Heroku link [https://fsnp-capstone.herokuapp.com/](https://fsnp-capstone.herokuapp.com/)

### Pre-requisites
### Installing Dependencies
Developers using this project should already have postgresql, git, Python3, pip installed on their local machines.

### Virtual Environment
To create and activate virtual environment from the project folder in terminal run the following command:
```bash
python -m venv myvenv
source venv/Scripts/activate
```

Once you have activated virtual environment, install dependencies, run the following command:
```bash
pip install -r requirements.txt
```
### Environment variables
Setup environment variables , in setup.sh change DATABASE_URL, as applicable to you
run the following command in terminal:
```bash
source setup.sh
```

### Database Setup
Before running the app create database capstone in the PostgreSQL server
```bash
DROP DATABASE capstone;
CREATE DATABASE capstone;
```
Also uncomment the line in the **app.py** *drop_and_create()* on the initial run to setup the required tables in the database.

### Running Server
To run the application run following command :
```bash
# Run the app
python app.py
```

Accessing the output at  [http://127.0.0.1:5000/](http://127.0.0.1:5000/)



### Testing
Before running test create database capstone_test in the PostgreSQL server

```bash
DROP DATABASE capstone_test;
CREATE DATABASE capstone_test
WITH TEMPLATE capstone;
```

To run test_app , from the project folder in terminal run the following command:
```bash
python test_app.py
```

### Errors
Errors are returned as JSON objects in the following format:

```bash
{
    "success": False,
    "error": 405,
    "message": "Method Not Allowed."
}
```
The API will return following error types when requests fail:
- 400: Bad Request.
- 401: Unauthorized
- 403: Forbidden
- 404: The requested resource doesn't exist.
- 405: Method Not Allowed.
- 422: Unprocessable Entity.
- 500: Internal Server Error.

### Rol Based Access Controls
**Assistent** has the following permissions:
- get:actors
- get:actor-info
- get:movie
- get:movie-info

**Director** has the following permissions:
- All permissions **Assistent** has
- post:actor
- delete:actor
- patch:actor
- patch:movie

**Producer** has the following permissions:
- All permissions a**Director** has
- post:movie
- delete:movie

All valid tokens are in the setup.sh file.

### Endpoints
### Index /
**Response:**
  - Type: String
  - Body: `Casting Agency`

#### GET/actors
- General: Returns all actors, total number of actors and success value
- Sample: `https://fsnp-capstone.herokuapp.com/actors`

```bash
{
    "actors": [
        {
            "id": 1,
            "name": "Dwayne Johnson"
        },
        {
            "id": 2,
            "name": "Scarlett Johansson"
        },
        {
            "id": 3,
            "name": "Robert Downey Jr."
        },
        {
            "id": 4,
            "name": "Arnold Schwarzenegger"
        }
    ],
    "success": true,
    "total_number_of_actors": 4
}
```
#### GET/actors/<Int:id>
- General: Returns full information about an actor and success value
- Sample: `https://fsnp-capstone.herokuapp.com/actors/1`

```bash
{
    "actor": {
        "age": 50,
        "gender": "Male",
        "id": 1,
        "name": "Dwayne Johnson"
    },
    "movie": "Scorpion King",
    "success": true
}
```


#### GET/movies
- General: Returns all movies, total number of movies and success value
- Sample: `https://fsnp-capstone.herokuapp.com/movies`

```bash
{
    "movies": [
        {
            "id": 1,
            "title": "Iron Man"
        },
        {
            "id": 2,
            "title": "Scorpion King"
        },
        {
            "id": 3,
            "title": "Terminator"
        }
    ],
    "success": true,
    "total_number_of_movies": 3
}
```

#### GET/movies/<Int:Id>
- General: Returns full information about a movie and success value
- Sample: `https://fsnp-capstone.herokuapp.com/movies/1`

```bash
{
    "movie": {
        "actors": [
            "Scarlett Johansson",
            "Robert Downey Jr."
        ],
        "id": 1,
        "release_date": "Feb 25 2022",
        "title": "Iron Man"
    },
    "success": true
}
```

#### POST/actors
- General:
    - Creates new actor
    - Returns name,id of the created actor and success value
- Sample: `https://fsnp-capstone.herokuapp.com/actors`
- Request body
```bash
{
    "name":"Kelli Enn Xu",
    "age":"54",
    "gender":"Female",
    "movie_id":2
}
```

- Response:
```bash
{
    "actor": {
        "id": 5,
        "name": "Kelli Enn Xu"
    },
    "success": true
}
```
#### POST/movies
- General:
    - Creates new movie
    - Returns info about created movie and success value
- Sample: `https://fsnp-capstone.herokuapp.com/movies`
- Request body
```bash
{
    "title":"Matrix",
    "release_date":"05-05-2022"
}
```

- Response:
```bash
{
    "movie": {
        "actors": [],
        "id": 4,
        "release_date": "May 05 2022",
        "title": "Matrix"
    },
    "success": true
}
```
#### DELETE /actors/<int:id>
- General
    - Deletes the actor of the given ID if it exists
    - Returns the id of the deleted actor and success value
- Sample: `https://fsnp-capstone.herokuapp.com/actors/5`
```bash
{
    "deleted": 5,
    "success": true
}
```

#### DELETE /movies/<int:id>
- General
    - Deletes the movie of the given ID if it exists
    - Returns the id of the deleted movie and success value
- Sample: `https://fsnp-capstone.herokuapp.com/movies/4`
```bash
{
    "deleted": 4,
    "success": true
}
```
#### PATCH/actors/<int:id>
- General
    - Updates actor
    - Returns info acout actor and success value
- Sample: `https://fsnp-capstone.herokuapp.com/actors/4`
- Request body:
```bash
{
    "age":80
}
```
- Response:
```bash
{
    "actor": {
        "age": 80,
        "gender": "Male",
        "id": 4,
        "name": "Arnold Schwarzenegger"
    },
    "success": true
}
```

#### PATCH/movies/<int:id>
- General
    - Updates movie
    - Returns info about movie and success value
- Sample: `https://fsnp-capstone.herokuapp.com/movies/3`
- Request body:
```bash
{
    "title":"Terminator 2"
}
```
- Response:
```bash
{
    "movie": {
        "actors": [
            "Arnold Schwarzenegger"
        ],
        "id": 3,
        "release_date": "Apr 06 2022",
        "title": "Terminator 2"
    },
    "success": true
}
```


### Authors
I implemented this project and during this program I gained more than expected!. Thanks Udacity’s team! Shahzod Ashurmatov
