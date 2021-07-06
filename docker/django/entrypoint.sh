#!/bin/bash

set -e
set -x

if ! test -d /app ; then
  echo "WARN: no app deployed to /app. Creating a sample."
  cd /
  django-admin startproject app
fi

cd /app
python manage.py migrate
ARGS=""
if ! [ -z $DJANGO_SETTINGS_MODULE] ; then
  echo "Using $DJANGO_SETTINGS_MODULE settings"
  ARGS="${ARGS} --settings ${DJANGO_SETTINGS_MODULE}"
fi
exec python manage.py runserver $ARGS
