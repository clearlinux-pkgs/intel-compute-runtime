#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intel-compute-runtime
Version  : 19.09.12487
Release  : 4
URL      : https://github.com/intel/compute-runtime/archive/19.09.12487.tar.gz
Source0  : https://github.com/intel/compute-runtime/archive/19.09.12487.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: intel-compute-runtime-bin = %{version}-%{release}
Requires: intel-compute-runtime-data = %{version}-%{release}
Requires: intel-compute-runtime-license = %{version}-%{release}
Requires: intel-graphics-compiler
Requires: libdrm
Requires: libva
Requires: ocl-icd
BuildRequires : buildreq-cmake
BuildRequires : gdb
BuildRequires : intel-graphics-compiler
BuildRequires : intel-graphics-compiler-dev
BuildRequires : libdrm-dev
BuildRequires : libva-dev
BuildRequires : nano
BuildRequires : opencl-clang-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(igc-opencl)
BuildRequires : pkgconfig(igdgmm)
BuildRequires : pkgconfig(libva)
BuildRequires : strace

%description
# Intel(R) Graphics Compute Runtime for OpenCL(TM)
## Introduction
The Intel(R) Graphics Compute Runtime for OpenCL(TM) is a open source project to
converge Intel's development efforts on OpenCL(TM) compute stacks supporting the
GEN graphics hardware architecture.

%package bin
Summary: bin components for the intel-compute-runtime package.
Group: Binaries
Requires: intel-compute-runtime-data = %{version}-%{release}
Requires: intel-compute-runtime-license = %{version}-%{release}

%description bin
bin components for the intel-compute-runtime package.


%package data
Summary: data components for the intel-compute-runtime package.
Group: Data

%description data
data components for the intel-compute-runtime package.


%package dev
Summary: dev components for the intel-compute-runtime package.
Group: Development
Requires: intel-compute-runtime-bin = %{version}-%{release}
Requires: intel-compute-runtime-data = %{version}-%{release}
Provides: intel-compute-runtime-devel = %{version}-%{release}

%description dev
dev components for the intel-compute-runtime package.


%package license
Summary: license components for the intel-compute-runtime package.
Group: Default

%description license
license components for the intel-compute-runtime package.


%prep
%setup -q -n compute-runtime-19.09.12487

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553194775
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake .. -DBUILD_TYPE=Release \
-DSKIP_UNIT_TESTS=1
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1553194775
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-compute-runtime
cp LICENSE %{buildroot}/usr/share/package-licenses/intel-compute-runtime/LICENSE
cp third_party/opencl_headers/LICENSE %{buildroot}/usr/share/package-licenses/intel-compute-runtime/third_party_opencl_headers_LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ocloc

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/OpenCL/vendors/intel.icd
/usr/share/defaults/etc/ld.so.conf.d/libintelopencl.conf

%files dev
%defattr(-,root,root,-)
/usr/lib64/libigdrcl.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intel-compute-runtime/LICENSE
/usr/share/package-licenses/intel-compute-runtime/third_party_opencl_headers_LICENSE
