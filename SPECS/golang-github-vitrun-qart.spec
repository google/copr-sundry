%global provider        github
%global provider_tld    com
%global project         vitrun
%global repo            qart
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     github.com/vitrun/qart

%global debug_package   %{nil}

Name:           golang-githib-vitrun-qart
Version:        0.1
Release:        1%{?dist}
Summary:        Qart generates not-so-ugly qr codes.
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{version}.tar.gz

BuildRequires:  golang

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(github.com/vitrun/qart/qr) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
github.com/vitrun/qart prefix.

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

%files -n golang-githib-vitrun-qart-devel
%license LICENSE
%doc README.md
%dir %{gopath}/src/%{import_path}
/usr/share/gocode/src/github.com/vitrun/qart/coding/coding.go
/usr/share/gocode/src/github.com/vitrun/qart/gf256/gf256.go
/usr/share/gocode/src/github.com/vitrun/qart/img.go
/usr/share/gocode/src/github.com/vitrun/qart/qart.go
/usr/share/gocode/src/github.com/vitrun/qart/qr/png.go
/usr/share/gocode/src/github.com/vitrun/qart/qr/qr.go
/usr/share/gocode/src/github.com/vitrun/qart/qr/resize.go

%changelog
* Wed Jun 15 2016 Vladimir Rusinov <vrusinov@google.com> 0.1-1
- First version.
