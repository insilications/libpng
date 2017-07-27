#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF54984BFA16C640F (glennrp+bmo@gmail.com)
#
Name     : libpng
Version  : 1.6.31
Release  : 46
URL      : https://sourceforge.net/projects/libpng/files/libpng16/1.6.31/libpng-1.6.31.tar.xz
Source0  : https://sourceforge.net/projects/libpng/files/libpng16/1.6.31/libpng-1.6.31.tar.xz
Source99 : https://sourceforge.net/projects/libpng/files/libpng16/1.6.31/libpng-1.6.31.tar.xz.asc
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
Requires: libpng-dev

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
%setup -q -n libpng-1.6.31
pushd ..
cp -a libpng-1.6.31 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1501162864
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong "
%configure --disable-static --enable-intel-sse
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --enable-intel-sse   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1501162864
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong -march=haswell "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong -march=haswell "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition -fstack-protector-strong -march=haswell "
make clean
%configure --disable-static--enable-intel-sse --libdir=/usr/lib64/haswell
make V=1  %{?_smp_mflags}
make DESTDIR=%{buildroot} install-libLTLIBRARIES
rm -f %{buildroot}/usr/lib64/haswell/*.la
rm -f %{buildroot}/usr/lib64/haswell/*.lo

%files
%defattr(-,root,root,-)
/usr/lib64/haswell/libpng16.a

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
/usr/lib64/haswell/libpng16.so
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
/usr/lib32/pkgconfig/libpng.pc
/usr/lib32/pkgconfig/libpng16.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libpng16.so.16
/usr/lib64/haswell/libpng16.so.16.31.0
/usr/lib64/libpng16.so.16
/usr/lib64/libpng16.so.16.31.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpng16.so.16
/usr/lib32/libpng16.so.16.31.0
