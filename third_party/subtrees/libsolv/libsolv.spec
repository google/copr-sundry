%{!?ruby_vendorarch: %global ruby_vendorarch %(ruby -r rbconfig -e "puts RbConfig::CONFIG['vendorarchdir'].nil? ? RbConfig::CONFIG['sitearchdir'] : RbConfig::CONFIG['vendorarchdir']")}
%filter_provides_in %{perl_vendorarch}/.*\.so$
%filter_provides_in %{python2_sitearch}/.*\.so$
%filter_provides_in %{python3_sitearch}/.*\.so$
%bcond_without python3
%if 0%{?fedora}
%global _cmake_opts \\\
            -DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
            -DENABLE_PERL=1 \\\
            -DENABLE_PYTHON=1 \\\
            -DENABLE_RUBY=1 \\\
            -DUSE_VENDORDIRS=1 \\\
            -DFEDORA=1 \\\
            -DENABLE_DEBIAN=1 \\\
            -DENABLE_ARCHREPO=1 \\\
            -DENABLE_LZMA_COMPRESSION=1 \\\
            -DMULTI_SEMANTICS=1 \\\
            -DENABLE_COMPLEX_DEPS=1 \\\
            %{nil}
%else
%global _cmake_opts \\\
            -DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
            -DENABLE_PYTHON=1 \\\
            -DFEDORA=1 \\\
            -DENABLE_ARCHREPO=1 \\\
            -DENABLE_LZMA_COMPRESSION=1 \\\
            %{nil}
%endif
%filter_provides_in %{ruby_vendorarch}/.*\.so$
%filter_setup

Name:       libsolv
Version:    0.6.14
Release:    6%{?dist}
License:	BSD
Url:		https://github.com/openSUSE/libsolv
Source:		https://github.com/openSUSE/libsolv/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:		0001-ruby-make-compatible-with-ruby-2.2.patch

Patch1:         0001-Move-allowuninstall-map-creation.patch
Patch2:         0002-Prefer-to-autouninstall-orphans.patch
Patch3:         0003-Check-keep_orphans-flag-in-solver_addduprules.patch
Patch4:         0004-Fix-spelling-duh.patch
Patch5:         0001-Simplify-solver_addduprules-a-bit.patch
Patch6:         0002-Drop-inline-from-solver_addtodupmaps.patch
Patch7:         0003-Rename-hasdupjobs-to-needduprules.patch
Patch8:         0004-Fix-typo-in-comment.patch
Patch9:         0005-Speed-up-choice-rule-generation.patch
Patch10:        0006-Make-keep_orphans-also-keep-multiversion-orphans-ins.patch

BuildRequires:  git-core

Group:		Development/Libraries
Summary:	Package dependency solver
BuildRequires:	cmake libdb-devel expat-devel rpm-devel zlib-devel
BuildRequires:	swig 
BuildRequires:  python2-devel
%if 0%{?fedora}
BuildRequires:	perl perl-devel ruby ruby-devel
%endif
%if %{with python3}
BuildRequires:	python3-devel
%endif
BuildRequires:  xz-devel
%description
A free package dependency solver using a satisfiability algorithm. The
library is based on two major, but independent, blocks:

- Using a dictionary approach to store and retrieve package
  and dependency information.

- Using satisfiability, a well known and researched topic, for
  resolving package dependencies.

%package devel
Summary:	A new approach to package dependency solving
Group:		Development/Libraries
Requires:	libsolv-tools%{?_isa} = %{version}-%{release}
Requires:	libsolv%{?_isa} = %{version}-%{release}
Requires:	rpm-devel%{?_isa}
Requires:	cmake

%description devel
Development files for libsolv,

%package tools
Summary:	A new approach to package dependency solving
Group:		Development/Libraries
Requires:	gzip bzip2 coreutils
Requires:	libsolv%{?_isa} = %{version}-%{release}

%description tools
Package dependency solver tools.

%package demo
Summary:	Applications demoing the libsolv library
Group:		Development/Libraries
Requires:	curl gnupg2

%description demo
Applications demoing the libsolv library.

%if 0%{?fedora}
%package -n ruby-solv
Summary:	Ruby bindings for the libsolv library
Group:		Development/Languages
Requires:	libsolv%{?_isa} = %{version}-%{release}

%description -n ruby-solv
Ruby bindings for sat solver.
%endif

%package -n python2-solv
Summary:	Python bindings for the libsolv library
Group:		Development/Languages
Requires:	python2
Requires:	libsolv%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python2-solv}

%description -n python2-solv
Python bindings for sat solver.

%if %{with python3}
%package -n python3-solv
Summary:	Python 3 bindings for the libsolv library
Group:		Development/Languages
Requires:	python3
Requires:	libsolv%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-solv}

%description -n python3-solv
Python 3 bindings for sat solver.
%endif

%if 0%{?fedora}
%package -n perl-solv
Summary:	Perl bindings for the libsolv library
Group:		Development/Languages
Requires:	perl
Requires:	libsolv%{?_isa} = %{version}-%{release}

