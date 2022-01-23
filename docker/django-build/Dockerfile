FROM vrusinov/python3-build:3.9.2022-01-03 as build

RUN emerge -v dev-python/django

COPY clean.sh /usr/local/bin/clean.sh
RUN chmod +x /usr/local/bin/clean.sh && \
    /usr/local/bin/clean.sh

ENTRYPOINT ["/usr/bin/python"]
#ENTRYPOINT ["/bin/bash"]
