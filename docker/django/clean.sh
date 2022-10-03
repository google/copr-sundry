#!/bin/sh

set -e

rm -f /usr/lib/gcc/x86_64-pc-linux-gnu/*/libquadmath.a
rm -f /usr/lib/gcc/x86_64-pc-linux-gnu/*/libstdc++fs.a
rm -f /usr/lib/gcc/x86_64-pc-linux-gnu/*/plugin/gtype.state
rm -f /usr/lib64/gconv/BIG5HKSCS.so
rm -f /usr/lib64/gconv/IBM1399.so
rm -rf /usr/lib64/perl5
rm -rf /usr/share/sgml/
rm /lib64/libsystemd.so.0.32.0
rm /usr/lib64/gconv/GB18030.so
rm /usr/lib64/gconv/IBM1390.so