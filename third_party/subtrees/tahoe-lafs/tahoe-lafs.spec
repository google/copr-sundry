%global full_release allmydata-tahoe-%{version}

Name:		tahoe-lafs
Summary:	Least Authority File System
Version:	1.10.0
Release:	0.4%{dist}
License:	GPLv2+
URL:		https://www.tahoe-lafs.org/trac/tahoe-lafs
Source0:	https://tahoe-lafs.org/source/tahoe-lafs/releases/%{full_release}.zip
Provides:	tahoe = %{version}

BuildArch: noarch
BuildRequires: git
BuildRequires: gcc-c++
BuildRequires: python2-devel
BuildRequires: libffi
BuildRequires: python-cffi
BuildRequires: openssl-devel

Requires: pyOpenSSL
Requires: pycryptopp
Requires: python-crypto
Requires: python-foolscap
Requires: python-mock
Requires: python-nevow
Requires: python-pyasn1
Requires: python-service-identity
Requires: python-setuptools
Requires: python-simplejson
Requires: python-twisted
Requires: python-zfec
Requires: python-zope-interface

%prep
%setup -q -n %{full_release}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}
rm -rf %{buildroot}/%{python_sitelib}/buildtest

%files
%{_bindir}/tahoe
%{python_sitelib}/allmydata/*
%{python_sitelib}/allmydata_tahoe-*

%description
Tahoe-LAFS is a distributed, secure filesystem.

%changelog
* Tue Oct 14 2014 Ryan Brown <ryansb@redhat.com> - 1.10.0-0.1
- New package
