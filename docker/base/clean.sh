#!/bin/sh

rm -f /bin/chroot
rm -f /bin/df
rm -f /bin/tar
rm -f /bin/tty
rm -f /bin/lsblk
rm -f /bin/su
rm -f /sbin/chcpu
rm -f /sbin/ctrlaltdel
rm -f /sbin/getpcaps
rm -f /sbin/setcap
rm -f /sbin/sln
rm -f /sbin/blkzone
rm -f /sbin/fsck
rm -f /sbin/hwclock
rm -f /sbin/mkfs.minix
rm -f /sbin/sfdisk
rm -f /sbin/swapoff

rm /etc/etc-update.conf
rm /etc/locale.gen
rm /etc/login.access
rm -rf /etc/portage
rm -rf /etc/revdep-rebuild
rm -rf /etc/sandbox.d
rm -rf /ect/bash
rm -rf /etc/env.d
rm -rf /etc/modprobe.d
rm /etc/profile
rm /etc/rpc
rm /etc/shells

rm -rf /lib/gentoo
rm /lib/cpp
rm /lib64/libfdisk.so.*

rm -rf /usr/include

rm /usr/bin/bzcmp
rm /usr/bin/g++*
rm /usr/bin/localedef
rm /usr/bin/pkgconf
rm /usr/bin/setarch
rm /usr/bin/x86_64-pc-linux-gnu-ld*
rm /usr/bin/msgattrib
rm /usr/bin/xzegrep
rm /usr/sbin/addgnupghome
rm /usr/sbin/archive-conf
rm /usr/sbin/chgpasswd
rm /usr/sbin/dispatch-conf
rm /usr/sbin/env-update
rm /usr/sbin/groupadd
rm /usr/sbin/groupmod
rm /usr/sbin/grpunconv
rm /usr/sbin/locale-gen
rm /usr/sbin/pwconv
rm /usr/sbin/regenworld
rm /usr/sbin/savelog
rm /usr/sbin/useradd
rm /usr/sbin/uuidd
rm /usr/sbin/addpart
rm /usr/sbin/delpart
rm /usr/sbin/groupdel
rm /usr/sbin/newusers
rm /usr/sbin/restore-tar
rm /usr/sbin/update-ca-certificates

rm -rf /usr/lib/portage
rm /usr/lib/python-exec/python3.*/2to3
rm /usr/lib/python-exec/python3.*/dispatch-conf
rm /usr/lib/python-exec/python3.*/ebuild
rm /usr/lib/python-exec/python3.*/eclean-dist
rm /usr/lib/python-exec/python3.*/egencache
rm /usr/lib/python-exec/python3.*/emaint
rm /usr/lib/python-exec/python3.*/emirrordist
rm /usr/lib/python-exec/python3.*/env-update
rm /usr/lib/python-exec/python3.*/equery
rm /usr/lib/python-exec/python3.*/fixpackages
rm /usr/lib/python-exec/python3.*/glsa-check
rm /usr/lib/python-exec/python3.*/meson
rm /usr/lib/python-exec/python3.*/pydoc
rm /usr/lib/python-exec/python3.*/python-config
rm /usr/lib/python-exec/python3.*/python3-config
rm /usr/lib/python-exec/python3.*/regenworld
rm /usr/lib/python-exec/python3.*/archive-conf
rm /usr/lib/python-exec/python3.*/eclean
rm /usr/lib/python-exec/python3.*/ekeyword
rm /usr/lib/python-exec/python3.*/enalyze
rm /usr/lib/python-exec/python3.*/eshowkw
rm /usr/lib/python-exec/python3.*/portageq
rm /usr/lib/python-exec/python3.*/quickpkg
rm /usr/lib/python-exec/python3.*/revdep-rebuild
rm -rf /usr/lib/python*/test
rm -rf /usr/lib/python*/site-packages/portage
rm -rf /usr/lib/python*/site-packages/mesonbuild
rm -rf /usr/lib/python*/site-packages/gentoolkit
rm -rf /usr/lib/tmpfiles.d
rm -rf /usr/lib64/cmake
rm -rf /usr/lib64/locale
rm -rf /usr/libexec/gcc
rm -rf /usr/x86_64-pc-linux-gnu

rm -rf /usr/share/aclocal*
rm -rf /usr/share/autoconf*
rm -rf /usr/share/baselayout
rm -rf /usr/share/bison
rm -rf /usr/share/eselect
rm -rf /usr/share/gdb
rm -rf /usr/share/gnuconfig
rm -rf /usr/share/nano
rm -rf /usr/share/polkit-1
rm -rf /usr/share/sandbox
rm -rf /usr/share/terminfo
rm -rf /usr/share/man
rm -rf /usr/share/binutils-data
rm -rf /usr/share/gcc-data
rm -rf /usr/share/i18n
rm -rf /usr/share/openpgp-keys

rm -rf /var/db
rm -rf /var/lib/gentoo
rm -rf /var/lib/portage


# Remove this script:
rm -rf /usr/local
