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

RUN rm -rf /usr/portage/distfiles/
RUN rm -rf /usr/lib64/python*/test
RUN rm -rf /usr/lib64/python*/site-packages/portage/tests
RUN rm -rf /usr/share/gtk-doc/
RUN rm -rf /usr/share/doc/
RUN rm -rf /var/tmp/portage
RUN rm -rf /etc/udev
RUN rm -rf /etc/terminfo
RUN rm /etc/sandbox.conf
RUN rm /etc/wgetrc
RUN rm -rf /boot
RUN rm -rf /media
RUN rm -rf /mnt
RUN rm -rf /opt
