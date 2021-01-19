# Python2 docker image

This is a base docker image with python2 installed.

Built using gentoo. Contains minimal, but still emerge-capable Gentoo
installation, using python2.

It is recommended to remove /usr/portage, includes and compiler in child images.
It may be also wise to flatten the end image.

## Download

Latest version can be downloaded at the
[Docker Hub](https://hub.docker.com/r/vrusinov/python2/).
