Name:           letsencrypt
Version:        0.1.1
Release:        2%{?dist}
Summary:        A free, automated certificate authority client


License:        ASL 2.0
URL:            https://letsencrypt.org/
Source0:        https://pypi.python.org/packages/source/l/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

Requires: python2-letsencrypt = %{version}-%{release}

# Required for documentation
BuildRequires: python-sphinx
BuildRequires: python-sphinx_rtd_theme
BuildRequires: python-repoze-sphinx-autointerface


#Require for testing
BuildRequires: python-nose-xcover
BuildRequires: python-pep8
BuildRequires: python-tox
BuildRequires: python-mock
BuildRequires: python-zope-interface
BuildRequires: python-zope-component
BuildRequires: python2-requests
BuildRequires: python2-dialog >= 3.3.0
BuildRequires: python-psutil
BuildRequires: python-parsedatetime
BuildRequires: python-configobj
BuildRequires: python2-configargparse
BuildRequires: python2-acme >= 0.1.0


%description
Let's Encrypt is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%package -n python2-letsencrypt
Requires:   python2-configargparse
Requires:   python2-dialog >= 3.3.0
Requires:   python-parsedatetime
Requires:   python-mock
Requires:   python-zope-interface
Requires:   python-zope-component
Requires:   python-psutil
Requires:   python-configobj
Requires:   python2-acme >= 0.1.0
Recommends: letsencrypt-doc
Summary:    Python 2 libraries used by letsencrypt
%{?python_provide:%python_provide python2-letsencrypt}

%description -n python2-letsencrypt
The python2 libraries to interface with letsencrypt

%package doc
Provides: bundled(jquery)
Provides: bundled(underscore)
Provides: bundled(inconsolata-fonts)
Provides: bundled(lato-fonts)
Provides: bundled(robotoslab-fonts)
Requires: fontawesome-fonts fontawesome-fonts-web
Summary:  Documentation for the reference letsencrypt client

%description doc
Documentation for the reference letsencrypt client and libraries

%prep
%autosetup -n %{name}-%{version}


%build
# We are using letsencrypt and not supporting letsencrypt-auto
sed -i 's/letsencrypt-auto/letsencrypt/g' letsencrypt/cli.py
%py2_build

# build documentation
%{__python2} setup.py install --user

# Clean up stuff we don't need fof docs
rm -rf docs/_build/html/{.buildinfo,_sources}

%install
%py2_install

# Unbundle fonts already on system and put the html docs in place
# Lato ttf is in texlive but that adds a lot of dependencies (30+MB) for just a font in documentation
# and lato is not in it's own -fonts package, only texlive
rm -f docs/_build/html/_static/fonts/fontawesome*


%check
%{__python2} setup.py test

%files
%license LICENSE.txt
%doc README.rst CHANGES.rst CONTRIBUTING.md
%{_bindir}/letsencrypt
%{_bindir}/letsencrypt-renewer
%ghost %dir %{_sysconfdir}/%{name}
%ghost %dir %{_sharedstatedir}/%{name}
%ghost %dir %{_var}/log/%{name}

%files -n python2-letsencrypt
%license LICENSE.txt
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}-%{version}*.egg-info

%files doc
%license LICENSE.txt

%changelog
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-2
- Fix packaging issues
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-1
- fix a confusing UI path that caused some users to repeatedly renew their
- certs while experimenting with the client, in some cases hitting issuance rate limits
- numerous Apache configuration parser fixes
- avoid attempting to issue for unqualified domain names like "localhost"
- fix --webroot permission handling for non-root users
* Tue Dec 08 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.0-3
- Add python-sphinx_rtd_theme build requirement
* Fri Dec 04 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-2
- Add documentation from upstream
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-1
- Update to new upstream release for the open beta
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-5.dev20151123
- Add missing build requirements that slipped through
* Wed Dec 02 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-4.dev20151123
- The python2 library should have the dependencies and not the bindir one
* Wed Dec 02 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-3.dev20151123
- Separate out the python libraries from the application itself
- Enable python tests
* Tue Dec 01 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-2.dev20151123
- Update spec to account for the runtime dependencies discovered
- Update spec to sit inline with current python practices
* Sun Apr 26 2015 Torrie Fischer <tdfischer@hackerbots.net> 0-1.git1d8281d.fc20
- Initial package
