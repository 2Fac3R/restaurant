# CRM

Heroku App -> https://restaurant-edt-d4de15bcd927.herokuapp.com/restaurants/

This repository is a simple Restaurant RESTful API implementation in Django with Django Rest Framework.

## Installation

Clone this repository

    git clone https://github.com/2Fac3R/restaurant.git

Create and start your virtual environment [venv](https://docs.python.org/3/library/venv.html)

    python3 -m venv .venv
    source .venv/bin/activate

Install requirements. Use the package manager [pip](https://pip.pypa.io/en/stable/)

    pip install -r requirements.txt

Create and configure a new database in .env file (rename .env.example to .env)

    DATABASE_URL=postgresql://user:password@localhost:5432/database

Make migrations and migrate

    python3 manage.py makemigrations
    python3 manage.py migrate

Run the server

    python3 manage.py runserver

You can now access the API root at http://127.0.0.1:8000/restaurants/

## Browseable API

Restaurant List (view all, create a new one):

    http://127.0.0.1:8000/restaurants/restaurants/

Restaurant Instance (view, edit, delete)

    http://127.0.0.1:8000/restaurants/restaurants/<id>/

## API Testing

You can find two postman collection files (local, remote heroku app) in the root directory.

## API Documentation

    http://127.0.0.1:8000/restaurants/swagger/
    http://127.0.0.1:8000/restaurants/redoc/

## Tests

You can run all tests

    python3 manage.py test

## Description

I decided to use the following packages:

- [djangorestframework](https://www.django-rest-framework.org/) It's a powerful and flexible toolkit for building Web APIs.
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) Automated generation of real Swagger/OpenAPI 2.0 schemas from Django REST Framework code.
- [django-filter](https://django-filter.readthedocs.io/en/stable/) Reusable Django app allowing users to add dynamic QuerySet filtering from URL parameters.

You can find more details about others in _requirements.txt_ file.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Any feedback is appreciated.
