from Config import *

# Not sure what this number does, but we need some threshold that we'd like to
# avoid crossing.
setOption("BadnessThreshold", 42)

# Ignore documentation issues.
addFilter('no-manual-page-for-binary')
addFilter('no-documentation')

# Ignore spelling errors unilt there's a support for custom dictionaries.
# TODO: add such support.
addFilter('spelling-error')

# Ignore all lint warnings in submodules:
addFilter('third_party/submodules/')
# Ignore all lint warnings in symlinks from submodules.
addFilter('SPECS/cmake.spec')
addFilter('SPECS/gdb.spec')
addFilter('SPECS/gperftools.spec')
addFilter('SPECS/libcomps.spec')
addFilter('SPECS/nginx.spec')
addFilter('SPECS/perl.spec')
addFilter('perl.src')
addFilter('perl-Data-OptList.src')
addFilter('perl-Data-Section.src')
addFilter('perl-Params-Util.x86_64')
addFilter('perl-Software-License.src')
addFilter('perl-Sub-Exporter\.(src|spec)')
addFilter('perl-Sub-Install.src')
addFilter('perl-Test-Pod\.(src|spec)')
addFilter('perl-TermReadKey\.(x86_64|src)')
addFilter('perl-Test-Pod\.(src|spec)')
addFilter('python-acme.src')
addFilter('SPECS/python-iniparse.spec')
addFilter('SPECS/os-prober.spec')
addFilter('SPECS/puppet.spec')
addFilter('SPECS/yum.spec')

# Python is mostly third-party and has lots of warnings.
addFilter('SPECS/python.spec')
addFilter('SPECS/python3.spec')
addFilter('third_party/subtrees/python/python.spec')
addFilter('third_party/subtrees/python3/python3.spec')

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
