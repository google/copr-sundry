FROM vrusinov/golang-build:latest as base

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

FROM scratch
COPY --from=base / /

ENTRYPOINT ["/usr/bin/go", "version"]
