%global with_devel 1
%global with_bundled 0
%global with_debug 0
# No test files so far
%global with_check 0
%global with_unit_test 0

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         gogo
%global repo            protobuf
# https://github.com/gogo/protobuf
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          c3995ae437bb78d1189f4f147dfe5f87ad3596e4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global nname           golang-github-gogo-protobuf
%global g_import_path   code.google.com/p/gogoprotobuf
%global devel_main      golang-github-gogo-protobuf-devel

Name:           golang-googlecode-gogoprotobuf
Version:        0.2
Release:        0.2.git%{shortcommit}%{?dist}
Summary:        A fork of goprotobuf with several extra features
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

Requires:       protobuf

Provides:       protoc-gen-gogo = %{version}-%{release}

%description
%{summary}

%if 0%{?with_devel}
%package -n %{nname}-devel
Summary:        %{summary}
BuildArch:      noarch

Provides:       golang(%{import_path}/codec) = %{version}-%{release}
Provides:       golang(%{import_path}/gogoproto) = %{version}-%{release}
Provides:       golang(%{import_path}/io) = %{version}-%{release}
Provides:       golang(%{import_path}/jsonpb) = %{version}-%{release}
Provides:       golang(%{import_path}/jsonpb/jsonpb_test_proto) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/defaultcheck) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/description) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/embedcheck) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/enumstringer) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/equal) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/face) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/gostring) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/grpc) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/marshalto) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/oneofcheck) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/populate) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/size) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/stringer) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/testgen) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/union) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/unmarshal) = %{version}-%{release}
Provides:       golang(%{import_path}/proto) = %{version}-%{release}
Provides:       golang(%{import_path}/proto/proto3_proto) = %{version}-%{release}
Provides:       golang(%{import_path}/proto/testdata) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-gogo) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-gogo/descriptor) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-gogo/generator) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-gogo/plugin) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-gogo/testdata/my_test) = %{version}-%{release}
Provides:       golang(%{import_path}/sortkeys) = %{version}-%{release}
Provides:       golang(%{import_path}/test) = %{version}-%{release}
Provides:       golang(%{import_path}/test/asymetric-issue125) = %{version}-%{release}
Provides:       golang(%{import_path}/test/casttype) = %{version}-%{release}
Provides:       golang(%{import_path}/test/casttype/combos/both) = %{version}-%{release}
Provides:       golang(%{import_path}/test/casttype/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/casttype/combos/neither) = %{version}-%{release}
Provides:       golang(%{import_path}/test/casttype/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/casttype/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{import_path}/test/casttype/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/casttype/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/castvalue) = %{version}-%{release}
Provides:       golang(%{import_path}/test/castvalue/combos/both) = %{version}-%{release}
Provides:       golang(%{import_path}/test/castvalue/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/castvalue/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/castvalue/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{import_path}/test/castvalue/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/castvalue/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/combos/both) = %{version}-%{release}
Provides:       golang(%{import_path}/test/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{import_path}/test/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/custom) = %{version}-%{release}
Provides:       golang(%{import_path}/test/custom-dash-type) = %{version}-%{release}
Provides:       golang(%{import_path}/test/custombytesnonstruct) = %{version}-%{release}
Provides:       golang(%{import_path}/test/dashfilename) = %{version}-%{release}
Provides:       golang(%{import_path}/test/defaultconflict) = %{version}-%{release}
Provides:       golang(%{import_path}/test/embedconflict) = %{version}-%{release}
Provides:       golang(%{import_path}/test/empty-issue70) = %{version}-%{release}
Provides:       golang(%{import_path}/test/enumcustomname) = %{version}-%{release}
Provides:       golang(%{import_path}/test/enumprefix) = %{version}-%{release}
Provides:       golang(%{import_path}/test/enumstringer) = %{version}-%{release}
Provides:       golang(%{import_path}/test/example) = %{version}-%{release}
Provides:       golang(%{import_path}/test/filedotname) = %{version}-%{release}
Provides:       golang(%{import_path}/test/fuzztests) = %{version}-%{release}
Provides:       golang(%{import_path}/test/group) = %{version}-%{release}
Provides:       golang(%{import_path}/test/importdedup) = %{version}-%{release}
Provides:       golang(%{import_path}/test/importdedup/subpkg) = %{version}-%{release}
Provides:       golang(%{import_path}/test/indeximport-issue72) = %{version}-%{release}
Provides:       golang(%{import_path}/test/indeximport-issue72/index) = %{version}-%{release}
Provides:       golang(%{import_path}/test/issue34) = %{version}-%{release}
Provides:       golang(%{import_path}/test/issue42order) = %{version}-%{release}
Provides:       golang(%{import_path}/test/issue8) = %{version}-%{release}
Provides:       golang(%{import_path}/test/mapsproto2) = %{version}-%{release}
Provides:       golang(%{import_path}/test/mapsproto2/combos/both) = %{version}-%{release}
Provides:       golang(%{import_path}/test/mapsproto2/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/mapsproto2/combos/neither) = %{version}-%{release}
Provides:       golang(%{import_path}/test/mapsproto2/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/mapsproto2/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{import_path}/test/mapsproto2/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/mapsproto2/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/moredefaults) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof/combos/both) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof/combos/neither) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof3) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof3/combos/both) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof3/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof3/combos/neither) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof3/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof3/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof3/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneof3/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/oneofembed) = %{version}-%{release}
Provides:       golang(%{import_path}/test/packed) = %{version}-%{release}
Provides:       golang(%{import_path}/test/protosize) = %{version}-%{release}
Provides:       golang(%{import_path}/test/required) = %{version}-%{release}
Provides:       golang(%{import_path}/test/sizeunderscore) = %{version}-%{release}
Provides:       golang(%{import_path}/test/tags) = %{version}-%{release}
Provides:       golang(%{import_path}/test/theproto3) = %{version}-%{release}
Provides:       golang(%{import_path}/test/theproto3/combos/both) = %{version}-%{release}
Provides:       golang(%{import_path}/test/theproto3/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/theproto3/combos/neither) = %{version}-%{release}
Provides:       golang(%{import_path}/test/theproto3/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/theproto3/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{import_path}/test/theproto3/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/theproto3/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/test/unmarshalmerge) = %{version}-%{release}
Provides:       golang(%{import_path}/test/unrecognized) = %{version}-%{release}
Provides:       golang(%{import_path}/test/unrecognizedgroup) = %{version}-%{release}
Provides:       golang(%{import_path}/vanity) = %{version}-%{release}
Provides:       golang(%{import_path}/vanity/command) = %{version}-%{release}
Provides:       golang(%{import_path}/vanity/test) = %{version}-%{release}
Provides:       golang(%{import_path}/vanity/test/fast) = %{version}-%{release}
Provides:       golang(%{import_path}/vanity/test/faster) = %{version}-%{release}
Provides:       golang(%{import_path}/vanity/test/slick) = %{version}-%{release}
Provides:       golang(%{import_path}/version) = %{version}-%{release}

