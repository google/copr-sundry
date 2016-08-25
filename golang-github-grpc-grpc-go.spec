%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 1
%global with_bundled 0
%global with_debug 0
%global with_check 1
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
%global project         grpc
%global repo            grpc-go
# https://github.com/grpc/grpc-go
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     google.golang.org/grpc
%global commit          02fca896ff5f50c6bbbee0860345a49344b37a03
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.11.git%{shortcommit}%{?dist}
Summary:        The Go language implementation of gRPC. HTTP/2 based RPC
License:        BSD
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
BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/net/http2/hpack)
BuildRequires: golang(golang.org/x/net/trace)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/oauth2/jwt)
%endif

Requires:      golang(github.com/golang/glog)
Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(golang.org/x/net/http2)
Requires:      golang(golang.org/x/net/http2/hpack)
Requires:      golang(golang.org/x/net/trace)
Requires:      golang(golang.org/x/oauth2)
Requires:      golang(golang.org/x/oauth2/google)
Requires:      golang(golang.org/x/oauth2/jwt)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/benchmark) = %{version}-%{release}
Provides:      golang(%{import_path}/benchmark/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/benchmark/stats) = %{version}-%{release}
Provides:      golang(%{import_path}/codes) = %{version}-%{release}
Provides:      golang(%{import_path}/credentials) = %{version}-%{release}
Provides:      golang(%{import_path}/examples/helloworld/helloworld) = %{version}-%{release}
Provides:      golang(%{import_path}/examples/route_guide/routeguide) = %{version}-%{release}
Provides:      golang(%{import_path}/credentials/oauth) = %{version}-%{release}
Provides:      golang(%{import_path}/grpclog) = %{version}-%{release}
Provides:      golang(%{import_path}/grpclog/glogger) = %{version}-%{release}
Provides:      golang(%{import_path}/health) = %{version}-%{release}
Provides:      golang(%{import_path}/health/grpc_health_v1) = %{version}-%{release}
Provides:      golang(%{import_path}/interop) = %{version}-%{release}
Provides:      golang(%{import_path}/interop/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/metadata) = %{version}-%{release}
Provides:      golang(%{import_path}/naming) = %{version}-%{release}
Provides:      golang(%{import_path}/peer) = %{version}-%{release}
Provides:      golang(%{import_path}/reflection) = %{version}-%{release}
Provides:      golang(%{import_path}/reflection/grpc_reflection_v1alpha) = %{version}-%{release}
Provides:      golang(%{import_path}/reflection/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/stress/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/test/codec_perf) = %{version}-%{release}
Provides:      golang(%{import_path}/test/grpc_testing) = %{version}-%{release}
Provides:      golang(%{import_path}/transport) = %{version}-%{release}

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
# find all *.go but no *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
chmod -x %{buildroot}%{gopath}/src/%{import_path}/interop/grpc_testing/test.pb.go
for ext in .pem .key .proto _test.go; do
    # find all files with $ext prefix and generate unit-test.file-list
    for file in $(find . -iname "*${ext}"); do
        echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
        install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
        cp $file %{buildroot}/%{gopath}/src/%{import_path}/$file
        echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
    done
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

%gotest %{import_path}
%gotest %{import_path}/benchmark
%gotest %{import_path}/metadata
# Leaked goroutine
#%%gotest %%{import_path}/test
%gotest %{import_path}/transport
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md
%dir %{gopath}/src/google.golang.org
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md
%endif

%changelog
* Mon Aug 08 2016 jchaloup <jchaloup@redhat.com> - 0-0.11.git02fca89
- Give back example provides, they are actually used by golang-github-cockroachdb-cmux-unit-test-devel
  related: #1250461

* Wed Aug 03 2016 jchaloup <jchaloup@redhat.com> - 0-0.10.git02fca89
- Bump to upstream 02fca896ff5f50c6bbbee0860345a49344b37a03
  related: #1250461

* Mon Aug 01 2016 jchaloup <jchaloup@redhat.com> - 0-0.9.gite78224b
- Bump to upstream e78224b060cf3215247b7be455f80ea22e469b66
  related: #1250461

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gitb062a3c
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun May 15 2016 jchaloup <jchaloup@redhat.com> - 0-0.7.gitb062a3c
- Bump to upstream b062a3c003c22bfef58fa99d689e6a892b408f9d
  related: #1250461

* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 0-0.6.gitb88c12e
- Bump to upstream b88c12e7caf74af3928de99a864aaa9916fa5aad
  related: #1250461

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gite29d659
- https://fedoraproject.org/wiki/Changes/golang1.6

* Thu Feb 18 2016 jchaloup <jchaloup@redhat.com> - 0-0.4.gite29d659
- Bump to upstream e29d659177655e589850ba7d3d83f7ce12ef23dd
  related: #1250461

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitd286668
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.gitd286668
- Update to spec-2.1
  resolves: #1250461

* Tue Jul 28 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitd286668
- First package for Fedora
  resolves: #1246205

