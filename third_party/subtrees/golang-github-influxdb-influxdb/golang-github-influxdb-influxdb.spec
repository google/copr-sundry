%global with_devel 1
%global with_bundled 0
%global with_debug 0
# tests are skiped as there are unresolved dependencies
%global with_check 0
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         influxdb
%global repo            influxdb
# https://github.com/influxdb/influxdb
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          9eab56311373ee6f788ae5dfc87e2240038f0eb4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.9.5.1
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Scalable datastore for metrics, events, and real-time analytics
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 ppc64le
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
InfluxDB is an open source distributed time series database with no external
dependencies. It's useful for recording metrics, events, and performing
analytics.

It has a built-in HTTP API so you don't have to write any server side code to
get up and running.

InfluxDB is designed to be scalable, simple to install and manage, and fast to
get data in and out.

It aims to answer queries in real-time. That means every data point is indexed
as it comes in and is immediately available in queries that should return
in < 100ms.

%if 0%{?with_devel}
%package client
Summary:        Golang client libs for influxdb
BuildArch:      noarch

%if 0%{?with_check}
%endif

Provides:       golang(%{import_path}/client) = %{version}-%{release}
Provides:       golang(%{import_path}/client/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/models) = %{version}-%{release}
Provides:       golang(%{import_path}/pkg/escape) = %{version}-%{release}

%description client
%{%description}

This package contains client part of influxdb.

%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/bmizerany/pat)
BuildRequires:  golang(github.com/boltdb/bolt)
BuildRequires:  golang(github.com/dgryski/go-bits)
BuildRequires:  golang(github.com/dgryski/go-bitstream)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/hashicorp/raft)
BuildRequires:  golang(github.com/hashicorp/raft-boltdb)
BuildRequires:  golang(github.com/influxdb/enterprise-client/v1)
BuildRequires:  golang(github.com/jwilder/encoding/simple8b)
BuildRequires:  golang(github.com/kimor79/gollectd)
BuildRequires:  golang(github.com/peterh/liner)
BuildRequires:  golang(github.com/rakyll/statik/fs)
BuildRequires:  golang(golang.org/x/crypto/bcrypt)
BuildRequires:  golang(gopkg.in/fatih/pool.v2)
%endif

Requires:       %{name}-client = %{version}-%{release}
Requires:       golang(github.com/BurntSushi/toml)
Requires:       golang(github.com/bmizerany/pat)
Requires:       golang(github.com/boltdb/bolt)
#Requires:       golang(github.com/dgryski/go-bits)
#Requires:       golang(github.com/dgryski/go-bitstream)
Requires:       golang(github.com/gogo/protobuf/proto)
Requires:       golang(github.com/golang/snappy)
Requires:       golang(github.com/hashicorp/raft)
Requires:       golang(github.com/hashicorp/raft-boltdb)
#Requires:       golang(github.com/influxdb/enterprise-client/v1)
#Requires:       golang(github.com/jwilder/encoding/simple8b)
Requires:       golang(github.com/kimor79/gollectd)
Requires:       golang(github.com/peterh/liner)
Requires:       golang(github.com/rakyll/statik/fs)
Requires:       golang(golang.org/x/crypto/bcrypt)
Requires:       golang(gopkg.in/fatih/pool.v2)

Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/cluster) = %{version}-%{release}
Provides:       golang(%{import_path}/cmd/influx/cli) = %{version}-%{release}
Provides:       golang(%{import_path}/cmd/influxd/backup) = %{version}-%{release}
Provides:       golang(%{import_path}/cmd/influxd/help) = %{version}-%{release}
Provides:       golang(%{import_path}/cmd/influxd/restore) = %{version}-%{release}
Provides:       golang(%{import_path}/cmd/influxd/run) = %{version}-%{release}
Provides:       golang(%{import_path}/importer/v8) = %{version}-%{release}
Provides:       golang(%{import_path}/influxql) = %{version}-%{release}
Provides:       golang(%{import_path}/meta) = %{version}-%{release}
Provides:       golang(%{import_path}/monitor) = %{version}-%{release}
Provides:       golang(%{import_path}/pkg/slices) = %{version}-%{release}
Provides:       golang(%{import_path}/services/admin) = %{version}-%{release}
Provides:       golang(%{import_path}/services/collectd) = %{version}-%{release}
Provides:       golang(%{import_path}/services/continuous_querier) = %{version}-%{release}
Provides:       golang(%{import_path}/services/copier) = %{version}-%{release}
Provides:       golang(%{import_path}/services/graphite) = %{version}-%{release}
Provides:       golang(%{import_path}/services/hh) = %{version}-%{release}
Provides:       golang(%{import_path}/services/httpd) = %{version}-%{release}
Provides:       golang(%{import_path}/services/opentsdb) = %{version}-%{release}
Provides:       golang(%{import_path}/services/precreator) = %{version}-%{release}
Provides:       golang(%{import_path}/services/registration) = %{version}-%{release}
Provides:       golang(%{import_path}/services/retention) = %{version}-%{release}
Provides:       golang(%{import_path}/services/snapshotter) = %{version}-%{release}
Provides:       golang(%{import_path}/services/subscriber) = %{version}-%{release}
Provides:       golang(%{import_path}/services/udp) = %{version}-%{release}
Provides:       golang(%{import_path}/snapshot) = %{version}-%{release}
Provides:       golang(%{import_path}/statik) = %{version}-%{release}
Provides:       golang(%{import_path}/stress) = %{version}-%{release}
Provides:       golang(%{import_path}/tcp) = %{version}-%{release}
Provides:       golang(%{import_path}/toml) = %{version}-%{release}
Provides:       golang(%{import_path}/tsdb) = %{version}-%{release}
Provides:       golang(%{import_path}/tsdb/engine) = %{version}-%{release}
Provides:       golang(%{import_path}/tsdb/engine/b1) = %{version}-%{release}
Provides:       golang(%{import_path}/tsdb/engine/bz1) = %{version}-%{release}
Provides:       golang(%{import_path}/tsdb/engine/tsm1) = %{version}-%{release}
Provides:       golang(%{import_path}/tsdb/engine/wal) = %{version}-%{release}
Provides:       golang(%{import_path}/uuid) = %{version}-%{release}