%package devel
Summary:        %{summary}
BuildArch:      noarch

Provides:       golang(%{g_import_path}/codec) = %{version}-%{release}
Provides:       golang(%{g_import_path}/gogoproto) = %{version}-%{release}
Provides:       golang(%{g_import_path}/io) = %{version}-%{release}
Provides:       golang(%{g_import_path}/jsonpb) = %{version}-%{release}
Provides:       golang(%{g_import_path}/jsonpb/jsonpb_test_proto) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/defaultcheck) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/description) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/embedcheck) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/enumstringer) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/equal) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/face) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/gostring) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/grpc) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/marshalto) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/oneofcheck) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/populate) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/size) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/stringer) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/testgen) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/union) = %{version}-%{release}
Provides:       golang(%{g_import_path}/plugin/unmarshal) = %{version}-%{release}
Provides:       golang(%{g_import_path}/proto) = %{version}-%{release}
Provides:       golang(%{g_import_path}/proto/proto3_proto) = %{version}-%{release}
Provides:       golang(%{g_import_path}/proto/testdata) = %{version}-%{release}
Provides:       golang(%{g_import_path}/protoc-gen-gogo) = %{version}-%{release}
Provides:       golang(%{g_import_path}/protoc-gen-gogo/descriptor) = %{version}-%{release}
Provides:       golang(%{g_import_path}/protoc-gen-gogo/generator) = %{version}-%{release}
Provides:       golang(%{g_import_path}/protoc-gen-gogo/plugin) = %{version}-%{release}
Provides:       golang(%{g_import_path}/protoc-gen-gogo/testdata/my_test) = %{version}-%{release}
Provides:       golang(%{g_import_path}/sortkeys) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/asymetric-issue125) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/casttype) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/casttype/combos/both) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/casttype/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/casttype/combos/neither) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/casttype/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/casttype/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/casttype/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/casttype/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/castvalue) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/castvalue/combos/both) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/castvalue/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/castvalue/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/castvalue/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/castvalue/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/castvalue/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/combos/both) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/custom) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/custom-dash-type) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/custombytesnonstruct) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/dashfilename) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/defaultconflict) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/embedconflict) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/empty-issue70) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/enumcustomname) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/enumprefix) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/enumstringer) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/example) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/filedotname) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/fuzztests) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/group) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/importdedup) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/importdedup/subpkg) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/indeximport-issue72) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/indeximport-issue72/index) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/issue34) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/issue42order) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/issue8) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/mapsproto2) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/mapsproto2/combos/both) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/mapsproto2/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/mapsproto2/combos/neither) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/mapsproto2/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/mapsproto2/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/mapsproto2/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/mapsproto2/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/moredefaults) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof/combos/both) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof/combos/neither) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof3) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof3/combos/both) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof3/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof3/combos/neither) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof3/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof3/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof3/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneof3/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/oneofembed) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/packed) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/protosize) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/required) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/sizeunderscore) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/tags) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/theproto3) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/theproto3/combos/both) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/theproto3/combos/marshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/theproto3/combos/neither) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/theproto3/combos/unmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/theproto3/combos/unsafeboth) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/theproto3/combos/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/theproto3/combos/unsafeunmarshaler) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/unmarshalmerge) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/unrecognized) = %{version}-%{release}
Provides:       golang(%{g_import_path}/test/unrecognizedgroup) = %{version}-%{release}
Provides:       golang(%{g_import_path}/vanity) = %{version}-%{release}
Provides:       golang(%{g_import_path}/vanity/command) = %{version}-%{release}
Provides:       golang(%{g_import_path}/vanity/test) = %{version}-%{release}
Provides:       golang(%{g_import_path}/vanity/test/fast) = %{version}-%{release}
Provides:       golang(%{g_import_path}/vanity/test/faster) = %{version}-%{release}
Provides:       golang(%{g_import_path}/vanity/test/slick) = %{version}-%{release}
Provides:       golang(%{g_import_path}/version) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use %{project}/%{repo}.

