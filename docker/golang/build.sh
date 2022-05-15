#!/bin/bash

set -e
set -x

n="golang"
date_v=$(date '+%Y-%m-%d')
v=1.17.0

docker build -t vrusinov/$n:latest -t vrusinov/golang:$date_v -t vrusinov/golang:$v -t vrusinov/golang:$v.$date_v .
docker run --rm -it vrusinov/$n:latest
docker push vrusinov/golang:latest
docker push vrusinov/golang:$date_v
docker push vrusinov/golang:$v
docker push vrusinov/golang:$v.$date_v
