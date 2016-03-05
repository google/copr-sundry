from Config import *

# Not sure what this number does, but we need some threshold that we'd like to
# avoid crossing.
setOption("BadnessThreshold", 42)

# Ignore documentation issues.
addFilter('no-manual-page-for-binary')
addFilter('no-documentation')
addFilter('name-repeated-in-summary')

# Ignore spelling errors unilt there's a support for custom dictionaries.
# TODO: add such support.
addFilter('spelling-error')

# Ignore unversioned bundled provides.
addFilter('unversioned-explicit-provides bundled\([a-z\-]+\)')

# Don't care about groups.
addFilter('non-standard-group')

# Ignore all lint warnings in submodules:
addFilter('third_party/submodules/')
# Ignore all lint warnings in symlinks from submodules.
addFilter('SPECS/cmake.spec')
addFilter('SPECS/gdb.spec')
addFilter('grub2\.(x86_64|src|spec)')
addFilter('grub2-(tools|debuginfo|efi|efi-modules)\.x86_64')
addFilter('SPECS/gperftools.spec')
addFilter('libev-devel.x86_64')
addFilter('SPECS/libcomps.spec')
addFilter('nginx\.(spec|x86_64|src)')
addFilter('perl-common-sense.x86_64')
addFilter('perl-Compress-Raw-Bzip2.x86_64')
addFilter('perl-Data-OptList.src')
addFilter('perl-Data-Section.src')
addFilter('perl-GD.x86_64')
addFilter('perl-HTML-Parser.x86_64')
addFilter('perl-libintl\.(x86_64|src|spec)')
addFilter('perl-Mojolicious\.(src|spec)')
addFilter('perl-Params-Util.x86_64')
addFilter('perl-Pod-Coverage.spec')
addFilter('perl-Software-License\.(src|spec)')
addFilter('perl-Sub-Exporter\.(src|spec)')
addFilter('perl-Sub-Install.src')
addFilter('perl-Pod-Coverage.src')
addFilter('perl-libintl\.(x86_64|src)')
addFilter('perl-Test-Pod\.(src|spec)')
addFilter('perl-TermReadKey\.(x86_64|src)')
addFilter('perl-Test-Pod\.(src|spec)')
addFilter('perl-Text-Template.noarch')
addFilter('perl-Time-HiRes.x86_64')
addFilter('SPECS/puppet.spec')
addFilter('pyOpenSSL(-doc)?\.(noarch|spec)')
addFilter('python(2|3)?-acme\.(src|noarch)')
addFilter('python(2|3)?-hypothesis\.(src|noarch)')
addFilter('python(2|3)-dialog.noarch')
addFilter('python-mock.spec')
addFilter('python-ndg_httpsclient\.(src|spec)')
addFilter('python-parsedatetime.spec')
addFilter('python-psutil.spec')
addFilter('python-pyrfc3339.src')
addFilter('python-twisted.x86_64')
addFilter('python(2|3)?-rpm-macros\.(noarch|src)')
addFilter('python-srpm-macros.noarch')
addFilter('python-zbase32.noarch')
addFilter('python3?-zope-event\.(noarch|spec)')
addFilter('python3?-zope-interface\.(x86_64|src)')
addFilter('SPECS/python-iniparse.spec')
addFilter('python-pyrfc3339.src')
addFilter('python-zope-event.noarch')
addFilter('pyutil.noarch')
addFilter('SPECS/os-prober.spec')
addFilter('SPECS/puppet.spec')
addFilter('yum\.(spec|src)')

# Python is mostly third-party and has lots of warnings.
# TODO: clean those up.
addFilter('SPECS/python.spec')
addFilter('SPECS/python3.spec')
addFilter('third_party/subtrees/python/python.spec')
addFilter('third_party/subtrees/python3/python3.spec')
addFilter('python-libs.x86_64')
addFilter('python-debuginfo.x86_64')
addFilter('python-libs.x86_64')
addFilter('python-devel.x86_64')
addFilter('python-macros.noarch')
addFilter('python.x86_64')
addFilter('python3?.src:[0-9]+: W: hardcoded-library-path')
addFilter('python.src: W: %ifarch-applied-patch Patch131')
addFilter('python.src:[0-9]+: W: unversioned-explicit-obsoletes')
addFilter('python.src:[0-9]+: W: unversioned-explicit-provides')
addFilter('python.src: W: strange-permission pythondeps.sh')

# RPM is special, let's ignore warnings from it.
addFilter('SPECS/rpm.spec')
addFilter('third_party/subtrees/rpm/rpm.spec')

# DNF have a lot of weird stuff:
addFilter('dnf.spec.*libdir-macro-in-noarch-package')

