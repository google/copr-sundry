FROM vrusinov/base-build:latest as base-build

COPY make.conf /etc/portage/make.conf/01-python.conf
COPY python3.use /etc/portage/package.use/python3

RUN emerge -uDN -v system && \
    emerge -uDN -v world && \
    emerge -v dev-lang/python:2.7

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN yes YES | etc-update --automode -9

# hadolint ignore=DL3059
RUN emerge --depclean && \
    revdep-rebuild

COPY clean.sh /usr/local/bin/clean.sh
RUN chmod +x /usr/local/bin/clean.sh && \
    /usr/local/bin/clean.sh

ENTRYPOINT ["/usr/bin/python2"]
