#!/bin/sh

# The original script name has been passed as the first argument:
"$@" |
  awk '
	$0 != "perl(FCGI)" &&
	$0 != "perl(Your::Module::Here)" &&
	$0 != "perl(Tk)" &&
	$0 !~ /^perl\(Tk::/ &&
	$0 !~ /^perl\(Mac::/
      '

# We used to filter also these:
#	NDBM perl(v5.6.0) perl(Tie::RangeHash)
# but they don't seem to be present anymore.
