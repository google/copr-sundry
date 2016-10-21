%global with_devel 1
%global with_bundled 0
%global with_debug 0
%global with_check 1
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%define copying() \
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7 \
%license %{*} \
%else \
%doc %{*} \
%endif

%global provider        github
%global provider_tld    com
%global project         golang
%global repo            oauth2
# https://github.com/golang/oauth2
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     golang.org/x/oauth2
%global commit          1364adb2c63445016c5ed4518fc71f6a3cda6169
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global gc_rev             afe77d958c701557ec5dc56f6936fcc194d15520
%global gc_shortrev        %(r=%{gc_rev}; echo ${r:0:12})
%global gc_provider        google
%global gc_provider_sub    code
%global gc_provider_tld    com
%global gc_repo            goauth2
%global gc_import_path     %{gc_provider_sub}.%{gc_provider}.%{gc_provider_tld}/p/%{gc_repo}
%global gc_name            golang-%{gc_provider}%{gc_provider_sub}-%{gc_repo}

%global x_name          golang-golangorg-oauth2
%global devel_main      %{x_name}-devel

Name:           golang-googlecode-goauth2
Version:        0
Release:        0.17.git%{shortcommit}%{?dist}
Summary:        OAuth 2.0 for Go clients
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source1:        https://%{gc_repo}.%{gc_provider}%{gc_provider_sub}.%{gc_provider_tld}/archive/%{gc_rev}.tar.gz

# If go_arches not defined fall through to implicit golang archs
%if 0%{?go_arches:1}
ExclusiveArch:  %{go_arches}
%else
ExclusiveArch:   %{ix86} x86_64 %{arm}
%endif
# If gccgo_arches does not fit or is not defined fall through to golang
%ifarch 0%{?gccgo_arches}
BuildRequires:   gcc-go >= %{gccgo_min_vers}
%else
BuildRequires:   golang
%endif

%description
%{summary}

%if 0%{?with_devel}
%package -n %{x_name}-devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/appengine)
BuildRequires: golang(google.golang.org/appengine/urlfetch)
BuildRequires: golang(google.golang.org/cloud/compute/metadata)
%endif

Requires:      golang(golang.org/x/net/context)
Requires:      golang(google.golang.org/appengine)
Requires:      golang(google.golang.org/appengine/urlfetch)
Requires:      golang(google.golang.org/cloud/compute/metadata)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/bitbucket) = %{version}-%{release}
Provides:      golang(%{import_path}/clientcredentials) = %{version}-%{release}
Provides:      golang(%{import_path}/facebook) = %{version}-%{release}
Provides:      golang(%{import_path}/fitbit) = %{version}-%{release}
Provides:      golang(%{import_path}/github) = %{version}-%{release}
Provides:      golang(%{import_path}/google) = %{version}-%{release}
Provides:      golang(%{import_path}/hipchat) = %{version}-%{release}
Provides:      golang(%{import_path}/jws) = %{version}-%{release}
Provides:      golang(%{import_path}/jwt) = %{version}-%{release}
Provides:      golang(%{import_path}/linkedin) = %{version}-%{release}
Provides:      golang(%{import_path}/microsoft) = %{version}-%{release}
Provides:      golang(%{import_path}/odnoklassniki) = %{version}-%{release}
Provides:      golang(%{import_path}/paypal) = %{version}-%{release}
Provides:      golang(%{import_path}/slack) = %{version}-%{release}
Provides:      golang(%{import_path}/vk) = %{version}-%{release}


%description -n %{x_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package -n %{gc_name}-devel
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{gc_import_path}/appengine/serviceaccount) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/compute/serviceaccount) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/oauth) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/oauth/jwt) = %{version}-%{release}

%description -n %{gc_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gc_import_path} prefix.
%endif

