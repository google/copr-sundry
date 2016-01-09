%global with_python3 1
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}

Name:           python-ply
Summary:        Python Lex-Yacc
Version:        3.6
Release:        3%{?dist}
License:        BSD
Group:          System Environment/Libraries
URL:            http://www.dabeaz.com/ply/
Source0:        http://www.dabeaz.com/ply/ply-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel

%if 0%{?with_python3}
BuildRequires:          /usr/bin/2to3
BuildRequires:          python3-devel
%endif # if with_python3

# Upstream fixes for https://github.com/dabeaz/ply/issues/63
# Remove when Ply 3.7 is released.
Patch0001: 0001-Fixed-issue-63.patch
Patch0002: 0002-Minor-fix-to-account-for-bad-None-arguments-for-tabm.patch

%description
PLY is a straightforward lex/yacc implementation. Here is a list of its 
essential features:
* It is implemented entirely in Python.
* It uses LR-parsing which is reasonably efficient and well suited for larger 
  grammars.
* PLY provides most of the standard lex/yacc features including support 
  for empty productions, precedence rules, error recovery, and support 
  for ambiguous grammars.
* PLY is straightforward to use and provides very extensive error checking.
* PLY doesn't try to do anything more or less than provide the basic lex/yacc 
  functionality. In other words, it's not a large parsing framework or a 
  component of some larger system. 

%if 0%{?with_python3}
%package -n python3-ply
Summary:        Python Lex-Yacc
Group:          System Environment/Libraries
Requires:       python3-setuptools

%description -n python3-ply
PLY is a straightforward lex/yacc implementation. Here is a list of its 
essential features:
* It is implemented entirely in Python.
* It uses LR-parsing which is reasonably efficient and well suited for larger 
  grammars.
* PLY provides most of the standard lex/yacc features including support 
  for empty productions, precedence rules, error recovery, and support 
  for ambiguous grammars.
* PLY is straightforward to use and provides very extensive error checking.
* PLY doesn't try to do anything more or less than provide the basic lex/yacc 
  functionality. In other words, it's not a large parsing framework or a 
  component of some larger system.
%endif # with_python3

%prep
%setup -q -n ply-%{version}

%patch0001 -p1
%patch0002 -p1

sed -i 's|/usr/local/bin/python|/usr/bin/python|g' example/yply/yply.py
chmod -x example/yply/yply.py example/newclasscalc/calc.py example/classcalc/calc.py example/cleanup.sh

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!/usr/bin/python|#!%{__python3}|'

# The README states: "You should not convert PLY using
# 2to3--it is not necessary and may in fact break the implementation."
#
# However, one of the example files contains python 2 "print" syntax, which
# lead to syntax errors during byte-compilation
#
# So we fix this file with 2to3:
pushd %{py3dir}
  2to3 --write --nobackups ply/cpp.py
popd
%endif # with_python3

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd
%endif # with_python3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc example/
%{python_sitelib}/ply/
%{python_sitelib}/ply*.egg-info

%if 0%{?with_python3}
%files -n python3-ply
%defattr(-,root,root,-)
%doc example/
%{python3_sitelib}/ply/
%{python3_sitelib}/ply*.egg-info
%endif # with_python3

%changelog
* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 3.6-3
- Rebuilt for Python3.5 rebuild

* Tue Aug 18 2015 Stephen Gallagher <sgallagh@redhat.com> 3.6-2
- Fixes for chromium and SlimIt
- Resolves: rhbz#1242929
- Resolves: rhbz#1254372

* Tue Jul 14 2015 Stephen Gallagher <sgallagh@redhat.com> 3.6-1
- Update to latest ply 3.6 for Python 3 fixes

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 3.4-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Tom Callaway <spot@fedoraproject.org> - 3.4-1
- update to 3.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 3.3-4
- update to most recent python packaging guidelines
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Apr  3 2010 David Malcolm <dmalcolm@redhat.com> - 3.3-2
- add python3-ply subpackage

* Mon Oct 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.3-1
- update to 3.3

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 22 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.2-1
- update to 3.2, license change to BSD

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.5-2
- Rebuild for Python 2.6

* Fri Oct 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.5-1
- update to 2.5

* Mon Mar 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.2.3-2
- add example dir as doc

* Sat Mar 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.2.3-1
- Initial package for Fedora
