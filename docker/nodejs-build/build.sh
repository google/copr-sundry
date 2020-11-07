#!/bin/bash

set -e
set -x

date_v=$(date '+%Y-%m-%d')
v="14.4.0"
n="nodejs-build"

docker build -t vrusinov/$n:latest -t vrusinov/$n:$date_v -t vrusinov/$n:$v -t vrusinov/$n:$v.$date_v .
#docker run --rm -it vrusinov/$n:latest
docker push vrusinov/$n:latest
docker push vrusinov/$n:$date_v
docker push vrusinov/$n:$v
docker push vrusinov/$n:$v.$date_v
