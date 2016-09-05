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
%global project         google
%global repo            google-api-go-client
# https://github.com/google/google-api-go-client
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     google.golang.org/api
%global commit          18450f4e95c7e76ce3a5dc3a8cb7178ab6d56121
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global gg_name         golang-google-golang-api

%global gc_rev             e1c259484b495133836706f46319f5897f1e9bf6
%global gc_shortrev        %(r=%{gc_rev}; echo ${r:0:12})
%global gc_provider        google
%global gc_provider_sub    code
%global gc_provider_tld    com
%global gc_repo            google-api-go-client
# code.google.com/p/google-api-go-client
%global gc_import_path     %{gc_provider_sub}.%{gc_provider}.%{gc_provider_tld}/p/%{gc_repo}
%global gc_name            golang-%{gc_provider}%{gc_provider_sub}-%{gc_repo}

%global devel_main         %{gg_name}-devel

Name:           golang-googlecode-google-api-client
Version:        0
Release:        0.15.git%{shortcommit}%{?dist}
Summary:        Go libraries for "new style" Google APIs
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/google-api-go-client-%{shortcommit}.tar.gz
Source1:        https://%{gc_repo}.%{gc_provider}%{gc_provider_sub}.%{gc_provider_tld}/archive/%{gc_rev}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
%{summary}

%if 0%{?with_devel}
%package -n %{gc_name}-devel
Summary:        Go libraries for "new style" Google APIs
BuildArch:      noarch

Provides: golang(%{gc_import_path}/adexchangebuyer/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangebuyer/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangebuyer/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangebuyer/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangeseller/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangeseller/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/admin/directory_v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/admin/email_migration_v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/admin/reports_v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsense/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsense/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsense/v1.4) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsensehost/v4.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/analytics/v2.4) = %{version}-%{release}
Provides: golang(%{gc_import_path}/analytics/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/androidpublisher/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/androidpublisher/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/androidpublisher/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/appsactivity/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/appstate/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/audit/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/autoscaler/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/bigquery/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/blogger/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/blogger/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/books/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/calendar/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/civicinfo/us_v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/civicinfo/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/cloudmonitoring/v2beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/compute/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/content/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/coordinate/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/customsearch/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/datastore/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/datastore/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/discovery/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dns/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/doubleclickbidmanager/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/doubleclicksearch/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/drive/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/drive/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/freebase/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/freebase/v1-sandbox) = %{version}-%{release}
Provides: golang(%{gc_import_path}/freebase/v1sandbox) = %{version}-%{release}
Provides: golang(%{gc_import_path}/games/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/gamesmanagement/v1management) = %{version}-%{release}
Provides: golang(%{gc_import_path}/gan/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/genomics/v1beta) = %{version}-%{release}
Provides: golang(%{gc_import_path}/gmail/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/google-api-go-generator) = %{version}-%{release}
Provides: golang(%{gc_import_path}/googleapi) = %{version}-%{release}
Provides: golang(%{gc_import_path}/googleapi/internal/uritemplates) = %{version}-%{release}
Provides: golang(%{gc_import_path}/googleapi/transport) = %{version}-%{release}
Provides: golang(%{gc_import_path}/groupsmigration/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/groupssettings/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/identitytoolkit/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/licensing/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/manager/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/mapsengine/exp2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/mapsengine/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/mirror/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/oauth2/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/oauth2/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/orkut/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/pagespeedonline/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/plus/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/plusdomains/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.4) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.5) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.6) = %{version}-%{release}
Provides: golang(%{gc_import_path}/pubsub/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/qpxexpress/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/replicapool/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/reseller/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/reseller/v1sandbox) = %{version}-%{release}
Provides: golang(%{gc_import_path}/resourceviews/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/siteverification/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/spectrum/v1explorer) = %{version}-%{release}
Provides: golang(%{gc_import_path}/sqladmin/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/sqladmin/v1beta3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/storage/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/storage/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/storage/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/taskqueue/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/taskqueue/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/tasks/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/translate/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/urlshortener/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/webfonts/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/youtube/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/youtubeanalytics/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/youtubeanalytics/v1beta1) = %{version}-%{release}

%description -n %{gc_name}-devel
%{summary}

These are auto-generated Go libraries from the Google Discovery Services JSON
description files of the available "new style" Google APIs.

Announcement email:
http://groups.google.com/group/golang-nuts/browse_thread/thread/6c7281450be9a21e

Status: Relative to the other Google API clients, this library is labeled alpha.
Some advanced features may not work. Please file bugs if any problems are found.

Getting started documentation:
    http://code.google.com/p/google-api-go-client/wiki/GettingStarted 

%package -n %{gg_name}-devel
Summary:        Go libraries for "new style" Google APIs
BuildArch:      noarch

%if 0%{?with_check}
BuildRequires:       golang(golang.org/x/net/context)
# cyclic dep, used in examples
#BuildRequires:       golang(golang.org/x/oauth2)
#BuildRequires:       golang(golang.org/x/oauth2/google)
%endif

Requires:       golang(golang.org/x/net/context)

