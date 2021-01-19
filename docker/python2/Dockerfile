FROM vrusinov/base-build:latest as base-build

COPY make.conf /etc/portage/make.conf/01-python.conf
COPY python3.use /etc/portage/package.use/python3

RUN emerge -uDN -v system
RUN yes YES | etc-update --automode -9
RUN emerge -uDN -v world
RUN yes YES | etc-update --automode -9

RUN emerge -v dev-lang/python:2.7

RUN emerge --update --deep --newuse --verbose system
RUN yes YES | etc-update --automode -9
RUN emerge --update --deep --newuse --verbose world
RUN yes YES | etc-update --automode -9

RUN emerge --depclean
RUN revdep-rebuild

COPY clean.sh /usr/local/bin/clean.sh
RUN chmod +x /usr/local/bin/clean.sh
RUN /usr/local/bin/clean.sh

ENTRYPOINT ["/usr/bin/python2"]
