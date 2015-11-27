#!/bin/bash
debug=""
#debug="echo "

cd `dirname $0`
LANG=C
SPEC=vim.spec
CHANGES=1

DATE=`date +"%a %b %d %Y"`
MAJORVERSION=`grep "define baseversion" vim.spec | cut -d ' ' -f 3`
ORIGPL=`grep "define patchlevel" vim.spec | cut -d ' ' -f 3 | sed -e "s/^0*//g"`
ORIGPLFILLED=`printf "%03d" $ORIGPL`

if [ ! -d vim-upstream ]; then
   git clone https://github.com/vim/vim.git vim-upstream
else
   pushd vim-upstream
   git pull
   popd
fi

pushd vim-upstream
# get the latest tag. Might be tricky with other packages, but upstream vim uses just a single branch:
LASTTAG=$(git describe --tags $(git rev-list --tags --max-count=1))
# vim upstream tags have the form v7.4.123. Remove the 'v' and get major release and patchlevel:
UPSTREAMMAJOR=$(echo $LASTTAG | sed -e 's/v\([0-9]*\.[0-9]*\).*/\1/')
LASTPL=`echo $LASTTAG| sed -e 's/.*\.//'`
LASTPLFILLED=`printf "%03d" $LASTPL`
if [ "$ORIGPLFILLED" == "$LASTPLFILLED" ]; then
    echo "No new patchlevel available"
    CHANGES=0
fi
rm -rf dist/* 2>/dev/null
make unixall
# include patchlevel in tarball name so that older sources won't get overwritten:
mv dist/vim-${UPSTREAMMAJOR}.tar.bz2 dist/vim-${UPSTREAMMAJOR}-${LASTPLFILLED}.tar.bz2
# We don't include the full upstream changelog in the rpm changelog, just ship a file with
# the changes:
git log > dist/README.patches
popd

cp -f vim-upstream/dist/README.patches README.patches
cp -f vim-upstream/dist/vim-${UPSTREAMMAJOR}-${LASTPLFILLED}.tar.bz2 .
if [ $CHANGES -ne 0 ]; then
   CHLOG="* $DATE Karsten Hopp <karsten@redhat.com> $UPSTREAMMAJOR"
   $debug sed -i -e "/Release: /cRelease: 1%{?dist}" $SPEC
   if [ "x$MAJORVERSION" != "x$UPSTREAMMAJOR" ]; then
      $debug sed -i -s "s/define baseversion: $MAJORVERSION/define baseversion: $UPSTREAMMAJOR=/" $SPEC
   fi
   $debug sed -i -e "s/define patchlevel $ORIGPLFILLED/define patchlevel $LASTPLFILLED/" $SPEC
   $debug sed -i -e "/\%changelog/a$CHLOG.$LASTPLFILLED-1\n- patchlevel $LASTPLFILLED\n" $SPEC
   $debug fedpkg new-sources vim-${UPSTREAMMAJOR}-${LASTPLFILLED}.tar.bz2
   $debug git add vim.spec README.patches
   $debug git commit -m "- patchlevel $LASTPL" 
   $debug git push
   if [ $? -eq 0 ]; then
      $debug rm -f $HOME/.koji/config
      $debug fedpkg build
      $debug ln -sf ppc-config $HOME/.koji/config
   else
      echo "GIT push failed"
   fi
fi