%description -n perl-solv
Perl bindings for sat solver.
%endif

%prep
%autosetup -S git

%if %{with python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%cmake %_cmake_opts \
        -DPythonLibs_FIND_VERSION=2 -DPythonLibs_FIND_VERSION_MAJOR=2
make %{?_smp_mflags}

%if %{with python3}
pushd %{py3dir}/
  %cmake %_cmake_opts \
        -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPythonLibs_FIND_VERSION=3 -DPythonLibs_FIND_VERSION_MAJOR=3
  make %{?_smp_mflags}
popd
%endif

%install
%make_install

%if %{with python3}
pushd %{py3dir}/
  %make_install
popd
%endif

%check
make ARGS="-V" test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE* README BUGS
%_libdir/libsolv.so.*
%_libdir/libsolvext.so.*

%files tools
%_bindir/archpkgs2solv
%_bindir/archrepo2solv
%if 0%{?fedora}
%_bindir/deb2solv
%endif
%_bindir/deltainfoxml2solv
%_bindir/dumpsolv
%_bindir/installcheck
%_bindir/mergesolv
%_bindir/repo2solv.sh
%_bindir/repomdxml2solv
%_bindir/rpmdb2solv
%_bindir/rpmmd2solv
%_bindir/rpms2solv
%_bindir/testsolv
%_bindir/updateinfoxml2solv

%files devel
%_libdir/libsolv.so
%_libdir/libsolvext.so
%_includedir/solv
%_datadir/cmake/Modules/FindLibSolv.cmake
%{_mandir}/man?/*
%{_libdir}/pkgconfig/%{name}.pc

%files demo
%_bindir/solv

%if 0%{?fedora}
%files -n perl-solv
%doc examples/p5solv
%{perl_vendorarch}/*

%files -n ruby-solv
%doc examples/rbsolv
%{ruby_vendorarch}/*
%endif

%files -n python2-solv
%doc examples/pysolv
%{python2_sitearch}/*

%if %{with python3}
%files -n python3-solv
%doc examples/pysolv
%{python3_sitearch}/*
%endif

%changelog
* Thu Nov 26 2015 Adam Williamson <awilliam@redhat.com> - 0.6.14-6
- revert obsolete, as %%python_provide does it (undocumented)

* Wed Nov 18 2015 Adam Williamson <awilliam@redhat.com> - 0.6.14-5
- adjust obsolete for stupid packaging

* Wed Nov 18 2015 Adam Williamson <awilliam@redhat.com> - 0.6.14-4
- python2-solv obsoletes python-solv (#1263230)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.14-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 14 2015 Michal Luscon <mluscon@redhat.com> - 0.6.14-2
- Backport patches from upstream

* Mon Oct 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.14-1
- Update to 0.6.14
- Backport patches from upstream

* Thu Sep 10 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.12-1
- Update to 0.6.12

* Wed Aug 05 2015 Jan Silhan <jsilhan@redhat.com> - 0.6.11-3
- added compile flag to support rich dependencies
- new version adding MIPS support
- Distribute testsolv in -tools subpackage (Igor Gnatenko)
- Enable python3 bindings for fedora (Igor Gnatenko)

* Tue Aug 04 2015 Adam Williamson <awilliam@redhat.com> - 0.6.11-2
- make bindings require the exact matching version of the lib (#1243737)

* Mon Jun 22 2015 Jan Silhan <jsilhan@redhat.com> - 0.6.11-1
- new version fixing segfault
- RbConfig fixed in the upstream (1928f1a), libsolv-ruby22-rbconfig.patch erased

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Jan Silhan <jsilhan@redhat.com> - 0.6.10-1
- new version fixing segfault

* Fri Mar 6 2015 Jan Silhan <jsilhan@redhat.com> - 0.6.8-3
- Rebuilt with new provides selection feature

* Mon Jan 19 2015 Vít Ondruch <vondruch@redhat.com> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Fri Jan 16 2015 Richard Hughes <richard@hughsie.com> - 0.6.8-2
- Update to latest upstream release to fix a crash in PackageKit.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild


* Mon Aug 11 2014 Jan Silhan <jsilhan@redhat.com> - 0.6.4-2
- Rebase to upstream 12af31a

* Mon Jul 28 2014 Aleš Kozumplík <akozumpl@redhat.com> - 0.6.4-1
- Rebase to upstream 5bd9589

* Mon Jul 14 2014 Jan Silhan <jsilhan@redhat.com> - 0.6.4-0.git2a5c1c4
- Rebase to upstream 2a5c1c4
- Filename selector can start with a star

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2.git6d968f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Aleš Kozumplík <ales@redhat.com> - 0.6.1-1.git6d968f1
- Rebase to upstream 6d968f1
- Fix RhBug:1049209

* Fri Apr 25 2014 Jan Silhan <jsilhan@redhat.com> - 0.6.1-0.gitf78f5de
- Rebase to 0.6.0, upstream commit f78f5de.

* Thu Apr 24 2014 Vít Ondruch <vondruch@redhat.com> - 0.6.0-0.git05baf54.1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Wed Apr 9 2014 Jan Silhan <jsilhan@redhat.com> - 0.6.0-0.git05baf54
- Rebase to 0.6.0, upstream commit 05baf54.

* Mon Dec 16 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.4.1-1.gitbcedc98
- Rebase upstream bcedc98
- Fix RhBug:1051917.

* Mon Dec 16 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.4.1-0.gita8e47f1
- Rebase to 0.4.1, upstream commit a8e47f1.

* Fri Nov 22 2013 Zdenek Pavlas <zpavlas@redhat.com> - 0.4.0-2.git4442b7f
- Rebase to 0.4.0, upstream commit 4442b7f.
- support DELTA_LOCATION_BASE for completeness

* Tue Oct 29 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.4.0-1.gitd49d319
- Rebase to 0.4.0, upstream commit d49d319.

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.3.0-9.gita59d11d
- Perl 5.18 rebuild

* Wed Jul 31 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-8.gita59d11d
- Rebase to upstream a59d11d.

* Fri Jul 19 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-7.git228d412
- Add build flags, including Deb, Arch, LZMA and MULTI_SEMANTICS. (RhBug:985905)

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.3.0-6.git228d412
- Perl 5.18 rebuild

* Mon Jun 24 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-5.git228d412
- Rebase to upstream 228d412.
- Fixes hawkey github issue https://github.com/akozumpl/hawkey/issues/13

* Thu Jun 20 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-4.git209e9cb
- Rebase to upstream 209e9cb.
- Package the new man pages.

* Thu May 16 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-3.git7399ad1
- Run 'make test' with libsolv build.

* Mon Apr 8 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-2.git7399ad1
- Rebase to upstream 7399ad1.
- Fixes RhBug:905209

* Mon Apr 8 2013 Aleš Kozumplík <akozumpl@redhat.com> - 0.3.0-1.gite372b78
- Rebase to upstream e372b78.
- Fixes RhBug:e372b78

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2.gitf663ca2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Aleš Kozumplík <akozumpl@redhat.com> - 0.0.0-17.git6c9d3eb
- Rebase to upstream 6c9d3eb.
- Drop the solv.i stdbool.h fix integrated upstream.
- Dropped the job reasons fix.

* Mon Jul 23 2012 Aleš Kozumplík <akozumpl@redhat.com> - 0.0.0-16.git1617994
- Fix build problems with Perl bindings.

* Mon Jul 23 2012 Aleš Kozumplík <akozumpl@redhat.com> - 0.0.0-15.git1617994
- Rebuilt after a failed mass rebuild.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-14.git1617994
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Aleš Kozumplik <akozumpl@redhat.com> - 0.0.0-13.git1617994%{?dist}
- preliminary fix for JOB resons in solver_describe_decision().

* Sun Jul 1 2012 Aleš Kozumplik <akozumpl@redhat.com> - 0.0.0-12.git1617994%{?dist}
- Rebase to upstream 1617994.
- Support for RPM_ADD_WITH_HDRID.

* Thu Jun  7 2012 Aleš Kozumplik <akozumpl@redhat.com> - 0.0.0-11.gitd39a42b%{?dist}
- Rebase to upstream d39a42b.
- Fix the epochs.
- Move the ruby modules into vendorarch dir, where they are expected.

* Thu May  17 2012 Aleš Kozumplik <akozumpl@redhat.com> - 0.0.0-9.git8cf7650%{?dist}
- Rebase to upstream 8cf7650.
- ruby bindings: fix USE_VENDORDIRS for Fedora.

* Thu Apr  12 2012 Aleš Kozumplik <akozumpl@redhat.com> - 0.0.0-7.gitaf1465a2%{?dist}
- Rebase to the upstream.
- Make repo_add_solv() work without stub repodata.

* Thu Apr  5 2012 Karel Klíč <kklic@redhat.com> - 0.0.0-6.git80afaf7%{?dist}
- Rebuild for the new libdb package.

* Mon Apr  2 2012 Karel Klíč <kklic@redhat.com> - 0.0.0-5.git80afaf7%{?dist}
- Rebuild for the new rpm package.

* Wed Mar 21 2012 Aleš Kozumplík <akozumpl@redhat.com> - 0.0.0-4.git80afaf7%{?dist}
- New upstream version, fix the .rpm release number.

* Wed Mar 21 2012 Aleš Kozumplík <akozumpl@redhat.com> - 0.0.0-3.git80afaf7%{?dist}
- New upstream version.

* Tue Feb  7 2012 Karel Klíč <kklic@redhat.com> - 0.0.0-2.git857fe28%{?dist}
- Adapted to Ruby 1.9.3 (workaround for broken CMake in Fedora and
  ruby template correction in bindings)

* Thu Feb  2 2012 Karel Klíč <kklic@redhat.com> - 0.0.0-1.git857fe28
- Initial packaging
- Based on Jindra Novy's spec file
- Based on upstream spec file
