#!/bin/bash

set -e
set -x

date_v=$(date '+%Y-%m-%d')
v=3.8.10
v_short=3.8
n="python3-build"

docker build -t vrusinov/$n:latest -t vrusinov/$n:$date_v -t vrusinov/$n:$v -t vrusinov/$n:$v.$date_v -t vrusinov/$n:$v_short -t vrusinov/$n:$v_short.$date_v .
docker run --rm -it vrusinov/$n:latest
docker push vrusinov/$n:latest
docker push vrusinov/$n:$date_v
docker push vrusinov/$n:$v
docker push vrusinov/$n:$v.$date_v
docker push vrusinov/$n:$v_short
docker push vrusinov/$n:$v_short.$date_v
