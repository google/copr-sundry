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
exec python manage.py runserver
