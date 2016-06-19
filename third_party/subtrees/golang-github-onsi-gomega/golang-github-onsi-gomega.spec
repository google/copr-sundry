%global with_devel 1
%global with_bundled 0
%global with_debug 0
%global with_check 0
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%define copying() \
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7 \
%license %{*} \
%else \
%doc %{*} \
%endif

%global provider        github
%global provider_tld    com
%global project         onsi
%global repo            gomega
# https://github.com/onsi/gomega
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          8adf9e1730c55cdc590de7d49766cb2acc88d8f2
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.7.git%{shortcommit}%{?dist}
Summary:        Ginkgo's Preferred Matcher Library
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

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
BuildRequires: golang(github.com/onsi/ginkgo)
%endif

Requires:      golang(github.com/onsi/ginkgo)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/format) = %{version}-%{release}
Provides:      golang(%{import_path}/gbytes) = %{version}-%{release}
Provides:      golang(%{import_path}/gexec) = %{version}-%{release}
Provides:      golang(%{import_path}/ghttp) = %{version}-%{release}
Provides:      golang(%{import_path}/matchers) = %{version}-%{release}
Provides:      golang(%{import_path}/matchers/support/goraph/bipartitegraph) = %{version}-%{release}
Provides:      golang(%{import_path}/matchers/support/goraph/edge) = %{version}-%{release}
Provides:      golang(%{import_path}/matchers/support/goraph/node) = %{version}-%{release}
Provides:      golang(%{import_path}/matchers/support/goraph/util) = %{version}-%{release}
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

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
%endif
# cp -pav {format,gbytes,gexec,ghttp,internal,matchers,types} %{buildroot}/%{gopath}/src/%{import_path}/

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
#go test can not be done as there is a circular dependency between golang-github-onsi-ginkgo and golang-github-onsi-gomega package

%if 0%{?with_devel}
%files devel -f devel.file-list
%copying LICENSE
%doc README.md CHANGELOG.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%copying LICENSE
%doc README.md CHANGELOG.md
%endif

%changelog
* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git8adf9e1
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git8adf9e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git8adf9e1
- internal packages are no longer provided
  related: #1248013

* Wed Jul 29 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.1.git8adf9e1
- Update of spec file to spec-2.0
  resolves: #1248013

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git8adf9e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git8adf9e1
- Bump to upstream 8adf9e1730c55cdc590de7d49766cb2acc88d8f2
  related: #1148452

* Mon Oct 13 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.gita0ee4df
- BuildArch to ExclusiveArch

* Wed Oct 01 2014 root - 0-0.1.git90d6a47
- First package for Fedora