# VIM: allow mixed space/tab usage in specific line.
addFilter('vim.spec:218: W: mixed-use-of-spaces-and-tabs')
# Ignore unversioned provide /bin/vi, versioning it triggers another lint
# warning.
addFilter('vim.spec:[0-9]+: W: unversioned-explicit-provides /bin/vi')

## Perl
# Perl packages are weird and often don't have -devel part.
addFilter('perl-Tk.x86_64: W: devel-file-in-non-devel-package')
# Some of them also depend on perl-devel
addFilter('perl-ExtUtils-Miniperl.noarch: W: devel-dependency')
# Perl-Tk has weird deps
addFilter('perl-Tk.spec:63: W: comparison-operator-in-deptoken')

## Let's encrypt:
# Allow pems in test files.
addFilter('python2-letsencrypt.noarch: W: pem-certificate /usr/lib/python2.7/site-packages/letsencrypt/tests/testdata/.*')
# Allow some nonstandard permissions
addFilter('letsencrypt.noarch: W: non-standard-dir-perm /var/log/letsencrypt 0')
addFilter('letsencrypt.noarch: W: non-standard-dir-perm /var/lib/letsencrypt 0')
addFilter('letsencrypt.noarch: W: non-standard-dir-perm /etc/letsencrypt 0')
# TODO: fix following
addFilter('letsencrypt.noarch: W: log-files-without-logrotate')

## Libcomps
# URL broken :(
addFilter('libcomps.spec: W: invalid-url Source0: https://github.com/midnightercz/libcomps/libcomps-0.1.7.tar.gz')

## GDB
# Following should be ok for debugger.
addFilter('gdb\.(spec|src):[0-9]+: W: unversioned-explicit-obsoletes devtoolset')
addFilter('gdb.x86_64: W: unstripped-binary-or-object /usr/bin/gdb')
addFilter('gdb-gdbserver.x86_64: W: unstripped-binary-or-object /usr/lib64/libinproctrace.so')
addFilter('gdb-gdbserver.x86_64: W: unstripped-binary-or-object /usr/bin/gdbserver')
addFilter('gdb-gdbserver.x86_64: W: shared-lib-calls-exit /usr/lib64/libinproctrace.so exit@GLIBC_2.2.5')
addFilter('gdb.x86_64: W: only-non-binary-in-usr-lib')
addFilter('gdb-gdbserver.x86_64: W: no-soname /usr/lib64/libinproctrace.so')
addFilter('gdb.spec:[0-9]+: W: hardcoded-library-path')
addFilter('gdb.x86_64: W: dangerous-command-in-%pre mv')
addFilter('gdb.x86_64: W: devel-file-in-non-devel-package /usr/include/gdb/jit-reader.h')
addFilter('gdb.src:[0-9]+: W: hardcoded-library-path')
# Snapshots dissapear quickly
addFilter('gdb\.(src|spec): W: invalid-url Source0: ftp://sourceware.org/pub/gdb/snapshots/current/.*')

## Python-pip
addFilter('python(3|2)?-pip.noarch: W: non-executable-script /usr/lib/python.\../site-packages/pip/_vendor/requests/packages/chardet/chardetect.py')

## Cython
# There's no -devel package.
addFilter('(python3-)?Cython.x86_64: W: devel-file-in-non-devel-package')
# false-positives
addFilter('(python3-)?Cython.x86_64: W: non-executable-script /usr/lib64/python(2|3)\.[0-9]/site-packages/cython.py')
addFilter('(python3-)?Cython.x86_64: W: non-executable-script /usr/lib64/python(2|3)\.[0-9]/site-packages/Cython/Build/Cythonize.py')
addFilter('(python3-)?Cython.x86_64: W: non-executable-script /usr/lib64/python[0-9]\.[0-9]/site-packages/Cython/Debugger/Cygdb.py')
addFilter('(python3-)?Cython.x86_64: W: non-executable-script /usr/lib64/python[0-9]\.[0-9]/site-packages/Cython/Debugger/libpython.py')

## Perl
addFilter('perl.spec: W: %ifarch-applied-patch Patch3: perl-5.8.0-libdir64.patch')
addFilter('perl\.(src|spec): W: invalid-license')
addFilter('perl.spec:[0-9]+: W: unversioned-explicit-obsoletes')

## Python-cryptoghraphy
addFilter('python3?-cryptography-vectors.noarch: W: pem-certificate')

## Python-ply
# cpython stuff:
addFilter('python3?-ply.noarch: W: python-bytecode-without-source.*cpython.*')

## libsolv
addFilter('libsolv.x86_64: W: shared-lib-calls-exit')

# Python-cffi
addFilter('python-cffi.x86_64: W: devel-file-in-non-devel-package')
addFilter('python3-cffi.x86_64: W: unstripped-binary-or-object')

# pyparsing
addFilter('pyparsing-doc.noarch: W: file-not-utf8')
