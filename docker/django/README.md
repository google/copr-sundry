# Django docker

Not intended to be used directly - build your own docker image on top of this one.

Put your app into /app.

Example final Dockerfile:

```docker
FROM vrusinov/django-build:latest as build

# Install additional requirements, e.g.:
RUN emerge -v dev-python/django-environ

FROM vrusinov/django:3.2.5


COPY --from=build /usr/lib/python3.8/site-packages/environ/ /usr/lib/python3.8/site-packages/environ/

COPY . /app

ENTRYPOINT ["/bin/entrypoint.sh"]
```

## Environment variables

*  DJANGO_SETTINGS_MODULE allows to pass `--settings` flag, e.g. 'config.settings.production'

## Ports

Listens on 0.0.0.0:8000, currently with no ability to override.

## Changelog

### 2022-01-23

* Upgraded to Django 3.2.6
* Upgraded to Python 3.9
* Use tag `3.2.6.2022-01-23`