%if 0%{?with_unit_test}
%package unit-test
Summary:         Unit tests for %{name} package
# If go_arches not defined fall through to implicit golang archs
%if 0%{?go_arches:1}
ExclusiveArch:  %{go_arches}
%else
ExclusiveArch:   %{ix86} x86_64 %{arm}
%endif
# If gccgo_arches does not fit or is not defined fall through to golang
%ifarch 0%{?gccgo_arches}
BuildRequires:   gcc-go >= %{gccgo_min_vers}
%else
BuildRequires:   golang
%endif

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{x_name}-devel = %{version}-%{release}

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{gc_repo}-%{gc_shortrev} -T -b 1
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done

install -d -p %{buildroot}/%{gopath}/src/%{gc_import_path}/
pushd ../%{gc_repo}-%{gc_shortrev}
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{gc_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{gc_import_path}/$file
    echo "%%{gopath}/src/%%{gc_import_path}/$file" >> ../%{repo}-%{commit}/gc_devel.file-list
done
popd

%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
done
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%ifarch 0%{?gccgo_arches}
function gotest { %{gcc_go_test} "$@"; }
%else
%if 0%{?golang_test:1}
function gotest { %{golang_test} "$@"; }
%else
function gotest { go test "$@"; }
%endif
%endif

export GOPATH=%{buildroot}/%{gopath}:%{gopath}
gotest %{import_path}
gotest %{import_path}/clientcredentials
# open testdata/gcloud/credentials: no such file or directory
#gotest %%{import_path}/google
gotest %{import_path}/internal
gotest %{import_path}/jws
gotest %{import_path}/jwt
%endif

%if 0%{?with_devel}
%files -n %{x_name}-devel -f devel.file-list
%copying LICENSE
%doc README.md CONTRIBUTING.md AUTHORS CONTRIBUTORS
%dir %{gopath}/src/%{import_path}

%files -n %{gc_name}-devel -f gc_devel.file-list
%copying LICENSE
%doc README.md CONTRIBUTING.md AUTHORS CONTRIBUTORS
%dir %{gopath}/src/%{gc_import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%copying LICENSE
%doc README.md CONTRIBUTING.md AUTHORS CONTRIBUTORS
%endif

%changelog
* Mon Aug 01 2016 jchaloup <jchaloup@redhat.com> - 0-0.17.git1364adb
- Bump to upstream 1364adb2c63445016c5ed4518fc71f6a3cda6169
  related: #1227273

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.16.git8914e50
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.15.git8914e50
- Bump to upstream 8914e5017ca260f2a3a1575b1e6868874050d95e
  related: #1227273

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.gitb5adcc2
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitb5adcc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.12.gitb5adcc2
- Choose the corret devel subpackage
  related: #1227273

* Wed Aug 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.11.gitb5adcc2
- Update spec file to spec-2.0
  related: #1227273

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.hgb5adcc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 jchaloup <jchaloup@redhat.com> - 0-0.9.hgb5adcc2
- Update provides of golang-googlecode-goauth2.
  There were not missing, it is just different subpackage.
  related: #1227273

* Tue Jun 09 2015 jchaloup <jchaloup@redhat.com> - 0-0.8.hgb5adcc2
- Add missing Provides
  related: #1227273

* Tue Jun 02 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.hgb5adcc2
- Bump to upstream b5adcc2dcdf009d0391547edc6ecbaff889f5bb9
  resolves: #1227273

* Sun Mar 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.hg267028f
- Add the latest commit of depricated code.google.com/o/goauth2 afe77d958c701557ec5dc56f6936fcc194d15520
  related: #1141822

* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.hgafe77d958c70
- Bump to upstream 267028f9bc2a1177dc5769be38c68c1b4fbe91c4
  related: #1141822

* Tue Nov 18 2014 jchaloup <jchaloup@redhat.com> - 0-0.4.hgafe77d958c70
- Choose the correct architecture
  related: #1141822

* Thu Sep 18 2014 jchaloup <jchaloup@redhat.com> - 0-0.3.hgafe77d958c70
- Initial commit to git

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.hgafe77d958c70
- update to afe77d958c70
- preserve timestamps of copied files

* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.hg6a3615e294b5
- First package for Fedora.
