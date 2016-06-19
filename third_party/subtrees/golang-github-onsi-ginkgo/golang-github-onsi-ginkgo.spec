%global with_devel 1
%global with_bundled 0
%global with_debug 0
# Cyclic dependency on gomega
%global with_check 0
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         onsi
%global repo            ginkgo
# https://github.com/onsi/ginkgo
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          462326b1628e124b23f42e87a8f2750e3c4e2d24
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.1.0
Release:        7%{?dist}
Summary:        A Golang BDD Testing Framework
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
# Upstream fix for aarch64 a0fde42
Patch1:         0001-Add-linux_arm64-support.patch

# If go_arches not defined fall through to implicit golang archs
%if 0%{?go_arches:1}
ExclusiveArch:  %{go_arches}
%else
ExclusiveArch:   %{ix86} x86_64 %{arm}
%endif
# If gccgo_arches does not fit or is not defined fall through to golang
%ifarch 0%{?gccgo_arches}
BuildRequires:   gcc-go >= %{gccgo_min_vers}
%else
BuildRequires:   golang
%endif

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
BuildRequires: golang(github.com/onsi/gomega)
BuildRequires: golang(github.com/onsi/gomega/gbytes)
BuildRequires: golang(github.com/onsi/gomega/gexec)
BuildRequires: golang(github.com/onsi/gomega/ghttp)
%endif

Requires:      golang(github.com/onsi/gomega)
Requires:      golang(github.com/onsi/gomega/gbytes)
Requires:      golang(github.com/onsi/gomega/gexec)
Requires:      golang(github.com/onsi/gomega/ghttp)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/config) = %{version}-%{release}
Provides:      golang(%{import_path}/ginkgo/convert) = %{version}-%{release}
Provides:      golang(%{import_path}/ginkgo/interrupthandler) = %{version}-%{release}
Provides:      golang(%{import_path}/ginkgo/nodot) = %{version}-%{release}
Provides:      golang(%{import_path}/ginkgo/testrunner) = %{version}-%{release}
Provides:      golang(%{import_path}/ginkgo/testsuite) = %{version}-%{release}
Provides:      golang(%{import_path}/ginkgo/watch) = %{version}-%{release}
Provides:      golang(%{import_path}/integration) = %{version}-%{release}
Provides:      golang(%{import_path}/reporters) = %{version}-%{release}
Provides:      golang(%{import_path}/reporters/stenographer) = %{version}-%{release}
Provides:      golang(%{import_path}/types) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test}
%package unit-test
Summary:         Unit tests for %{name} package

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
%setup -q -n %{repo}-%{commit}
%patch1 -p1 -b .arm64

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
done
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%ifarch 0%{?gccgo_arches}
function gotest { %{gcc_go_test} "$@"; }
%else
%if 0%{?golang_test:1}
function gotest { %{golang_test} "$@"; }
%else
function gotest { go test "$@"; }
%endif
%endif

export GOPATH=%{buildroot}/%{gopath}:%{gopath}
gotest %{import_path}/ginkgo/nodot
gotest %{import_path}/ginkgo/testsuite
gotest %{import_path}/integration
gotest %{import_path}/internal/codelocation
gotest %{import_path}/internal/containernode
gotest %{import_path}/internal/failer
gotest %{import_path}/internal/leafnodes
gotest %{import_path}/internal/remote
gotest %{import_path}/internal/spec
gotest %{import_path}/internal/specrunner
gotest %{import_path}/internal/suite
gotest %{import_path}/internal/writer
gotest %{import_path}/reporters
gotest %{import_path}/types
%endif

%if 0%{?with_devel}
%files devel -f devel.file-list
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG.md README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG.md README.md
%endif

%changelog
* Tue Feb 23 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-7
- Add patch for aarch64
- Use %%license

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 1.1.0-4
- Update spec file to spec-2.0
  related: #1214619

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 jchaloup <jchaloup@redhat.com> - 1.1.0-2
- Bump to upstream 462326b1628e124b23f42e87a8f2750e3c4e2d24
  related: #1214619

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 1.1.0-1
- Bump to upstream dbb5c6caf33238b57facc1d975b1aaca6b90288c
  resolves: #1214619

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git17ea479
- Add buildtime dependency on github.com/onsi/gomega
- Fix installtime dependency on github.com/onsi/gomega
  related: #1148456

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git17ea479
- Bump to upstream 17ea479729ee427265ac1e913443018350946ddf
  related: #1148456

* Mon Oct 13 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.git90d6a47
- BuildArch to ExclusiveArch

* Wed Oct 01 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git90d6a47
- First package for Fedora
