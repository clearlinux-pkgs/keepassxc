#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xB7A66F03B59076A8 (release@keepassxc.org)
#
Name     : keepassxc
Version  : 2.7.6
Release  : 38
URL      : https://github.com/keepassxreboot/keepassxc/releases/download/2.7.6/keepassxc-2.7.6-src.tar.xz
Source0  : https://github.com/keepassxreboot/keepassxc/releases/download/2.7.6/keepassxc-2.7.6-src.tar.xz
Source1  : https://github.com/keepassxreboot/keepassxc/releases/download/2.7.6/keepassxc-2.7.6-src.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT OFL-1.1
Requires: keepassxc-bin = %{version}-%{release}
Requires: keepassxc-data = %{version}-%{release}
Requires: keepassxc-lib = %{version}-%{release}
Requires: keepassxc-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cmake
BuildRequires : glibc-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(botan-2)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libargon2)
BuildRequires : pkgconfig(libpcsclite)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(readline)
BuildRequires : qrencode-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtx11extras-dev
BuildRequires : quazip-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# <img src="https://keepassxc.org/images/keepassxc-logo.svg" width="40" height="40"/> KeePassXC
[![TeamCity Build Status](https://ci.keepassxc.org/app/rest/builds/buildType:\(project:KeepassXC\)/statusIcon)](https://ci.keepassxc.org/?guest=1)
[![codecov](https://codecov.io/gh/keepassxreboot/keepassxc/branch/develop/graph/badge.svg)](https://codecov.io/gh/keepassxreboot/keepassxc)
[![GitHub release](https://img.shields.io/github/release/keepassxreboot/keepassxc)](https://github.com/keepassxreboot/keepassxc/releases/)

%package bin
Summary: bin components for the keepassxc package.
Group: Binaries
Requires: keepassxc-data = %{version}-%{release}
Requires: keepassxc-license = %{version}-%{release}

%description bin
bin components for the keepassxc package.


%package data
Summary: data components for the keepassxc package.
Group: Data

%description data
data components for the keepassxc package.


%package lib
Summary: lib components for the keepassxc package.
Group: Libraries
Requires: keepassxc-data = %{version}-%{release}
Requires: keepassxc-license = %{version}-%{release}

%description lib
lib components for the keepassxc package.


%package license
Summary: license components for the keepassxc package.
Group: Default

%description license
license components for the keepassxc package.


%prep
%setup -q -n keepassxc-2.7.6
cd %{_builddir}/keepassxc-2.7.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692197679
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake .. -DWITH_ASAN=OFF \
-DWITH_XC_BROWSER=ON \
-DWITH_XC_DOCS=OFF \
-DWITH_XC_FDOSECRETS=ON \
-DWITH_XC_KEESHARE=ON \
-DWITH_XC_NETWORKING=ON \
-DWITH_XC_SSHAGENT=ON \
-DWITH_XC_UPDATECHECK=OFF \
-DWITH_XC_YUBIKEY=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DWITH_ASAN=OFF \
-DWITH_XC_BROWSER=ON \
-DWITH_XC_DOCS=OFF \
-DWITH_XC_FDOSECRETS=ON \
-DWITH_XC_KEESHARE=ON \
-DWITH_XC_NETWORKING=ON \
-DWITH_XC_SSHAGENT=ON \
-DWITH_XC_UPDATECHECK=OFF \
-DWITH_XC_YUBIKEY=ON
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
LD_LIBRARY_PATH=/usr/lib64 ctest .

%install
export SOURCE_DATE_EPOCH=1692197679
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keepassxc
cp %{_builddir}/keepassxc-%{version}/LICENSE.BSD %{buildroot}/usr/share/package-licenses/keepassxc/b550c747927caf17f4a96cb188467315e5f0ca8a || :
cp %{_builddir}/keepassxc-%{version}/LICENSE.CC0 %{buildroot}/usr/share/package-licenses/keepassxc/a6d187f326922e8d9bcc1ce585e92fa8d1700c4e || :
cp %{_builddir}/keepassxc-%{version}/LICENSE.GPL-2 %{buildroot}/usr/share/package-licenses/keepassxc/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/keepassxc-%{version}/LICENSE.GPL-3 %{buildroot}/usr/share/package-licenses/keepassxc/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/keepassxc-%{version}/LICENSE.LGPL-2.1 %{buildroot}/usr/share/package-licenses/keepassxc/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/keepassxc-%{version}/LICENSE.LGPL-3 %{buildroot}/usr/share/package-licenses/keepassxc/a8a12e6867d7ee39c21d9b11a984066099b6fb6b || :
cp %{_builddir}/keepassxc-%{version}/LICENSE.MIT %{buildroot}/usr/share/package-licenses/keepassxc/6f86c7f33294f02ab56862165f378421999f1840 || :
cp %{_builddir}/keepassxc-%{version}/LICENSE.NOKIA-LGPL-EXCEPTION %{buildroot}/usr/share/package-licenses/keepassxc/17848d7714522f96d68e99d87509c582e2244c50 || :
cp %{_builddir}/keepassxc-%{version}/LICENSE.OFL %{buildroot}/usr/share/package-licenses/keepassxc/931598fba0b3756401d967c3a7bab7ceaeb259ca || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/keepassxc
/V3/usr/bin/keepassxc-cli
/V3/usr/bin/keepassxc-proxy
/usr/bin/keepassxc
/usr/bin/keepassxc-cli
/usr/bin/keepassxc-proxy

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.keepassxc.KeePassXC.desktop
/usr/share/icons/hicolor/256x256/apps/keepassxc.png
/usr/share/icons/hicolor/scalable/apps/keepassxc-locked.svg
/usr/share/icons/hicolor/scalable/apps/keepassxc-monochrome-dark-locked.svg
/usr/share/icons/hicolor/scalable/apps/keepassxc-monochrome-dark.svg
/usr/share/icons/hicolor/scalable/apps/keepassxc-monochrome-light-locked.svg
/usr/share/icons/hicolor/scalable/apps/keepassxc-monochrome-light.svg
/usr/share/icons/hicolor/scalable/apps/keepassxc-unlocked.svg
/usr/share/icons/hicolor/scalable/apps/keepassxc.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-x-keepassxc.svg
/usr/share/keepassxc/icons/application/256x256/apps/keepassxc.png
/usr/share/keepassxc/translations/keepassxc_ar.qm
/usr/share/keepassxc/translations/keepassxc_bg.qm
/usr/share/keepassxc/translations/keepassxc_ca.qm
/usr/share/keepassxc/translations/keepassxc_cs.qm
/usr/share/keepassxc/translations/keepassxc_da.qm
/usr/share/keepassxc/translations/keepassxc_de.qm
/usr/share/keepassxc/translations/keepassxc_el.qm
/usr/share/keepassxc/translations/keepassxc_en.qm
/usr/share/keepassxc/translations/keepassxc_en_GB.qm
/usr/share/keepassxc/translations/keepassxc_en_US.qm
/usr/share/keepassxc/translations/keepassxc_es.qm
/usr/share/keepassxc/translations/keepassxc_et.qm
/usr/share/keepassxc/translations/keepassxc_fi.qm
/usr/share/keepassxc/translations/keepassxc_fil.qm
/usr/share/keepassxc/translations/keepassxc_fr.qm
/usr/share/keepassxc/translations/keepassxc_fr_CA.qm
/usr/share/keepassxc/translations/keepassxc_he.qm
/usr/share/keepassxc/translations/keepassxc_hr.qm
/usr/share/keepassxc/translations/keepassxc_hu.qm
/usr/share/keepassxc/translations/keepassxc_id.qm
/usr/share/keepassxc/translations/keepassxc_it.qm
/usr/share/keepassxc/translations/keepassxc_ja.qm
/usr/share/keepassxc/translations/keepassxc_km.qm
/usr/share/keepassxc/translations/keepassxc_ko.qm
/usr/share/keepassxc/translations/keepassxc_lt.qm
/usr/share/keepassxc/translations/keepassxc_my.qm
/usr/share/keepassxc/translations/keepassxc_nb.qm
/usr/share/keepassxc/translations/keepassxc_nl.qm
/usr/share/keepassxc/translations/keepassxc_pl.qm
/usr/share/keepassxc/translations/keepassxc_pt_BR.qm
/usr/share/keepassxc/translations/keepassxc_pt_PT.qm
/usr/share/keepassxc/translations/keepassxc_ro.qm
/usr/share/keepassxc/translations/keepassxc_ru.qm
/usr/share/keepassxc/translations/keepassxc_si.qm
/usr/share/keepassxc/translations/keepassxc_sk.qm
/usr/share/keepassxc/translations/keepassxc_sl.qm
/usr/share/keepassxc/translations/keepassxc_sq.qm
/usr/share/keepassxc/translations/keepassxc_sr.qm
/usr/share/keepassxc/translations/keepassxc_sv.qm
/usr/share/keepassxc/translations/keepassxc_th.qm
/usr/share/keepassxc/translations/keepassxc_tr.qm
/usr/share/keepassxc/translations/keepassxc_uk.qm
/usr/share/keepassxc/translations/keepassxc_zh_CN.qm
/usr/share/keepassxc/translations/keepassxc_zh_TW.qm
/usr/share/keepassxc/wordlists/eff_large.wordlist
/usr/share/metainfo/org.keepassxc.KeePassXC.appdata.xml
/usr/share/mime-packages/keepassxc.xml

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/keepassxc/libkeepassxc-autotype-xcb.so
/usr/lib64/keepassxc/libkeepassxc-autotype-xcb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/keepassxc/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/keepassxc/17848d7714522f96d68e99d87509c582e2244c50
/usr/share/package-licenses/keepassxc/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/keepassxc/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/keepassxc/6f86c7f33294f02ab56862165f378421999f1840
/usr/share/package-licenses/keepassxc/931598fba0b3756401d967c3a7bab7ceaeb259ca
/usr/share/package-licenses/keepassxc/a6d187f326922e8d9bcc1ce585e92fa8d1700c4e
/usr/share/package-licenses/keepassxc/a8a12e6867d7ee39c21d9b11a984066099b6fb6b
/usr/share/package-licenses/keepassxc/b550c747927caf17f4a96cb188467315e5f0ca8a
