#!/bin/bash

set -e
set -x

date_v=$(date '+%Y-%m-%d')
v=2.5.2
vr=2.5.2-r1
n="openvpn"

docker build -t vrusinov/$n:latest -t vrusinov/$n:$date_v -t vrusinov/$n:$v -t vrusinov/$n:$vr -t vrusinov/$n:$v.$date_v  -t vrusinov/$n:$vr.$date_v .
docker run --rm -it vrusinov/$n:latest
docker push vrusinov/$n:latest
docker push vrusinov/$n:$date_v
docker push vrusinov/$n:$v
docker push vrusinov/$n:$vr
docker push vrusinov/$n:$v.$date_v
docker push vrusinov/$n:$vr.$date_v
