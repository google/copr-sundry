#!/bin/bash

set -e
set -x

if ! test -f /app/manage.py ; then
  echo "WARN: no app deployed to /app. Creating a sample."
  cd /app
  django-admin startproject app .
fi

cd /app
python manage.py migrate
ARGS=""
if ! [ -z $DJANGO_SETTINGS_MODULE ] ; then
  echo "Using $DJANGO_SETTINGS_MODULE settings"
  ARGS="${ARGS} --settings ${DJANGO_SETTINGS_MODULE}"
fi
python3 manage.py runserver 0.0.0.0:8000 $ARGS
