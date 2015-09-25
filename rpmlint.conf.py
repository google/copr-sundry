from Config import *

# Not sure what this number does, but we need some threshold that we'd like to
# avoid crossing.
setOption("BadnessThreshold", 42)

# Ignore all lint warnings in submodules:
addFilter('third_party/submodules/')

# Ignore all lint warnings in yum.spec - symlink from submodules.
addFilter('SPECS/yum.spec')
