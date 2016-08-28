Summary: Web application construction kit written in Python
Name: python-nevow
Version: 0.13.0
Release: 1%{?dist}
License: MIT
Group: Development/Languages
URL: http://divmod.org/trac/wiki/DivmodNevow
Source: https://github.com/twisted/nevow/archive/nevow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-twisted-core
Requires: python-twisted-web
BuildRequires: python-devel
BuildRequires: python-twisted-core
BuildRequires: python-twisted-web
# To fix up docs
Buildrequires: dos2unix
BuildArch: noarch

%description
Nevow (pronounced as the French "nouveau", or "noo-voh") is a web application
construction kit written in Python. It is designed to allow the programmer to
express as much of the view logic as desired in Python.


%prep
%setup -q -n nevow-nevow-%{version}
# Convert all DOS files to UNIX
find examples \( -name '*.html' -o -name '*.xml' -o -name '*.css' \) \
    -exec dos2unix {} \;

# build script is broken when setuptools is installed. This problem surfaced
# only recently because setuptools is now being dragged in by the other
# dependencies. This needs a proper fix. Workaround for now:
sed -i 's|import setuptools|import setuptoolsBAD|' setup.py

%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
# Install man page
%{__install} -D -p -m 0644 doc/man/nevow-xmlgettext.1 \
    %{buildroot}%{_mandir}/man1/nevow-xmlgettext.1
# Clean up some stuff instanned to /usr/doc/
rm %{buildroot}/usr/doc/Makefile
rm -r %{buildroot}/usr/doc/_static/
rm -r %{buildroot}/usr/doc/_templates/
rm %{buildroot}/usr/doc/conf.py
rm -r %{buildroot}/usr/doc/howto/
rm -r %{buildroot}/usr/doc/index.rst
rm -r %{buildroot}/usr/doc/man/
rm -r %{buildroot}/usr/doc/old/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/nevow-xmlgettext
%{_bindir}/nit
%{python_sitelib}/Nevow-*.egg-info
%{python_sitelib}/formless/
%{python_sitelib}/nevow/
%{python_sitelib}/twisted/plugins/nevow_widget.py*
%{_mandir}/man1/nevow-xmlgettext.1*


%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar  8 2012 Tom Callaway <spot@fedoraproject.org> - 0.10.0-6
- fix FTBFS (egg-info is a file, not a directory)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug  1 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.10.0-3
- Workaround broken setuptools setup

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jun  7 2010 Matthias Saou <http://freshrpms.net/> 0.10.0-1
- Update to 0.10.0 (#600847).
- Don't include anything from doc/* as it doesn't seem usable in 0.10.0.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.32-1
- Update to 0.9.32

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.31-2
- Rebuild for Python 2.6

* Tue Sep  2 2008 Matthias Saou <http://freshrpms.net/> 0.9.31-1
- Update to 0.9.31 (seems to fix tracebacks with Twisted 8).
- Remove no longer included NEWS.txt.

* Sun Feb  3 2008 Matthias Saou <http://freshrpms.net/> 0.9.29-3
- Include NEWS.txt instead of the untouched ChangeLog.

* Sun Feb  3 2008 Matthias Saou <http://freshrpms.net/> 0.9.29-2
- Update to 0.9.29.
- Apparently, egg-info files are only installed on F-9+.

* Mon Dec 17 2007 Matthias Saou <http://freshrpms.net/> 0.9.26-1
- Update to 0.9.26.
- Include new egg directory and twisted/plugins/nevow_widget.py files.

* Tue Apr 10 2007 Matthias Saou <http://freshrpms.net/> 0.9.18-2
- Fix some end-of-line encodings and executable bits in the docs.

* Fri Mar 23 2007 Matthias Saou <http://freshrpms.net/> 0.9.18-1
- Update to 0.9.18.

* Fri Feb  9 2007 Matthias Saou <http://freshrpms.net/> 0.9.0-1
- Initial RPM release.

