%global with_python3 1

Name:           python-pycparser
Summary:        C parser and AST generator written in Python
Version:        2.14
Release:        4%{?dist}
License:        BSD
Group:          System Environment/Libraries
URL:            http://github.com/eliben/pycparser
Source0:        http://github.com/eliben/pycparser/archive/release_v%{version}.tar.gz
Source1:        pycparser-0.91.1-remove-relative-sys-path.py

Patch100:       pycparser-2.10-ply.patch
# This is Fedora-specific; I don't think we should request upstream to
# remove embedded libraries from their distribuution, when we can remove
# them during packaging.

BuildArch:      noarch

BuildRequires:  python2-devel python-setuptools
# for unit tests
BuildRequires:  dos2unix
BuildRequires:  python-ply >= 3.6
BuildRequires:  python3-devel python3-setuptools
# for unit tests
BuildRequires:  python3-ply       

Requires:       python-ply >= 3.6

%description
pycparser is a complete parser for the C language, written in pure Python.
It is a module designed to be easily integrated into applications that
need to parse C source code.

%if 0%{?with_python3}
%package -n python3-pycparser
Summary:        C parser and AST generator written in Python
Group:          System Environment/Libraries
Requires:       python3-ply

%description -n python3-pycparser
pycparser is a complete parser for the C language, written in pure Python.
It is a module designed to be easily integrated into applications that
need to parse C source code.
%endif # if with_python3

%prep
%setup -q -n pycparser-release_v%{version}
%patch100 -p1 -F5 -b .ply

# remove embedded copy of ply
rm -rf pycparser/ply

# examples
%{__python} %{SOURCE1} examples
dos2unix LICENSE

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!/usr/bin/python|#!%{__python3}|'
%endif # with_python3

%build
%{__python} setup.py build
pushd build/lib/pycparser
%{__python} _build_tables.py
popd

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
pushd build/lib/pycparser
%{__python3} _build_tables.py
popd
popd
%endif # with_python3

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%check
%{__python} tests/all_tests.py 

%if 0%{?with_python3}
%{__python3} tests/all_tests.py 
pushd %{py3dir}
popd
%endif # with_python3
 
%files
%doc examples LICENSE
%{python_sitelib}/pycparser/
%{python_sitelib}/pycparser-*.egg-info

%if 0%{?with_python3}
%files -n python3-pycparser
%{python3_sitelib}/pycparser/
%{python3_sitelib}/pycparser-*.egg-info
%endif # with_python3

%changelog
* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 2.14-4
- Rebuilt for Python3.5 rebuild

* Tue Jul 14 2015 Stephen Gallagher <sgallagh@redhat.com> - 2.14-3
- Rebuild alongside python-ply 3.6

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Nathaniel McCallum <npmccallum@redhat.com> - 2.14-1
- Update to 2.14

* Wed Aug 20 2014 Eric Smith <brouhaha@fedoraproject.org> 2.10-1
- Update to latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.09.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Eric Smith <brouhaha@fedoraproject.org> 2.09.1-6
- Added Python 3 support.

* Mon Jul 22 2013 Eric Smith <brouhaha@fedoraproject.org> 2.09.1-5
- Renumbered Fedora-specific Patch1 to Patch100
- Added new Patch1 to fix table generation when the build system
  already has a python-pycparser package installed.
- Submitted Patch0 and Patch1 as upstream issues.
- Added comments about patches.

* Sun Jul 21 2013 Eric Smith <brouhaha@fedoraproject.org> 2.09.1-4
- Upstream repository is now on github.
- Fix rpmlint strange-permission complaint.
- Rename patches, Source1 to all start with pycparser-{version}, to
  simplify updating patches for future upstream releases.

* Sun Jul 21 2013 Eric Smith <brouhaha@fedoraproject.org> 2.09.1-3
- Run _build_tables.py to build the lextab.py and yacctab.py; otherwise
  they have to be regenerated at runtime for no benefit.

* Tue Mar 19 2013 Jos de Kloe <josdekloe@gmail.com> 2.09.1-2
- remove the embedded ply code

* Fri Jan 18 2013 Scott Tsai <scottt.tw@gmail.com> 2.09.1-1
- upstream 2.09.1
