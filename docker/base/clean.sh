#!/bin/sh

rm -rf /usr/portage/distfiles/
rm -rf /usr/lib64/python*/test
rm -rf /usr/lib64/python*/site-packages/portage/tests
rm -rf /usr/share/gtk-doc/
rm -rf /usr/share/doc/
rm /usr/share/portage/config/make.conf.example
rm -rf /usr/src

rm -rf /var/tmp/portage
rm -rf /var/cache/*
rm -rf /var/lib/gentoo/news
rm -rf /var/log/*

rm -rf /etc/udev
rm -rf /etc/terminfo
rm /etc/sandbox.conf
rm /etc/wgetrc
rm -rf /etc/skel

rm /sbin/pivot_root
rm /sbin/mkswap

rm -rf /boot
rm -rf /media
rm -rf /mnt
rm -rf /opt
rm -rf /home
rm -rf /root
