#!/bin/sh

set -e

rm -f /usr/lib64/gconv/BIG5HKSCS.so
rm -f /usr/lib64/gconv/IBM1399.so
rm -r /usr/lib/python3.9/site-packages/Cython
rm -r /usr/lib/python3.9/site-packages/pydantic
rm -r /usr/lib/python3.9/site-packages/setuptools
rm -rf /usr/lib64/perl5
rm -rf /usr/share/sgml/