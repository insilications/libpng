#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpng
Version  : 1.6.26
Release  : 34
URL      : http://downloads.sourceforge.net/libpng/libpng-1.6.26.tar.xz
Source0  : http://downloads.sourceforge.net/libpng/libpng-1.6.26.tar.xz
Summary  : Loads and saves PNG files
Group    : Development/Tools
License  : GPL-2.0 Libpng zlib-acknowledgement
Requires: libpng-bin
Requires: libpng-lib
Requires: libpng-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gdb
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : zlib-dev32

%description
See the note about version numbers near the top of png.h
See INSTALL for instructions on how to install libpng.

%package bin
Summary: bin components for the libpng package.
Group: Binaries

%description bin
bin components for the libpng package.


%package dev
Summary: dev components for the libpng package.
Group: Development
Requires: libpng-lib
Requires: libpng-bin
Provides: libpng-devel

%description dev
dev components for the libpng package.


%package dev32
Summary: dev32 components for the libpng package.
Group: Default
Requires: libpng-lib32
Requires: libpng-bin

%description dev32
dev32 components for the libpng package.


%package doc
Summary: doc components for the libpng package.
Group: Documentation

%description doc
doc components for the libpng package.


%package lib
Summary: lib components for the libpng package.
Group: Libraries

%description lib
lib components for the libpng package.


%package lib32
Summary: lib32 components for the libpng package.
Group: Default

%description lib32
lib32 components for the libpng package.


%prep
%setup -q -n libpng-1.6.26
pushd ..
cp -a libpng-1.6.26 build32
popd

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
make clean
%configure --disable-static  --libdir=/usr/lib64/avx2
make V=1  %{?_smp_mflags}
make DESTDIR=%{buildroot} install-libLTLIBRARIES
rm -f %{buildroot}/usr/lib64/avx2/*.la
rm -f %{buildroot}/usr/lib64/avx2/*.lo

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libpng-config
/usr/bin/libpng16-config
/usr/bin/png-fix-itxt
/usr/bin/pngfix

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/libpng16/png.h
/usr/include/libpng16/pngconf.h
/usr/include/libpng16/pnglibconf.h
/usr/lib64/avx2/libpng16.so
/usr/lib64/libpng.so
/usr/lib64/libpng16.so
/usr/lib64/pkgconfig/libpng.pc
/usr/lib64/pkgconfig/libpng16.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpng.so
/usr/lib32/libpng16.so
/usr/lib32/pkgconfig/32libpng.pc
/usr/lib32/pkgconfig/32libpng16.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/avx2/libpng16.so.16
/usr/lib64/avx2/libpng16.so.16.26.0
/usr/lib64/libpng16.so.16
/usr/lib64/libpng16.so.16.26.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpng16.so.16
/usr/lib32/libpng16.so.16.26.0
