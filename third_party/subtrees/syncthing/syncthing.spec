%global debug_package %{nil}

Name: syncthing
Version: 0.14.3
Release: 2%{?dist}
Summary: Synchronization service
License:MIT
URL:http://syncthing.net/    
Source0: https://github.com/syncthing/syncthing/archive/v%{version}.zip
BuildRequires:  systemd
BuildRequires:  golang >= 1.2-7
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

BuildRequires: golang(golang.org/x/crypto/bcrypt)
BuildRequires: golang(github.com/vitrun/qart/qr)
BuildRequires: golang(github.com/jackpal/gateway)
BuildRequires: golang(github.com/AudriusButkevicius/go-nat-pmp)
BuildRequires: golang(github.com/kardianos/osext)
BuildRequires: golang(github.com/syndtr/goleveldb/leveldb/util)
BuildRequires: golang(github.com/rcrowley/go-metrics)
BuildRequires: golang(github.com/gobwas/glob)
BuildRequires: golang(golang.org/x/net/ipv6)
BuildRequires: golang(golang.org/x/net/proxy)
BuildRequires: golang(github.com/calmh/du)
BuildRequires: golang(golang.org/x/text/unicode/norm)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(github.com/thejerf/suture)
BuildRequires: golang(github.com/lib/pq)
BuildRequires: golang(github.com/juju/ratelimit)
BuildRequires: golang(github.com/golang/groupcache/lru)
BuildRequires: golang(github.com/cznic/ql)
BuildRequires: golang(github.com/calmh/xdr)
BuildRequires: golang(github.com/calmh/luhn)
BuildRequires: golang(github.com/bkaradzic/go-lz4)
BuildRequires: golang(github.com/cznic/b)
BuildRequires: golang(github.com/cznic/bufs)
BuildRequires: golang(github.com/cznic/fileutil)
BuildRequires: golang(github.com/cznic/mathutil)
BuildRequires: golang(github.com/cznic/sortutil)
BuildRequires: golang(github.com/cznic/strutil)
BuildRequires: golang(github.com/cznic/zappy)
BuildRequires: golang(github.com/gogo/protobuf/gogoproto)
BuildRequires: golang(github.com/oschwald/geoip2-golang)
BuildRequires: golang(github.com/oschwald/maxminddb-golang)
BuildRequires: golang(golang.org/x/sys/unix)


%description
Syncthing replaces Dropbox and BitTorrent Sync with something open,
trustworthy and decentralized. Your data is your data alone and you deserve to
choose where it is stored, if it is shared with some third party and how it's
transmitted over the Internet.

Using syncthing, that control is returned to you.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p ./_build/src/github.com/%{name}
ln -s $(pwd) ./_build/src/github.com/%{name}/%{name}
rm -rf ./_build/src/github.com/syncthing/syncthing/vendor/

# Starting with 0.7, sytncthing build script behaves weird with multiple things in GOPATH.
ln -s /usr/share/gocode/src/github.com/* $(pwd)/_build/src/github.com/
ln -s /usr/share/gocode/src/golang.org $(pwd)/_build/src/
export GOPATH=$(pwd)/_build
export GOBIN=$(pwd)/bin

go run build.go assets
go build -i -v -ldflags "-w -X main.Version=v%{version}" -tags noupgrade ./cmd/syncthing
go install -v -ldflags "-w -X main.Version=v%{version}" -tags noupgrade ./cmd/syncthing

%check
export GOPATH=$(pwd)/_build:%{gopath}
# Tests are failing due to missing runtime/race.
# TODO: re-enable tests.
#./build.sh test

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 ./bin/syncthing %{buildroot}%{_bindir}
strip -s %{buildroot}%{_bindir}/syncthing

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 ./etc/linux-systemd/system/syncthing@.service %{buildroot}%{_unitdir}


%post
%systemd_post %{name}@.service

%preun
%systemd_preun %{name}@.servie

%postun
%systemd_postun_with_restart %{name}@.service 

%files
%doc AUTHORS CONDUCT.md CONTRIBUTING.md LICENSE NICKS README.md
%{_bindir}/syncthing
%{_unitdir}/%{name}@.service


%changelog
* Sun Aug 07 2016 Vladimir Rusinov <vrusinov@google.com> 0.14.3-2
- Fix supplied version.

* Fri Jul 29 2016 Vladimir Rusinov <vrusinov@google.com> 0.14.3-1
- Version bump.

* Wed Jun 15 2016 Vladimir Rusinov <vrusinov@google.com> 0.13.7-1
- Version update to v0.13.7.

* Sat Jan 09 2016 Vladimir Rusinov <vrusinov@google.com> 0.12.11-1
- Version update to v0.12.11.

* Mon Sep 21 2015 Vladimir Rusinov <vrusinov@google.com> 0.9.17-2.1
- Use source tarball instead of binary package.

* Sat Sep 20 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.17-2.0
- Version update to v0.9.17

* Sat Sep 20 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.17-2.0
- Version update to v0.9.17

* Fri Sep 12 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.15-9
- Version update to v0.9.15

* Wed Sep 10 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.14-8
- Version updated to v0.9.14
- Spec files fixed

* Tue Sep 9 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.13-7
- Version updated to v0.9.13

* Mon Sep 1 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.10-6
- Version updated to v0.9.10
- Spec files dates fixed and re-checked.

* Wed Aug 27 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.9-5
- Version updated to v0.9.9
- Readme fixes
- Source folder path fixed

* Mon Aug 25 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.8-4
- Version updated to v0.9.8

* Sun Aug 17 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.5-3
- Version updated to v0.9.5

* Sat Aug 16 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.4-2
- Version updated to v0.9.4

* Mon Jul 28 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.8.21-1
- Initial Version

