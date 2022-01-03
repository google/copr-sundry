FROM vrusinov/base-build:2021-09-11 as build

COPY make.conf /etc/portage/make.conf/01-python.conf
# hadolint: disable=DL3059
RUN emerge -v dev-lang/python:3.9
# hadolint: disable=DL3059
RUN emerge -uDN -v1 system
# hadolint: disable=DL3059
RUN emerge -uDN -v1 world
# hadolint: disable=DL3059
RUN emerge --depclean
# hadolint: disable=DL3059
RUN etc-update --automode -5

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

ENTRYPOINT ["/usr/bin/python3"]
#ENTRYPOINT ["/bin/bash"]