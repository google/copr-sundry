FROM vrusinov/base-build:2022-05-29 as base-build

COPY make.conf /etc/portage/make.conf/01-python.conf
COPY python3.use /etc/portage/package.use/python3

RUN emerge -uDN -v system && \
    emerge -uDN -v world && \
    emerge -v dev-lang/python:2.7

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN etc-update --automode -5

# hadolint ignore=DL3059
RUN emerge --depclean && \
    revdep-rebuild

ENTRYPOINT ["/usr/bin/python2"]
