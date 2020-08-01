#!/bin/sh

rm -rf /usr/portage/distfiles/
rm -rf /usr/lib64/python*/test
rm -rf /usr/lib64/python*/site-packages/portage/tests
rm -rf /usr/lib64/python*/site-packages/twisted/test
rm -rf /usr/lib64/python*/site-packages/allmydata/test
rm -rf /usr/share/gtk-doc/
rm -rf /usr/share/doc/
rm /usr/share/portage/config/make.conf.example
rm -rf /usr/src

rm -rf /var/tmp/portage
rm -rf /tmp/*
rm -rf /var/cache/*
rm -rf /var/lib/gentoo/news
rm -rf /var/log/*

rm -rf /etc/udev
rm -rf /etc/terminfo
rm -f /etc/sandbox.conf
rm -f /etc/wgetrc
rm -rf /etc/skel
rm /etc/DIR_COLORS
rm -rf /etc/default
rm -rf /etc/init.d
rm /etc/issue
rm /etc/nanorc
rm /etc/rc.conf
rm /etc/sysctl.conf
rm /etc/xattr.conf

rm -rf /lib/systemd

rm /bin/dmesg
rm /bin/findmnt
rm /bin/login
rm /bin/mount
rm /bin/umount
rm /bin/wdctl
rm /bin/run-parts
rm /sbin/pivot_root
rm /sbin/mkswap
rm /sbin/agetty
rm /sbin/blkid
rm /sbin/blockdev
rm /sbin/findfs
rm /sbin/fsck.minix
rm /sbin/fstrim
rm /sbin/installkernel
rm /sbin/losetup
rm /sbin/mkfs.bfs
rm /sbin/raw
rm /sbin/swaplabel
rm /sbin/swapon
rm /sbin/wipefs
rm /usr/sbin/rfkill
rm /usr/sbin/partx

rm /usr/lib/cracklib_dict.hwm
rm /usr/lib/cracklib_dict.pwd
rm /usr/lib/cracklib_dict.pwi
rm -rf /usr/lib/systemd

rm -rf /usr/share/vim
rm -rf /usr/share/info
rm -rf /usr/share/locale

rm -rf /var/cache


rm -rf /boot
rm -rf /media
rm -rf /mnt
rm -rf /opt
rm -rf /home
rm -rf /root
