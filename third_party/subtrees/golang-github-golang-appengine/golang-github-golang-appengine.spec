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

%global provider        github
%global provider_tld    com
%global project         golang
%global repo            appengine
# https://github.com/golang/appengine
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     google.golang.org/appengine
%global commit          1c3fdc51e1021e4822cf8475c97d3a14a2a6648e
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.7.git%{shortcommit}%{?dist}
Summary:        Go App Engine for Managed VMs
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

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
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(golang.org/x/net/context)
%endif

Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(golang.org/x/net/context)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/channel) = %{version}-%{release}
Provides:      golang(%{import_path}/datastore) = %{version}-%{release}
Provides:      golang(%{import_path}/delay) = %{version}-%{release}
Provides:      golang(%{import_path}/demos/guestbook) = %{version}-%{release}
Provides:      golang(%{import_path}/demos/helloworld) = %{version}-%{release}
Provides:      golang(%{import_path}/file) = %{version}-%{release}
Provides:      golang(%{import_path}/image) = %{version}-%{release}
Provides:      golang(%{import_path}/internal) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/aetesting) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/app_identity) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/base) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/channel) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/datastore) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/image) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/log) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/mail) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/memcache) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/modules) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/remote_api) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/search) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/taskqueue) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/urlfetch) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/user) = %{version}-%{release}
Provides:      golang(%{import_path}/internal/xmpp) = %{version}-%{release}
Provides:      golang(%{import_path}/log) = %{version}-%{release}
Provides:      golang(%{import_path}/mail) = %{version}-%{release}
Provides:      golang(%{import_path}/memcache) = %{version}-%{release}
Provides:      golang(%{import_path}/module) = %{version}-%{release}
Provides:      golang(%{import_path}/remote_api) = %{version}-%{release}
Provides:      golang(%{import_path}/search) = %{version}-%{release}
Provides:      golang(%{import_path}/taskqueue) = %{version}-%{release}
Provides:      golang(%{import_path}/urlfetch) = %{version}-%{release}
Provides:      golang(%{import_path}/user) = %{version}-%{release}
Provides:      golang(%{import_path}/xmpp) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
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
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.proto and generate devel.file-list
for file in $(find . -iname "*.proto") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
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

%global gotest go test

%gotest %{import_path}
%gotest %{import_path}/channel
%gotest %{import_path}/datastore
%gotest %{import_path}/delay
# Dial hang took too long: 1.049004095s > 1s
#gotest %%{import_path}/internal
%gotest %{import_path}/log
%gotest %{import_path}/mail
%gotest %{import_path}/memcache
%gotest %{import_path}/module
%gotest %{import_path}/remote_api
%gotest %{import_path}/search
%gotest %{import_path}/taskqueue
%gotest %{import_path}/user
%gotest %{import_path}/xmpp
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md
%dir %{gopath}/src/google.golang.org
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc README.md
%endif

%changelog
* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git1c3fdc5
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git1c3fdc5
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git1c3fdc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git1c3fdc5
- Update to spec-2.1
  related: #1249049

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git1c3fdc5
- Update spec file to spec-2.0
  resolves: #1249049

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git1c3fdc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git1c3fdc5
- First package for Fedora
  resolves: #1185082

