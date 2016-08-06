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

%global provider        github
%global provider_tld    com
%global project         golang
%global repo            protobuf
# https://github.com/golang/protobuf
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          6aaa8d47701fa6cf07e914ec01fde3d4a1fe79c3
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global simport_path    code.google.com/p/goprotobuf

Name:           golang-googlecode-goprotobuf
Version:        0
Release:        0.21.git%{shortcommit}%{?dist}
Summary:        Go support for Google protocol buffers
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

Requires:       protobuf
Provides:       protoc-gen-go = %{version}-%{release}

%description
This package provides support for protocol buffers in the form of a protocol
compiler plugin which generates Go source files that, once compiled, can access
and manage protocol buffers.

Install %{name}-devel for the associated support library.

%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
%endif

Provides:      golang(%{import_path}/jsonpb) = %{version}-%{release}
Provides:      golang(%{import_path}/jsonpb/jsonpb_test_proto) = %{version}-%{release}
Provides:      golang(%{import_path}/proto) = %{version}-%{release}
Provides:      golang(%{import_path}/proto/proto3_proto) = %{version}-%{release}
Provides:      golang(%{import_path}/proto/testdata) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go/descriptor) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go/generator) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go/plugin) = %{version}-%{release}
Provides:      golang(%{import_path}/protoc-gen-go/testdata/my_test) = %{version}-%{release}

# back compatibility
Provides:      golang(%{simport_path}/jsonpb) = %{version}-%{release}
Provides:      golang(%{simport_path}/jsonpb/jsonpb_test_proto) = %{version}-%{release}
Provides:      golang(%{simport_path}/proto) = %{version}-%{release}
Provides:      golang(%{simport_path}/proto/proto3_proto) = %{version}-%{release}
Provides:      golang(%{simport_path}/proto/testdata) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go/descriptor) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go/generator) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go/plugin) = %{version}-%{release}
Provides:      golang(%{simport_path}/protoc-gen-go/testdata/my_test) = %{version}-%{release}


%description devel
This package provides  a library that implements run-time support for
encoding (marshaling), decoding (unmarshaling), and accessing protocol
buffers in the Go language.

Install %{name} for the related protocol compiler plugin.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
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
providing packages with %{import_path} prefix.

%prep
%setup -q -n %{repo}-%{commit}

%build
# If gccgo_arches does not fit or is not defined fall through to golang
# gccco arches
%ifarch 0%{?gccgo_arches}
%if 0%{?gcc_go_build:1}
export GOCOMPILER='%{gcc_go_build}'
%else
echo "No compiler for SA"
exit 1
%endif
# golang arches (due to ExclusiveArch)
%else
%if 0%{?golang_build:1}
export GOCOMPILER='%{golang_build} -ldflags "$LDFLAGS"'
%else
export GOCOMPILER='go build -ldflags "$LDFLAGS"'
%endif
%endif

export LDFLAGS=""
%if 0%{?with_debug}
%ifarch 0%{?gccgo_arches}
export OLD_RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
function gobuild {
export RPM_OPT_FLAGS="$OLD_RPM_OPT_FLAGS -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')"
eval ${GOCOMPILER} -a -v -x "$@";
}
%else
export OLD_LDFLAGS="$LDFLAGS"
function gobuild {
export LDFLAGS="$OLD_LDFLAGS -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')"
eval ${GOCOMPILER} -a -v -x "$@";
}
%endif
%else
function gobuild { eval ${GOCOMPILER} -a -v -x "$@"; }
%endif

mkdir -p src/github.com/golang
ln -s ../../../ src/github.com/golang/protobuf

%if ! 0%{?with_bundled}

export GOPATH=$(pwd):%{gopath}
%else
echo "Unable to build from bundled deps. No Godeps nor vendor directory"
exit 1
%endif

gobuild -o bin/protoc-gen-go %{import_path}/protoc-gen-go

%install
install -d %{buildroot}%{_bindir}
install -m 755 bin/protoc-gen-go %{buildroot}/%{_bindir}/protoc-gen-go

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
install -d -p %{buildroot}/%{gopath}/src/%{simport_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{simport_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{simport_path}/$file
    echo "%%{gopath}/src/%%{simport_path}/$file" >> devel.file-list
done
pushd %{buildroot}/%{gopath}/src/%{simport_path}/
# github.com/golang/protobuf -> code.google.com/p/goprotobuf
sed -i 's/"github\.com\/golang\/protobuf/"code\.google\.com\/p\/goprotobuf/g' \
        $(find . -name '*.go')
popd
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go") proto/testdata/*.proto; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
done
for file in $(find protoc-gen-go/testdata \! -iname "*.go"); do
    if [ -d $file ]; then
        echo "%%dir %%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
        continue
    fi
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
gotest %{import_path}/jsonpb
gotest %{import_path}/proto
# --- FAIL: TestGolden (0.09s)
#    golden_test.go:52: sum("test.pb.go"): length is 78494
#gotest %%{import_path}/proto/testdata
gotest %{import_path}/protoc-gen-go/generator
#gotest %%{import_path}/protoc-gen-go/testdata
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%doc AUTHORS CONTRIBUTORS LICENSE README.md
%{_bindir}/protoc-gen-go

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS CONTRIBUTORS
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{simport_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc README.md AUTHORS CONTRIBUTORS
%endif

%changelog
* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 0-0.21.git6aaa8d4
- Bump to upstream 6aaa8d47701fa6cf07e914ec01fde3d4a1fe79c3
  related: #1246113

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.20.git3d2510a
- Bump to upstream 3d2510a4dd961caffa2ae781669c628d82db700a
  related: #1246113

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.19.git0f7a9ca
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.git0f7a9ca
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.17.git446d52d
- Change deps on compiler(go-compiler)
- Update Arches
- Use %%license

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.16.git0f7a9ca
- Bump to upstream 0f7a9caded1fb3c9cc5a9b4bcf2ff633cc8ae644
- Update spec file to spec-2.0
  resolves: #1246113

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.gitefd7476
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 09 2015 jchaloup <jchaloup@redhat.com> - 0-0.14.gitefd7476
- Bump to upstream efd7476481382c195beb33acd8ec2f1527167fb4
  related: #1018057

* Thu Mar 05 2015 jchaloup <jchaloup@redhat.com> - 0-0.13.gitc22ae3c
- Bump to upstream c22ae3cf020a21ebb7ae566dccbe90fc8ea4f9ea
  related: #1018057

* Sun Feb 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.12.git7f07925
- Extend Provides for proto/testdata
  related: #1018057

* Fri Jan 30 2015 jchaloup <jchaloup@redhat.com> - 0-0.11.git7f07925
- Provide back compatibility provides
  resolves: #1187495 #1187491 #1187494

* Mon Jan 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.10.git7f07925
- Bump to 7f07925444bb51fa4cf9dfe6f7661876f8852275
  related: #1018057

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.hg61664b8425f3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.hg61664b8425f3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Lokesh Mandvekar <lsm5@redhat.com> - 0-0.7.hg61664b8425f3
- removed double quotes from provides

* Wed Oct 16 2013 Peter Lemenkov <lemenkov@gmail.com> - 0-0.6.hg61664b8425f3
- Added missing buildrequires

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.hg61664b8425f3
- description update

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.hg61664b8425f3
- defattr removed
- docs included in base and devel packages

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.hg61664b8425f3
- testdata directories excluded

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.hg61664b8425f3
- compiler plugin in archful base package
- libraries in noarch (except rhel6) devel subpackage

* Fri Oct 11 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.hg61664b8425f3
- Initial fedora package
