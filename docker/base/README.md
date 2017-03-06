# Base docker image

This is a base docker image.

Built using gentoo. Contains minimal, but still emerge-capable Gentoo
installation.

It is recommended to remove /usr/portage, includes and compiler in child images.
It may be also wise to flatten the end image.

## Download

Latest version can be downloaded at the
[Docker Hub](https://hub.docker.com/r/vrusinov/base/).
