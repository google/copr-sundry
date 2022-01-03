FROM vrusinov/base-build:latest as base

COPY openjdk.use /etc/portage/package.use/openjdk
COPY make.conf /etc/portage/make.conf/01-java.conf

RUN emerge -C sys-apps/systemd
# hadolint ignore=DL3059
RUN emerge -uDN -v system && \
    emerge -uDN -v world
# hadolint ignore=DL3059
RUN etc-update --automode -5
# hadolint ignore=DL3059
RUN emerge --depclean

# hadolint ignore=DL3059
RUN emerge -v virtual/jre
# hadolint ignore=DL3059
RUN eselect java-vm set system 1

COPY clean.sh /bin/clean.sh
RUN chmod +x /bin/clean.sh && /bin/clean.sh

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/usr/bin/java", "-version"]
