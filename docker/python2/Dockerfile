FROM vrusinov/python2-build:latest as build

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

FROM vrusinov/base:latest
COPY --from=build / /

ENTRYPOINT ["/usr/bin/python2"]
