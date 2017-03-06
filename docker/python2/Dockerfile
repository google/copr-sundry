FROM vrusinov/base

COPY make.conf /etc/portage/make.conf

# Make sure we are up-to-date wrt make.conf changes:
#RUN emerge --update --deep --newuse --verbose system
#RUN emerge --update --deep --newuse --verbose world

# Cleanup
#RUN yes YES | etc-update --automode -9
#RUN emerge --depclean
#RUN revdep-rebuild
