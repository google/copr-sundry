FROM vrusinov/golang-build:1.19.4 as base

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

FROM vrusinov/base:2022-12-18
COPY --from=base /usr/bin/go /bin/
COPY --from=base /usr/lib/go/bin/go /usr/lib/go/bin/go

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/bin/go", "version"]
