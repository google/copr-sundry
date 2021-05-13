#!/bin/sh

set -x

cd /opt/tsunami

if [ -z "${IP_V4_TARGET}${IP_V6_TARGET}" ] ; then
  echo "No scan target specified."
  echo "Set IP_V4_TARGET or IP_V6_TARGET environment variable"
  exit 1
fi

[[ ! -z "$IP_V4_TARGET" ]] && target_args="--ip-v4-target=${IP_V4_TARGET}"
[[ ! -z "$IP_V6_TARGET" ]] && target_args="${target_args} --ip-v6-target=${IP_V6_TARGET}"


java -cp tsunami.jar:plugins/* -Dtsunami-config.location=tsunami.yaml \
  com.google.tsunami.main.cli.TsunamiCli \
  ${target_args} \
  --scan-results-local-output-format=JSON --scan-results-local-output-filename=out

cat out