%description -n %{nname}-devel
%{summary}

This package contains library source intended for
building other packages which use %{project}/%{repo}.
%endif

%if 0%{?with_unit_test}
%package unit-test
Summary:         Unit tests for %{name} package
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{nname}-devel = %{version}-%{release}

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build
mkdir -p src/github.com/gogo/
ln -s ../../../ src/github.com/gogo/protobuf

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{gopath}
%else
echo "Unable to build from bundled deps. No Godeps nor vendor directory"
exit 1
%endif

#%gobuild -o bin/protoc-gen-gogo %{import_path}/protoc-gen-gogo
go build -o bin/protoc-gen-gogo %{import_path}/protoc-gen-gogo

%install
#### binary ####
install -d %{buildroot}%{_bindir}
install -m 755 bin/protoc-gen-gogo %{buildroot}/%{_bindir}/protoc-gen-gogo
rm -rf proto/testdata protoc-gen-gogo/{protoc-gen-gogo,testdata} fieldpath/fieldpath-gen

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}
install -d -p %{buildroot}/%{gopath}/src/%{g_import_path}
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
echo "%%dir %%{gopath}/src/%%{g_import_path}/." >> g_devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -o -iname "*.proto" -o -iname "*.golden" \) \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    echo "%%dir %%{gopath}/src/%%{g_import_path}/$(dirname $file)" >> g_devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{g_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{g_import_path}/$file
    echo "%%{gopath}/src/%%{g_import_path}/$file" >> g_devel.file-list
done

pushd %{buildroot}/%{gopath}/src/%{g_import_path}/
# github.com/gogo/protobuf -> code.google.com/p/gogoprotobuf
sed -i 's/"github\.com\/gogo\/protobuf/"code\.google\.com\/p\/gogoprotobuf/g' \
        $(find . -name '*.go')
popd
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
sort -u -o g_devel.file-list g_devel.file-list
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

%gotest %{import_path}/codec
%gotest %{import_path}/fieldpath
%gotest %{import_path}/io
%gotest %{import_path}/jsonpb
%gotest %{import_path}/parser
#%gotest %%{import_path}/proto
#%gotest %%{import_path}/proto/testdata
%gotest %{import_path}/protoc-gen-gogo/generator
%gotest %{import_path}/test
%gotest %{import_path}/test/casttype/combos/both
%gotest %{import_path}/test/casttype/combos/marshaler
%gotest %{import_path}/test/casttype/combos/neither
%gotest %{import_path}/test/casttype/combos/unmarshaler
%gotest %{import_path}/test/casttype/combos/unsafeboth
%gotest %{import_path}/test/casttype/combos/unsafemarshaler
%gotest %{import_path}/test/casttype/combos/unsafeunmarshaler
%gotest %{import_path}/test/combos/both
%gotest %{import_path}/test/combos/marshaler
%gotest %{import_path}/test/combos/unmarshaler
%gotest %{import_path}/test/combos/unsafeboth
%gotest %{import_path}/test/combos/unsafemarshaler
%gotest %{import_path}/test/combos/unsafeunmarshaler
%gotest %{import_path}/test/custom
%gotest %{import_path}/test/custombytesnonstruct
#%gotest %%{import_path}/test/dashfilename
%gotest %{import_path}/test/defaultconflict
%gotest %{import_path}/test/embedconflict
%gotest %{import_path}/test/empty-issue70
%gotest %{import_path}/test/enumstringer
%gotest %{import_path}/test/group
%gotest %{import_path}/test/importdedup
%gotest %{import_path}/test/indeximport-issue72
%gotest %{import_path}/test/indeximport-issue72/index
%gotest %{import_path}/test/issue34
%gotest %{import_path}/test/issue42order
%gotest %{import_path}/test/issue8
%gotest %{import_path}/test/mapsproto2/combos/both
%gotest %{import_path}/test/mapsproto2/combos/marshaler
%gotest %{import_path}/test/mapsproto2/combos/neither
%gotest %{import_path}/test/mapsproto2/combos/unmarshaler
%gotest %{import_path}/test/mapsproto2/combos/unsafeboth
%gotest %{import_path}/test/mapsproto2/combos/unsafemarshaler
%gotest %{import_path}/test/mapsproto2/combos/unsafeunmarshaler
%gotest %{import_path}/test/moredefaults
%gotest %{import_path}/test/packed
%gotest %{import_path}/test/required
%gotest %{import_path}/test/sizeunderscore
%gotest %{import_path}/test/tags
%gotest %{import_path}/test/theproto3/combos/both
%gotest %{import_path}/test/theproto3/combos/marshaler
%gotest %{import_path}/test/theproto3/combos/neither
%gotest %{import_path}/test/theproto3/combos/unmarshaler
%gotest %{import_path}/test/theproto3/combos/unsafeboth
%gotest %{import_path}/test/theproto3/combos/unsafemarshaler
%gotest %{import_path}/test/theproto3/combos/unsafeunmarshaler
%gotest %{import_path}/test/unmarshalmerge
%gotest %{import_path}/test/unrecognized
%gotest %{import_path}/test/unrecognizedgroup
%gotest %{import_path}/vanity/test
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc CONTRIBUTORS README
%{_bindir}/protoc-gen-gogo

%if 0%{?with_devel}
%files -n %{nname}-devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS README
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}

