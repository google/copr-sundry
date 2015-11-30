from Config import *

# Not sure what this number does, but we need some threshold that we'd like to
# avoid crossing.
setOption("BadnessThreshold", 42)

# Ignore spelling errors as there's currently no sane way to add words into
# dictionary.
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
addFilter('SPECS/puppet.spec')
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

# Vim provides /bin/vi, which cannot be versioned since it's a path.
addFilter('vim.spec:[0-9]+: W: unversioned-explicit-provides /bin/vi')
# There's shell command that I don't want to touch.
addFilter('vim.spec:218: W: mixed-use-of-spaces-and-tabs')
