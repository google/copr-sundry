FROM vrusinov/base-build:latest as base-build

RUN emerge -v net-libs/nodejs

COPY clean.sh /usr/local/bin/clean.sh
RUN chmod +x /usr/local/bin/clean.sh && \
    /usr/local/bin/clean.sh

ENTRYPOINT ["/usr/bin/node", "--version"]
