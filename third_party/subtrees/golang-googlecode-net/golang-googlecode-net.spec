%global with_devel 1
%global with_bundled 0
%global with_debug 0
%global with_check 0
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider_tld    com
%global provider        github
%global project         golang
%global repo            net
# https://github.com/golang/net
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     code.google.com/p/go.net
%global commit          6acef71eb69611914f7a30939ea9f6e194c78172
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global x_provider      golang
%global x_provider_tld  org
%global x_repo          net
%global x_import_path   %{x_provider}.%{x_provider_tld}/x/%{x_repo}
%global x_name          golang-%{x_provider}%{x_provider_tld}-%{repo}

%global devel_main      golang-golangorg-net-devel
%global devel_prefix    x

Name:       golang-googlecode-net
Version:    0
Release:    0.31.git%{shortcommit}%{?dist}
Summary:    Supplementary Go networking libraries
License:    BSD
URL:        https://%{provider_prefix}
Source0:    https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       Supplementary Go networking libraries
BuildArch:     noarch

%if 0%{?with_check}
BuildRequires:  golang(code.google.com/p/go.text/encoding)
BuildRequires:  golang(code.google.com/p/go.text/encoding/charmap)
BuildRequires:  golang(code.google.com/p/go.text/encoding/htmlindex)
BuildRequires:  golang(code.google.com/p/go.text/transform)
%endif

Requires:  golang(code.google.com/p/go.text/encoding)
Requires:  golang(code.google.com/p/go.text/encoding/charmap)
Requires:  golang(code.google.com/p/go.text/encoding/htmlindex)
Requires:  golang(code.google.com/p/go.text/transform)

Provides:   golang(%{import_path}/context) = %{version}-%{release}
Provides:   golang(%{import_path}/context/ctxhttp) = %{version}-%{release}
Provides:   golang(%{import_path}/dict) = %{version}-%{release}
Provides:   golang(%{import_path}/html) = %{version}-%{release}
Provides:   golang(%{import_path}/html/atom) = %{version}-%{release}
Provides:   golang(%{import_path}/html/charset) = %{version}-%{release}
Provides:   golang(%{import_path}/http2) = %{version}-%{release}
Provides:   golang(%{import_path}/http2/hpack) = %{version}-%{release}
Provides:   golang(%{import_path}/icmp) = %{version}-%{release}
Provides:   golang(%{import_path}/idna) = %{version}-%{release}
Provides:   golang(%{import_path}/ipv4) = %{version}-%{release}
Provides:   golang(%{import_path}/ipv6) = %{version}-%{release}
Provides:   golang(%{import_path}/netutil) = %{version}-%{release}
Provides:   golang(%{import_path}/proxy) = %{version}-%{release}
Provides:   golang(%{import_path}/publicsuffix) = %{version}-%{release}
Provides:   golang(%{import_path}/trace) = %{version}-%{release}
Provides:   golang(%{import_path}/webdav) = %{version}-%{release}
Provides:   golang(%{import_path}/websocket) = %{version}-%{release}
Provides:   golang(%{import_path}/xsrftoken) = %{version}-%{release}

%package -n %{x_name}-devel
Summary:       Supplementary Go networking libraries for golang.org/x/ imports
BuildArch:     noarch

%if 0%{?with_unit_test}
BuildRequires:  golang(golang.org/x/text/encoding)
BuildRequires:  golang(golang.org/x/text/encoding/charmap)
BuildRequires:  golang(golang.org/x/text/encoding/htmlindex)
BuildRequires:  golang(golang.org/x/text/transform)
%endif

Requires:  golang(golang.org/x/text/encoding)
Requires:  golang(golang.org/x/text/encoding/charmap)
Requires:  golang(golang.org/x/text/encoding/htmlindex)
Requires:  golang(golang.org/x/text/transform)

