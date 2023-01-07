%{!?perl_vendorarch: %define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)}
%define perlver %(eval "`%{__perl} -V:version`"; echo $version)

%global use_x11_tests 1

Name:           perl-Tk
Version:        804.033
Release:        3%{?dist}
Summary:        Perl Graphical User Interface ToolKit

Group:          Development/Libraries
License:        (GPL+ or Artistic) and SWL
URL:            http://search.cpan.org/dist/Tk/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SR/SREZIC/Tk-%{version}.tar.gz
Patch0:         perl-Tk-widget.patch
# fix segfaults as in #235666 because of broken cashing code
Patch2:         perl-Tk-seg.patch


# Versions before this have Unicode issues
BuildRequires:  perl-devel >= 3:5.8.3
BuildRequires:  freetype-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)

%if %{use_x11_tests}
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(locale)
# Image::Info is optional
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(overload)
BuildRequires:  perl(subs)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

# Tests:
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
BuildRequires:  font(:lang=en)
# Specific font is needed for tests, bug #1141117, CPAN RT#98831
BuildRequires:  liberation-sans-fonts
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(ExtUtils::Command::MM)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Optional tests:
BuildRequires:  perl(MIME::Base64)
%endif

Requires:       perl(:MODULE_COMPAT_%{perlver})
Provides:       perl(Tk::LabRadio) = 4.004
Provides:       perl(Tk) = %{version}

%{?perl_default_filter}
# Explicity filter "useless" unversioned provides. For some reason, rpm is
# detecting these both with and without version.
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Tk\\)
%global __provides_exclude %__provides_exclude|perl\\(Tk::Clipboard\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Frame\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Listbox\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Scale\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Scrollbar\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Table\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Toplevel\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Widget\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Wm\\)$


%description
This a re-port of a perl interface to Tk8.4.
C code is derived from Tcl/Tk8.4.5.
It also includes all the C code parts of Tix8.1.4 from SourceForge.
The perl code corresponding to Tix's Tcl code is not fully implemented.

Perl API is essentially the same as Tk800 series Tk800.025 but has not
been verified as compliant. There ARE differences see pod/804delta.pod.

%package devel
Summary: perl-Tk ExtUtils::MakeMaker support module
Requires: perl-Tk = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -q -n Tk-%{version}
find . -type f -exec %{__perl} -pi -e \
's,^(#!)(/usr/local)?/bin/perl\b,$1%{__perl}, if ($. == 1)' {} \;
chmod -x pod/Popup.pod Tixish/lib/Tk/balArrow.xbm
# fix for widget as docs
%patch0
%{__perl} -pi -e \
's,\@demopath\@,%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}/demos,g' demos/widget
# debian patch
#%%patch1 -p1
# patch to fix #235666 ... seems like caching code is broken
%patch2 -p1 -b .seg

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor X11LIB=%{_libdir} XFT=1
find . -name Makefile | xargs %{__perl} -pi -e 's/^\tLD_RUN_PATH=[^\s]+\s*/\t/'
make %{?_smp_mflags}

%check
%if %{use_x11_tests}
    xvfb-run -a make test
%endif

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*
mkdir __demos
cp -pR $RPM_BUILD_ROOT%{perl_vendorarch}/Tk/demos __demos
find __demos/ -type f -exec chmod -x {} \;

%files
%doc Changes README README.linux ToDo pTk/*license* __demos/demos demos/widget COPYING
%doc blib/man1/widget.1
%{_bindir}/p*
%{_bindir}/tkjpeg
%{perl_vendorarch}/auto/Tk
%{perl_vendorarch}/T*
%exclude %{perl_vendorarch}/Tk/MMutil.pm
%exclude %{perl_vendorarch}/Tk/install.pm
%exclude %{perl_vendorarch}/Tk/MakeDepend.pm
%{_mandir}/man*/*
%exclude %{_mandir}/man1/widget.1*
%exclude %{_bindir}/gedi
%exclude %{_bindir}/widget
%exclude %{perl_vendorarch}/Tk/demos

%files devel
%dir %{perl_vendorarch}/Tk
%{perl_vendorarch}/Tk/MMutil.pm
%{perl_vendorarch}/Tk/install.pm
%{perl_vendorarch}/Tk/MakeDepend.pm


%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 804.033-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 804.033-2
- Perl 5.22 rebuild

* Wed May 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 804.033-1
- 804.033 bump

