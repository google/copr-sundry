FROM vrusinov/django-build:3.2.6 as build

COPY group /etc/group
COPY passwd /etc/passwd

RUN mkdir -p /app
# hadolint ignore=DL3059
RUN chown django:django /app

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

FROM vrusinov/python3:3.9.2022-01-03

COPY group /etc/group
COPY passwd /etc/passwd

COPY --from=build /usr/bin/django* /usr/bin/
COPY --from=build /usr/lib/python-exec/python3.9/django* /usr/lib/python-exec/python3.9/
COPY --from=build /usr/lib/python3.9/site-packages/asgiref /usr/lib/python3.9/site-packages/asgiref
COPY --from=build /usr/lib/python3.9/site-packages/Django-3.2.6-py3.9.egg-info/ /usr/lib/python3.9/site-packages/Django-3.2.6-py3.9.egg-info/
COPY --from=build /usr/lib/python3.9/site-packages/django/ /usr/lib/python3.9/site-packages/django
COPY --from=build /usr/lib/python3.9/site-packages/pytz /usr/lib/python3.9/site-packages/pytz
COPY --from=build /usr/lib/python3.9/site-packages/sqlparse /usr/lib/python3.9/site-packages/sqlparse
COPY --from=build --chown=django:django /app /app
COPY entrypoint.sh /bin/entrypoint.sh

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

USER django

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/bin/entrypoint.sh"]
