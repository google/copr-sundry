from Config import *

# Not sure what this number does, but we need some threshold that we'd like to
# avoid crossing.
setOption("BadnessThreshold", 42)

# Ignore all lint warnings in submodules:
addFilter('third_party/submodules/')
# Ignore all lint warnings in symlinks from submodules.
addFilter('SPECS/cmake.spec')
addFilter('SPECS/gdb.spec')
addFilter('SPECS/gperftools.spec')
addFilter('SPECS/libcomps.spec')
addFilter('SPECS/nginx.spec')
addFilter('SPECS/perl.spec')
addFilter('SPECS/python-iniparse.spec')
addFilter('SPECS/os-prober.spec')
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
