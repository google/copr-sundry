FROM vrusinov/django-build:latest as build

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

FROM vrusinov/python3:3.8
COPY --from=build /usr/bin/django* /usr/bin/
COPY --from=build /usr/lib/python-exec/python3.8/django* /usr/lib/python-exec/python3.8/
COPY --from=build /usr/lib/python3.8/site-packages/asgiref /usr/lib/python3.8/site-packages/asgiref
COPY --from=build /usr/lib/python3.8/site-packages/Django-3.2.5-py3.8.egg-info/ /usr/lib/python3.8/site-packages/Django-3.2.5-py3.8.egg-info/
COPY --from=build /usr/lib/python3.8/site-packages/django/ /usr/lib/python3.8/site-packages/django
COPY --from=build /usr/lib/python3.8/site-packages/pytz /usr/lib/python3.8/site-packages/pytz
COPY --from=build /usr/lib/python3.8/site-packages/sqlparse /usr/lib/python3.8/site-packages/sqlparse
COPY entrypoint.sh /bin/entrypoint.sh

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/bin/entrypoint.sh"]
