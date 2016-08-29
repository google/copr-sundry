Name:           python-zfec
Version:        1.4.24
Release:        10%{?dist}
Summary:        A fast erasure codec with python bindings
License:        GPLv2+
URL:            http://allmydata.org/trac/zfec
Source0:        http://pypi.python.org/packages/source/z/zfec/zfec-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  pyutil
Requires:       pyutil

%description
Fast, portable, programmable erasure coding a.k.a. "forward error correction":
the generation of redundant blocks of information such that if some blocks are
lost then the original data can be recovered from the remaining blocks.

%prep
%setup -qn zfec-%{version}

%build
CFLAGS="%{optflags}" %{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

rm -rf %{buildroot}%{_docdir}/zfec
find %{buildroot} -name *.c -delete
find %{buildroot} -name *.h -delete

# Remove shebangs on modules
sed -i '/^#!\/usr\/bin\/env/d' %{buildroot}%{python_sitearch}/zfec/test/test_zfec.py
sed -i '/^#!\/usr\/bin\/env/d' %{buildroot}%{python_sitearch}/zfec/cmdline_zfec.py
sed -i '/^#!\/usr\/bin\/env/d' %{buildroot}%{python_sitearch}/zfec/cmdline_zunfec.py

%files
%doc README.rst TODO NEWS.txt COPYING.GPL COPYING.TGPPL.html
%{_bindir}/zfec
%{_bindir}/zunfec
%{python2_sitearch}/zfec
%{python2_sitearch}/zfec-%{version}-py%{python2_version}.egg-info

%changelog
* Mon Aug 29 2016 Vladimir Rusinov <vrusinov@google.com> - 1.4.24-10
- Rebuilt

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.4.24-8
- Update patch to avoid use of bundled setuptools (#1106939)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 30 2013 Christopher Meng <rpm@cicku.me> - 1.4.24-1
- Update to 1.4.24
- SPEC cleanup, drop patch merged upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 01 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.4.22-2
- Use setuptools_trial to run unit tests

* Tue Mar 08 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.4.22-1
- Upstream released new version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.4.7-1
- Upstream released new version

* Sun Jan 31 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.4.6-1
- Upstream released new version

* Mon Sep 07 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.4.5-1
- Initial import

