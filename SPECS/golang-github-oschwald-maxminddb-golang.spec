%global provider        github
%global provider_tld    com
%global project         oschwald
%global repo            maxminddb-golang
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider}.com/%{project}/%{repo}
%global commit          f4aa55714a3f843869ca9a38625e177a627c1ce6
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global debug_package   %{nil}

Name:           golang-github-%{project}-%{repo}
Version:        0
Release:        1%{?dist}
Summary:        MaxMind DB Reader for Go

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
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/decoder.go
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/errors.go
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/key_appengine.go
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/key_other.go
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/mmap_unix.go
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/mmap_windows.go
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/reader.go
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/reader_appengine.go
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/reader_other.go
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/traverse.go
/usr/share/gocode/src/github.com/oschwald/maxminddb-golang/verifier.go



%changelog
* Sun Jul 31 2016 Vladimir Rusinov <vrusinov@google.com> 0-1.gitf4aa5
- First version.
