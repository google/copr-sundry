FROM gentoo/portage:latest as portage

FROM gentoo/stage3:amd64-nomultilib-systemd as gentoo

COPY --from=portage /var/db/repos/gentoo /var/db/repos/gentoo

RUN rm /etc/portage/make.conf && \
    mkdir -p /etc/portage/make.conf
COPY make.conf /etc/portage/make.conf/00-base.conf
COPY package-use-python /etc/portage/package.use/python
COPY packages /etc/portage/profile/packages
COPY locale.gen /etc/locale.gen

# hadolint ignore=DL3059
RUN emerge --sync
# hadolint ignore=DL3059
RUN emerge --update --deep --newuse --verbose system
# hadolint ignore=DL3059
RUN emerge --update --deep --newuse --verbose world
# hadolint ignore=DL3059
RUN etc-update --automode -5

# hadolint ignore=DL3059
RUN emerge -v app-eselect/eselect-repository

# hadolint ignore=DL3059
RUN emerge --depclean && \
    emerge -v app-portage/gentoolkit && \
    revdep-rebuild

ENTRYPOINT ["/bin/bash"]
