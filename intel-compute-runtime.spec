#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intel-compute-runtime
Version  : 19.32.13826
Release  : 26
URL      : https://github.com/intel/compute-runtime/archive/19.32.13826/compute-runtime-19.32.13826.tar.gz
Source0  : https://github.com/intel/compute-runtime/archive/19.32.13826/compute-runtime-19.32.13826.tar.gz
Summary  : Intel(R) Graphics Compute Runtime for OpenCL(TM). Replaces Beignet for Gen8 (Broadwell) and beyond.
Group    : Development/Tools
License  : MIT
Requires: intel-compute-runtime-bin = %{version}-%{release}
Requires: intel-compute-runtime-data = %{version}-%{release}
Requires: intel-compute-runtime-lib = %{version}-%{release}
Requires: intel-compute-runtime-license = %{version}-%{release}
Requires: intel-gmmlib-lib
Requires: intel-graphics-compiler
Requires: libdrm
Requires: libva
Requires: ocl-icd
Requires: opencl-clang-dev
BuildRequires : buildreq-cmake
BuildRequires : intel-graphics-compiler
BuildRequires : intel-graphics-compiler-dev
BuildRequires : libdrm
BuildRequires : libdrm-dev
BuildRequires : libva
BuildRequires : libva-dev
BuildRequires : ocl-icd
BuildRequires : opencl-clang-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(igc-opencl)
BuildRequires : pkgconfig(igdgmm)
BuildRequires : pkgconfig(libva)
Patch1: 0001-remove-Werror-from-forced-flags.patch

%description
Common clang is a thin wrapper library around clang. Common clang has OpenCL-oriented API and is capable to compile OpenCL C kernels to SPIR-V modules.

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


%package lib
Summary: lib components for the intel-compute-runtime package.
Group: Libraries
Requires: intel-compute-runtime-data = %{version}-%{release}
Requires: intel-compute-runtime-license = %{version}-%{release}

%description lib
lib components for the intel-compute-runtime package.


%package license
Summary: license components for the intel-compute-runtime package.
Group: Default

%description license
license components for the intel-compute-runtime package.


%prep
%setup -q -n compute-runtime-19.32.13826
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565892486
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DBUILD_TYPE=Release \
-DSKIP_UNIT_TESTS=1
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1565892486
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-compute-runtime
cp LICENSE %{buildroot}/usr/share/package-licenses/intel-compute-runtime/LICENSE
cp third_party/opencl_headers/LICENSE %{buildroot}/usr/share/package-licenses/intel-compute-runtime/third_party_opencl_headers_LICENSE
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/share/defaults/etc/ld.so.conf.d/libintelopencl.conf
## install_append content
mkdir -p %{buildroot}/usr/share/OpenCL/vendors
mv %{buildroot}/usr/share/defaults/etc/OpenCL/vendors/intel.icd %{buildroot}/usr/share/OpenCL/vendors
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ocloc

%files data
%defattr(-,root,root,-)
/usr/share/OpenCL/vendors/intel.icd

%files lib
%defattr(-,root,root,-)
/usr/lib64/intel-opencl/libigdrcl.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intel-compute-runtime/LICENSE
/usr/share/package-licenses/intel-compute-runtime/third_party_opencl_headers_LICENSE
