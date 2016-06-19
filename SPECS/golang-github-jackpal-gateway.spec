%global provider        github
%global provider_tld    com
%global project         jackpal
%global repo            gateway
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     github.com/jackpal/gateway

%global debug_package   %{nil}

Name:           golang-githib-jackpal-gateway
Version:        1.0.4
Release:        2%{?dist}
Summary:        A simple library for discovering the IP address of the default gateway.
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}.tar.gz

BuildRequires:  golang

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -q -n %{repo}-%{version}

%build

%install
# source codes for building projects
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
for ext in go s; do
	# find all *.go but no *_test.go files.
	for file in $(find . -iname "*.$ext" \! -iname "*_test.go") ; do
	    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
	    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
	done
done

%files -n %{name}-devel
%license LICENSE
%doc README.md
%dir %{gopath}/src/%{import_path}
/usr/share/gocode/src/github.com/jackpal/gateway/gateway_common.go
/usr/share/gocode/src/github.com/jackpal/gateway/gateway_darwin.go
/usr/share/gocode/src/github.com/jackpal/gateway/gateway_freebsd.go
/usr/share/gocode/src/github.com/jackpal/gateway/gateway_linux.go
/usr/share/gocode/src/github.com/jackpal/gateway/gateway_solaris.go
/usr/share/gocode/src/github.com/jackpal/gateway/gateway_unimplemented.go
/usr/share/gocode/src/github.com/jackpal/gateway/gateway_windows.go

%changelog
* Sun Jun 19 2016 Vladimir Rusinov <vrusinov@google.com> 1.0.4-2
- Fixed provides.

* Thu Jun 16 2016 Vladimir Rusinov <vrusinov@google.com> 1.0.4-1
- First version.
