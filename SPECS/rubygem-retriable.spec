# Generated from retriable-2.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name retriable

Name: rubygem-%{gem_name}
Version: 1.4.1
Release: 2%{?dist}
Summary: Retriable is an simple DSL to retry failed code blocks with randomized exponential backoff
Group: Development/Languages
License: MIT
URL: http://github.com/kamui/retriable
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: ruby-irb
BuildArch: noarch

%description
Retriable is an simple DSL to retry failed code blocks with randomized
exponential backoff. This is especially useful when interacting external
api/services or file system calls.


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
%defattr(-,root,root,-)
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
/usr/share/gems/gems/retriable-1.4.1/test/retriable_test.rb
/usr/share/gems/specifications/retriable-1.4.1.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/retriable.gemspec

%changelog
* Fri Aug 21 2015 Vladimir Rusinov <vrusinov@google.com> - 1.4.1-2
- Initial package
