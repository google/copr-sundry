%define patchlevel 942
%if %{?WITH_SELINUX:0}%{!?WITH_SELINUX:1}
%define WITH_SELINUX 1
%endif
%define desktop_file 1
%if %{desktop_file}
%define desktop_file_utils_version 0.2.93
%endif

%define withnetbeans 1

%define withvimspell 0
%define withhunspell 0
%define withruby 1
%define withlua 1

%define baseversion 7.4
%define vimdir vim74

Summary: The VIM editor
URL:     http://www.vim.org/
Name: vim
Version: %{baseversion}.%{patchlevel}
Release: 1%{?dist}
License: Vim
Group: Applications/Editors
Source0: https://github.com/vim/vim/archive/v%{version}.tar.gz
Source3: gvim.desktop
Source4: vimrc
Source5: ftp://ftp.vim.org/pub/vim/patches/README
Source7: gvim16.png
Source8: gvim32.png
Source9: gvim48.png
Source10: gvim64.png
Source12: vi_help.txt
%if %{withvimspell}
Source13: vim-spell-files.tar.bz2
%endif
Source14: spec-template
Source15: spec-template.new

Patch2002: vim-7.0-fixkeys.patch
Patch2003: vim-6.2-specsyntax.patch
%if %{withhunspell}
Patch2011: vim-7.0-hunspell.patch
BuildRequires: hunspell-devel
%endif

Patch3000: vim-7.4-syntax.patch
Patch3002: vim-7.1-nowarnings.patch
Patch3004: vim-7.0-rclocation.patch
Patch3006: vim-7.4-checkhl.patch
Patch3007: vim-7.4-fstabsyntax.patch
Patch3008: vim-7.0-warning.patch
Patch3009: vim-7.4-syncolor.patch
Patch3011: vim72-rh514717.patch
Patch3012: vim-7.3-manpage-typo-668894-675480.patch
Patch3013: vim-manpagefixes-948566.patch
Patch3014: vim-7.4-licensemacro-1151450.patch
Patch3015: vim-7.4-ssh-keywords.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-devel python3-devel ncurses-devel gettext perl-devel
BuildRequires: perl(ExtUtils::Embed) perl(ExtUtils::ParseXS)
BuildRequires: libacl-devel gpm-devel autoconf file
%if %{WITH_SELINUX}
BuildRequires: libselinux-devel
%endif
%if "%{withruby}" == "1"
Buildrequires: ruby-devel ruby
%endif
%if "%{withlua}" == "1"
Buildrequires: lua-devel
%endif
%if %{desktop_file}
# for /usr/bin/desktop-file-install
Requires: desktop-file-utils
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
%endif
Epoch: 2
Conflicts: filesystem < 3

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%package common
Summary: The common files needed by any version of the VIM editor
Group: Applications/Editors
Conflicts: man-pages-fr < 0.9.7-14
Conflicts: man-pages-it < 0.3.0-17
Conflicts: man-pages-pl < 0.24-2
Requires: %{name}-filesystem

%description common
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-common package contains files which every VIM binary will need in
order to run.

If you are installing vim-enhanced or vim-X11, you'll also need
to install the vim-common package.

%package spell
Summary: The dictionaries for spell checking. This package is optional
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release}

%description spell
This subpackage contains dictionaries for vim spell checking in
many different languages.

%package minimal
Summary: A minimal version of the VIM editor
Group: Applications/Editors
Provides: vi = %{version}-%{release}
Provides: /bin/vi = %{version}

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more. The
vim-minimal package includes a minimal version of VIM, which is
installed into /bin/vi for use when only the root partition is
present. NOTE: The online help is only available when the vim-common
package is installed.

%package enhanced
Summary: A version of the VIM editor which includes recent enhancements
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release} which
Provides: vim = %{version}-%{release}
Provides: mergetool = %{version}-%{release}
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description enhanced
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-enhanced package contains a version of VIM with extra, recently
introduced features like Python and Perl interpreters.

Install the vim-enhanced package if you'd like to use a version of the
VIM editor which includes recently added enhancements like
interpreters for the Python and Perl scripting languages.  You'll also
need to install the vim-common package.

%package filesystem
Summary: VIM filesystem layout
Group: Applications/Editors

%Description filesystem
This package provides some directories which are required by other
packages that add vim files, p.e.  additional syntax files or filetypes.

%package X11
Summary: The VIM version of the vi editor for the X Window System
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release} libattr >= 2.4 gtk2 >= 2.6
Provides: gvim = %{version}-%{release}
Provides: mergetool = %{version}-%{release}
BuildRequires: gtk2-devel libSM-devel libXt-devel libXpm-devel
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: hicolor-icon-theme

%description X11
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and
more. VIM-X11 is a version of the VIM editor which will run within the
X Window System.  If you install this package, you can run VIM as an X
application with a full GUI interface and mouse support.

Install the vim-X11 package if you'd like to try out a version of vi
with graphics and mouse capabilities.  You'll also need to install the
vim-common package.

%prep
%setup -q -b 0 -n vim-%{version}
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2002 -p1
%patch2003 -p1
%if %{withhunspell}
%patch2011 -p1
%endif
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

# install spell files
%if %{withvimspell}
%{__tar} xjf %{SOURCE13}
%endif

%patch3000 -p1
%patch3002 -p1
%patch3004 -p1
%patch3006 -p1
%patch3007 -p1
%patch3008 -p1
%patch3009 -p1
%patch3011 -p1
%patch3012 -p1

%patch3013 -p1
%patch3015 -p1

%build
cp -f %{SOURCE5} .
cd src
autoconf

sed -e "s+VIMRCLOC	= \$(VIMLOC)+VIMRCLOC	= /etc+" Makefile > Makefile.tmp
mv -f Makefile.tmp Makefile

export CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
export CXXFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"

cp -f os_unix.h os_unix.h.save
cp -f ex_cmds.c ex_cmds.c.save

perl -pi -e "s/help.txt/vi_help.txt/"  os_unix.h ex_cmds.c
perl -pi -e "s/\/etc\/vimrc/\/etc\/virc/"  os_unix.h
%configure --prefix=%{_prefix} --with-features=small --with-x=no \
  --enable-multibyte \
  --disable-netbeans \
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=ncurses --enable-gui=no --disable-gpm --exec-prefix=/ \
  --with-compiledby="<bugzilla@redhat.com>" \
  --with-modified-by="<bugzilla@redhat.com>"

make VIMRCLOC=/etc VIMRUNTIMEDIR=/usr/share/vim/%{vimdir} %{?_smp_mflags}
cp vim minimal-vim
make clean

mv -f os_unix.h.save os_unix.h
mv -f ex_cmds.c.save ex_cmds.c

