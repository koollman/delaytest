#!/bin/sh

PORT=5000
FLASK_APP=delaytest.py
FLASK_ENV=development

. ~/venv-flask/bin/activate
export FLASK_APP FLASK_ENV
flask run -h 0.0.0.0 -p $PORT