%description devel
InfluxDB is an open source distributed time series database with no external
dependencies. It's useful for recording metrics, events, and performing
analytics.

It has a built-in HTTP API so you don't have to write any server side code to
get up and running.

InfluxDB is designed to be scalable, simple to install and manage, and fast to
get data in and out.

It aims to answer queries in real-time. That means every data point is indexed
as it comes in and is immediately available in queries that should return
in < 100ms.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test}
%package unit-test
Summary:         Unit tests for %{name} package
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
BuildRequires: golang(github.com/davecgh/go-spew/spew)
%endif

Requires:      golang(github.com/davecgh/go-spew/spew)

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
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go" | grep -v -E "^./client|^./models|^./pkg/escape") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go" | grep -E "^./client|^./models|^./pkg/escape") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> client_devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> client_devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
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

%gotest %{import_path}/client
%gotest %{import_path}/client/v2
%gotest %{import_path}/cluster
%gotest %{import_path}/cmd/influx/cli
%gotest %{import_path}/cmd/influxd/backup
%gotest %{import_path}/cmd/influxd/restore
%gotest %{import_path}/cmd/influxd/run
%gotest %{import_path}/influxql
%gotest %{import_path}/meta
%gotest %{import_path}/models
%gotest %{import_path}/monitor
%gotest %{import_path}/pkg/escape
%gotest %{import_path}/services/admin
%gotest %{import_path}/services/collectd
%gotest %{import_path}/services/continuous_querier
%gotest %{import_path}/services/copier
%gotest %{import_path}/services/graphite
%gotest %{import_path}/services/hh
%gotest %{import_path}/services/httpd
%gotest %{import_path}/services/opentsdb
%gotest %{import_path}/services/precreator
%gotest %{import_path}/services/registration
%gotest %{import_path}/services/retention
%gotest %{import_path}/services/snapshotter
%gotest %{import_path}/services/subscriber
%gotest %{import_path}/services/udp
%gotest %{import_path}/snapshot
%gotest %{import_path}/stress
%gotest %{import_path}/tcp
%gotest %{import_path}/toml
%gotest %{import_path}/tsdb
%gotest %{import_path}/tsdb/engine/b1
%gotest %{import_path}/tsdb/engine/bz1
%gotest %{import_path}/tsdb/engine/tsm1
%gotest %{import_path}/tsdb/engine/wal
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files client -f client_devel.file-list
%license LICENSE
%doc *.md
%dir %{gopath}/src/%{import_path}/client

%files devel -f devel.file-list
%license LICENSE
%doc *.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc *.md
%endif

%changelog
* Sun May 22 2016 jchaloup <jchaloup@redhat.com> - 0.9.5.1-0.1.git9eab563
- Update to 0.9.5.1
  related: #1250485

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-0.6.git9485e99
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-0.5.git9485e99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 jchaloup <jchaloup@redhat.com> - 0.8.5-0.4.git9485e99
- Update spec file to spec-2.0
  resolves: #1250485

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0.8.5-0.3.git9485e99
- Update BR/R
  related: #1161618

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-0.2.git9485e99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 06 2015 jchaloup <jchaloup@redhat.com> - 0.8.5-0.1.git9485e99
- Update to 0.8.5
  resolves: #1161618

* Sun Nov 09 2014 jchaloup <jchaloup@redhat.com> - 0.8.0-0.5.rc4.git67f9869
- Choose the correct architecture
  related: #1141892
- Bump to upstream b611d020cd78886232cfa6c2ea0606b49d307ed2
  resolves: #1161618

* Tue Oct 14 2014 jchaloup <jchaloup@redhat.com> - 0.8.0-0.4.rc4.git67f9869
- Adding BR on gomdb

* Thu Oct 09 2014 jchaloup <jchaloup@redhat.com> - 0.8.0-0.3.rc4.git67f9869
- Add subpackages (client for kubernetes, datastore for databases, devel for all)
- Add dependencies (not all of them yet)
- Test still missing (missing deps and databases in Fedora), at least add them partionally later

* Mon Sep 29 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.8.0-0.2.rc4.git67f9869
- Resolves: rhbz#1141892 - initial package upload
- preserve timestamps of source copied
- gopath is provided by the golang rpm

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.8.0-0.1.rc4.git67f9869
- First package for Fedora.
