%global provider        github
%global provider_tld    com
%global project         calmh
%global repo            luhn
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     github.com/%{project}/%{repo}

%global debug_package   %{nil}

Name:           golang-%{provider}-%{project}-luhn
Version:        1.0.0
Release:        1%{?dist}
Summary:        A Luhn-mod-N implementation in Go
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}.tar.gz

BuildRequires:  golang

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(github.com/vitrun/qart/qr) = %{version}-%{release}

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

%files devel
%license LICENSE
%dir %{gopath}/src/%{import_path}
/usr/share/gocode/src/github.com/calmh/luhn/luhn.go

%changelog
* Fri Jun 24 2016 Vladimir Rusinov <vrusinov@google.com> 1.0.0-1
- First version.
