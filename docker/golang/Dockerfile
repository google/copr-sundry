FROM vrusinov/golang-build:1.18.2 as base

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

FROM vrusinov/base:2022-05-29
COPY --from=base /usr/bin/go /bin/
COPY --from=base /usr/lib/go/bin/go /usr/lib/go/bin/go

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/bin/go", "version"]
