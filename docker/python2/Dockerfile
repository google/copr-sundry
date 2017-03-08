FROM vrusinov/base

COPY make.conf /etc/portage/make.conf

# Make sure we are up-to-date wrt make.conf changes:
RUN emerge --update --deep --newuse --verbose system
RUN emerge --update --deep --newuse --verbose world

# Make sure python2 is in world file:
RUN emerge -v --noreplace dev-lang/python:2.7

# Cleanup
RUN yes YES | etc-update --automode -9
RUN emerge --depclean
RUN revdep-rebuild
COPY clean.sh /usr/local/bin/clean.sh
RUN /usr/local/bin/clean.sh
