# Created by pyp2rpm-0.4.2
%global pypi_name jsonschema

%if 0%{?fedora} > 12
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

Name:           python-%{pypi_name}
Version:        2.4.0
Release:        2%{?dist}
Summary:        An implementation of JSON Schema validation for Python

License:        MIT
URL:            http://pypi.python.org/pypi/jsonschema
Source0:        http://pypi.python.org/packages/source/j/jsonschema/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{?rhel}%{!?rhel:0} == 6
BuildRequires:  python-unittest2
BuildRequires:  python-argparse
%endif
BuildRequires:  python2-devel
BuildRequires:  python-nose
BuildRequires:  python-mock
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-mock
%endif


%description
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        An implementation of JSON Schema validation for Python
%description -n python3-%{pypi_name}
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

%build
%if 0%{?with_python3}
pushd %{py3dir}
    %{__python3} setup.py build
popd
%endif
%{__python} setup.py build


%install
%if 0%{?with_python3}
pushd %{py3dir}
    %{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%if 0%{?with_python3}
pushd %{py3dir}
    %{_bindir}/nosetests-3* -v
popd
%endif
%{_bindir}/nosetests -v

%files
%doc README.rst COPYING
%{_bindir}/jsonschema
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst COPYING
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif


%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Sep 06 2014 Alan Pevec <apevec@redhat.com> - 2.4.0-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 10 2014 Pádraig Brady <pbrady@redhat.com> - 2.3.0-1
- Latest upstream

* Tue Feb 04 2014 Matthias Runge <mrunge@redhat.com> - 2.0.0-3
- fix %%{? issues in spec

* Thu Oct 17 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.0.0-2
- add python3 subpackage (#1016207)
- add %%check

* Fri Aug 16 2013 Alan Pevec <apevec@redhat.com> 2.0.0-1
- Update to 2.0.0 release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Pádraig Brady <P@draigBrady.com> - 1.3.0-1
- Update to 1.3.0 release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Pádraig Brady <P@draigBrady.com> - 0.2-1
- Initial package.