Provides:       golang(%{import_path}/adexchangebuyer/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v2.0) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/directory_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/email_migration_v2) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/reports_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/adsensehost/v4.1) = %{version}-%{release}
Provides:       golang(%{import_path}/analytics/v2.4) = %{version}-%{release}
Provides:       golang(%{import_path}/analytics/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/androidenterprise/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/appengine/v1beta4) = %{version}-%{release}
Provides:       golang(%{import_path}/appsactivity/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/appstate/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/autoscaler/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/bigquery/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/blogger/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/blogger/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/books/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/calendar/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/civicinfo/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/classroom/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/classroom/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudlatencytest/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudmonitoring/v2beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudresourcemanager/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/clouduseraccounts/v0.alpha) = %{version}-%{release}
Provides:       golang(%{import_path}/clouduseraccounts/vm_alpha) = %{version}-%{release}
Provides:       golang(%{import_path}/compute/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/computeaccounts/v0.alpha) = %{version}-%{release}
Provides:       golang(%{import_path}/container/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/container/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/content/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/coordinate/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/customsearch/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dataflow/v1b3) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/deploymentmanager/v2beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/deploymentmanager/v2beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.0) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.1) = %{version}-%{release}
Provides:       golang(%{import_path}/discovery/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dns/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dns/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/doubleclickbidmanager/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/doubleclicksearch/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/drive/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/drive/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/fitness/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase/v1-sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase/v1sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/fusiontables/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/fusiontables/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/games/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/gamesconfiguration/v1configuration) = %{version}-%{release}
Provides:       golang(%{import_path}/gamesmanagement/v1management) = %{version}-%{release}
Provides:       golang(%{import_path}/gan/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/genomics/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/genomics/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/gmail/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/googleapi) = %{version}-%{release}
Provides:       golang(%{import_path}/googleapi/transport) = %{version}-%{release}
Provides:       golang(%{import_path}/groupsmigration/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/groupssettings/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/identitytoolkit/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/licensing/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/logging/v1beta3) = %{version}-%{release}
Provides:       golang(%{import_path}/manager/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/mapsengine/exp2) = %{version}-%{release}
Provides:       golang(%{import_path}/mapsengine/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/mirror/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth2/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth2/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/pagespeedonline/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/pagespeedonline/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/partners/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/playmoviespartner/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/plus/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/plusdomains/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.5) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.6) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub/v1beta1a) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/qpxexpress/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapool/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapool/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapoolupdater/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/reseller/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/reseller/v1sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/resourceviews/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/resourceviews/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/siteverification/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/spectrum/v1explorer) = %{version}-%{release}
Provides:       golang(%{import_path}/sqladmin/v1beta3) = %{version}-%{release}
Provides:       golang(%{import_path}/sqladmin/v1beta4) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/tagmanager/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/taskqueue/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/taskqueue/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/tasks/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/translate/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/urlshortener/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/webfonts/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/webmasters/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/youtube/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/youtubeanalytics/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/youtubeanalytics/v1beta1) = %{version}-%{release}

%description -n %{gg_name}-devel
%{summary}

These are auto-generated Go libraries from the Google Discovery Services JSON
description files of the available "new style" Google APIs.

Announcement email:
http://groups.google.com/group/golang-nuts/browse_thread/thread/6c7281450be9a21e

Status: Relative to the other Google API clients, this library is labeled alpha.
Some advanced features may not work. Please file bugs if any problems are found.

Getting started documentation:
    http://code.google.com/p/google-api-go-client/wiki/GettingStarted 
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{gg_name}-devel = %{version}-%{release}

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{gc_repo}-%{gc_shortrev} -T -b 1
%setup -q -n google-api-go-client-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{gc_import_path}/
echo "%%dir %%{gopath}/src/%%{gc_import_path}/." >> gc_devel.file-list
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
pushd ../%{gc_repo}-%{gc_shortrev}
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{gc_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{gc_import_path}/$file
    echo "%%{gopath}/src/%%{gc_import_path}/$file" >> ../google-api-go-client-%{commit}/gc_devel.file-list
done
popd
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
done
for file in $(find ./google-api-go-generator/testdata/ -iname "*"); do
    if [ "$file" == "./google-api-go-generator/testdata/" ]; then
        continue
    fi
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
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

%gotest %{import_path}/google-api-go-generator
%gotest %{import_path}/googleapi
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files -n %{gg_name}-devel -f devel.file-list
%license LICENSE
%doc AUTHORS CONTRIBUTORS NOTES README.md TODO CONTRIBUTING.md

%files -n %{gc_name}-devel -f gc_devel.file-list
%license LICENSE
%doc AUTHORS CONTRIBUTORS NOTES README.md TODO CONTRIBUTING.md
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc AUTHORS CONTRIBUTORS NOTES README.md TODO CONTRIBUTING.md
%endif

%changelog
* Tue Aug 09 2016 jchaloup <jchaloup@redhat.com> - 0-0.15.git18450f4
- Polish spec file, enable devel and unit-test for epel7
  related: #1250521

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.git18450f4
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.13.git18450f4
- Update provided packages
  related: #1250521

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.12.git18450f4
- Bump to upstream 18450f4e95c7e76ce3a5dc3a8cb7178ab6d56121
  related: #1250521

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.gitfc402b0
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitfc402b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.9.gitfc402b0
- Fix runtime dependency on devel
  related: #1250521

* Wed Aug 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.8.gitfc402b0
- Update spec file to spec-2.0
  resolves: #1250521

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitfc402b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitfc402b0
- fix provides
  related: #1141841

* Thu Mar 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitfc402b0
- add devel subpackage for code.google.com/p/... import path (for back-compatibility)
  related: #1141841

* Fri Jan 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.gitfc402b0
- update to fc402b0d6f2a46ba7dcf0a4606031f45fb82a728
  related: #1141841

* Fri Nov 14 2014 Eric Paris <eparis@redhat.com> - 0-0.3.alpha.hg98c781851970
- update to 98c78185197025f935947caac56a7b6d022f89d2

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.alpha.hge1c259484b49
- update to e1c259484b495133836706f46319f5897f1e9bf6
- preserve timestamps of copied files

* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.alpha.hg0923cdda5b82
- First package for Fedora.
