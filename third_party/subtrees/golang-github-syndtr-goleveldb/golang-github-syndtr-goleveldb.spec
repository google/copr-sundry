%global with_devel 1
%global with_bundled 0
%global with_debug 0
%global with_check 1
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
%global project         syndtr
%global repo            goleveldb
# https://github.com/syndtr/goleveldb
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          012f65f74744ed62a80abac6e9a8c86e71c2b6fa
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.6.git%{shortcommit}%{?dist}
Summary:        LevelDB key/value database in Go
License:        BSD
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
BuildRequires: golang(github.com/onsi/ginkgo/config)
BuildRequires: golang(github.com/onsi/gomega)
BuildRequires: golang(github.com/syndtr/gosnappy/snappy)
%endif

Requires:      golang(github.com/onsi/ginkgo)
Requires:      golang(github.com/onsi/ginkgo/config)
Requires:      golang(github.com/onsi/gomega)
Requires:      golang(github.com/syndtr/gosnappy/snappy)

Provides:      golang(%{import_path}/leveldb) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/cache) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/comparer) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/errors) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/filter) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/iterator) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/journal) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/memdb) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/opt) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/storage) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/table) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/testutil) = %{version}-%{release}
Provides:      golang(%{import_path}/leveldb/util) = %{version}-%{release}

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
# Failed in Koji - timeout
#gotest %%{import_path}/leveldb
# timeout here as well.
#gotest %%{import_path}/leveldb/cache
gotest %{import_path}/leveldb/filter
gotest %{import_path}/leveldb/iterator
gotest %{import_path}/leveldb/journal
gotest %{import_path}/leveldb/memdb
gotest %{import_path}/leveldb/storage
gotest %{import_path}/leveldb/table
gotest %{import_path}/leveldb/util
%endif

%if 0%{?with_devel}
%files devel -f devel.file-list
%copying LICENSE
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%copying LICENSE
%doc README.md
%endif

%changelog
* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git012f65f
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git012f65f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.1.git012f65f
- Update spec file to spec-2.0
- Disable leveldb test
  related: #1220163

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git012f65f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 10 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git012f65f
- Bump to upstream 012f65f74744ed62a80abac6e9a8c86e71c2b6fa
  resolves: #1220163

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gite9e2c8f
- First package for Fedora
  resolves: #1190418
