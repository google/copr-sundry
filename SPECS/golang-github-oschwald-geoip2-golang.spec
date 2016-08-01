%global provider        github
%global provider_tld    com
%global project         oschwald
%global repo            geoip2-golang
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider}.com/%{project}/%{repo}
%global commit          51714a0e79df40e00a94ae5086ec2a5532c9ee57
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global debug_package   %{nil}

Name:           golang-github-%{project}-%{repo}
Version:        0
Release:        1%{?dist}
Summary:        Unofficial MaxMind GeoIP2 Reader for Go

License:        ISC
URL:            https://%{provider_prefix}
Source0:        https://github.com/%{project}/%{repo}/archive/%{commit}.zip

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
/usr/share/gocode/src/github.com/oschwald/geoip2-golang/reader.go


%changelog
* Fri Jul 29 2016 Vladimir Rusinov <vrusinov@google.com> 0-1.git51714
- First version.
