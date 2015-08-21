# Generated from fog-profitbricks-0.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-profitbricks

Name: rubygem-%{gem_name}
Version: 0.0.3
Release: 1%{?dist}
Summary: Module for the 'fog' gem to support ProfitBricks
Group: Development/Languages
License: MIT
URL: https://github.com/fog/fog-profitbricks
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: ruby-irb
# BuildRequires: rubygem(minitest)
# BuildRequires: rubygem(shindo)
# BuildRequires: rubygem(turn)
# BuildRequires: rubygem(pry)
# BuildRequires: rubygem(rubocop)
# BuildRequires: rubygem(coveralls)
BuildArch: noarch

%description
Module for the 'fog' gem to support ProfitBricks.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%{gem_instdir}/.ruby-gemset
%{gem_instdir}/.ruby-version
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/fog-profitbricks.gemspec
%{gem_instdir}/spec
%{gem_instdir}/tests

%changelog
* Fri Aug 21 2015 Vladimir Rusinov <vrusinov@google.com> - 0.0.3-1
- Initial version
