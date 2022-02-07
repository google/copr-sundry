FROM vrusinov/base-build:latest as build

# hadolint: disable=DL3059
RUN emerge -v dev-lang/python:3.8
# hadolint: disable=DL3059
RUN etc-update --automode -5

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

ENTRYPOINT ["/usr/bin/python3"]
#ENTRYPOINT ["/bin/bash"]
