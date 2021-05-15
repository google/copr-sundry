FROM vrusinov/base-build:latest as base-build

RUN emerge -v dev-lang/go

COPY clean.sh /usr/local/bin/clean.sh
RUN chmod +x /usr/local/bin/clean.sh && \
    /usr/local/bin/clean.sh

ENTRYPOINT ["/bin/bash"]
