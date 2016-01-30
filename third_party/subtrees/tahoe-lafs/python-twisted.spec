Name:           python-twisted
Version:        14.0.0
Release:        2%{?dist}
Summary:        Twisted is a networking engine written in Python
License:        MIT
URL:            http://twistedmatrix.com/
Source0:        http://twistedmatrix.com/Releases/Twisted/14.0/Twisted-14.0.0.tar.bz2
Patch0:         python-twisted-14.0.0-doc-lore-man-fix.patch
BuildRequires:  python2-devel >= 2.6
BuildRequires:  python-zope-interface >= 3.6.0
BuildRequires:  python-crypto >= 2.6.1
BuildRequires:  pyOpenSSL >= 0.10
BuildRequires:  python-service-identity >= 1.0.0

Requires:       python-zope-interface >= 3.6.0
Requires:       pyOpenSSL >= 0.10
Requires:       python-service-identity >= 1.0.0

# Bring all provided resources back into the main package namespace.
Obsoletes:      python-twisted-conch < 14
Provides:       python-twisted-conch = %{version}-%{release}
Obsoletes:      python-twisted-core < 14
Provides:       python-twisted-core = %{version}-%{release}
Obsoletes:      python-twisted-lore < 14
Provides:       python-twisted-lore = %{version}-%{release}
Obsoletes:      python-twisted-mail < 14
Provides:       python-twisted-mail = %{version}-%{release}
Obsoletes:      python-twisted-names < 14
Provides:       python-twisted-names = %{version}-%{release}
Obsoletes:      python-twisted-news < 14
Provides:       python-twisted-news = %{version}-%{release}
Obsoletes:      python-twisted-runner < 14
Provides:       python-twisted-runner = %{version}-%{release}
Obsoletes:      python-twisted-web < 14
Provides:       python-twisted-web = %{version}-%{release}
Obsoletes:      python-twisted-web2 < 14
Provides:       python-twisted-web2 = %{version}-%{release}
Obsoletes:      python-twisted-words < 14
Provides:       python-twisted-words = %{version}-%{release}

# Capture previous namespace.
Obsoletes:      Twisted < 2.4.0-1
Provides:       Twisted = %{version}-%{release}
Obsoletes:      twisted < 2.4.0-1
Provides:       twisted = %{version}-%{release}

# python-twisted-conch
Requires:       python-crypto
Requires:       python-pyasn1
Requires:       tkinter

# python-twisted-core
Requires:       pyserial


%description
Twisted is a networking engine written in Python, supporting numerous protocols.
It contains a web server, numerous chat clients, chat servers, mail servers
and more.


%prep
%setup -q -n Twisted-%{version}
%patch0 -p1


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# egg-info
if [ -f %{buildroot}%{python2_sitearch}/Twisted*.egg-info ]; then
    echo %{buildroot}%{python2_sitearch}/Twisted*.egg-info |
        sed -e "s|^%{buildroot}||"
fi > egg-info

