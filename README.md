# URL-Short

Url shortener, builded with Flask.

## Requirements

* Python 3.8.6
* A virtual environment

## Installation

Install with pip:

```#!/bin/bash
pip install -r requirements.txt
```

## Flask Configuration

### Create a .env file in the project root with the next configurations:

```env
SECRET_KEY=Your Secret Key, example: 23432
DATABASE_URL=sqlite:///shorty.db
APP_SETTINGS=config.DevelopmentConfig
FLASK_APP=core
FLASK_ENV=development
```

## Run Flask

### Run flask for develop

```#!/bin/bash
flask db init
flask run
```

In flask, Default port is `5000`

## Reference

Offical Website

* [Flask](http://flask.pocoo.org/)
* [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
* [gunicorn](http://gunicorn.org/)