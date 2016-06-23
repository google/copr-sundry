%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_python3 1

%global srcname iso8601

Name:           python-%{srcname}
Version:        0.1.10
Release:        8%{?dist}
Summary:        Simple module to parse ISO 8601 dates

License:        MIT
URL:            http://pypi.python.org/pypi/%{srcname}/
Source0:        http://pypi.python.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
This module parses the most common forms of ISO 8601 date strings
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

%package -n python2-iso8601
Summary:        Simple module to parse ISO 8601 dates
%{?python_provide:%python_provide python2-iso8601}
# python_provide does not exist in CBS Cloud buildroot
Provides:       python-iso8601 = %{version}-%{release}
Obsoletes:      python-iso8601 < 0.1.10-6

BuildRequires:  python2-devel python-setuptools

%description -n python2-iso8601
This module parses the most common forms of ISO 8601 date strings
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

%if 0%{?with_python3}
%package -n python3-iso8601
Summary:        Simple module to parse ISO 8601 dates

BuildRequires:  python3-devel python3-setuptools

%description -n python3-iso8601
This module parses the most common forms of ISO 8601 date strings
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.
%endif

%prep
%setup -qn %{srcname}-%{version}

%build
%{__python2} setup.py build

%if 0%{?with_python3}
%{__python3} setup.py build
%endif

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%files -n python2-iso8601
%doc LICENSE README.rst
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-iso8601
%doc LICENSE README.rst
%{python3_sitelib}/*
%endif

%changelog
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 04 2015 Robert Kuska <rkuska@redhat.com> - 0.1.10-7
- Rebuilt for Python3.5 rebuild

* Mon Sep 07 2015 Chandan Kumar <chkumar246@gmail.com> - 0.1.10-6
- Added python2 along with python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 23 2014 Pádraig Brady <pbrady@redhat.com> - 0.1.10-2
- Add python3 package

* Thu Mar 27 2014 Pádraig Brady <pbrady@redhat.com> - 0.1.10-1
- Latest upstream

* Tue Nov 12 2013 Pádraig Brady <pbrady@redhat.com> - 0.1.8-1
- Latest upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul  9 2010 Ian Weller <iweller@redhat.com> - 0.1.4-2
- Correct python_sitelib macro

* Mon Jun 28 2010 Ian Weller <iweller@redhat.com> - 0.1.4-1
- Initial package build
