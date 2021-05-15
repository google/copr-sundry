FROM vrusinov/base-build:latest as base

COPY openjdk.use /etc/portage/package.use/openjdk

RUN emerge -uDN -v system
RUN emerge -uDN -v world
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN yes YES | etc-update --automode -9

RUN emerge -v dev-java/openjdk

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

ENTRYPOINT ["/usr/bin/java", "-version"]
