FROM gentoo/stage3-amd64-nomultilib

COPY make.conf /etc/portage/make.conf
COPY rsync-excludes /etc/portage/rsync-excludes
COPY packages /etc/portage/profile/packages
COPY locale.gen /etc/locale.gen

#RUN emaint -a sync
RUN emerge --sync
RUN emerge --update --deep --newuse --verbose system
RUN yes YES | etc-update --automode -9

#RUN emerge --update --deep --newuse --verbose world
