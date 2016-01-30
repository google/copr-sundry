%if 0%{?fedora}
%global with_python3 1
%endif

%global srcname characteristic

Name:           python-%{srcname}
Version:        14.1.0
Release:        1%{?dist}
Summary:        Python library that eases the chores of implementing attributes

License:        MIT
URL:            https://github.com/hynek/characteristic/
Source0:        https://pypi.python.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if 0%{?fedora} > 20
BuildRequires:  pytest >= 2.6
%endif # fedora > 20

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?fedora} > 20
BuildRequires:  python3-pytest >= 2.6
%endif # fedora > 20
%endif # with_python3


%description
Say 'yes' to types but 'no' to typing!

characteristic is a Python package with class decorators that ease the chores
of implementing the most common attribute-related object protocols.

You just specify the attributes to work with and ``characteristic`` gives you:

- a nice human-readable ``__repr__``,
- a complete set of comparison methods,
- and a kwargs-based initializer (that cooperates with your existing one)

*without* writing dull boilerplate code again and again.

So put down that type-less data structures and welcome some class into your
life!


%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        Python library that eases the chores of implementing attributes

%description -n python3-%{srcname}
Say 'yes' to types but 'no' to typing!

characteristic is a Python package with class decorators that ease the chores
of implementing the most common attribute-related object protocols.

You just specify the attributes to work with and ``characteristic`` gives you:

- a nice human-readable ``__repr__``,
- a complete set of comparison methods,
- and a kwargs-based initializer (that cooperates with your existing one)

*without* writing dull boilerplate code again and again.

So put down that type-less data structures and welcome some class into your
life!
%endif # with_python3

%prep
%setup -q -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3


%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%{__python2} setup.py install --skip-build --root %{buildroot}

%if 0%{?fedora} > 20
%check
py.test --pyargs test_characteristic

%if 0%{?with_python3}
pushd %{py3dir}
py.test-%{python3_version} --pyargs test_characteristic
popd
%endif # with_python3
%endif # fedora > 20


%files
%doc README.rst LICENSE

%{python2_sitelib}/%{srcname}.py*
%{python2_sitelib}/test_characteristic.py*
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info

%if 0%{?with_python3}
%files -n python3-%{srcname}
%doc README.rst LICENSE

%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/test_%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*.py[co]
%{python3_sitelib}/__pycache__/test_%{srcname}.*.py[co]
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%endif # with_python3

%changelog
* Wed Sep 10 2014 Tom Prince <tom.prince@twistedmatrix.com> - 14.1.0-1
- Bump version to 14.1.0.
- Address review comments (#1119004).

* Sun Jul 13 2014 Tom Prince <tom.prince@twistedmatrix.com> - 0.1.0-3
- Address review comments (#1119004).

* Sat Jul 12 2014 Tom Prince <tom.prince@twistedmatrix.com> - 0.1.0-2
- Add python3 support.

* Tue Jun 10 2014 Tom Prince <tom.prince@twistedmatrix.com> - 0.1.0-1
- Initial package.