Provides:   golang(%{x_import_path}/context) = %{version}-%{release}
Provides:   golang(%{x_import_path}/context/ctxhttp) = %{version}-%{release}
Provides:   golang(%{x_import_path}/dict) = %{version}-%{release}
Provides:   golang(%{x_import_path}/html) = %{version}-%{release}
Provides:   golang(%{x_import_path}/html/atom) = %{version}-%{release}
Provides:   golang(%{x_import_path}/html/charset) = %{version}-%{release}
Provides:   golang(%{x_import_path}/http2) = %{version}-%{release}
Provides:   golang(%{x_import_path}/http2/hpack) = %{version}-%{release}
Provides:   golang(%{x_import_path}/icmp) = %{version}-%{release}
Provides:   golang(%{x_import_path}/idna) = %{version}-%{release}
Provides:   golang(%{x_import_path}/ipv4) = %{version}-%{release}
Provides:   golang(%{x_import_path}/ipv6) = %{version}-%{release}
Provides:   golang(%{x_import_path}/netutil) = %{version}-%{release}
Provides:   golang(%{x_import_path}/proxy) = %{version}-%{release}
Provides:   golang(%{x_import_path}/publicsuffix) = %{version}-%{release}
Provides:   golang(%{x_import_path}/trace) = %{version}-%{release}
Provides:   golang(%{x_import_path}/webdav) = %{version}-%{release}
Provides:   golang(%{x_import_path}/websocket) = %{version}-%{release}
Provides:   golang(%{x_import_path}/xsrftoken) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go networking libraries with code.google.com/p/ imports.

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
Requires:        %{name}-devel = %{version}-%{release}

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
install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for ext in go s; do
    for file in $(find . -iname "*.${ext}" \! -iname "*_test.go") ; do
        install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
        cp $file %{buildroot}/%{gopath}/src/%{import_path}/$file
        echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

        install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/$(dirname $file)
        cp $file %{buildroot}/%{gopath}/src/%{x_import_path}/$file
        echo "%%{gopath}/src/%%{x_import_path}/$file" >> x_devel.file-list
    done
done

pushd %{buildroot}/%{gopath}/src/%{import_path}/
sed -i 's/"golang\.org\/x\//"code\.google\.com\/p\/go\./g' \
        $(find . -name '*.go')
popd
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/
install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/html/testdata
install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/html/charset/testdata
cp -rpav html/testdata %{buildroot}/%{gopath}/src/%{x_import_path}/html
cp -rpav html/charset/testdata %{buildroot}/%{gopath}/src/%{x_import_path}/html/charset
echo "%%{gopath}/src/%%{x_import_path}/html/testdata" >> unit-test.file-list
echo "%%{gopath}/src/%%{x_import_path}/html/charset/testdata" >> unit-test.file-list
# find all files with $ext prefix and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/$(dirname $file)
    cp $file %{buildroot}/%{gopath}/src/%{x_import_path}/$file
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

%gotest %{x_import_path}/context
%gotest %{x_import_path}/context/ctxhttp
%gotest %{x_import_path}/html
%gotest %{x_import_path}/html/atom
%gotest %{x_import_path}/html/charset
# socket: permission denied
#%%gotest %%{x_import_path}/icmp
%gotest %{x_import_path}/idna
%gotest %{x_import_path}/internal/timeseries
%gotest %{x_import_path}/ipv4
%gotest %{x_import_path}/ipv6
%gotest %{x_import_path}/netutil
%gotest %{x_import_path}/proxy
%gotest %{x_import_path}/publicsuffix
%gotest %{x_import_path}/trace
%gotest %{x_import_path}/webdav
%gotest %{x_import_path}/webdav/internal/xml
%gotest %{x_import_path}/websocket
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc AUTHORS CONTRIBUTORS PATENTS README CONTRIBUTING.md
%dir %{gopath}/src/%{import_path}

