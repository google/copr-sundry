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

%define copying() \
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7 \
%license %{*} \
%else \
%doc %{*} \
%endif

%global provider        github
%global provider_tld    com
%global project         syndtr
%global repo            gosnappy
# https://github.com/syndtr/gosnappy
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          156a073208e131d7d2e212cb749feae7c339e846
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global g_commit          723cc1e459b8eea2dea4583200fd60757d40097a
%global g_shortcommit     %(c=%{g_commit}; echo ${c:0:7})
%global g_provider_prefix github.com/golang/snappy
%global g_import_path     %{g_provider_prefix}
%global g_name            golang-github-golang-snappy

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.7.git%{shortcommit}%{?dist}
Summary:        Implementation of the Snappy compression format for Go
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source1:        https://%{g_provider_prefix}/archive/%{g_commit}/snappy-%{g_shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
%endif

Provides:      golang(%{import_path}/snappy) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package -n %{g_name}-devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
%endif

Provides:      golang(%{g_import_path}) = %{version}-%{release}

%description -n %{g_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{g_import_path} prefix.

%endif

%if 0%{?with_unit_test}
%package -n %{g_name}-unit-test
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{g_name}-devel = %{version}-%{release}

%description -n %{g_name}-unit-test
%{summary}

This package contains unit tests for project
providing packages with %{g_import_path} prefix.
%endif

%prep
%setup -q -n snappy-%{g_commit} -T -b 1
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
install -d -p %{buildroot}/%{gopath}/src/%{g_import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
echo "%%dir %%{gopath}/src/%%{g_import_path}/." >> g_devel.file-list

# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done

pushd ../snappy-%{g_commit}

# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{g_import_path}/$(dirname $file)" >> ../%{repo}-%{commit}/g_devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{g_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{g_import_path}/$file
    echo "%%{gopath}/src/%%{g_import_path}/$file" >> ../%{repo}-%{commit}/g_devel.file-list
done

popd
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{gopath}/src/%{g_import_path}/
# find all *_test.go files and generate unit-test.file-list

pushd ../snappy-%{g_commit}

for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{gopath}/src/%%{g_import_path}/$(dirname $file)" >> ../%{repo}-%{commit}/g_devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{g_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{g_import_path}/$file
    echo "%%{gopath}/src/%%{g_import_path}/$file" >> ../%{repo}-%{commit}/unit-test.file-list
done
popd
%endif

%if 0%{?with_devel}
sort -u -o g_devel.file-list g_devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/Godeps/_workspace:%{gopath}:/usr/include:/usr/lib64
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{g_import_path}
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README AUTHORS CONTRIBUTORS
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}

%files -n %{g_name}-devel -f g_devel.file-list
%license LICENSE
%doc README AUTHORS CONTRIBUTORS
%dir %{gopath}/src/github.com/golang
%endif

%if 0%{?with_unit_test}
%files -n %{g_name}-unit-test -f unit-test.file-list
%license LICENSE
%doc README AUTHORS CONTRIBUTORS
%endif

%changelog
* Fri Apr 15 2016 jchaloup <jchaloup@redhat.com> - 0-0.7.git156a073
- Polish the spec file
- Extend the spec with github.com/golang/snappy (which is newer version of gosnappy)
  related: #1220164

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git156a073
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git156a073
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.git156a073
- Update spec file to spec-2.0
  related: #1220164

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git156a073
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 10 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git156a073
- Bump to upstream 156a073208e131d7d2e212cb749feae7c339e846
  resolves: #1220164

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitce8acff
- First package for Fedora
  resolves: #1190411

