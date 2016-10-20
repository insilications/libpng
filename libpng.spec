#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpng
Version  : 1.6.26
Release  : 29
URL      : http://downloads.sourceforge.net/libpng/libpng-1.6.26.tar.xz
Source0  : http://downloads.sourceforge.net/libpng/libpng-1.6.26.tar.xz
Summary  : Loads and saves PNG files
Group    : Development/Tools
License  : GPL-2.0 zlib-acknowledgement
Requires: libpng-bin
Requires: libpng-lib
Requires: libpng-doc
BuildRequires : gdb

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


%prep
%setup -q -n libpng-1.6.26

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition -mavx2 "
make clean
%configure --disable-static --libdir=/usr/lib64/avx2
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
/usr/lib64/*.so
/usr/lib64/avx2/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/avx2/*.so.*
