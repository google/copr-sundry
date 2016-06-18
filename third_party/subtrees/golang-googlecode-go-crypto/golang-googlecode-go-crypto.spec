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

%global provider        github
%global provider_tld    com
%global project         golang
%global repo            crypto
# https://github.com/golang/crypto
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     golang.org/x/crypto
%global commit          c10c31b5e94b6f7a0283272dc2bb27163dcea24b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global gc_import_path     code.google.com/p/go.crypto
%global gc_rev             69e2a90ed92d03812364aeb947b7068dc42e561e
%global gc_shortrev        %(r=%{rev}; echo ${r:0:12})

%global x_name          golang-golangorg-crypto

%global devel_main      %{x_name}-devel

Name:           golang-googlecode-go-crypto
Version:        0
Release:        0.10.git%{shortcommit}%{?dist}
Summary:        Supplementary Go cryptography libraries
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

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

Provides:      golang(%{gc_import_path}/bcrypt) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/blowfish) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/bn256) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/cast5) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/curve25519) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/hkdf) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/md4) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/nacl/box) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/nacl/secretbox) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/ocsp) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/openpgp) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/openpgp/armor) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/openpgp/clearsign) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/openpgp/elgamal) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/openpgp/errors) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/openpgp/packet) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/openpgp/s2k) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/otr) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/pbkdf2) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/poly1305) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/ripemd160) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/salsa20) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/salsa20/salsa) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/scrypt) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/sha3) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/ssh) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/ssh/agent) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/ssh/terminal) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/ssh/test) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/ssh/testdata) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/twofish) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/xtea) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/xts) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gc_import_path} prefix.

%package -n %{x_name}-devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
%endif

Provides:      golang(%{import_path}/bcrypt) = %{version}-%{release}
Provides:      golang(%{import_path}/blowfish) = %{version}-%{release}
Provides:      golang(%{import_path}/bn256) = %{version}-%{release}
Provides:      golang(%{import_path}/cast5) = %{version}-%{release}
Provides:      golang(%{import_path}/curve25519) = %{version}-%{release}
Provides:      golang(%{import_path}/hkdf) = %{version}-%{release}
Provides:      golang(%{import_path}/md4) = %{version}-%{release}
Provides:      golang(%{import_path}/nacl/box) = %{version}-%{release}
Provides:      golang(%{import_path}/nacl/secretbox) = %{version}-%{release}
Provides:      golang(%{import_path}/ocsp) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/armor) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/clearsign) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/elgamal) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/errors) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/packet) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/s2k) = %{version}-%{release}
Provides:      golang(%{import_path}/otr) = %{version}-%{release}
Provides:      golang(%{import_path}/pbkdf2) = %{version}-%{release}
Provides:      golang(%{import_path}/poly1305) = %{version}-%{release}
Provides:      golang(%{import_path}/ripemd160) = %{version}-%{release}
Provides:      golang(%{import_path}/salsa20) = %{version}-%{release}
Provides:      golang(%{import_path}/salsa20/salsa) = %{version}-%{release}
Provides:      golang(%{import_path}/scrypt) = %{version}-%{release}
Provides:      golang(%{import_path}/sha3) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/agent) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/terminal) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/test) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/testdata) = %{version}-%{release}
Provides:      golang(%{import_path}/twofish) = %{version}-%{release}
Provides:      golang(%{import_path}/xtea) = %{version}-%{release}
Provides:      golang(%{import_path}/xts) = %{version}-%{release}

%description -n %{x_name}-devel
%{summary}

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
Requires:        %{x_name}-devel = %{version}-%{release}

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
install -d -p %{buildroot}/%{gopath}/src/%{gc_import_path}/
echo "%%dir %%{gopath}/src/%%{gc_import_path}/." >> gc_devel.file-list
for ext in go s; do
	# find all *.go but no *_test.go files and generate devel.file-list
	for file in $(find . -iname "*.$ext" \! -iname "*_test.go") ; do
	    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
	    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
	    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
	    install -d -p %{buildroot}/%{gopath}/src/%{gc_import_path}/$(dirname $file)
	    cp -pav $file %{buildroot}/%{gopath}/src/%{gc_import_path}/$file
	    echo "%%{gopath}/src/%%{gc_import_path}/$file" >> gc_devel.file-list
	done
done
pushd %{buildroot}/%{gopath}/src/%{gc_import_path}
sed -i 's/"golang\.org\/x\/crypto/"code\.google\.com\/p\/go\.crypto/g' \
        $(find . -name '*.go')
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
for file in ./sha3/testdata/keccakKats.json.deflate; do
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/sha3/testdata
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
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

%gotest %{import_path}/bcrypt
%gotest %{import_path}/blowfish
%gotest %{import_path}/bn256
%gotest %{import_path}/cast5
%gotest %{import_path}/curve25519
%gotest %{import_path}/hkdf
%gotest %{import_path}/md4
%gotest %{import_path}/nacl/box
%gotest %{import_path}/nacl/secretbox
# undefined: elliptic.P224
#%gotest %%{import_path}/ocsp
%gotest %{import_path}/openpgp
%gotest %{import_path}/openpgp/armor
%gotest %{import_path}/openpgp/clearsign
%gotest %{import_path}/openpgp/elgamal
%gotest %{import_path}/openpgp/packet
%gotest %{import_path}/openpgp/s2k
%gotest %{import_path}/otr
%gotest %{import_path}/pbkdf2
%gotest %{import_path}/poly1305
%gotest %{import_path}/ripemd160
%gotest %{import_path}/salsa20
%gotest %{import_path}/salsa20/salsa
%gotest %{import_path}/scrypt
%gotest %{import_path}/sha3
# undefined: elliptic.P224
#%%gotest %%{import_path}/ssh
%gotest %{import_path}/ssh/agent
%gotest %{import_path}/ssh/terminal
%gotest %{import_path}/ssh/test
%gotest %{import_path}/twofish
%gotest %{import_path}/xtea
%gotest %{import_path}/xts
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files -n %{x_name}-devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTING.md README AUTHORS CONTRIBUTORS
%dir %{gopath}/src/%{import_path}

%files devel -f gc_devel.file-list
%license LICENSE
%doc CONTRIBUTING.md README AUTHORS CONTRIBUTORS
%dir %{gopath}/src/%{gc_import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc CONTRIBUTING.md README AUTHORS CONTRIBUTORS
%endif

%changelog
* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.10.gitc10c31b
- Bump to upstream c10c31b5e94b6f7a0283272dc2bb27163dcea24b
  related: #1231618

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.gitc57d4a7
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitc57d4a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.gitc57d4a7
- Fix sed for import path
  related: #1231618

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitc57d4a7
- Choose the correct devel subpackage
  related: #1231618

* Wed Aug 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitc57d4a7
- Update spec file to spec-2.0
  related: #1231618

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitc57d4a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git%%{shortcommit}
- Repository has moved to github.com/golang/crypto, updating spec file accordingly
  resolves: #1231618

* Sun Dec 14 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.hg69e2a90ed92d
- Correct Source0 URL
- Correct paths for golang.org/x/crypto/*

* Thu Dec 04 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.hg69e2a90ed92d
- First package for Fedora
  resolves: #1148704
