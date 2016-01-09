%global debug_package %{nil}

%ifarch x86_64
%global altarch amd64
%endif
%ifarch %{ix86}
%global altarch 386
%endif
%ifarch %{arm}
%global altarch armv7
%endif

Name:syncthing
Version:0.9.17
Release:2.0%{?dist}
Summary:Syncthing
License:MIT
URL:http://syncthing.net/    
Source0:https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-linux-%{altarch}-v%{version}.tar.gz
Source1:	syncthing@.service
Source2:	%{name}-linux-386-v%{version}.tar.gz
ExclusiveArch:  x86_64 %{ix86}
BuildRequires:  systemd

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Syncthing replaces Dropbox and BitTorrent Sync with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

Using syncthing, that control is returned to you.

%prep
%setup -c

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{name}-linux-%{altarch}-v%{version}/syncthing %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{S:1} %{buildroot}%{_unitdir}


%post
%systemd_post %{name}@.service

%preun
%systemd_preun %{name}@.servie

%postun
%systemd_postun_with_restart %{name}@.service 

%files
%doc  %{name}-linux-%{altarch}-v%{version}/README.txt %{name}-linux-%{altarch}-v%{version}/LICENSE.txt %{name}-linux-%{altarch}-v%{version}/CONTRIBUTORS.txt
%{_bindir}/syncthing
%{_unitdir}/%{name}@.service


%changelog
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

