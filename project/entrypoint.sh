#!/bin/sh

python3 manage.py makemigrations
python3 manage.py migrate
uwsgi --socket :8000 --module project.wsgi -b 30000

exec "$@"