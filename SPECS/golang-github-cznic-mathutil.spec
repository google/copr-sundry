%global provider        github
%global provider_tld    com
%global project         cznic
%global repo            mathutil
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider}.com/%{project}/%{repo}
%global commit          78ad7f262603437f0ecfebc835d80094f89c8f54
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global debug_package   %{nil}

Name:           golang-github-cznic-%{repo}
Version:        0
Release:        1%{?dist}
Summary:        Utilities supplemental to the Go standard "rand" and "math" packages
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
/usr/share/gocode/src/github.com/cznic/mathutil/bits.go
/usr/share/gocode/src/github.com/cznic/mathutil/envelope.go
/usr/share/gocode/src/github.com/cznic/mathutil/example/example.go
/usr/share/gocode/src/github.com/cznic/mathutil/example2/example2.go
/usr/share/gocode/src/github.com/cznic/mathutil/example3/example3.go
/usr/share/gocode/src/github.com/cznic/mathutil/example4/main.go
/usr/share/gocode/src/github.com/cznic/mathutil/ff/main.go
/usr/share/gocode/src/github.com/cznic/mathutil/mathutil.go
/usr/share/gocode/src/github.com/cznic/mathutil/mersenne/mersenne.go
/usr/share/gocode/src/github.com/cznic/mathutil/permute.go
/usr/share/gocode/src/github.com/cznic/mathutil/primes.go
/usr/share/gocode/src/github.com/cznic/mathutil/rat.go
/usr/share/gocode/src/github.com/cznic/mathutil/rnd.go
/usr/share/gocode/src/github.com/cznic/mathutil/tables.go
/usr/share/gocode/src/github.com/cznic/mathutil/test_deps.go


%changelog
* Tue Jul 05 2016 Vladimir Rusinov <vrusinov@google.com> 0-1.git78ad7f2
- First version.
