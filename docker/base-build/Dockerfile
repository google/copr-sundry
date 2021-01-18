FROM gentoo/portage:latest as portage

FROM gentoo/stage3:amd64-nomultilib as gentoo

COPY --from=portage /var/db/repos/gentoo /var/db/repos/gentoo

RUN rm /etc/portage/make.conf
RUN mkdir -p /etc/portage/make.conf
COPY make.conf /etc/portage/make.conf/00-base.conf
COPY package-use-python /etc/portage/package.use/python
COPY packages /etc/portage/profile/packages
COPY locale.gen /etc/locale.gen

RUN emerge --sync

RUN emerge --update --deep --newuse --verbose system
RUN yes YES | etc-update --automode -9

RUN emerge --update --deep --newuse --verbose world

RUN emerge --depclean
RUN emerge -v app-portage/gentoolkit
RUN revdep-rebuild

COPY clean.sh /usr/local/bin/clean.sh
RUN chmod +x /usr/local/bin/clean.sh
RUN /usr/local/bin/clean.sh

ENTRYPOINT ["/bin/bash"]
