%global with_python3 1

Name:           python-keyring
Version:        5.0
Release:        2%{?dist}
Summary:        Python 2 library to store and access passwords safely
License:        MIT and Python
URL:            http://bitbucket.org/kang/python-keyring-lib/
Source0:        http://pypi.python.org/packages/source/k/keyring/keyring-%{version}.zip
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Obsoletes:      %{name}-kwallet < %{version}-%{release}
Obsoletes:      %{name}-gnome < %{version}-%{release}

%description
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.
        
The keyring services supported by the Python keyring lib:
        
* **OSXKeychain**: supports the Keychain service in Mac OS X.
* **KDEKWallet**: supports the KDE's Kwallet service.
* **GnomeKeyring**: for GNOME environment.
* **SecretServiceKeyring**: for newer GNOME and KDE environments.
* **WinVaultKeyring**: supports the Windows Credential Vault
        
Besides these native password storing services provided by operating systems.
Python keyring lib also provides following build-in keyrings.
    
* **Win32CryptoKeyring**: for Windows 2k+.
* **CryptedFileKeyring**: a command line interface keyring base on PyCrypto.
* **UncryptedFileKeyring**: a keyring which leaves passwords directly in file.

%if 0%{?with_python3}
%package -n     python3-keyring
Summary:        Python 3 library to access the system keyring service
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-keyring
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.
        
The keyring services supported by the Python keyring lib:
        
* **OSXKeychain**: supports the Keychain service in Mac OS X.
* **KDEKWallet**: supports the KDE's Kwallet service.
* **GnomeKeyring**: for GNOME environment.
* **SecretServiceKeyring**: for newer GNOME and KDE environments.
* **WinVaultKeyring**: supports the Windows Credential Vault
        
Besides these native password storing services provided by operating systems.
Python keyring lib also provides following build-in keyrings.
    
* **Win32CryptoKeyring**: for Windows 2k+.
* **CryptedFileKeyring**: a command line interface keyring base on PyCrypto.
* **UncryptedFileKeyring**: a keyring which leaves passwords directly in file.
%endif

%prep
%setup -qn keyring-%{version}
rm -frv keyring.egg-info
# Drop redundant shebangs.
sed -i '1{\@^#!/usr/bin/env python@d}' keyring/cli.py
# Drop slags from upstream of using his own versioning system.
sed -i -e "\@use_vcs_version@s/^.*$/\tversion = \"%{version}\",/g" \
       -e {/\'hgtools\'/d} setup.py

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python2} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
cp -a %{buildroot}%{_bindir}/keyring %{buildroot}%{_bindir}/keyring-%{python3_version}
popd
%endif
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# Failed on Koji due to X environment not available.
#%check
#%if 0%{?with_python3}
#pushd %{py3dir}
#%{__python3} setup.py ptr
#nosetests-%{python3_version}
#popd
#%endif
#%{__python2} setup.py ptr
#nosetests

%files
%doc CHANGES.rst README.rst CONTRIBUTORS.txt
%{_bindir}/keyring
%{python2_sitelib}/keyring
%{python2_sitelib}/keyring-%{version}-py%{python2_version}.egg-info

%if 0%{?with_python3}
%files -n python3-keyring
%doc CHANGES.rst README.rst CONTRIBUTORS.txt
%{_bindir}/keyring-%{python3_version}
%{python3_sitelib}/keyring-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/keyring
%endif

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Christopher Meng <rpm@cicku.me> - 5.0-1
- Update to 5.0
- Revise license tag to match upstream.

* Sat Aug 02 2014 Christopher Meng <rpm@cicku.me> - 4.0-1
- Update to 4.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue May 13 2014 Christopher Meng <rpm@cicku.me> - 3.8-1
- Update to 3.8

* Sat Mar 08 2014 Christopher Meng <rpm@cicku.me> - 3.6-1
- Update to 3.6

* Thu Feb 13 2014 Christopher Meng <rpm@cicku.me> - 3.4-1
- Update to 3.4(BZ#1064256)
- Ensure the obsolete line works for the old packages really.

* Mon Dec 02 2013 Christopher Meng <rpm@cicku.me> - 3.3-1
- Update to 3.3(BZ#1007354,BZ#872262)
- Cleanup dependencies mess(BZ#1030944).
- Optimize the %%changelog section of the spec.

* Tue Oct 22 2013 Ratnadeep Debnath <rtnpro@gmail.com> - 3.1-1
- Bump to version 3.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Ratnadeep Debnath <rtnpro@gmail.com> 0.7-1
- Python 3 is now supported. All tests now pass under Python 3.2 on Windows and
Linux (although Linux backend support is limited). Fixes #28.
- Extension modules on Mac and Windows replaced by pure-Python ctypes
implementations. Thanks to Jérôme Laheurte.
- WinVaultKeyring now supports multiple passwords for the same service.
Fixes #47.
- Most of the tests don't require user interaction anymore.
- Entries stored in Gnome Keyring appears now with a meaningful name if you try
to browser your keyring (for ex. with Seahorse)
- Tests from Gnome Keyring no longer pollute the user own keyring.
- keyring.util.escape now accepts only unicode strings. Don't try to encode
strings passed to it.

* Tue Nov 08 2011 Ratnadeep Debnath <rtnpro@gmail.com> 0.6.2-1
- fix compiling on OSX with XCode 4.0
- Gnome keyring should not be used if there is no DISPLAY or if the dbus is not around
    (https://bugs.launchpad.net/launchpadlib/+bug/752282).
- Added keyring.http for facilitating HTTP Auth using keyring.
- Add a utility to access the keyring from the command line.

* Mon Jan 10 2011 Ratnadeep Debnath <rtnpro@gmail.com> 0.5.1-1
- Remove a spurious KDE debug message when using KWallet
- Fix a bug that caused an exception if the user canceled the KWallet dialog

* Sun Nov 28 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.5-2
- Removed sub-packages: gnome and kwallet; removed "Requires: PyKDE4 PyQt4"

* Mon Nov 22 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.5-1
- RPM for keyring-0.5

* Mon Nov 01 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.4-1
- Updated rpm to python-keyring version 0.4

* Sat Oct 30 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2-4
- Filtered gnome_keyring.so from the provides list, removed kdelibs-devel

* Sat Oct 02 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2-3
- Updated dependencies to kdelibs4-devel, some cleanup

* Tue Aug 24 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2-2
- Some updates according to bugzilla reviews

* Sat Jun 26 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2-1.3
- Some cleanup

* Sat Jun 26 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 0.2-1.2
- add KWallet subpackage

* Mon Jun 21 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 0.2-1.1
- add build dependencies
- create subpackage for gnome, disable KWallet for now
- look for files in arch-dependend site-packages

* Tue May 25 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2-1
- Incorporated some changes with reference to http://vcrhonek.fedorapeople.org/python-keyring/python-keyring.spec
- Fixed some rpmlint errors

* Wed May 19 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2
- Initial RPM package
