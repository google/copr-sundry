%global full_release allmydata-tahoe-%{version}

Name:		tahoe-lafs
Summary:	Least Authority File System
Version:	1.10.2
Release:	1%{dist}
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
BuildRequires: python-foolscap
BuildRequires: python-zfec
BuildRequires: python-nevow >= 0.11.1
BuildRequires: python-twisted >= 13.0.0

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
Requires: python-twisted >= 13.0.0
Requires: python-zfec
Requires: python-zope-interface

%prep
%setup -q -n %{full_release}

%build
rm -rf setuptools-*.egg
mkdir -p setuptools-0.0.0.egg

%install
# build does not accept --single-version-externally-managed, so we actually have to build here.
%{__python} setup.py install -O1 --single-version-externally-managed --root=%{buildroot}
rm -rf %{buildroot}/%{python_sitelib}/buildtest

%files
%{_bindir}/tahoe
%{python_sitelib}/allmydata/*
%{python_sitelib}/allmydata_tahoe-*

%description
Tahoe-LAFS is a distributed, secure filesystem.

%changelog
* Sun Feb 21 2016 Vladimir Rusinov <vrusinov@google.com> - 1.10.2-1
- Version bump
- Added some new dependencies.

* Tue Oct 14 2014 Ryan Brown <ryansb@redhat.com> - 1.10.0-0.1
- New package
