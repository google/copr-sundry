%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 1
%global with_bundled 0
%global with_debug 0
# test fails
%global with_check 0
%global with_unit_test 1
%else
%global with_devel 0
%global with_bundled 0
%global with_debug 0
%global with_check 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         go-check
%global repo            check
# https://github.com/go-check/check
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     gopkg.in/check.v1
%global import_path_sec launchpad.net/gocheck
%global commit          4f90aeace3a26ad7021961c297b22c42160c7b25
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global gimport_path    github.com/go-check/check

# github.com/motain/gocheck, cloned from github.com/go-check/check on Oct 23, 2013
%global mcommit         10bfe0586b48cbca10fe6c43d6e18136f25f8c0c
%global mscommit        %(c=%{mcommit}; echo ${c:0:7})
%global mimport_path    github.com/motain/gocheck

Name:           golang-gopkg-%{repo}
Version:        1
Release:        10%{?dist}
Summary:        Rich testing for the Go language
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{mcommit}/%{repo}-%{mscommit}.tar.gz
Source1:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Obsoletes:      golang-launchpad-gocheck

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
%endif

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path_sec}) = %{version}-%{release}
Provides:      golang(%{mimport_path}) = %{version}-%{release}
Provides:      golang(%{gimport_path}) = %{version}-%{release}
Obsoletes:     golang-launchpad-gocheck-devel

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test}
%package unit-test
Summary:         Unit tests for %{name} package
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -n %{repo}-%{mcommit} -q
%setup -n %{repo}-%{commit} -q -T -b 1

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
install -d -p %{buildroot}/%{gopath}/src/%{import_path_sec}/
install -d -p %{buildroot}/%{gopath}/src/%{gimport_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    install -d -p %{buildroot}/%{gopath}/src/%{import_path_sec}/$(dirname $file)
    cp $file %{buildroot}/%{gopath}/src/%{import_path_sec}/$file
    echo "%%{gopath}/src/%%{import_path_sec}/$file" >> devel.file-list

    install -d -p %{buildroot}/%{gopath}/src/%{gimport_path}/$(dirname $file)
    cp $file %{buildroot}/%{gopath}/src/%{gimport_path}/$file
    echo "%%{gopath}/src/%%{gimport_path}/$file" >> devel.file-list
done
%endif

pushd ../%{repo}-%{mcommit}
install -d -p %{buildroot}/%{gopath}/src/%{mimport_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{mimport_path}/$(dirname $file)
    cp $file %{buildroot}/%{gopath}/src/%{mimport_path}/$file
    echo "%%{gopath}/src/%%{mimport_path}/$file" >> ../%{repo}-%{commit}/devel.file-list
done
popd

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
done
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/Godeps/_workspace:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path_sec}
%dir %{gopath}/src/%{gimport_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc README.md
%endif

%changelog
* Tue Feb 23 2016 jchaloup <jchaloup@redhat.com> - 1-10
- Update spec file to spec 2.1
  support 4 import path prefixes
  related: #1248138

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-9
- https://fedoraproject.org/wiki/Changes/golang1.6

* Sun Feb 07 2016 Antonio Murdaca <runcom@fedoraproject.org> - 1-8
- rebuilt

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 jchaloup <jchaloup@redhat.com> - 0-6
- Update of spec file to spec-2.0
  resolves: #1248138

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 13 2015 jchaloup <jchaloup@redhat.com> - 0-4
- Add github.com/motain/gocheck into Provides
  related: #1151779

* Tue Jan 13 2015 jchaloup <jchaloup@redhat.com> - 0-3
- Add github.com/motain/gocheck into devel subpackage
  related: #1151779

* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-2
- Obsolete golang-launchpad-gocheck-devel with devel subpackage
  related: #1151779

* Fri Oct 10 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-1
- First package for Fedora
