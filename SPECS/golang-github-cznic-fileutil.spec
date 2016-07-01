%global provider        github
%global provider_tld    com
%global project         cznic
%global repo            fileutil
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider}.com/%{project}/%{repo}
%global commit          1c9c88fbf552b3737c7b97e1f243860359687976
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global debug_package   %{nil}

Name:           golang-github-cznic-%{repo}
Version:        0
Release:        1%{?dist}
Summary:        Package fileutil collects some file utility functions
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
%doc README
%dir %{gopath}/src/%{import_path}
/usr/share/gocode/src/github.com/cznic/fileutil/falloc/docs.go
/usr/share/gocode/src/github.com/cznic/fileutil/falloc/error.go
/usr/share/gocode/src/github.com/cznic/fileutil/falloc/falloc.go
/usr/share/gocode/src/github.com/cznic/fileutil/falloc/test_deps.go
/usr/share/gocode/src/github.com/cznic/fileutil/fileutil.go
/usr/share/gocode/src/github.com/cznic/fileutil/fileutil_arm.go
/usr/share/gocode/src/github.com/cznic/fileutil/fileutil_darwin.go
/usr/share/gocode/src/github.com/cznic/fileutil/fileutil_freebsd.go
/usr/share/gocode/src/github.com/cznic/fileutil/fileutil_linux.go
/usr/share/gocode/src/github.com/cznic/fileutil/fileutil_netbsd.go
/usr/share/gocode/src/github.com/cznic/fileutil/fileutil_openbsd.go
/usr/share/gocode/src/github.com/cznic/fileutil/fileutil_plan9.go
/usr/share/gocode/src/github.com/cznic/fileutil/fileutil_solaris.go
/usr/share/gocode/src/github.com/cznic/fileutil/fileutil_windows.go
/usr/share/gocode/src/github.com/cznic/fileutil/hdb/hdb.go
/usr/share/gocode/src/github.com/cznic/fileutil/hdb/test_deps.go
/usr/share/gocode/src/github.com/cznic/fileutil/storage/cache.go
/usr/share/gocode/src/github.com/cznic/fileutil/storage/file.go
/usr/share/gocode/src/github.com/cznic/fileutil/storage/mem.go
/usr/share/gocode/src/github.com/cznic/fileutil/storage/probe.go
/usr/share/gocode/src/github.com/cznic/fileutil/storage/storage.go
/usr/share/gocode/src/github.com/cznic/fileutil/storage/test_deps.go
/usr/share/gocode/src/github.com/cznic/fileutil/test_deps.go

%changelog
* Fri Jul 01 2016 Vladimir Rusinov <vrusinov@google.com> 0-1.git1c9c88f
- First version.
