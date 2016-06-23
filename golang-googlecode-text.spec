%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 1
%global with_bundled 0
%global with_debug 0
%global with_check 1
%global with_unit_test 1
%else
%global with_devel 0
%global with_bundled 0
%global with_debug 0
%global with_check 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider_tld    com 
%global provider        github
%global project         golang
%global repo            text
# https://github.com/golang/text
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     code.google.com/p/go.text
%global commit          6fc2e00a0d64b1f7fc1212dae5b0c939cf6d9ac4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global x_provider      golang
%global x_provider_tld  org
%global x_repo          text
%global x_import_path   %{x_provider}.%{x_provider_tld}/x/%{x_repo}
%global x_name          golang-%{x_provider}%{x_provider_tld}-%{repo}

%global devel_main      %{x_name}-devel
%global devel_prefix    x

Name:       golang-googlecode-text
Version:    0
Release:    0.10.git%{shortcommit}%{?dist}
Summary:    Supplementary Go text libraries
License:    BSD
URL:        https://%{provider_prefix}
Source0:    https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

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
%package devel
Summary:    Supplementary Go text libraries for code.google.com/p/ imports
BuildArch:  noarch

%if 0%{?with_check}
%endif

Provides:   golang(%{import_path}) = %{version}-%{release}
Provides:   golang(%{import_path}/cases) = %{version}-%{release}
Provides:   golang(%{import_path}/collate) = %{version}-%{release}
Provides:   golang(%{import_path}/collate/build) = %{version}-%{release}
Provides:   golang(%{import_path}/collate/colltab) = %{version}-%{release}
Provides:   golang(%{import_path}/currency) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/charmap) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/htmlindex) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/ianaindex) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/japanese) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/korean) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/simplifiedchinese) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/traditionalchinese) = %{version}-%{release}
Provides:   golang(%{import_path}/encoding/unicode) = %{version}-%{release}
Provides:   golang(%{import_path}/language) = %{version}-%{release}
Provides:   golang(%{import_path}/language/display) = %{version}-%{release}
Provides:   golang(%{import_path}/message) = %{version}-%{release}
Provides:   golang(%{import_path}/runes) = %{version}-%{release}
Provides:   golang(%{import_path}/search) = %{version}-%{release}
Provides:   golang(%{import_path}/transform) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/bidi) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/cldr) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/norm) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/precis) = %{version}-%{release}
Provides:   golang(%{import_path}/unicode/rangetable) = %{version}-%{release}
Provides:   golang(%{import_path}/width) = %{version}-%{release}

%package -n %{x_name}-devel
Summary:    Supplementary Go text libraries for golang.org/x/ imports
BuildArch:  noarch

%if 0%{?with_check}
%endif

Provides:   golang(%{x_import_path}) = %{version}-%{release}
Provides:   golang(%{x_import_path}/cases) = %{version}-%{release}
Provides:   golang(%{x_import_path}/collate) = %{version}-%{release}
Provides:   golang(%{x_import_path}/collate/build) = %{version}-%{release}
Provides:   golang(%{x_import_path}/collate/colltab) = %{version}-%{release}
Provides:   golang(%{x_import_path}/currency) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/charmap) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/htmlindex) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/ianaindex) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/japanese) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/korean) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/simplifiedchinese) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/traditionalchinese) = %{version}-%{release}
Provides:   golang(%{x_import_path}/encoding/unicode) = %{version}-%{release}
Provides:   golang(%{x_import_path}/language) = %{version}-%{release}
Provides:   golang(%{x_import_path}/language/display) = %{version}-%{release}
Provides:   golang(%{x_import_path}/message) = %{version}-%{release}
Provides:   golang(%{x_import_path}/runes) = %{version}-%{release}
Provides:   golang(%{x_import_path}/search) = %{version}-%{release}
Provides:   golang(%{x_import_path}/transform) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/bidi) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/cldr) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/norm) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/precis) = %{version}-%{release}
Provides:   golang(%{x_import_path}/unicode/rangetable) = %{version}-%{release}
Provides:   golang(%{x_import_path}/width) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go text libraries with code.google.com/p/ imports.

