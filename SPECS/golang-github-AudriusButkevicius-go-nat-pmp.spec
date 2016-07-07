%global provider        github
%global provider_tld    com
%global project         AudriusButkevicius
%global repo            go-nat-pmp
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     github.com/%{project}/%{repo}
%global commit          452c97607362b2ab5a7839b8d1704f0396b640ca
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global debug_package   %{nil}

Name:           golang-github-%{project}-%{repo}
Version:        0
Release:        1git%{shortcommit}%{?dist}
Summary:        A Go language client for the NAT-PMP internet protocol.
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}.zip

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
%setup -q -n %{repo}-%{commit}

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
%{gopath}/src/github.com/AudriusButkevicius/go-nat-pmp/natpmp.go

%changelog
* Thu Jul 07 2016 Vladimir Rusinov <vrusinov@google.com> 0.git452c976
- First version, forked from golang-github-jackpal-go-nat-pmp
