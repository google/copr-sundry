%global provider        github
%global provider_tld    com
%global project         cznic
%global repo            ql
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     github.com/%{project}/%{repo}

%global debug_package   %{nil}

Name:           golang-github-cznic-%{repo}
Version:        1.0.3
Release:        1%{?dist}
Summary:        A pure Go embedded (S)QL database
License:        BSD
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
/usr/share/gocode/src/github.com/cznic/ql/blob.go
/usr/share/gocode/src/github.com/cznic/ql/btree.go
/usr/share/gocode/src/github.com/cznic/ql/builtin.go
/usr/share/gocode/src/github.com/cznic/ql/coerce.go
/usr/share/gocode/src/github.com/cznic/ql/design/doc.go
/usr/share/gocode/src/github.com/cznic/ql/doc.go
/usr/share/gocode/src/github.com/cznic/ql/driver.go
/usr/share/gocode/src/github.com/cznic/ql/driver/driver.go
/usr/share/gocode/src/github.com/cznic/ql/errors.go
/usr/share/gocode/src/github.com/cznic/ql/etc.go
/usr/share/gocode/src/github.com/cznic/ql/expr.go
/usr/share/gocode/src/github.com/cznic/ql/file.go
/usr/share/gocode/src/github.com/cznic/ql/helper/helper.go
/usr/share/gocode/src/github.com/cznic/ql/httpfs.go
/usr/share/gocode/src/github.com/cznic/ql/introspection.go
/usr/share/gocode/src/github.com/cznic/ql/mem.go
/usr/share/gocode/src/github.com/cznic/ql/parser.go
/usr/share/gocode/src/github.com/cznic/ql/plan.go
/usr/share/gocode/src/github.com/cznic/ql/ql.go
/usr/share/gocode/src/github.com/cznic/ql/ql/main.go
/usr/share/gocode/src/github.com/cznic/ql/scanner.go
/usr/share/gocode/src/github.com/cznic/ql/stmt.go
/usr/share/gocode/src/github.com/cznic/ql/storage.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/camlistore/go4/lock/lock.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/camlistore/go4/lock/lock_appengine.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/camlistore/go4/lock/lock_darwin_amd64.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/camlistore/go4/lock/lock_freebsd.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/camlistore/go4/lock/lock_linux_amd64.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/camlistore/go4/lock/lock_linux_arm.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/camlistore/go4/lock/lock_plan9.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/camlistore/go4/lock/lock_sigzero.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/2pc.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/2pc_docs.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/btree.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/errors.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/falloc.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/filer.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/gb.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/lldb.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/memfiler.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/osfiler.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/simplefilefiler.go
/usr/share/gocode/src/github.com/cznic/ql/vendored/github.com/cznic/exp/lldb/xact.go

%changelog
* Tue Jun 21 2016 Vladimir Rusinov <vrusinov@google.com> 1.0.3-1
- First version.
