!/bin/bash

set -e
set -x

date_v=$(date '+%Y-%m-%d')
n="base"

docker build -t vrusinov/$n:latest -t vrusinov/$n:$date_v .
docker run --rm -it vrusinov/$n:latest
docker push vrusinov/$n:latest
docker push vrusinov/$n:$date_v