%files devel -f g_devel.file-list
%license LICENSE
%doc CONTRIBUTORS README
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc CONTRIBUTORS README
%endif

%changelog
* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-0.2.gitc3995ae
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun May 15 2016 jchaloup <jchaloup@redhat.com> - 0.2-0.1.gitc3995ae
- Bump to upstream c3995ae437bb78d1189f4f147dfe5f87ad3596e4
  related: #1246215

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.gite8904f5
- https://fedoraproject.org/wiki/Changes/golang1.6

* Thu Feb 18 2016 jchaloup <jchaloup@redhat.com> - 0.1-0.3.gite8904f5
- Bump to upstream e8904f58e872a473a5b91bc9bf3377d223555263
  related: #1246215

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.2.git8edb24c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 jchaloup <jchaloup@redhat.com> - 0.1-0.1.git8edb24c
- Bump to upstream 8edb24c179ed858a38f18920d9005c2dde05ec17
  related: #1246215

* Sat Aug 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.13.git5ba1012
- Update spec file to spec-2.0
  related: #1246215

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.12.git5ba1012
- Bump to upstream 5ba1012ef3868db1b9ff374280a558c1bfff39c3
- Disable tests
  resolves: #1246215

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.gitbc946d0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 jchaloup <jchaloup@redhat.com> - 0-0.10.gitbc946d0
- Bump to upstream bc946d07d1016848dfd2507f90f0859c9471681e
  import path has changed -> add devel package to keep back compatibility
  with code.google.com/p/gogoprotobuf import paths

* Fri Sep 19 2014 jchaloup <jchaloup@redhat.com> - 0-0.9.gitd228c1a
- initial commit (package review #1120882)

* Fri Sep 19 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.8.gitd228c1a
- preserve timestamps
- don't own golang dirs
- don't redifine gopath
- ExcluseBuild for goarches

* Thu Jul 17 2014 Colin Walters <walters@verbum.org> - 0-0.7.gitd228c1a
- Initial package
