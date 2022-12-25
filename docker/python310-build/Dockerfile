FROM vrusinov/base-build:2022-12-25 as build

COPY make.conf /etc/portage/make.conf/01-python.conf
# hadolint: disable=DL3059
RUN emerge -v  --noreplace dev-lang/python:3.10
# hadolint: disable=DL3059
RUN emerge -uDN -v1 world
# hadolint: disable=DL3059
RUN emerge --depclean
# hadolint: disable=DL3059
RUN etc-update --automode -5

ENTRYPOINT ["/usr/bin/python3"]
#ENTRYPOINT ["/bin/bash"]