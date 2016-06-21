%global provider        github
%global provider_tld    com
%global project         jackpal
%global repo            go-nat-pmp
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     github.com/jackpal/%{repo}
%global import_path_AudriusButkevicius github.com/AudriusButkevicius/%{repo}

%global debug_package   %{nil}

Name:           golang-github-jackpal-%{repo}
Version:        1.0.1
Release:        1%{?dist}
Summary:        A Go language client for the NAT-PMP internet protocol.
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
Provides:      golang(%{import_path_AudriusButkevicius}) = %{version}-%{release}

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
mkdir -p %{buildroot}/%{gopath}/src/github.com/AudriusButkevicius
ln -s /%{gopath}/src/%{import_path} %{buildroot}/%{gopath}/src/%{import_path_AudriusButkevicius}

%files -n %{name}-devel
%license LICENSE
%doc README.md
%dir %{gopath}/src/%{import_path}
%{gopath}/src/github.com/jackpal/go-nat-pmp/natpmp.go
%{gopath}/src/github.com/jackpal/go-nat-pmp/network.go
%{gopath}/src/github.com/jackpal/go-nat-pmp/recorder.go

/usr/share/gocode/src/%{import_path_AudriusButkevicius}

%changelog
* Sun Jun 19 2016 Vladimir Rusinov <vrusinov@google.com> 1.0.1-1
- First version.
