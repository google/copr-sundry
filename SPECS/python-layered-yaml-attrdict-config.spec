Name: python-layered-yaml-attrdict-config
Version: 16.1.0
Release: 1%{?dist}
Summary: Simple YAML-based configuration module.
License: WTFPL
URL: https://github.com/mk-fg/layered-yaml-attrdict-config

Source0: https://pypi.python.org/packages/source/l/layered-yaml-attrdict-config/layered-yaml-attrdict-config-%{version}.tar.gz

BuildRequires: python-devel
BuildRequires: python-setuptools
BuildArch: noarch

Provides: %{name} = %{version}-%{release}

%description
Simple YAML-based configuration module, does what it says in the name.

%prep
%setup -n layered-yaml-attrdict-config-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
* Fri Jan 29 2016 Vladimir Rusinov <vrusinov@google.com> - 16.1.0-1
- Initial package.
