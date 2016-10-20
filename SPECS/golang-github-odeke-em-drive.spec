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
%global project         odeke-em
%global repo            drive
# https://github.com/odeke-em/drive
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.3.7
Release:        1%{?dist}
Summary:        Google Drive client for the commandline
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/odeke-em/extractor)
BuildRequires: golang(github.com/odeke-em/go-utils/pkger/src)
BuildRequires: golang(github.com/odeke-em/go-utils/tmpfile)
BuildRequires: golang(github.com/odeke-em/pretty-words)
BuildRequires: golang(golang.org/x/crypto/scrypt)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(github.com/odeke-em/meddler)
BuildRequires: golang(github.com/odeke-em/semalim)
BuildRequires: golang(github.com/odeke-em/cache)
BuildRequires: golang(github.com/odeke-em/command)
BuildRequires: golang(google.golang.org/api/drive/v2) >= 0-0.16
BuildRequires: golang(github.com/skratchdot/open-golang/open)

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
#BuildRequires: golang(github.com/boltdb/bolt)
#BuildRequires: golang(github.com/boltdb/bolt/cmd/bolt)
#BuildRequires: golang(github.com/cheggaaa/pb)
#BuildRequires: golang(github.com/mattn/go-isatty)
#BuildRequires: golang(github.com/odeke-em/cli-spinner)
#BuildRequires: golang(github.com/odeke-em/exponential-backoff)
#BuildRequires: golang(github.com/odeke-em/log)
#BuildRequires: golang(github.com/odeke-em/statos)
#BuildRequires: golang(github.com/olekukonko/ts)
#BuildRequires: golang(golang.org/x/oauth2)
#BuildRequires: golang(golang.org/x/oauth2/google)
#BuildRequires: golang(golang.org/x/oauth2/internal)
#BuildRequires: golang(golang.org/x/oauth2/jws)
#BuildRequires: golang(golang.org/x/oauth2/jwt)
#BuildRequires: golang(google.golang.org/api/googleapi)
#BuildRequires: golang(google.golang.org/api/googleapi/internal/uritemplates)
#BuildRequires: golang(google.golang.org/appengine)
#BuildRequires: golang(google.golang.org/appengine/urlfetch)
#BuildRequires: golang(google.golang.org/cloud)
#BuildRequires: golang(google.golang.org/cloud/compute/metadata)
#BuildRequires: golang(google.golang.org/cloud/internal)
#BuildRequires: golang(google.golang.org/cloud/internal/opts)
#BuildRequires: golang(google.golang.org/grpc)
#BuildRequires: golang(google.golang.org/grpc/credentials)
#BuildRequires: golang(google.golang.org/grpc/credentials/oauth)
%endif

Requires:      golang(github.com/boltdb/bolt)
Requires:      golang(github.com/boltdb/bolt/cmd/bolt)
Requires:      golang(github.com/cheggaaa/pb)
Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(github.com/mattn/go-isatty)
Requires:      golang(github.com/odeke-em/cache)
Requires:      golang(github.com/odeke-em/cli-spinner)
Requires:      golang(github.com/odeke-em/exponential-backoff)
Requires:      golang(github.com/odeke-em/extractor)
Requires:      golang(github.com/odeke-em/go-utils/pkger/src)
Requires:      golang(github.com/odeke-em/go-utils/tmpfile)
Requires:      golang(github.com/odeke-em/log)
Requires:      golang(github.com/odeke-em/meddler)
Requires:      golang(github.com/odeke-em/pretty-words)
Requires:      golang(github.com/odeke-em/semalim)
Requires:      golang(github.com/odeke-em/statos)
Requires:      golang(github.com/olekukonko/ts)
Requires:      golang(github.com/skratchdot/open-golang/open)
Requires:      golang(golang.org/x/crypto/scrypt)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(golang.org/x/oauth2)
Requires:      golang(golang.org/x/oauth2/google)
Requires:      golang(golang.org/x/oauth2/internal)
Requires:      golang(golang.org/x/oauth2/jws)
Requires:      golang(golang.org/x/oauth2/jwt)
Requires:      golang(google.golang.org/api/drive/v2)
Requires:      golang(google.golang.org/api/googleapi)
Requires:      golang(google.golang.org/api/googleapi/internal/uritemplates)
Requires:      golang(google.golang.org/appengine)
Requires:      golang(google.golang.org/appengine/urlfetch)
Requires:      golang(google.golang.org/cloud)
Requires:      golang(google.golang.org/cloud/compute/metadata)
Requires:      golang(google.golang.org/cloud/internal)
Requires:      golang(google.golang.org/cloud/internal/opts)
Requires:      golang(google.golang.org/grpc)
Requires:      golang(google.golang.org/grpc/credentials)
Requires:      golang(google.golang.org/grpc/credentials/oauth)

Provides:      golang(%{import_path}/config) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/github.com/mattn/go-isatty) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/github.com/odeke-em/cache) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/github.com/odeke-em/cli-spinner) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/github.com/odeke-em/exponential-backoff) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/github.com/odeke-em/log) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/github.com/odeke-em/ripper/src) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/github.com/odeke-em/statos) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/github.com/odeke-em/xon/pkger/src) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/net/context) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2/clientcredentials) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2/facebook) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2/github) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2/google) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2/jws) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2/jwt) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2/linkedin) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2/odnoklassniki) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2/paypal) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/golang.org/x/oauth2/vk) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/google.golang.org/api/googleapi) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/google.golang.org/api/googleapi/transport) = %{version}-%{release}
Provides:      golang(%{import_path}/drive-gen/Godeps/_workspace/src/google.golang.org/cloud/compute/metadata) = %{version}-%{release}
Provides:      golang(%{import_path}/gen) = %{version}-%{release}
Provides:      golang(%{import_path}/src) = %{version}-%{release}
Provides:      golang(%{import_path}/src/dcrypto) = %{version}-%{release}
Provides:      golang(%{import_path}/src/dcrypto/v1) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{version}
# Bundled version of command is too old and not compatible.
rm -r ./drive-gen/Godeps/_workspace/src/github.com/odeke-em/command

%build
export GOROOT=/usr/share/gocode
export GOPATH=%{gopath}:/usr/lib/golang:$(pwd)/Godeps/_workspace:$(pwd)/drive-gen/Godeps/_workspace:%{gopath}
mkdir -p $(pwd)/Godeps/_workspace/src/github.com/odeke-em
ln -s $(pwd) $(pwd)/Godeps/_workspace/src/github.com/odeke-em/drive
go build ./cmd/drive
#%gobuild ./cmd/drive

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
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
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list
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

go test %{import_path}/src/dcrypto
go test %{import_path}/src/dcrypto/v1
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md platform_packages.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md platform_packages.md
%endif

%changelog
* Thu Aug 11 2016 Vladimir Rusinov <vladimir@greenmice.info> - 0.3.7-1
- First package for Fedora.
