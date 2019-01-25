# Ireporter
[![Build Status](https://travis-ci.org/66hakeem/ireporter-db.svg?branch=feedback)](https://travis-ci.org/66hakeem/ireporter-db)

[![Coverage Status](https://coveralls.io/repos/github/66hakeem/ireporter-db/badge.svg?branch=feedback)](https://coveralls.io/github/66hakeem/ireporter-db?branch=feedback)

[![Maintainability](https://api.codeclimate.com/v1/badges/a05b04a92d0f954a9873/maintainability)](https://codeclimate.com/github/66hakeem/ireporter-db/maintainability)

iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

##Languages and Tools Used
* [Python 3.6](https://www.python.org)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://www.heroku.com/)
* [Coveralls](https://coveralls.io/)
* [Code Climate](https://codeclimate.com/)

## Installation

### create a virtual environment:

```
virtualenv ivenv
```

### Activate the virtual environment:

```
ivenv\scripts\activate
```

### Install requirements from the requirements.txt file:

```
pip install -r requirements.txt
```

### Run the Application:

```
python run.py
```


## Endpoints in the API

|REQUEST TYPE| URL | DESCRIPTION |
|------------|-----|-------------|
|POST| /api/v1/users |Register a new User
|POST| /api/v1/users |Get all users
|POST| /api/v1/red_flags |Create a red flag|
|GET| /api/v1/red_flags |Get all red flags|
|GET| /api/v1/red_flags/<int:red_flag_id> |Get specific red flag|
|DELETE| /api/v1/red_flags/<int:red_flag_id>|Delete a specific red flag|
|PATCH| /api/v1/red-flags/<int:red_flag_id>/location |Update location of a red flag incident|
|PATCH| /api/v1/red-flags/<int:red_flag_id>/comment |Update comment of a red flag incident|
|PUT| /api/v1/red-flags/<int:red_flag_id> |Edit any field location of a red flag incident|



## Deployment

Application is deployed using Heroku.

https://ireportercapt-api-heroku.herokuapp.com/api/v1/red_flags/)
