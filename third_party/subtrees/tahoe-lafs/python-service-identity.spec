%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-service-identity
Version:        1.0.0
Release:        2%{?dist}
Summary:        Service identity verification for pyOpenSSL

License:        MIT
URL:            https://github.com/pyca/service_identity
Source0:        https://pypi.python.org/packages/source/s/service_identity/service_identity-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if 0%{?fedora} > 20
# Fedora 20 doesn't have a new enough version of pytest,
# so skip running the tests there.
# For tests
BuildRequires:  pytest >= 2.5
BuildRequires:  python-characteristic
BuildRequires:  python-pyasn1
BuildRequires:  python-pyasn1-modules
BuildRequires:  pyOpenSSL >= 0.12
BuildRequires:  python-idna
%endif # fedora > 20

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?fedora} > 20
# For tests
BuildRequires:  python3-pytest >= 2.5
BuildRequires:  python3-characteristic
BuildRequires:  python3-pyasn1
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-pyOpenSSL >= 0.12
BuildRequires:  python3-idna
%endif # fedora > 20
%endif # with_python3

Requires:       python-characteristic
Requires:       python-pyasn1
Requires:       python-pyasn1-modules
Requires:       pyOpenSSL >= 0.12
Requires:       python-idna

%if 0%{?with_python3}
%package -n python3-service-identity
Summary:        Logging as Storytelling
Requires:       python3-six
Requires:       python3-characteristic
Requires:       python3-pyasn1
Requires:       python3-pyasn1-modules
Requires:       python3-pyOpenSSL >= 0.12
Requires:       python3-idna
%endif # with_python3

%description
Service Identity Verification for pyOpenSSL

TL;DR: Use this package if you use pyOpenSSL and don’t want to be MITMed.

service_identity aspires to give you all the tools you need for verifying
whether a certificate is valid for the intended purposes.

In the simplest case, this means host name verification. However,
service_identity implements RFC 6125 fully and plans to add other relevant RFCs
too.

%if 0%{?with_python3}
%description -n python3-service-identity
Service Identity Verification for pyOpenSSL

TL;DR: Use this package if you use pyOpenSSL and don’t want to be MITMed.

service_identity aspires to give you all the tools you need for verifying
whether a certificate is valid for the intended purposes.

In the simplest case, this means host name verification. However,
service_identity implements RFC 6125 fully and plans to add other relevant RFCs
too.
%endif # with_python3

%prep
%setup -q -n service_identity-%{version}
# Remove bundled egg-info
rm -rf service_identity.egg-info

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

%if 0%{?fedora} > 20
%check

# https://bitbucket.org/hpk42/pytest/issue/539/pytest-doctest-modules-fails-if-python
echo "collect_ignore = ['build']" >> conftest.py
py.test --doctest-modules --doctest-glob='*.rst'

%if 0%{?with_python3}
pushd %{py3dir}
# https://bitbucket.org/hpk42/pytest/issue/539/pytest-doctest-modules-fails-if-python
echo "collect_ignore = ['build']" >> conftest.py
py.test --doctest-modules --doctest-glob='*.rst'
popd
%endif # with_python3
%endif # fedora > 20

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc README.rst LICENSE
%{python2_sitelib}/service_identity
%{python2_sitelib}/service_identity-%{version}-py%{python2_version}.egg-info

%if 0%{?with_python3}
%files -n python3-service-identity
%doc README.rst LICENSE
%{python3_sitelib}/service_identity
%{python3_sitelib}/service_identity-%{version}-py%{python3_version}.egg-info
%endif # with_python3

%changelog
* Sat Jul 12 2014 tom.prince@twistedmatrix.com - 1.0.0-2
- Add python-idna dependency.

* Sat Jul 12 2014 tom.prince@twistedmatrix.com - 1.0.0-1
- Initial package.