%files -n %{x_name}-devel -f x_devel.file-list
%license LICENSE
%doc AUTHORS CONTRIBUTORS PATENTS README CONTRIBUTING.md
%dir %{gopath}/src/%{x_import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc AUTHORS CONTRIBUTORS PATENTS README CONTRIBUTING.md
%endif

%changelog
* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 0-0.31.git6acef71
- Bump to upstream 6acef71eb69611914f7a30939ea9f6e194c78172
  related: #1230677

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.30.git04b9de9
- https://fedoraproject.org/wiki/Changes/golang1.6

* Fri Feb 19 2016 jchaloup <jchaloup@redhat.com> - 0-0.29.git04b9de9
- Bump to upstream 04b9de9b512f58addf28c9853d50ebef61c3953e
  related: #1230677

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.git1bc0720
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.27.git1bc0720
- Bump to upstream 1bc0720082d79ce7ffc6ef6e523d00d46b0dee45
  related: #1230677

* Thu Sep 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.6.git446d52d
- Change deps on compiler(go-compiler)
- Update Arches
- Use %%license

* Wed Jul 29 2015 jchaloup <jchaloup@redhat.com> - 0-0.25.git446d52d
- Update of spec file to spec-2.0
  related: #1230677

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.24.git446d52d
- No debuginfo
  related: #1230677

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.23.git446d52d
- Bump to upstream 446d52dd4018303a13b36097e26d0888aca5d6ef
  related: #1230677

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.22.git7dbad50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 jchaloup <jchaloup@redhat.com> - 0-0.21.git7dbad50
- Bump to 7dbad50ab5b31073856416cdcfeb2796d682f844
  resolves: #1230677

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.20.git71586c3
- Bump to upstream 71586c3cf98f806af322c5a361660eb046e00501
- Repo moved to github, changing spec file header and globals

* Thu Dec 18 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.19.hg937a34c9de13
- Resolves: rhbz#1056185 disable ipv6 test
- also disable html/charset test

* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.18.hg937a34c9de13
- Update to the latest commit 937a34c9de13c766c814510f76bca091dee06028
  related: #1009967

* Mon Nov 24 2014 jchaloup <jchaloup@redhat.com> - 0-0.17.hg90e232e2462d
- Extend import paths for golang.org/x/
- context test failing on master
  related: #1009967

* Mon Sep 29 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.16.hg90e232e2462d
- Resolves: rhbz#1147193 - update to latest upstream revision 
  90e232e2462dedc03bf3c93358da62d54d55dfb6
- don't redefine gopath, don't own dirs owned by golang
- use golang >= 1.2.1-3 for golang specific rpm macros
- preserve timestamps of copied files
- br stuff from golang-googlecode-text

* Fri Jul 11 2014 Vincent Batts <vbatts@fedoraproject.org> - 0-0.15.hg84a4013f96e0
- don't fail on ipv6 test bz1056185

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.hg84a4013f96e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.13.hg84a4013f96e0
- golang exclusivearch for el6+
- add check

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.12.hg84a4013f96e0
- revert golang >= 1.2 version requirement

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.11.hg84a4013f96e0
- require golang 1.2 and up

* Wed Oct 16 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.10.hg84a4013f96e0
- removed double quotes from Provides

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.9.hg84a4013f96e0
- noarch for f19+ and rhel7+, exclusivearch otherwise

* Mon Oct 07 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.8.hg84a4013f96e0
- exclusivearch as per golang package
- debug_package nil

* Sun Sep 22 2013 Matthew Miller <mattdm@fedoraproject.org> 0-0.7.hg
- install just the source code for devel package

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.6.hg
- All Provides listed explicitly

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.hg
- Provides corrected

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.hg
- comment cleanup
- build explanation

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.hg
- html/webkit/scripted ownership set
- codereview.cfg not packaged

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.hg
- IPv6 doesn't build
- Typo correction
- directory ownership taken care of

* Thu Sep 19 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.hg
- Initial fedora package
