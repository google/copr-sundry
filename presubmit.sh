#!/bin/bash
#
# Presubmit script for copr-sundry repository.
# Needs to be execute from top of the repo (cwd matters).

set -e

rpmlint -f rpmlint.conf.py .
