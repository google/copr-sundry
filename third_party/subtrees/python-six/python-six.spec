%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2:        %global __python2 /usr/bin/python2}
%{!?python2_sitelib:  %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%if 0%{?fedora} > 12 || 0%{?rhel} > 7
%global with_python3 1

%global __python3 python3
%endif

Name:           python-six
Version:        1.10.0
Release:        1%{?dist}
Summary:        Python 2 and 3 compatibility utilities

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/six/
Source0:        http://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
# For use by selftests:
BuildRequires:  pytest
BuildRequires:  tkinter
%if 0%{?with_python3}
BuildRequires:  python3-devel
# For use by selftests:
BuildRequires:  python3-pytest
BuildRequires:  python3-tkinter
%endif
Provides:       python2-six = %{version}-%{release}

%description
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

This is the Python 2 build of the module.

%if 0%{?with_python3}
%package -n python3-six
Summary:        Python 2 and 3 compatibility utilities
Group:          Development/Languages

%description -n python3-six
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

This is the Python 3 build of the module.
%endif

%prep
%setup -q -n six-%{version}
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
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%check
py.test -rfsxX test_six.py
%if 0%{?with_python3}
pushd %{py3dir}
py.test-%{python3_version} -rfsxX test_six.py
popd
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README documentation/index.rst
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-six
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README documentation/index.rst
%{python3_sitelib}/*
%endif


%changelog
* Fri Nov 13 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 1.9.0-4
- Rebuilt for Python3.5 rebuild

* Mon Jul 13 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.9.0-3
- Added python2-six provide to python-six

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 23 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 1.9.0-1
- Upstream 1.9.0
- Packaging cleanups

* Fri Nov 14 2014 Slavek Kabrda <bkabrda@redhat.com> - 1.8.0-1
- upgrade to 1.8.0 (rhbz#1105861)

* Sun Aug  3 2014 Tom Callaway <spot@fedoraproject.org> - 1.7.3-2
- fix license handling

* Thu Jul 31 2014 Pádraig Brady <pbrady@redhat.com> - 1.7.3-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Orion Poplawski <orion@cora.nwra.com> - 1.6.1-2
- Rebuild for Python 3.4

* Tue Apr 29 2014 Matthias Runge <mrugne@redhat.com> - 1.6.1-1
- upgrade to 1.6.1 (rhbz#1076578)

* Fri Mar 07 2014 Matthias Runge <mrunge@redhat.com> - 1.5.2-1
- upgrade to 1.5.2 (rhbz#1048819)

* Mon Sep 16 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.1-1
- 1.4.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 21 2013 David Malcolm <dmalcolm@redhat.com> - 1.3.0-1
- 1.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 David Malcolm <dmalcolm@redhat.com> - 1.2.0-1
- 1.2.0 (rhbz#852658)
- add %%check section

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Conditionalized python3-six, allowing an el6 build.

* Tue Feb  7 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.0-1
- 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 David Malcolm <dmalcolm@redhat.com> - 1.0.0-1
- initial packaging


