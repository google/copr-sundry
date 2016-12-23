Name:           python-foolscap
Version:        0.12.5
Release:        1%{?dist}
Summary:        Next-generation RPC protocol, intended to replace Perspective Broker
License:        MIT
URL:            http://foolscap.lothar.com
Source0:        https://pypi.python.org/packages/18/aa/995cadcacfbfb452ed6ec1c9f203d3e3caf708d8ed76d5cddf32f0766828/foolscap-%{version}.tar.gz
BuildArch:      noarch
# python-service-identity inherited.
BuildRequires:  pyOpenSSL
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-twisted-web
# This is covered by PyOpenSSL, but list here still,
# for maintainers in the future, be aware of this dep.
#Recommends:     python-service-identity
Requires:       python-twisted-web
Requires:       pyOpenSSL

%description
Foolscap (aka newpb) is a new version of Twisted's native RPC protocol, known
as 'Perspective Broker'. This allows an object in one process to be used by
code in a distant process. This module provides data marshaling, a remote
object reference system, and a capability-based security model.

%prep
%setup -qn foolscap-%{version}

%build
%{__python2} setup.py build
find doc/ -name \*.py | xargs chmod 0644

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# TODO: re-enable tests.
#%%check
#trial foolscap

%files
%doc README LICENSE NEWS doc/*
%dir %{python2_sitelib}/foolscap
%{python2_sitelib}/foolscap/*
%{python2_sitelib}/*egg-info
%{_bindir}/flappclient
%{_bindir}/flappserver
%{_bindir}/flogtool

%changelog
* Fri Dec 23 2016 Vladimir Rusinov <vrusinov@google.com> - 0.12.5-1
- Update to 0.12.5

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Feb 14 2016 Athmane Madjoudj <athmane@fedoraproject.org> 0.10.1-1
- Update to 0.10.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Christopher Meng <rpm@cicku.me> - 0.8.0-1
- Update to 0.8.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.4-1
- New upstream 0.6.4 release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 06 2012 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.6.3-1
- Upstream released new version, for compatibility with Twisted-11.1.0

* Wed Feb 09 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> - 0.6.1-1
- Upstream released new version, Twisted-10.2 compatible

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jun 13 2010 Thomas Spura <tomspur@fedoraproject.org> 0.5.1-1
- update to new version

* Wed Sep 09 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.4.2-3
- Add requirement on pyOpenSSL

* Tue Sep 08 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.4.2-2
- Disable a single test which only fails in Koji

* Mon Sep 07 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.4.2-1
- Upstream released new version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 20 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.3.2-1
- New version from upstream

* Sun Nov 02 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.3.1-3
- More cleanup according to review (#462535)

* Fri Oct 31 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.3.1-2
- Cleanup according to review (#462535)

* Tue Sep 16 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.3.1-1
- Initial import