# no-manual-page-for-binary
%{__mkdir_p} %{buildroot}%{_mandir}/man1/
for s in conch core lore mail; do
%{__cp} -a doc/$s/man/*.1 %{buildroot}%{_mandir}/man1/
done

# devel-file-in-non-devel-package
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/runner/portmap.c
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/python/_initgroups.c
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/test/raiser.c
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/internet/iocpreactor/iocpsupport/winsock_pointers.c
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/internet/iocpreactor/iocpsupport/winsock_pointers.h
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/internet/iocpreactor/iocpsupport/iocpsupport.c
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/python/sendmsg.c

# pem-certificate
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/internet/test/fake_CAs/thing1.pem
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/mail/test/server.pem
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/test/server.pem
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/internet/test/fake_CAs/chain.pem
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/internet/test/fake_CAs/thing2.pem
%{__rm} -v %{buildroot}%{python2_sitearch}/twisted/internet/test/fake_CAs/thing2-duplicate.pem

# non-executable-script
%{__chmod} +x %{buildroot}%{python2_sitearch}/twisted/mail/test/pop3testserver.py
%{__chmod} +x %{buildroot}%{python2_sitearch}/twisted/python/test/pullpipe.py
%{__chmod} +x %{buildroot}%{python2_sitearch}/twisted/trial/test/scripttest.py

# non-standard-executable-perm
%{__chmod} 755 %{buildroot}%{python2_sitearch}/twisted/python/sendmsg.so
%{__chmod} 755 %{buildroot}%{python2_sitearch}/twisted/runner/portmap.so
%{__chmod} 755 %{buildroot}%{python2_sitearch}/twisted/test/raiser.so


%check
# bin/trial twisted
# can't get this to work within the buildroot yet due to multicast
# https://twistedmatrix.com/trac/ticket/7494


%clean
rm -rf $RPM_BUILD_ROOT


%files -f egg-info
%doc CONTRIBUTING LICENSE NEWS README
%{_bindir}/cftp
%{_bindir}/ckeygen
%{_bindir}/conch
%{_bindir}/lore
%{_bindir}/mailmail
%{_bindir}/manhole
%{_bindir}/pyhtmlizer
%{_bindir}/tap2deb
%{_bindir}/tap2rpm
%{_bindir}/tapconvert
%{_bindir}/tkconch
%{_bindir}/trial
%{_bindir}/twistd
%{_mandir}/man1/cftp.1*
%{_mandir}/man1/ckeygen.1*
%{_mandir}/man1/conch.1*
%{_mandir}/man1/lore.1*
%{_mandir}/man1/mailmail.1*
%{_mandir}/man1/manhole.1*
%{_mandir}/man1/pyhtmlizer.1*
%{_mandir}/man1/tap2deb.1*
%{_mandir}/man1/tap2rpm.1*
%{_mandir}/man1/tapconvert.1*
%{_mandir}/man1/tkconch.1*
%{_mandir}/man1/trial.1*
%{_mandir}/man1/twistd.1*
%{python2_sitearch}/twisted


%changelog
* Sun Jul 13 2014 Tom Prince <tom.prince@twistedmatrix.com> - 14.0.0-2
- Depend on python-service-identity for proper SSL certificate verification.

* Sat Jun 07 2014 Jonathan Steffan <jsteffan@fedoraproject.org> - 14.0.0-1
- Update to 14.0.0
- Ship Twisted as a fully featured package without subpackages on the advice
  of upstream and to mirror what pypi provides
- Explictly build for python2 with new macros

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 03 2012 Julian Sikorski <belegdol@fedoraproject.org> - 12.2.0-1
- Updated to 12.2.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Julian Sikorski <belegdol@fedoraproject.org> - 12.1.0-1
- Updated to 12.1.0

* Sun Feb 12 2012 Julian Sikorski <belegdol@fedoraproject.org> - 12.0.0-1
- Updated to 12.0.0

* Sat Jan 07 2012 Julian Sikorski <belegdol@fedoraproject.org> - 11.1.0-2
- Rebuilt for gcc-4.7

* Fri Nov 18 2011 Julian Sikorski <belegdol@fedoraproject.org> - 11.1.0-1
- Updated to 11.1.0
- Dropped obsolete Group, Buildroot, %%clean and %%defattr

* Sat Apr 30 2011 Julian Sikorski <belegdol@fedoraproject.org> - 11.0.0-1
- Updated to 11.0.0
- Added comment on how to obtain the PKG-INFO file

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Julian Sikorski <belegdol@fedoraproject.org> - 10.2.0-1
- Updated to 10.2.0

* Mon Nov 08 2010 Julian Sikorski <belegdol@fedoraproject.org> - 10.1.0-3
- Use python_sitelib instead of python-sitearch
- The aforementioned macros are defined in Fedora 13 and above

* Sun Nov 07 2010 Julian Sikorski <belegdol@fedoraproject.org> - 10.1.0-2
- Added egg-info file

* Tue Sep 21 2010 Julian Sikorski <belegdol@fedoraproject.org> - 10.1.0-1
- Updated to 10.1.0
- Switched to macros for versioned dependencies

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 29 2008 Matthias Saou <http://freshrpms.net/> 8.2.0-1
- Update to 8.2.0.
- Change back spec cosmetic details from Paul's to Thomas' preference.

* Wed Jul 16 2008 Matthias Saou <http://freshrpms.net/> 8.1.0-2
- Update to 8.1.0.
- Minor spec file cleanups.
- Merge back changes from Paul Howarth.

* Wed May 21 2008 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.5.0-1
- update to 2.5.0 release (only the umbrella package was missing)

* Tue Jan 16 2007 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.4.0-3
- list packages in README.fedora

* Wed Jan 03 2007 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.4.0-2
- add a README.fedora
- made noarch, since it doesn't actually install any python twisted/ module
  code
- fixed provides/obsoletes

* Wed Jun 07 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.4.0-1
- this is now a pure umbrella package

* Mon Oct 10 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.1.0-1
- upstream release

* Tue Aug 23 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.1-1
- upstream release

* Mon Apr 04 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-2
- add zsh support

* Fri Mar 25 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-1
- final release

* Thu Mar 17 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-0.2.a3
- dropped web2

* Wed Mar 16 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-0.1.a3
- upstream release

* Sat Mar 12 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-0.1.a2
- new prerelease; FE versioning

* Mon Feb 07 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0a1-1
- prep for split

* Fri Aug 20 2004 Jeff Pitman <symbiont+pyvault@berlios.de> 1.3.0-1
- new version

* Mon Apr 19 2004 Jeff Pitman <symbiont+pyvault@berlios.de> 1.2.0-3
- vaultize

* Mon Apr 12 2004 Jeff Pitman <symbiont+pyvault@berlios.de> 1.2.0-2
- require pyOpenSSL, SOAPpy, openssh-clients, crypto, dia so trial can run

