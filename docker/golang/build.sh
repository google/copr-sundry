!/bin/bash

set -e
set -x

date_v=$(date '+%Y-%m-%d')
v=1.14.5

docker build -t vrusinov/golang:latest -t vrusinov/golang:$date_v -t vrusinov/golang:$v -t vrusinov/golang:$v.$date_v .
docker push vrusinov/golang:latest
docker push vrusinov/golang:$date_v
docker push vrusinov/golang:$v
docker push vrusinov/golang:$v.$date_v
