#!/bin/sh

rm -f /usr/lib/gcc/x86_64-pc-linux-gnu/*/libstdc++.a
rm -rf /usr/lib/gcc/x86_64-pc-linux-gnu/*/include
rm -rf /usr/lib/gcc/x86_64-pc-linux-gnu/*/libgcc.a
rm -rf /usr/lib/gcc/x86_64-pc-linux-gnu/*/plugin/include
rm -rf /usr/lib/python*/site-packages/gentoolkit*
rm -rf /usr/lib/python*/site-packages/mesonbuild*
rm -rf /usr/lib/python*/site-packages/portage*
rm -rf /usr/lib/python3.7/
rm -rf /usr/lib/python3.8/
rm -rf /usr/lib64/perl5