%description -n %{x_name}-devel

This package contains library source intended for building other packages
which use the supplementary Go text libraries with golang.org/x/ imports.
%endif

%if 0%{?with_unit_test}
%package unit-test
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{x_name}-devel = %{version}-%{release}

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{x_import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
install -d -p %{buildroot}%{gopath}/src/%{x_import_path}
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{x_import_path}/$file
    echo "%%{gopath}/src/%%{x_import_path}/$file" >> x_devel.file-list
done
pushd %{buildroot}/%{gopath}/src/%{import_path}
# from https://groups.google.com/forum/#!topic/golang-nuts/eD8dh3T9yyA, first post
sed -i 's/"golang\.org\/x\//"code\.google\.com\/p\/go\./g' \
        $(find . -name '*.go')
popd
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{x_import_path}/$file
    echo "%%{gopath}/src/%%{x_import_path}/$file" >> unit-test.file-list
done
for file in $(find ./encoding/testdata -iname "*.txt"); do
    install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{x_import_path}/$file
    echo "%%{gopath}/src/%%{x_import_path}/$file" >> unit-test.file-list
done
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/Godeps/_workspace:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{x_import_path}/cases
%gotest %{x_import_path}/collate
%gotest %{x_import_path}/collate/build
%gotest %{x_import_path}/collate/colltab
%gotest %{x_import_path}/currency
%gotest %{x_import_path}/encoding
%gotest %{x_import_path}/encoding/charmap
%gotest %{x_import_path}/encoding/htmlindex
%gotest %{x_import_path}/encoding/ianaindex
%gotest %{x_import_path}/encoding/japanese
%gotest %{x_import_path}/encoding/korean
%gotest %{x_import_path}/encoding/simplifiedchinese
%gotest %{x_import_path}/encoding/traditionalchinese
%gotest %{x_import_path}/encoding/unicode
%gotest %{x_import_path}/internal
%gotest %{x_import_path}/internal/colltab
%gotest %{x_import_path}/internal/format
%gotest %{x_import_path}/internal/tag
%gotest %{x_import_path}/internal/triegen
%gotest %{x_import_path}/internal/ucd
%gotest %{x_import_path}/language
%gotest %{x_import_path}/language/display
%gotest %{x_import_path}/message
%gotest %{x_import_path}/runes
%gotest %{x_import_path}/search
%gotest %{x_import_path}/transform
%gotest %{x_import_path}/unicode/bidi
%gotest %{x_import_path}/unicode/cldr
%gotest %{x_import_path}/unicode/norm
%gotest %{x_import_path}/unicode/precis
%gotest %{x_import_path}/unicode/rangetable
%gotest %{x_import_path}/width
%endif

%if 0%{?with_devel}
%files devel
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc AUTHORS CONTRIBUTORS PATENTS README
%{gopath}/src/%{import_path}

%files -n %{x_name}-devel
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc AUTHORS CONTRIBUTORS PATENTS README
%{gopath}/src/%{x_import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CONTRIBUTORS
%endif

%changelog
* Tue Feb 23 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.10.git6fc2e00
- License and arch definition cleanup

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git6fc2e00
- https://fedoraproject.org/wiki/Changes/golang1.6

* Fri Feb 19 2016 jchaloup <jchaloup@redhat.com> - 0-0.8.git6fc2e00
- Bump to upstream 6fc2e00a0d64b1f7fc1212dae5b0c939cf6d9ac4
  Repository has moved from code.google.com/p/go.text to github.com/golang/text
  related: #1254601

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.hg5b2527008a4c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.hg5b2527008a4c
- Choose the correct devel subpackage
  related: #1254601

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.hg5b2527008a4c
- Update spec file to spec-2.0
  resolves: #1254601

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.hg5b2527008a4c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.3.hg5b2527008a4c
- Update to the latest commit 5b2527008a4c8988ca9dc6f010ebfb9dae67150b
  related: #1056285

* Fri Nov 21 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.hg024681b033be
- Extend import paths for golang.org/x/
- Choose the correct architecture
  related: #1056285

* Sun Sep 28 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.1.hg024681b033be
- Resolves: rhbz#1056285 - Initial package