%configure --with-features=huge \
  --enable-pythoninterp=dynamic \
  --enable-python3interp=dynamic \
  --enable-perlinterp \
  --disable-tclinterp --with-x=yes \
  --enable-xim --enable-multibyte \
  --with-tlib=ncurses \
  --enable-gtk2-check --enable-gui=gtk2 \
  --with-compiledby="<bugzilla@redhat.com>" --enable-cscope \
  --with-modified-by="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp=dynamic \
%else
  --disable-rubyinterp \
%endif
%if "%{withlua}" == "1"
  --enable-luainterp=dynamic \
%else
  --disable-luainterp \
%endif

make VIMRCLOC=/etc VIMRUNTIMEDIR=/usr/share/vim/%{vimdir} %{?_smp_mflags}
cp vim gvim
make clean

%configure --prefix=%{_prefix} --with-features=huge \
 --enable-pythoninterp=dynamic \
 --enable-python3interp=dynamic \
 --enable-perlinterp \
 --disable-tclinterp \
 --with-x=no \
 --enable-gui=no --exec-prefix=%{_prefix} --enable-multibyte \
 --enable-cscope --with-modified-by="<bugzilla@redhat.com>" \
 --with-tlib=ncurses \
 --with-compiledby="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp=dynamic \
%else
  --disable-rubyinterp \
%endif
%if "%{withlua}" == "1"
  --enable-luainterp=dynamic \
%else
  --disable-luainterp \
%endif

