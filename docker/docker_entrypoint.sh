#!/bin/bash

# if FLASK_ENV is set to development, then run the flask development server
if [ "$FLASK_ENV" = "development" ]; then
    flask run --host=0.0.0.0 -p 5000
else
    gunicorn --bind 0.0.0.0:5000 introducing.wsgi:app
fi