FROM vrusinov/base-build:latest as build

# hadolint: disable=DL3059
RUN emerge -v dev-lang/python
# hadolint: disable=DL3059
RUN etc-update --automode -5
# python.1 is needed for eselect to work
RUN mkdir -p /usr/share/man/man1/
# hadolint: disable=DL3059
RUN touch /usr/share/man/man1/python.1
RUN eselect python set python3.9

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

ENTRYPOINT ["/usr/bin/python3"]
#ENTRYPOINT ["/bin/bash"]
