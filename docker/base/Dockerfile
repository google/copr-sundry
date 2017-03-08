FROM gentoo/stage3-amd64-nomultilib

COPY make.conf /etc/portage/make.conf
COPY rsync-excludes /etc/portage/rsync-excludes
COPY packages /etc/portage/profile/packages
COPY package-use-python /etc/portage/package.use/python
COPY locale.gen /etc/locale.gen

RUN emerge --sync
RUN emerge --update --deep --newuse --verbose system
RUN yes YES | etc-update --automode -9

RUN emerge --update --deep --newuse --verbose world

RUN emerge --depclean
RUN emerge -v app-portage/gentoolkit
RUN revdep-rebuild

COPY clean.sh /usr/local/bin/clean.sh
COPY strip.sh /usr/local/bin/clean.sh
RUN /usr/local/bin/clean.sh
