FROM vrusinov/python2

COPY package.accept_keywords /etc/portage/package.accept_keywords
COPY package-use-python /etc/portage/package.use/python

# Update wrt new configs.
RUN emerge --update --deep --newuse --verbose system
RUN emerge --update --deep --newuse --verbose world

# Install tahoe.
RUN emerge -v --noreplace net-fs/tahoe-lafs

# Cleanup
RUN yes YES | etc-update --automode -9
RUN emerge --depclean
RUN revdep-rebuild
RUN /usr/local/bin/clean.sh
