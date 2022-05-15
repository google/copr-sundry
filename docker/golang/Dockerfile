FROM vrusinov/golang-build:1.17.0 as base

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

FROM scratch
COPY --from=base / /

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/usr/bin/go", "version"]
