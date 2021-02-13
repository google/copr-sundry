!/bin/bash

set -e
set -x

date_v=$(date '+%Y-%m-%d')

docker build -t vrusinov/build:latest -t vrusinov/build:$date_v .
#docker run --rm -it vrusinov/base:latest
docker push vrusinov/base:latest
docker push vrusinov/base:$date_v
