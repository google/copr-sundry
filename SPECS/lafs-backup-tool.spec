%define release_date 20160229
%define github_rev 33f73846323ebd9fc626fc9ab0469306f56f5ba3
%define github_short_rev 33f7384

Name: lafs-backup-tool
Version: %{release_date}.%{github_short_rev}
Release: 1%{?dist}
Summary: Tool to securely push incremental backups to Tahoe LAFS.
License: WTFPL
URL: https://github.com/mk-fg/lafs-backup-tool/

Source0: https://github.com/mk-fg/lafs-backup-tool/archive/%{github_rev}.zip

BuildRequires: python-devel
BuildRequires: python-setuptools

BuildRequires: libacl-devel
BuildRequires: libcap-devel
BuildRequires: python-cffi
BuildRequires: python-twisted-core

Provides: %{name} = %{version}-%{release}

%description
Tool to securely push incremental (think "rsync --link-dest") backups to Tahoe
Least Authority File System.

%prep
%setup -n %{name}-%{github_rev}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitearch}/*
/usr/bin/lafs-backup-tool

%changelog
* Fri Jan 29 2016 Vladimir Rusinov <vrusinov@google.com> - 20160229-33f7384
- Initial package.