* Fri Nov 07 2014 Petr Pisar <ppisar@redhat.com> - 804.032-5
- Restore compatibility with perl-ExtUtils-MakeMaker-7.00 (bug #1161470)

* Fri Sep 12 2014 Petr Pisar <ppisar@redhat.com> - 804.032-4
- Fix freetype detection
- Fix creating a window with perl 5.20 (bug #1141117)
- Enable X11 tests
- Specify all dependencies
- Fix t/fileevent2.t failure with /dev/null on stdin (bug #1141117)

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 804.032-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 804.032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Jitka Plesnikova <jplesnik@redhat.com> - 804.032-1
- 804.032 bump

* Fri Jun 20 2014 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 804.031-6
- add patch from Yaakov Selkowitz to fix freetype detection (rhbz#1110872)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 804.031-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 10 2013 Ville Skyttä <ville.skytta@iki.fi> - 804.031-4
- Use %%{_pkgdocdir} where available.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 804.031-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Jitka Plesnikova <jplesnik@redhat.com> - 804.031-2
- Update license
- Package COPYING
- Specify all dependencies
- Replace PERL_INSTALL_ROOT with DESTDIR

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 804.031-1
- 804.031 bump

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 804.030-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 804.030-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 804.030-3
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 804.030-2
- rebuild against new libjpeg

* Wed Aug 29 2012 Jitka Plesnikova <jplesnik@redhat.com> - 804.030-1
- 804.030 bump, update source link

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 804.029-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 804.029-8
- Perl 5.16 rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 804.029-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 804.029-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Iain Arnell <iarnell@gmail.com> 804.029-5
- Rebuild for libpng 1.5

* Fri Oct 21 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 804.029-4
- Split out Tk/MMutil.pm, Tk/install.pm, Tk/MakeDepend.pm into perl-Tk-devel.
  (Avoid dependency on perl-devel - BZ 741777).

* Tue Jun 21 2011 Iain Arnell <iarnell@gmail.com> 804.029-3
- Perl mass rebuild

* Tue Jun 21 2011 Iain Arnell <iarnell@gmail.com> 804.029-2
- properly filter useless provides

* Fri Jun 17 2011 Iain Arnell <iarnell@gmail.com> 804.029-1
- update to 804.029_500 development version to fix FTBFS with perl 5.14
- clean up spec for modern rpmbuild
- use perl_default_filter and filter useless provides

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 804.028-16
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 804.028-15
- Perl 5.14 mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 804.028-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 804.028-13
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 804.028-12
- Mass rebuild with perl-5.12.0 & update to development release

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 804.028-11
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 804.028-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 804.028-9
- fix getOpenFile (#487122)

* Mon Jun 15 2009 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 804.028-8
- fix events (#489228, #491536, #506496)

* Thu Mar 19 2009 Stepan Kasal <skasal@redhat.com> - 804.028-7
- perl-Tk-XIM.patch (#489228)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 804.028-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 804.028-5
- rework patch2 to fix menu and test case failures (bz 431330, upstream 33880)

* Tue Feb 05 2008 Tom "spot" Callaway <tcallawa@redhat.com>
- 804.028-4
- rebuild for new perl

* Tue Feb 05 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 804.028-3
- fix #431529 gif overflow in tk (see also #431518)

* Fri Jan 04 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 804.028-2
- add relevant parts of debian patch
- add patch for #235666

* Wed Jan 02 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 804.028-1
- version upgrade
- fix #210718 SIGSEGV on exit from texdoctk
- fix #234404 Cannot manage big listboxes
- fix #235666 Segfault occurs when using Perl-Tk on FC6

* Wed Dec 19 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 804.027-13
- fix BR

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 804.027-12
- rebuild for buildid

* Sun Apr 01 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-11
- F7 rebuild (#234404)

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-10
- FE6 rebuild

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-9
- Rebuild for Fedora Extras 5

* Fri Nov 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-8
- modular xorg integration

* Sun Jul 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-7
- fix #164716

* Mon Jun 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-6
- some small cleanups
- add dist tag

* Thu Jun 16 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-5
- exclude gedi
- move widget to doc dir and patch it to work from there

* Wed Jun 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-4
- more cleanups from Ville Skyttä

* Wed Jun 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-3
- more cleanups

* Tue Jun 14 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-2
- add some stuff (e.g. xft) suggested by Steven Pritchard

* Tue Jun 14 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
804.027-1
- rebuild for fc4

* Fri Jun 04 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:804.027-0.fdr.1
- Initial Version (thanks to perl-Archive-Zip spec)
