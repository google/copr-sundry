%global provider        github
%global provider_tld    com
%global project         gobwas
%global repo            glob
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     github.com/%{project}/%{repo}

%global debug_package   %{nil}

Name:           golang-github-gobwas-%{repo}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Go Globbing Library
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{version}.tar.gz

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
%doc readme.md
%dir %{gopath}/src/%{import_path}
/usr/share/gocode/src/github.com/gobwas/glob/cmd/globdraw/main.go
/usr/share/gocode/src/github.com/gobwas/glob/cmd/globtest/main.go
/usr/share/gocode/src/github.com/gobwas/glob/compiler/compiler.go
/usr/share/gocode/src/github.com/gobwas/glob/glob.go
/usr/share/gocode/src/github.com/gobwas/glob/match/any.go
/usr/share/gocode/src/github.com/gobwas/glob/match/any_of.go
/usr/share/gocode/src/github.com/gobwas/glob/match/btree.go
/usr/share/gocode/src/github.com/gobwas/glob/match/contains.go
/usr/share/gocode/src/github.com/gobwas/glob/match/debug/debug.go
/usr/share/gocode/src/github.com/gobwas/glob/match/every_of.go
/usr/share/gocode/src/github.com/gobwas/glob/match/list.go
/usr/share/gocode/src/github.com/gobwas/glob/match/match.go
/usr/share/gocode/src/github.com/gobwas/glob/match/max.go
/usr/share/gocode/src/github.com/gobwas/glob/match/min.go
/usr/share/gocode/src/github.com/gobwas/glob/match/nothing.go
/usr/share/gocode/src/github.com/gobwas/glob/match/prefix.go
/usr/share/gocode/src/github.com/gobwas/glob/match/prefix_suffix.go
/usr/share/gocode/src/github.com/gobwas/glob/match/range.go
/usr/share/gocode/src/github.com/gobwas/glob/match/row.go
/usr/share/gocode/src/github.com/gobwas/glob/match/segments.go
/usr/share/gocode/src/github.com/gobwas/glob/match/single.go
/usr/share/gocode/src/github.com/gobwas/glob/match/suffix.go
/usr/share/gocode/src/github.com/gobwas/glob/match/super.go
/usr/share/gocode/src/github.com/gobwas/glob/match/text.go
/usr/share/gocode/src/github.com/gobwas/glob/syntax/ast/ast.go
/usr/share/gocode/src/github.com/gobwas/glob/syntax/ast/parser.go
/usr/share/gocode/src/github.com/gobwas/glob/syntax/lexer/lexer.go
/usr/share/gocode/src/github.com/gobwas/glob/syntax/lexer/token.go
/usr/share/gocode/src/github.com/gobwas/glob/syntax/syntax.go
/usr/share/gocode/src/github.com/gobwas/glob/util/runes/runes.go
/usr/share/gocode/src/github.com/gobwas/glob/util/strings/strings.go

%changelog
* Tue Jun 21 2016 Vladimir Rusinov <vrusinov@google.com> 0.2.0-1
- First version.
