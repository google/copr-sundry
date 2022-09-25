#!/bin/sh

rm -f /usr/bin/ctest
rm -rf /opt/openjdk-bin-*/man
rm -rf /usr/lib/python*
rm -rf /usr/lib64/binutils/x86_64-pc-linux-gnu/*/ldscripts
rm -rf /usr/lib64/gconv/GB18030.so
rm -rf /usr/lib64/gconv/IBM1371.so
rm -rf /usr/lib64/gconv/IBM1388.so
rm -rf /usr/lib64/perl5
rm -rf /usr/share/sgml/
rm /usr/lib64/gconv/IBM1390.so
rm /usr/lib64/gconv/IBM1399.so

# Remove this script:
rm -rf /usr/local
