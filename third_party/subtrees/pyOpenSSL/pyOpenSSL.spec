%if 0%{?fedora} > 12
%global with_python3 1
%endif

Summary: Python wrapper module around the OpenSSL library
Name: pyOpenSSL
Version: 0.15.1
Release: 2%{?dist}
Source0: http://pypi.python.org/packages/source/p/pyOpenSSL/pyOpenSSL-%{version}.tar.gz

BuildArch: noarch
License: ASL 2.0
Group: Development/Libraries
Url: http://pyopenssl.sourceforge.net/

BuildRequires: python-setuptools
BuildRequires: python-sphinx

BuildRequires: python2-devel
BuildRequires: python-cryptography
Requires: python-cryptography
%if 0%{?with_python3}
BuildRequires: python3-devel
BuildRequires: python3-cryptography
%endif

%description
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes

%if 0%{?with_python3}
%package -n python3-pyOpenSSL
Summary: Python wrapper module around the OpenSSL library
Requires: python3-cryptography

%description -n python3-pyOpenSSL
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes
%endif

%package doc
Summary: Documentation for pyOpenSSL
BuildArch: noarch

%description doc
Documentation for pyOpenSSL

%prep
%setup -q -n pyOpenSSL-%{version}

%build
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

CFLAGS="%{optflags} -fno-strict-aliasing" %{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="%{optflags} -fno-strict-aliasing" %{__python3} setup.py build
popd
%endif

%{__make} -C doc html

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%files
%{python_sitelib}/OpenSSL/
%{python_sitelib}/pyOpenSSL-*.egg-info

%if 0%{?with_python3}
%files -n python3-pyOpenSSL
%{python3_sitelib}/OpenSSL/
%{python3_sitelib}/pyOpenSSL-*.egg-info
%endif

%files doc
%doc examples doc/_build/html

%changelog
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Aug  7 2015 Tomáš Mráz <tmraz@redhat.com> - 0.15.1-1
- Upgrade to 0.15.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Tomáš Mráz <tmraz@redhat.com> - 0.14-4
- allow changing the digest used when exporting CRL and use SHA1 by default

* Fri Jan 30 2015 Miro Hrončok <mhroncok@redhat.com> - 0.14-3
- Fix bogus requires (python3-cryptography should belong to python3-pyOpenSSL)

* Wed Jan  7 2015 Tomáš Mráz <tmraz@redhat.com> - 0.14-2
- Add missing python-cryptography requires

* Wed Jan  7 2015 Tomáš Mráz <tmraz@redhat.com> - 0.14-1
- Upgrade to 0.14 with help of Matěj Cepl and Kevin Fenzi

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Sep  5 2013 Tomáš Mráz <tmraz@redhat.com> - 0.13.1-1
- new upstream release fixing a security issue with string
  formatting subjectAltName of a certificate

* Tue Aug 06 2013 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.13-8
- Python 3 subpackage
- Split documentation off into noarch subpackage

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr  4 2013 Tomáš Mráz <tmraz@redhat.com> - 0.13-6
- Check for error returns which cause segfaults in FIPS mode
- Fix missing error check and leak found by gcc-with-cpychecker (#800086)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 12 2012 Petr Pisar <ppisar@redhat.com> - 0.13-4
- Do not scan documentation for dependencies (bug #865806)

* Mon Oct 08 2012 Dan Horák <dan[at]danny.cz> - 0.13-3
- rebuilt because ARM packages had wrong Requires autodetected

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Tomas Mraz <tmraz@redhat.com> - 0.13-1
- New upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Tomas Mraz <tmraz@redhat.com> - 0.12-1
- New upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 7 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10-2
- Fix incompatibility with python-2.7's socket module.

* Mon Oct  4 2010 Tomas Mraz <tmraz@redhat.com> - 0.10-1
- Merge-review cleanup by Parag Nemade (#226335)
- New upstream release

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Sep 29 2009 Matěj Cepl <mcepl@redhat.com> - 0.9-1
- New upstream release
- Fix BuildRequires to make Postscript documentation buildable

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.7-7
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Dennis Gilmore <dennis@ausil.us> - 0.7-4
- rebuild against now openssl

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.7-3
- Rebuild for Python 2.6

* Fri Sep 19 2008 Dennis Gilmore <dennis@ausil.us> - 0.7-2
- update threadsafe  patch
- bug#462807

* Mon Sep 15 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7-1
- bump to new release
- the inevitable patch fixes


* Wed Mar 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6-4
- fix horrific release tag
- fix license tag
- add egg-info

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6-3.p24.9
- Autorebuild for GCC 4.3

* Wed Dec  5 2007 Jeremy Katz <katzj@redhat.com> - 0.6-2.p24.9
- rebuild for new openssl

* Mon Dec 11 2006 Paul Howarth <paul@city-fan.org> - 0.6-1.p24.9
- add missing buildreq latex2html, needed to build HTML docs
- rewrite to be more in line with Fedora python spec template and use
  %%{python_sitearch} rather than a script-generated %%files list
- package is not relocatable - drop Prefix: tag
- buildreq perl not necessary
- fix permissions for files going into debuginfo package

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.6-1.p24.8
- rebuild for python 2.5

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.6-1.p24.7.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.6-1.p24.7.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.6-1.p24.7.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov  9 2005 Mihai Ibanescu <misa@redhat.com> - 0.6-1.p24.7
- rebuilt against newer openssl

* Wed Aug 24 2005 Jeremy Katz <katzj@redhat.com> - 0.6-1.p24.6
- add dcbw's patch to fix some threading problems

* Wed Aug 03 2005 Karsten Hopp <karsten@redhat.de> 0.6-1.p24.5
- current rpm creates .pyo files, include them in filelist

* Thu Mar 17 2005 Mihai Ibanescu <misa@redhat.com> 0.6-1.p24.4
- rebuilt

* Mon Mar 14 2005 Mihai Ibanescu <misa@redhat.com> 0.6-1.p24.3
- rebuilt

* Mon Mar  7 2005 Tomas Mraz <tmraz@redhat.com> 0.6-1.p23.2
- rebuild with openssl-0.9.7e

* Tue Nov  9 2004 Nalin Dahyabhai <nalin@redhat.com> 0.6-1.p23.1
- rebuild

* Fri Aug 13 2004 Mihai Ibanescu <misa@redhat.com> 0.6-1
- 0.6 is out

* Tue Aug 10 2004 Mihai Ibanescu <misa@redhat.com> 0.6-0.90.rc1
- release candidate

* Thu Jun 24 2004 Mihai Ibanescu <misa@redhat.com> 0.5.1-24
- rebuilt

* Mon Jun 21 2004 Mihai Ibanescu <misa@redhat.com> 0.5.1-23
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Nov  5 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-20
- rebuilt against python 2.3.2

* Fri Aug  8 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-12
- lynx no longer supported, using elinks instead (patch from
  Michael Redinger <michael.redinger@uibk.ac.at>, bug #101947 )

* Wed Jun  4 2003 Elliot Lee <sopwith@redhat.com> 0.5.1-11
- Rebuilt

* Wed Jun  4 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-10.7.x
- Built on 7.x

* Mon Mar  3 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-9
- bug #73967: Added Requires: python

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 21 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-7
- bug #84803: Added patch to expose more flags

* Fri Jan 31 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-5
- installing to %%{_libdir}

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.5.1-3
- rebuild

* Fri Jan  3 2003 Nalin Dahyabhai <nalin@redhat.com>
- Add -I and -L flags for finding Kerberos headers and libraries, in case
  they're referenced

* Tue Dec  3 2002 Mihai Ibanescu <misa@redhat.com>
- Fix for bug 73967: site-packages/OpenSSL not owned by this package
- Adding hacks around the lack of latex2html on ia64

* Tue Sep 24 2002 Mihai Ibanescu <misa@redhat.com>
- 0.5.1

* Thu Aug 29 2002 Mihai Ibanescu <misa@redhat.com>
- Building 0.5.1rc1 with version number 0.5.0.91 (this should also fix the big
  error of pushing 0.5pre previously, since it breaks rpm's version comparison
  algorithm).
- We use %%{__python}. Too bad I can't pass --define's to distutils.

* Fri Aug 16 2002 Mihai Ibanescu <misa@redhat.com>
- Building 0.5

* Fri Jun 14 2002 Mihai Ibanescu <misa@redhat.com>
- Added documentation
