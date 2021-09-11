!/bin/bash

set -e
set -x

date_v=$(date '+%Y-%m-%d')
n="base-build"

docker pull gentoo/portage:latest
docker pull gentoo/stage3:amd64-nomultilib-systemd

docker build -t vrusinov/$n:latest -t vrusinov/$n:$date_v .
docker run --rm -it vrusinov/$n:latest
docker push vrusinov/$n:latest
docker push vrusinov/$n:$date_v
