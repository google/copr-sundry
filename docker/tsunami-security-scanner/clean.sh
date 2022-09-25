#!/bin/sh

rm -f /usr/lib64/gconv/IBM*.so
rm -r /etc/udev
rm -r /usr/share/doc
rm -rf /usr/lib64/binutils/
rm /usr/lib64/gconv/BIG5*.so
rm /usr/lib64/gconv/libJISX0213.so

# Clean this script
rm -f /usr/local/bin/clean.sh
