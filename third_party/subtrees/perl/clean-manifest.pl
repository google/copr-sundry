#!/usr/bin/perl -w
use strict;

my ($arch, $patfile, $infile, $outfile, $libdir, $thread_arch) = @ARGV;

if (not $arch or not $patfile or not $infile or not $outfile or not $libdir) {
  die "Usage: $0 arch thread_arch pattern-file in-file out-file libdir [ threadarch ]";
}

$thread_arch ||= '';

open IN, "<$infile"
  or die "Can't open $infile: $!";
open OUT, ">$outfile"
  or die "Can't open $outfile: $!";
open PATTERN, "<$patfile"
  or die "Can't open $patfile: $!";

my @patterns = <PATTERN>;
chomp @patterns;
for my $p (@patterns) {
  $p =~ s/%{_libdir}/$libdir/g;
  $p =~ s/%{_arch}/$arch/g;
  $p =~ s/%{thread_arch}/$thread_arch/g;
}

my %exclude = map { $_ => 1 } @patterns;

close PATTERN;

while(<IN>) {
  chomp;

  print OUT "$_\n"
    unless exists $exclude{$_}
}

close IN;
close OUT;