make VIMRCLOC=/etc VIMRUNTIMEDIR=/usr/share/vim/%{vimdir} %{?_smp_mflags}
cp vim enhanced-vim

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/vimfiles/{after,autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
mkdir -p %{buildroot}/%{_datadir}/%{name}/vimfiles/after/{autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
cp -f %{SOURCE11} .
%if %{?fedora}%{!?fedora:0} >= 16 || %{?rhel}%{!?rhel:0} >= 6
cp -f %{SOURCE15} %{buildroot}/%{_datadir}/%{name}/vimfiles/template.spec
%else
cp -f %{SOURCE14} %{buildroot}/%{_datadir}/%{name}/vimfiles/template.spec
%endif
cp runtime/doc/uganda.txt LICENSE
# Those aren't Linux info files but some binary files for Amiga:
rm -f README*.info


cd src
make install DESTDIR=%{buildroot} BINDIR=%{_bindir} VIMRCLOC=/etc VIMRUNTIMEDIR=/usr/share/vim/%{vimdir}
make installgtutorbin  DESTDIR=%{buildroot} BINDIR=%{_bindir} VIMRCLOC=/etc VIMRUNTIMEDIR=/usr/share/vim/%{vimdir}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m755 minimal-vim %{buildroot}%{_bindir}/vi
install -m755 enhanced-vim %{buildroot}%{_bindir}/vim
install -m755 gvim %{buildroot}%{_bindir}/gvim
install -p -m644 %{SOURCE7} \
   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gvim.png
install -p -m644 %{SOURCE8} \
   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gvim.png
install -p -m644 %{SOURCE9} \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gvim.png
install -p -m644 %{SOURCE10} \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gvim.png

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/gvim.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: Bram@moolenaar.net>
SentUpstream: 2014-05-22
-->
<application>
  <id type="desktop">gvim.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>Vim</project_license>
  <description>
    <p>
     Vim is an advanced text editor that seeks to provide the power of the
     de-facto Unix editor 'Vi', with a more complete feature set.
     It's useful whether you're already using vi or using a different editor.
    </p>
    <p>
     Vim is a highly configurable text editor built to enable efficient text
     editing.
     Vim is often called a "programmer's editor," and so useful for programming
     that many consider it an entire IDE. It's not just for programmers, though.
     Vim is perfect for all kinds of text editing, from composing email to
     editing configuration files.
    </p>
  </description>
  <url type="homepage">http://www.vim.org/</url>
</application>
EOF

( cd %{buildroot}
  ln -sf vi ./%{_bindir}/rvi
  ln -sf vi ./%{_bindir}/rview
  ln -sf vi ./%{_bindir}/view
  ln -sf vi ./%{_bindir}/ex
  ln -sf vim ./%{_bindir}/rvim
  ln -sf vim ./%{_bindir}/vimdiff
  perl -pi -e "s,%{buildroot},," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz
  ln -sf gvim ./%{_bindir}/gview
  ln -sf gvim ./%{_bindir}/gex
  ln -sf gvim ./%{_bindir}/evim
  ln -sf gvim ./%{_bindir}/gvimdiff
  ln -sf gvim ./%{_bindir}/vimx
  %if "%{desktop_file}" == "1"
    mkdir -p %{buildroot}/%{_datadir}/applications
    desktop-file-install \
    %if 0%{?fedora} && 0%{?fedora} < 19
        --vendor fedora \
    %endif
        --dir %{buildroot}/%{_datadir}/applications \
        %{SOURCE3}
        # --add-category "Development;TextEditor;X-Red-Hat-Base" D\
  %else
    mkdir -p ./%{_sysconfdir}/X11/applnk/Applications
    cp %{SOURCE3} ./%{_sysconfdir}/X11/applnk/Applications/gvim.desktop
  %endif
  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./%{_datadir}/%{name}/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

pushd %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tutor
mkdir conv
   iconv -f CP1252 -t UTF8 tutor.ca > conv/tutor.ca
   iconv -f CP1252 -t UTF8 tutor.it > conv/tutor.it
   #iconv -f CP1253 -t UTF8 tutor.gr > conv/tutor.gr
   iconv -f CP1252 -t UTF8 tutor.fr > conv/tutor.fr
   iconv -f CP1252 -t UTF8 tutor.es > conv/tutor.es
   iconv -f CP1252 -t UTF8 tutor.de > conv/tutor.de
   #iconv -f CP737 -t UTF8 tutor.gr.cp737 > conv/tutor.gr.cp737
   #iconv -f EUC-JP -t UTF8 tutor.ja.euc > conv/tutor.ja.euc
   #iconv -f SJIS -t UTF8 tutor.ja.sjis > conv/tutor.ja.sjis
   iconv -f UTF8 -t UTF8 tutor.ja.utf-8 > conv/tutor.ja.utf-8
   iconv -f UTF8 -t UTF8 tutor.ko.utf-8 > conv/tutor.ko.utf-8
   iconv -f CP1252 -t UTF8 tutor.no > conv/tutor.no
   iconv -f ISO-8859-2 -t UTF8 tutor.pl > conv/tutor.pl
   iconv -f ISO-8859-2 -t UTF8 tutor.sk > conv/tutor.sk
   iconv -f KOI8R -t UTF8 tutor.ru > conv/tutor.ru
   iconv -f CP1252 -t UTF8 tutor.sv > conv/tutor.sv
   mv -f tutor.ja.euc tutor.ja.sjis tutor.ko.euc tutor.pl.cp1250 tutor.zh.big5 tutor.ru.cp1251 tutor.zh.euc conv/
   rm -f tutor.ca tutor.de tutor.es tutor.fr tutor.gr tutor.it tutor.ja.utf-8 tutor.ko.utf-8 tutor.no tutor.pl tutor.sk tutor.ru tutor.sv
mv -f conv/* .
rmdir conv
popd

# Dependency cleanups
chmod 644 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl \
 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tools/*.pl \
 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
cat >%{buildroot}/%{_sysconfdir}/profile.d/vim.sh <<EOF
if [ -n "\$BASH_VERSION" -o -n "\$KSH_VERSION" -o -n "\$ZSH_VERSION" ]; then
  [ -x %{_bindir}/id ] || return
  ID=\`/usr/bin/id -u\`
  [ -n "\$ID" -a "\$ID" -le 200 ] && return
  # for bash and zsh, only if no alias is already set
  alias vi >/dev/null 2>&1 || alias vi=vim
fi
EOF
cat >%{buildroot}/%{_sysconfdir}/profile.d/vim.csh <<EOF
if ( -x /usr/bin/id ) then
    if ( "\`/usr/bin/id -u\`" > 200 ) then
        alias vi vim
    endif
endif
EOF
chmod 0644 %{buildroot}/%{_sysconfdir}/profile.d/*
install -p -m644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/vimrc
install -p -m644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/virc
(cd %{buildroot}/%{_datadir}/%{name}/%{vimdir}/doc;
 gzip -9 *.txt
 gzip -d help.txt.gz version7.txt.gz sponsor.txt.gz
 cp %{SOURCE12} .
 cat tags | sed -e 's/\t\(.*.txt\)\t/\t\1.gz\t/;s/\thelp.txt.gz\t/\thelp.txt\t/;s/\tversion7.txt.gz\t/\tversion7.txt\t/;s/\tsponsor.txt.gz\t/\tsponsor.txt\t/' > tags.new; mv -f tags.new tags
cat >> tags << EOF
vi_help.txt	vi_help.txt	/*vi_help.txt*
vi-author.txt	vi_help.txt	/*vi-author*
vi-Bram.txt	vi_help.txt	/*vi-Bram*
vi-Moolenaar.txt	vi_help.txt	/*vi-Moolenaar*
vi-credits.txt	vi_help.txt	/*vi-credits*
EOF
LANG=C sort tags > tags.tmp; mv tags.tmp tags
 )
(cd ../runtime; rm -rf doc; ln -svf ../../vim/%{vimdir}/doc docs;) 
rm -f %{buildroot}/%{_datadir}/vim/%{vimdir}/macros/maze/maze*.c
rm -rf %{buildroot}/%{_datadir}/vim/%{vimdir}/tools
rm -rf %{buildroot}/%{_datadir}/vim/%{vimdir}/doc/vim2html.pl
rm -f %{buildroot}/%{_datadir}/vim/%{vimdir}/tutor/tutor.gr.utf-8~
( cd %{buildroot}/%{_mandir}
  for i in `find ??/ -type f`; do
    if [[ "`file $i`" == *UTF-8\ Unicode\ text* ]]; then
      continue
    fi
    bi=`basename $i`
    iconv -f latin1 -t UTF8 $i > %{buildroot}/$bi
    mv -f %{buildroot}/$bi $i
  done
)

# Remove not UTF-8 manpages
for i in pl.ISO8859-2 it.ISO8859-1 ru.KOI8-R fr.ISO8859-1; do
  rm -rf %{buildroot}/%{_mandir}/$i
done

# use common man1/ru directory
mv %{buildroot}/%{_mandir}/ru.UTF-8 %{buildroot}/%{_mandir}/ru

# Remove duplicate man pages
for i in fr.UTF-8 it.UTF-8 pl.UTF-8; do
  rm -rf %{buildroot}/%{_mandir}/$i
done

for i in rvim.1 gvim.1 gex.1 gview.1 vimx.1; do 
  echo ".so man1/vim.1" > %{buildroot}/%{_mandir}/man1/$i
done
echo ".so man1/vimdiff.1" > %{buildroot}/%{_mandir}/man1/gvimdiff.1
echo ".so man1/vimtutor.1" > %{buildroot}/%{_mandir}/man1/gvimtutor.1
mkdir -p %{buildroot}/%{_mandir}/man5
for i in virc.5 vimrc.5; do 
  echo ".so man1/vim.1" > %{buildroot}/%{_mandir}/man5/$i
done
touch %{buildroot}/%{_datadir}/%{name}/vimfiles/doc/tags

%post X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /%{_bindir}/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --ignore-theme-index -q %{_datadir}/icons/hicolor
fi
update-desktop-database &> /dev/null ||:

%postun X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /%{_bindir}/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --ignore-theme-index -q %{_datadir}/icons/hicolor
fi
update-desktop-database &> /dev/null ||:

%clean
rm -rf %{buildroot}

%files common
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/vimrc
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README*
%doc runtime/docs
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/vimfiles/template.spec
%dir %{_datadir}/%{name}/%{vimdir}
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/doc
%{_datadir}/%{name}/%{vimdir}/*.vim
%{_datadir}/%{name}/%{vimdir}/ftplugin
%{_datadir}/%{name}/%{vimdir}/indent
%{_datadir}/%{name}/%{vimdir}/keymap
%{_datadir}/%{name}/%{vimdir}/lang/*.vim
%{_datadir}/%{name}/%{vimdir}/lang/*.txt
%dir %{_datadir}/%{name}/%{vimdir}/lang
%{_datadir}/%{name}/%{vimdir}/macros
%{_datadir}/%{name}/%{vimdir}/plugin
%{_datadir}/%{name}/%{vimdir}/print
%{_datadir}/%{name}/%{vimdir}/syntax
%{_datadir}/%{name}/%{vimdir}/tutor
%if ! %{withvimspell}
%{_datadir}/%{name}/%{vimdir}/spell
%endif
%lang(af) %{_datadir}/%{name}/%{vimdir}/lang/af
%lang(ca) %{_datadir}/%{name}/%{vimdir}/lang/ca
%lang(cs) %{_datadir}/%{name}/%{vimdir}/lang/cs
%lang(cs.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/cs.cp1250
%lang(de) %{_datadir}/%{name}/%{vimdir}/lang/de
%lang(en_GB) %{_datadir}/%{name}/%{vimdir}/lang/en_GB
%lang(eo) %{_datadir}/%{name}/%{vimdir}/lang/eo
%lang(es) %{_datadir}/%{name}/%{vimdir}/lang/es
%lang(fi) %{_datadir}/%{name}/%{vimdir}/lang/fi
%lang(fr) %{_datadir}/%{name}/%{vimdir}/lang/fr
%lang(ga) %{_datadir}/%{name}/%{vimdir}/lang/ga
%lang(it) %{_datadir}/%{name}/%{vimdir}/lang/it
%lang(ja) %{_datadir}/%{name}/%{vimdir}/lang/ja
%lang(ja.euc-jp) %{_datadir}/%{name}/%{vimdir}/lang/ja.euc-jp
%lang(ja.sjis) %{_datadir}/%{name}/%{vimdir}/lang/ja.sjis
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko.UTF-8
%lang(nb) %{_datadir}/%{name}/%{vimdir}/lang/nb
%lang(nl) %{_datadir}/%{name}/%{vimdir}/lang/nl
%lang(no) %{_datadir}/%{name}/%{vimdir}/lang/no
%lang(pl) %{_datadir}/%{name}/%{vimdir}/lang/pl
%lang(pl.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/pl.UTF-8
%lang(pl.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/pl.cp1250
%lang(pt_BR) %{_datadir}/%{name}/%{vimdir}/lang/pt_BR
%lang(ru) %{_datadir}/%{name}/%{vimdir}/lang/ru
%lang(ru.cp1251) %{_datadir}/%{name}/%{vimdir}/lang/ru.cp1251
%lang(sk) %{_datadir}/%{name}/%{vimdir}/lang/sk
%lang(sk.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/sk.cp1250
%lang(sv) %{_datadir}/%{name}/%{vimdir}/lang/sv
%lang(uk) %{_datadir}/%{name}/%{vimdir}/lang/uk
%lang(uk.cp1251) %{_datadir}/%{name}/%{vimdir}/lang/uk.cp1251
%lang(vi) %{_datadir}/%{name}/%{vimdir}/lang/vi
%lang(zh_CN) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN
%lang(zh_CN.cp936) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.cp936
%lang(zh_TW) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW
%lang(zh_CN.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.UTF-8
%lang(zh_TW.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW.UTF-8
/%{_bindir}/xxd
%{_mandir}/man1/ex.*
%{_mandir}/man1/gex.*
%{_mandir}/man1/gview.*
%{_mandir}/man1/gvim*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vi.*
%{_mandir}/man1/view.*
%{_mandir}/man1/vim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*
%{_mandir}/man1/vimx.*
%{_mandir}/man1/xxd.*
%{_mandir}/man5/vimrc.*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*

%if %{withvimspell}
%files spell
%defattr(-,root,root)
%dir %{_datadir}/%{name}/%{vimdir}/spell
%{_datadir}/%{name}/vim70/spell/cleanadd.vim
%lang(af) %{_datadir}/%{name}/%{vimdir}/spell/af.*
%lang(am) %{_datadir}/%{name}/%{vimdir}/spell/am.*
%lang(bg) %{_datadir}/%{name}/%{vimdir}/spell/bg.*
%lang(ca) %{_datadir}/%{name}/%{vimdir}/spell/ca.*
%lang(cs) %{_datadir}/%{name}/%{vimdir}/spell/cs.*
%lang(cy) %{_datadir}/%{name}/%{vimdir}/spell/cy.*
%lang(da) %{_datadir}/%{name}/%{vimdir}/spell/da.*
%lang(de) %{_datadir}/%{name}/%{vimdir}/spell/de.*
%lang(el) %{_datadir}/%{name}/%{vimdir}/spell/el.*
%lang(en) %{_datadir}/%{name}/%{vimdir}/spell/en.*
%lang(eo) %{_datadir}/%{name}/%{vimdir}/spell/eo.*
%lang(es) %{_datadir}/%{name}/%{vimdir}/spell/es.*
%lang(fo) %{_datadir}/%{name}/%{vimdir}/spell/fo.*
%lang(fr) %{_datadir}/%{name}/%{vimdir}/spell/fr.*
%lang(ga) %{_datadir}/%{name}/%{vimdir}/spell/ga.*
%lang(gd) %{_datadir}/%{name}/%{vimdir}/spell/gd.*
%lang(gl) %{_datadir}/%{name}/%{vimdir}/spell/gl.*
%lang(he) %{_datadir}/%{name}/%{vimdir}/spell/he.*
%lang(hr) %{_datadir}/%{name}/%{vimdir}/spell/hr.*
%lang(hu) %{_datadir}/%{name}/%{vimdir}/spell/hu.*
%lang(id) %{_datadir}/%{name}/%{vimdir}/spell/id.*
%lang(it) %{_datadir}/%{name}/%{vimdir}/spell/it.*
%lang(ku) %{_datadir}/%{name}/%{vimdir}/spell/ku.*
%lang(la) %{_datadir}/%{name}/%{vimdir}/spell/la.*
%lang(lt) %{_datadir}/%{name}/%{vimdir}/spell/lt.*
%lang(lv) %{_datadir}/%{name}/%{vimdir}/spell/lv.*
%lang(mg) %{_datadir}/%{name}/%{vimdir}/spell/mg.*
%lang(mi) %{_datadir}/%{name}/%{vimdir}/spell/mi.*
%lang(ms) %{_datadir}/%{name}/%{vimdir}/spell/ms.*
%lang(nb) %{_datadir}/%{name}/%{vimdir}/spell/nb.*
%lang(nl) %{_datadir}/%{name}/%{vimdir}/spell/nl.*
%lang(nn) %{_datadir}/%{name}/%{vimdir}/spell/nn.*
%lang(ny) %{_datadir}/%{name}/%{vimdir}/spell/ny.*
%lang(pl) %{_datadir}/%{name}/%{vimdir}/spell/pl.*
%lang(pt) %{_datadir}/%{name}/%{vimdir}/spell/pt.*
%lang(ro) %{_datadir}/%{name}/%{vimdir}/spell/ro.*
%lang(ru) %{_datadir}/%{name}/%{vimdir}/spell/ru.*
%lang(rw) %{_datadir}/%{name}/%{vimdir}/spell/rw.*
%lang(sk) %{_datadir}/%{name}/%{vimdir}/spell/sk.*
%lang(sl) %{_datadir}/%{name}/%{vimdir}/spell/sl.*
%lang(sv) %{_datadir}/%{name}/%{vimdir}/spell/sv.*
%lang(sw) %{_datadir}/%{name}/%{vimdir}/spell/sw.*
%lang(tet) %{_datadir}/%{name}/%{vimdir}/spell/tet.*
%lang(th) %{_datadir}/%{name}/%{vimdir}/spell/th.*
%lang(tl) %{_datadir}/%{name}/%{vimdir}/spell/tl.*
%lang(tn) %{_datadir}/%{name}/%{vimdir}/spell/tn.*
%lang(uk) %{_datadir}/%{name}/%{vimdir}/spell/uk.*
%lang(yi) %{_datadir}/%{name}/%{vimdir}/spell/yi.*
%lang(yi-tr) %{_datadir}/%{name}/%{vimdir}/spell/yi-tr.*
%lang(zu) %{_datadir}/%{name}/%{vimdir}/spell/zu.*
%endif

%files minimal
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/virc
%{_bindir}/ex
%{_bindir}/vi
%{_bindir}/view
%{_bindir}/rvi
%{_bindir}/rview
%{_mandir}/man1/vim.*
%{_mandir}/man1/vi.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/view.*
%{_mandir}/man5/virc.*

%files enhanced
%defattr(-,root,root)
%{_bindir}/vim
%{_bindir}/rvim
%{_bindir}/vimdiff
%{_bindir}/vimtutor
%config(noreplace) %{_sysconfdir}/profile.d/vim.*

%files filesystem
%defattr(-,root,root)
%dir %{_datadir}/%{name}/vimfiles
%dir %{_datadir}/%{name}/vimfiles/after
%dir %{_datadir}/%{name}/vimfiles/after/*
%dir %{_datadir}/%{name}/vimfiles/autoload
%dir %{_datadir}/%{name}/vimfiles/colors
%dir %{_datadir}/%{name}/vimfiles/compiler
%dir %{_datadir}/%{name}/vimfiles/doc
%ghost %{_datadir}/%{name}/vimfiles/doc/tags
%dir %{_datadir}/%{name}/vimfiles/ftdetect
%dir %{_datadir}/%{name}/vimfiles/ftplugin
%dir %{_datadir}/%{name}/vimfiles/indent
%dir %{_datadir}/%{name}/vimfiles/keymap
%dir %{_datadir}/%{name}/vimfiles/lang
%dir %{_datadir}/%{name}/vimfiles/plugin
%dir %{_datadir}/%{name}/vimfiles/print
%dir %{_datadir}/%{name}/vimfiles/spell
%dir %{_datadir}/%{name}/vimfiles/syntax
%dir %{_datadir}/%{name}/vimfiles/tutor

%files X11
%defattr(-,root,root)
%if "%{desktop_file}" == "1"
%{_datadir}/appdata/*.appdata.xml
/%{_datadir}/applications/*
%else
/%{_sysconfdir}/X11/applnk/*/gvim.desktop
%endif
%{_bindir}/gvimtutor
%{_bindir}/gvim
%{_bindir}/gvimdiff
%{_bindir}/gview
%{_bindir}/gex
%{_bindir}/vimtutor
%{_bindir}/vimx
%{_bindir}/evim
%{_mandir}/man1/evim.*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Thu Nov 26 2015 Karsten Hopp <karsten@redhat.com> 7.4.942-1
- patchlevel 942

* Wed Nov 25 2015 Karsten Hopp <karsten@redhat.com> 7.4.941-1
- patchlevel 941

* Mon Nov 23 2015 Karsten Hopp <karsten@redhat.com> 7.4.936-1
- patchlevel 936

* Sun Nov 22 2015 Karsten Hopp <karsten@redhat.com> 7.4.934-1
- patchlevel 934

* Fri Nov 20 2015 Karsten Hopp <karsten@redhat.com> 7.4.930-1
- patchlevel 930

* Wed Nov 11 2015 Karsten Hopp <karsten@redhat.com> 7.4.922-1
- patchlevel 922

* Tue Nov 10 2015 Karsten Hopp <karsten@redhat.com> 7.4.917-1
- patchlevel 917

* Wed Nov 04 2015 Karsten Hopp <karsten@redhat.com> 7.4.909-1
- patchlevel 909
- Fedora vim now uses tarballs created from upstream git instead
  of just upstream patches. Now runtime files will have fixes, too.

* Tue Nov 03 2015 Karsten Hopp <karsten@redhat.com> 7.4.908-1
- patchlevel 908

* Mon Nov 02 2015 Karsten Hopp <karsten@redhat.com> 7.4.903-1
- patchlevel 903

* Sat Oct 31 2015 Karsten Hopp <karsten@redhat.com> 7.4.902-1
- patchlevel 902

* Mon Oct 26 2015 Karsten Hopp <karsten@redhat.com> 7.4.900-1
- patchlevel 900

* Wed Oct 14 2015 Karsten Hopp <karsten@redhat.com> 7.4.898-1
- patchlevel 898

* Thu Oct 08 2015 Karsten Hopp <karsten@redhat.com> 7.4.891-1
- patchlevel 891

* Wed Oct 07 2015 Karsten Hopp <karsten@redhat.com> 7.4.890-1
- patchlevel 890

* Wed Sep 30 2015 Karsten Hopp <karsten@redhat.com> 7.4.889-1
- patchlevel 889

* Sat Sep 26 2015 Karsten Hopp <karsten@redhat.com> 7.4.884-1
- patchlevel 884

* Tue Sep 22 2015 Karsten Hopp <karsten@redhat.com> 7.4.873-2
- fix garbled xxd manpage in Japanese locale (bugzilla #1035606), Masayuki Oshima

* Tue Sep 22 2015 Karsten Hopp <karsten@redhat.com> 7.4.873-1
- add Provides: mergetool for bugzilla #990444

* Fri Sep 18 2015 Karsten Hopp <karsten@redhat.com> 7.4.873-1
- patchlevel 873

* Wed Sep 16 2015 Karsten Hopp <karsten@redhat.com> 7.4.871-1
- patchlevel 871

* Thu Sep 10 2015 Karsten Hopp <karsten@redhat.com> 7.4.865-1
- patchlevel 865

* Wed Sep 09 2015 Karsten Hopp <karsten@redhat.com> 7.4.861-1
- patchlevel 861

* Wed Sep 02 2015 Karsten Hopp <karsten@redhat.com> 7.4.854-1
- patchlevel 854

* Fri Aug 28 2015 Karsten Hopp <karsten@redhat.com> 7.4.843-1
- patchlevel 843

* Thu Aug 27 2015 Karsten Hopp <karsten@redhat.com> 7.4.841-1
- patchlevel 841

* Wed Aug 26 2015 Karsten Hopp <karsten@redhat.com> 7.4.838-1
- patchlevel 838

* Wed Aug 19 2015 Karsten Hopp <karsten@redhat.com> 7.4.827-1
- patchlevel 827
- re-enable lua
- enable python3

* Fri Jul 10 2015 Lubomir Rintel <lkundrak@v3.sk> 7.4.769-3
- drop forcing background, vim detects this since 7.4.757, rhbz#1159920

* Sat Jul 04 2015 Karsten Hopp <karsten@redhat.com> 7.4.769-1
- patchlevel 769

* Fri Jul 03 2015 Karsten Hopp <karsten@redhat.com> 7.4.768-1
- patchlevel 768

* Mon Jun 29 2015 Karsten Hopp <karsten@redhat.com> 7.4.764-1
- patchlevel 764

* Sun Jun 28 2015 Karsten Hopp <karsten@redhat.com> 7.4.763-1
- patchlevel 763

* Fri Jun 26 2015 Karsten Hopp <karsten@redhat.com> 7.4.761-1
- patchlevel 761

* Thu Jun 25 2015 Karsten Hopp <karsten@redhat.com> 7.4.757-1
- patchlevel 757

* Mon Jun 22 2015 Karsten Hopp <karsten@redhat.com> 7.4.752-1
- patchlevel 752

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:7.4.737-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Karsten Hopp <karsten@redhat.com> 7.4.737-1
- patchlevel 737

* Thu May 14 2015 Karsten Hopp <karsten@redhat.com> 7.4.729-1
- patchlevel 729

* Wed May 06 2015 Karsten Hopp <karsten@redhat.com> 7.4.728-1
- patchlevel 728

* Tue May 05 2015 Karsten Hopp <karsten@redhat.com> 7.4.726-1
- patchlevel 726

* Mon May 04 2015 Karsten Hopp <karsten@redhat.com> 7.4.723-1
- patchlevel 723

* Thu Apr 23 2015 Karsten Hopp <karsten@redhat.com> 7.4.712-1
- patchlevel 712

* Wed Apr 22 2015 Karsten Hopp <karsten@redhat.com> 7.4.711-1
- patchlevel 711

* Tue Apr 21 2015 Karsten Hopp <karsten@redhat.com> 7.4.708-1
- patchlevel 708

* Sat Apr 18 2015 Karsten Hopp <karsten@redhat.com> 7.4.703-1
- patchlevel 703

* Fri Apr 17 2015 Karsten Hopp <karsten@redhat.com> 7.4.702-1
- patchlevel 702

* Wed Apr 15 2015 Karsten Hopp <karsten@redhat.com> 7.4.701-1
- patchlevel 701

* Tue Apr 14 2015 Karsten Hopp <karsten@redhat.com> 7.4.699-1
- patchlevel 699

* Mon Apr 13 2015 Karsten Hopp <karsten@redhat.com> 7.4.698-1
- patchlevel 698

* Fri Apr 10 2015 Karsten Hopp <karsten@redhat.com> 7.4.692-1
- patchlevel 692

* Sat Apr 04 2015 Karsten Hopp <karsten@redhat.com> 7.4.691-1
- patchlevel 691

* Fri Apr 03 2015 Karsten Hopp <karsten@redhat.com> 7.4.690-1
- patchlevel 690

* Wed Apr 01 2015 Karsten Hopp <karsten@redhat.com> 7.4.688-1
- patchlevel 688

* Tue Mar 31 2015 Karsten Hopp <karsten@redhat.com> 7.4.686-1
- patchlevel 686

* Thu Mar 26 2015 Karsten Hopp <karsten@redhat.com> 7.4.683-1
- patchlevel 683

* Wed Mar 25 2015 Karsten Hopp <karsten@redhat.com> 7.4.682-1
- patchlevel 682

* Tue Mar 24 2015 Karsten Hopp <karsten@redhat.com> 7.4.681-1
- patchlevel 681

* Sun Mar 22 2015 Karsten Hopp <karsten@redhat.com> 7.4.674-1
- patchlevel 674

* Sat Mar 21 2015 Karsten Hopp <karsten@redhat.com> 7.4.672-1
- patchlevel 672

* Fri Mar 20 2015 Karsten Hopp <karsten@redhat.com> 7.4.668-1
- patchlevel 668

* Thu Mar 19 2015 Jitka Plesnikova <jplesnik@redhat.com> - 7.4.663-3
- Perl 5.22 rebuild

* Wed Mar 18 2015 Richard Hughes <rhughes@redhat.com> - 7.4.663-2
- Add an AppData file for the software center

* Sat Mar 14 2015 Karsten Hopp <karsten@redhat.com> 7.4.663-1
- patchlevel 663

* Fri Mar 13 2015 Karsten Hopp <karsten@redhat.com> 7.4.662-1
- patchlevel 662

* Sun Mar 08 2015 Karsten Hopp <karsten@redhat.com> 7.4.658-1
- patchlevel 658

* Sat Mar 07 2015 Karsten Hopp <karsten@redhat.com> 7.4.657-1
- patchlevel 657

* Fri Mar 06 2015 Karsten Hopp <karsten@redhat.com> 7.4.656-1
- patchlevel 656

* Thu Mar 05 2015 Karsten Hopp <karsten@redhat.com> 7.4.652-1
- patchlevel 652

* Sat Feb 28 2015 Karsten Hopp <karsten@redhat.com> 7.4.648-1
- patchlevel 648

* Fri Feb 27 2015 Karsten Hopp <karsten@redhat.com> 7.4.643-1
- patchlevel 643

* Fri Feb 27 2015 Dave Airlie <airlied@redhat.com> 7.4.640-4
- fix vimrc using wrong comment character

* Thu Feb 26 2015 Karsten Hopp <karsten@redhat.com> 7.4.640-3
- bump release

* Thu Feb 26 2015 Karsten Hopp <karsten@redhat.com> 7.4.640-2
- set background to dark in gnome-terminal, rhbz#1159920

* Wed Feb 25 2015 Karsten Hopp <karsten@redhat.com> 7.4.640-1
- patchlevel 640

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 7.4.629-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Feb 11 2015 Karsten Hopp <karsten@redhat.com> 7.4.629-2
- fix syntax highlighting for some ssh_config sshd_config keywords

* Wed Feb 11 2015 Karsten Hopp <karsten@redhat.com> 7.4.629-1
- patchlevel 629

* Fri Feb 06 2015 Karsten Hopp <karsten@redhat.com> 7.4.622-1
- patchlevel 622

* Thu Feb 05 2015 Karsten Hopp <karsten@redhat.com> 7.4.621-1
- patchlevel 621

* Wed Feb 04 2015 Karsten Hopp <karsten@redhat.com> 7.4.618-1
- patchlevel 618

* Tue Feb 03 2015 Karsten Hopp <karsten@redhat.com> 7.4.615-1
- patchlevel 615

* Wed Jan 28 2015 Karsten Hopp <karsten@redhat.com> 7.4.608-1
- patchlevel 608

* Tue Jan 27 2015 Karsten Hopp <karsten@redhat.com> 7.4.604-1
- patchlevel 604

* Fri Jan 23 2015 Karsten Hopp <karsten@redhat.com> 7.4.591-1
- patchlevel 591

* Wed Jan 21 2015 Karsten Hopp <karsten@redhat.com> 7.4.589-1
- patchlevel 589

* Tue Jan 20 2015 Karsten Hopp <karsten@redhat.com> 7.4.586-1
- patchlevel 586

* Sun Jan 18 2015 Karsten Hopp <karsten@redhat.com> 7.4.582-1
- patchlevel 582

* Thu Jan 15 2015 Karsten Hopp <karsten@redhat.com> 7.4.580-1
- patchlevel 580

* Wed Jan 14 2015 Karsten Hopp <karsten@redhat.com> 7.4.576-1
- patchlevel 576

* Mon Jan 12 2015 Karsten Hopp <karsten@redhat.com> 7.4.567-1
- use %%make_install in spec-template.new (rhbz#919270)

* Thu Jan 08 2015 Karsten Hopp <karsten@redhat.com> 7.4.567-1
- patchlevel 567

* Wed Jan 07 2015 Karsten Hopp <karsten@redhat.com> 7.4.566-1
- patchlevel 566

* Thu Dec 18 2014 Karsten Hopp <karsten@redhat.com> 7.4.560-1
- patchlevel 560

* Wed Dec 17 2014 Karsten Hopp <karsten@redhat.com> 7.4.557-1
- patchlevel 557

* Sun Dec 14 2014 Karsten Hopp <karsten@redhat.com> 7.4.552-1
- patchlevel 552

* Sat Dec 13 2014 Karsten Hopp <karsten@redhat.com> 7.4.546-1
- patchlevel 546

* Mon Dec 08 2014 Karsten Hopp <karsten@redhat.com> 7.4.542-1
- patchlevel 542

* Sun Dec 07 2014 Karsten Hopp <karsten@redhat.com> 7.4.541-1
- patchlevel 541

* Mon Dec 01 2014 Karsten Hopp <karsten@redhat.com> 7.4.540-1
- patchlevel 540

* Sun Nov 30 2014 Karsten Hopp <karsten@redhat.com> 7.4.539-1
- patchlevel 539

* Fri Nov 28 2014 Karsten Hopp <karsten@redhat.com> 7.4.537-1
- patchlevel 537

* Thu Nov 27 2014 Karsten Hopp <karsten@redhat.com> 7.4.534-1
- patchlevel 534

* Sun Nov 23 2014 Karsten Hopp <karsten@redhat.com> 7.4.527-1
- patchlevel 527

* Fri Nov 21 2014 Karsten Hopp <karsten@redhat.com> 7.4.526-1
- patchlevel 526

* Thu Nov 20 2014 Karsten Hopp <karsten@redhat.com> 7.4.525-1
- patchlevel 525

* Wed Nov 19 2014 Karsten Hopp <karsten@redhat.com> 7.4.521-1
- patchlevel 521

* Thu Nov 13 2014 Karsten Hopp <karsten@redhat.com> 7.4.516-1
- patchlevel 516

* Wed Nov 12 2014 Karsten Hopp <karsten@redhat.com> 7.4.512-1
- patchlevel 512

* Thu Nov 06 2014 Karsten Hopp <karsten@redhat.com> 7.4.507-1
- patchlevel 507

* Wed Nov 05 2014 Karsten Hopp <karsten@redhat.com> 7.4.502-1
- patchlevel 502

* Sat Nov 01 2014 Karsten Hopp <karsten@redhat.com> 7.4.492-1
- patchlevel 492

* Fri Oct 31 2014 Karsten Hopp <karsten@redhat.com> 7.4.491-1
- patchlevel 491

* Thu Oct 23 2014 Karsten Hopp <karsten@redhat.com> 7.4.488-1
- patchlevel 488

* Wed Oct 22 2014 Karsten Hopp <karsten@redhat.com> 7.4.487-1
- patchlevel 487

* Tue Oct 21 2014 Karsten Hopp <karsten@redhat.com> 7.4.483-1
- patchlevel 483

* Fri Oct 17 2014 Karsten Hopp <karsten@redhat.com> 7.4.481-1
- patchlevel 481

* Thu Oct 16 2014 Karsten Hopp <karsten@redhat.com> 7.4.480-1
- patchlevel 480

* Wed Oct 15 2014 Karsten Hopp <karsten@redhat.com> 7.4.477-1
- patchlevel 477

* Mon Oct 13 2014 Karsten Hopp <karsten@redhat.com> 7.4.475-2
- add support for %%license macro (Petr Šabata)

* Sat Oct 11 2014 Karsten Hopp <karsten@redhat.com> 7.4.475-1
- patchlevel 475

* Fri Oct 10 2014 Karsten Hopp <karsten@redhat.com> 7.4.473-1
- patchlevel 473

* Thu Oct 09 2014 Karsten Hopp <karsten@redhat.com> 7.4.471-1
- patchlevel 471

* Tue Oct 07 2014 Karsten Hopp <karsten@redhat.com> 7.4.465-1
- patchlevel 465

* Tue Sep 30 2014 Karsten Hopp <karsten@redhat.com> 7.4.463-1
- patchlevel 463

* Mon Sep 29 2014 Karsten Hopp <karsten@redhat.com> 7.4.462-1
- patchlevel 462

* Sat Sep 27 2014 Karsten Hopp <karsten@redhat.com> 7.4.461-1
- patchlevel 461

* Wed Sep 24 2014 Karsten Hopp <karsten@redhat.com> 7.4.460-1
- patchlevel 460

* Wed Sep 24 2014 Karsten Hopp <karsten@redhat.com> 7.4.458-1
- patchlevel 458

* Tue Sep 23 2014 Karsten Hopp <karsten@redhat.com> 7.4.457-1
- patchlevel 457

* Sat Sep 20 2014 Karsten Hopp <karsten@redhat.com> 7.4.453-1
- patchlevel 453

* Tue Sep 16 2014 Karsten Hopp <karsten@redhat.com> 7.4.444-1
- patchlevel 444

* Mon Sep 15 2014 Karsten Hopp <karsten@redhat.com> 7.4.443-1
- patchlevel 443

* Wed Sep 10 2014 Karsten Hopp <karsten@redhat.com> 7.4.442-1
- patchlevel 442

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:7.4.417-2
- Perl 5.20 rebuild

* Tue Aug 26 2014 Karsten Hopp <karsten@redhat.com> 7.4.417-1
- patchlevel 417

* Fri Aug 22 2014 Karsten Hopp <karsten@redhat.com> 7.4.410-1
- patchlevel 410
- xsubpp-path patch is obsolete now

* Fri Aug 22 2014 Karsten Hopp <karsten@redhat.com> 7.4.402-3
- fix help file names

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:7.4.402-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild


* Wed Aug 13 2014 Karsten Hopp <karsten@redhat.com> 7.4.402-1
- patchlevel 402

* Tue Aug 12 2014 Karsten Hopp <karsten@redhat.com> 7.4.401-1
- patchlevel 401

* Wed Aug  6 2014 Tom Callaway <spot@fedoraproject.org> 2:7.4.373-2
- fix license handling

* Tue Jul 22 2014 Karsten Hopp <karsten@redhat.com> 7.4.373-1
- patchlevel 373

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:7.4.307-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Karsten Hopp <karsten@redhat.com> 7.4.307-1
- patchlevel 307

* Tue Apr 29 2014 Vít Ondruch <vondruch@redhat.com> - 2:7.4.258-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Wed Apr 16 2014 Karsten Hopp <karsten@redhat.com> 7.4.258-1
- patchlevel 258

* Mon Apr 07 2014 Karsten Hopp <karsten@redhat.com> 7.4.253-1
- patchlevel 253

* Wed Mar 12 2014 Karsten Hopp <karsten@redhat.com> 7.4.204-1
- patchlevel 204

* Mon Feb 24 2014 Karsten Hopp <karsten@redhat.com> 7.4.192-1
- patchlevel 192

* Tue Feb 18 2014 Karsten Hopp <karsten@redhat.com> 7.4.182-1
- patchlevel 182

* Tue Feb 18 2014 Karsten Hopp <karsten@redhat.com> 7.4.179-2
- enable dynamic lua interpreter

* Sat Feb 15 2014 Karsten Hopp <karsten@redhat.com> 7.4.179-1
- patchlevel 179

* Wed Jan 29 2014 Karsten Hopp <karsten@redhat.com> 7.4.160-1
- patchlevel 160

* Tue Dec 17 2013 Karsten Hopp <karsten@redhat.com> 7.4.131-1
- patchlevel 131

* Wed Nov 20 2013 Karsten Hopp <karsten@redhat.com> 7.4.094-1
- patchlevel 094

* Tue Oct 15 2013 Karsten Hopp <karsten@redhat.com> 7.4.052-1
- patchlevel 052

* Wed Sep 11 2013 Karsten Hopp <karsten@redhat.com> 7.4.027-2
- update vim icons (#1004788)
- check if 'id -u' returns empty string (vim.sh)

* Wed Sep 11 2013 Karsten Hopp <karsten@redhat.com> 7.4.027-1
- patchlevel 027

* Wed Sep 04 2013 Karsten Hopp <karsten@redhat.com> 7.4.016-1
- patchlevel 016

* Wed Aug 28 2013 Karsten Hopp <karsten@redhat.com> 7.4.009-1
- patchlevel 009
  mkdir("foo/bar/", "p") gives an error message
  creating a preview window on startup messes up the screen
  new regexp engine can't be interrupted
  too easy to write a file was not decrypted (yet)

* Wed Aug 21 2013 Karsten Hopp <karsten@redhat.com> 7.4.5-1
- patchlevel 5
- when closing a window fails ":bwipe" may hang
- "vaB" while 'virtualedit' is set selects the wrong area

* Wed Aug 21 2013 Karsten Hopp <karsten@redhat.com> 7.4.3-1
- patchlevel 3, memory access error in Ruby syntax highlighting

* Wed Aug 21 2013 Karsten Hopp <karsten@redhat.com> 7.4.2-1
- patchlevel 2, pattern with two alternative look-behind matches doesn't match

* Wed Aug 21 2013 Karsten Hopp <karsten@redhat.com> 7.4.1-1
- patchlevel 1, 'ic' doesn't work for patterns such as [a-z]

* Mon Aug 12 2013 Karsten Hopp <karsten@redhat.com> 7.4.0-1
- update to vim-7.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:7.3.1314-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Karsten Hopp <karsten@redhat.com> 7.3.1314-2
- document gex and vimx in man page
- fix gvimdiff and gvimtutor man page redirects

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2:7.3.1314-2
- Perl 5.18 rebuild

* Tue Jul 09 2013 Karsten Hopp <karsten@redhat.com> 7.3.1314-1
- patchlevel 1314

* Thu Jul 04 2013 Karsten Hopp <karsten@redhat.com> 7.3.1293-1
- patchlevel 1293

* Fri Jun 14 2013 Karsten Hopp <karsten@redhat.com> 7.3.1189-1
- patchlevel 1189

* Tue Jun 04 2013 Karsten Hopp <karsten@redhat.com> 7.3.1109-1
- patchlevel 1109

* Wed May 22 2013 Karsten Hopp <karsten@redhat.com> 7.3.1004-1
- patchlevel 1004

* Wed May 22 2013 Karsten Hopp <karsten@redhat.com> 7.3.1000-1
- patchlevel 1000 !

* Tue May 21 2013 Karsten Hopp <karsten@redhat.com> 7.3.987-1
- patchlevel 987

* Tue May 21 2013 Karsten Hopp <karsten@redhat.com> 7.3.944-2
- consistent use of macros in spec file
- add some links to man pages

* Tue May 14 2013 Karsten Hopp <karsten@redhat.com> 7.3.944-1
- patchlevel 944

* Mon May 13 2013 Karsten Hopp <karsten@redhat.com> 7.3.943-2
- add BR perl(ExtUtils::ParseXS)

* Mon May 13 2013 Karsten Hopp <karsten@redhat.com> 7.3.943-1
- patchlevel 943

* Wed May 08 2013 Karsten Hopp <karsten@redhat.com> 7.3.931-1
- patchlevel 931

* Wed May 08 2013 Karsten Hopp <karsten@redhat.com> 7.3.903-1
- fix ruby version check

* Fri Apr 19 2013 Karsten Hopp <karsten@redhat.com> 7.3.903-1
- drop crv patch
- update 7.3.838 patch, it was broken upstream

* Mon Apr 15 2013 Karsten Hopp <karsten@redhat.com> 7.3.903-1
- patchlevel 903

* Mon Feb 18 2013 Karsten Hopp <karsten@redhat.com> 7.3.822-1
- patchlevel 822

* Fri Feb 15 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 7.3.797-2
- Only use --vendor for desktop-file-install on F18 or less

* Thu Jan 31 2013 Karsten Hopp <karsten@redhat.com> 7.3.797-1
- patchlevel 797

* Mon Jan 28 2013 Karsten Hopp <karsten@redhat.com> 7.3.785-1
- patchlevel 785

* Tue Nov 20 2012 Karsten Hopp <karsten@redhat.com> 7.3.715-1
- patchlevel 715

* Mon Nov 12 2012 Karsten Hopp <karsten@redhat.com> 7.3.712-1
- patchlevel 712

* Mon Nov 12 2012 Karsten Hopp <karsten@redhat.com> 7.3.682-2
- fix vim.csh syntax

* Tue Oct 23 2012 Karsten Hopp <karsten@redhat.com> 7.3.712-1
- patchlevel 712

* Mon Oct 15 2012 Karsten Hopp <karsten@redhat.com> 7.3.691-1
- patchlevel 691

* Fri Oct 05 2012 Karsten Hopp <karsten@redhat.com> 7.3.682-1
- patchlevel 682
- use --enable-rubyinterp=dynamic and --enable-pythoninterp=dynamic

* Mon Sep 03 2012 Karsten Hopp <karsten@redhat.com> 7.3.646-1
- patchlevel 646

* Tue Aug 28 2012 Karsten Hopp <karsten@redhat.com> 7.3.638-2
- fix some man page typos (#668894, #675480)
- own usr/share/vim/vimfiles/doc/tags (#845564)
- add path to csope database (#844843)

* Tue Aug 28 2012 Karsten Hopp <karsten@redhat.com> 7.3.638-1
- patchlevel 638

# vim:nrformats-=octal
