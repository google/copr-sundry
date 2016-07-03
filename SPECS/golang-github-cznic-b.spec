%global provider        github
%global provider_tld    com
%global project         cznic
%global repo            b
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider}.com/%{project}/%{repo}
%global commit          47184dd8c1d2c7e7f87dae8448ee2007cdf0c6c4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global debug_package   %{nil}

Name:           golang-github-cznic-%{repo}
Version:        0
Release:        1%{?dist}
Summary:        Package b implements a B+tree
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://github.com/cznic/%{repo}/archive/%{commit}.zip

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
/usr/share/gocode/src/github.com/cznic/b/btree.go
/usr/share/gocode/src/github.com/cznic/b/doc.go
/usr/share/gocode/src/github.com/cznic/b/example/int.go


%changelog
* Sun Jul 03 2016 Vladimir Rusinov <vrusinov@google.com> 0-1.git47184dd
- First version.
