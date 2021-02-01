#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB7A66F03B59076A8 (release@keepassxc.org)
#
Name     : keepassxc
Version  : 2.6.4
Release  : 24
URL      : https://github.com/keepassxreboot/keepassxc/releases/download/2.6.4/keepassxc-2.6.4-src.tar.xz
Source0  : https://github.com/keepassxreboot/keepassxc/releases/download/2.6.4/keepassxc-2.6.4-src.tar.xz
Source1  : https://github.com/keepassxreboot/keepassxc/releases/download/2.6.4/keepassxc-2.6.4-src.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT OFL-1.1
Requires: keepassxc-bin = %{version}-%{release}
Requires: keepassxc-data = %{version}-%{release}
Requires: keepassxc-lib = %{version}-%{release}
Requires: keepassxc-license = %{version}-%{release}
BuildRequires : argon2-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-golang
BuildRequires : buildreq-kde
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libsodium)
BuildRequires : qrencode-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtx11extras-dev
BuildRequires : quazip-dev
BuildRequires : zlib-dev

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
%setup -q -n keepassxc-2.6.4
cd %{_builddir}/keepassxc-2.6.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612201920
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DWITH_XC_BROWSER=ON \
-DWITH_XC_NETWORKING=ON \
-DWITH_XC_SSHAGENT=ON \
-DWITH_XC_KEESHARE=ON \
-DWITH_XC_KEESHARE_SECURE=ON \
-DWITH_XC_UPDATECHECK=OFF \
-DWITH_XC_DOCS=OFF
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
LD_LIBRARY_PATH=/usr/lib64 ctest .

%install
export SOURCE_DATE_EPOCH=1612201920
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keepassxc
cp %{_builddir}/keepassxc-2.6.4/LICENSE.BSD %{buildroot}/usr/share/package-licenses/keepassxc/b550c747927caf17f4a96cb188467315e5f0ca8a
cp %{_builddir}/keepassxc-2.6.4/LICENSE.CC0 %{buildroot}/usr/share/package-licenses/keepassxc/a6d187f326922e8d9bcc1ce585e92fa8d1700c4e
cp %{_builddir}/keepassxc-2.6.4/LICENSE.GPL-2 %{buildroot}/usr/share/package-licenses/keepassxc/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/keepassxc-2.6.4/LICENSE.GPL-3 %{buildroot}/usr/share/package-licenses/keepassxc/842745cb706f8f2126506f544492f7a80dbe29b3
cp %{_builddir}/keepassxc-2.6.4/LICENSE.LGPL-2.1 %{buildroot}/usr/share/package-licenses/keepassxc/3704f4680301a60004b20f94e0b5b8c7ff1484a9
cp %{_builddir}/keepassxc-2.6.4/LICENSE.LGPL-3 %{buildroot}/usr/share/package-licenses/keepassxc/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/keepassxc-2.6.4/LICENSE.MIT %{buildroot}/usr/share/package-licenses/keepassxc/6f86c7f33294f02ab56862165f378421999f1840
cp %{_builddir}/keepassxc-2.6.4/LICENSE.NOKIA-LGPL-EXCEPTION %{buildroot}/usr/share/package-licenses/keepassxc/17848d7714522f96d68e99d87509c582e2244c50
cp %{_builddir}/keepassxc-2.6.4/LICENSE.OFL %{buildroot}/usr/share/package-licenses/keepassxc/931598fba0b3756401d967c3a7bab7ceaeb259ca
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/keepassxc/translations/keepassx_ar.qm
/usr/share/keepassxc/translations/keepassx_bg.qm
/usr/share/keepassxc/translations/keepassx_ca.qm
/usr/share/keepassxc/translations/keepassx_cs.qm
/usr/share/keepassxc/translations/keepassx_da.qm
/usr/share/keepassxc/translations/keepassx_de.qm
/usr/share/keepassxc/translations/keepassx_en.qm
/usr/share/keepassxc/translations/keepassx_en_GB.qm
/usr/share/keepassxc/translations/keepassx_en_US.qm
/usr/share/keepassxc/translations/keepassx_es.qm
/usr/share/keepassxc/translations/keepassx_et.qm
/usr/share/keepassxc/translations/keepassx_fi.qm
/usr/share/keepassxc/translations/keepassx_fr.qm
/usr/share/keepassxc/translations/keepassx_hr_HR.qm
/usr/share/keepassxc/translations/keepassx_hu.qm
/usr/share/keepassxc/translations/keepassx_id.qm
/usr/share/keepassxc/translations/keepassx_it.qm
/usr/share/keepassxc/translations/keepassx_ja.qm
/usr/share/keepassxc/translations/keepassx_ko.qm
/usr/share/keepassxc/translations/keepassx_lt.qm
/usr/share/keepassxc/translations/keepassx_nb.qm
/usr/share/keepassxc/translations/keepassx_nl_NL.qm
/usr/share/keepassxc/translations/keepassx_pl.qm
/usr/share/keepassxc/translations/keepassx_pt_BR.qm
/usr/share/keepassxc/translations/keepassx_pt_PT.qm
/usr/share/keepassxc/translations/keepassx_ro.qm
/usr/share/keepassxc/translations/keepassx_ru.qm
/usr/share/keepassxc/translations/keepassx_sk.qm
/usr/share/keepassxc/translations/keepassx_sl_SI.qm
/usr/share/keepassxc/translations/keepassx_sv.qm
/usr/share/keepassxc/translations/keepassx_th.qm
/usr/share/keepassxc/translations/keepassx_tr.qm
/usr/share/keepassxc/translations/keepassx_uk.qm
/usr/share/keepassxc/translations/keepassx_zh_CN.qm
/usr/share/keepassxc/translations/keepassx_zh_TW.qm
/usr/share/keepassxc/wordlists/eff_large.wordlist
/usr/share/metainfo/org.keepassxc.KeePassXC.appdata.xml
/usr/share/mime-packages/keepassxc.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/keepassxc/libkeepassx-autotype-xcb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/keepassxc/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/keepassxc/17848d7714522f96d68e99d87509c582e2244c50
/usr/share/package-licenses/keepassxc/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/keepassxc/6f86c7f33294f02ab56862165f378421999f1840
/usr/share/package-licenses/keepassxc/842745cb706f8f2126506f544492f7a80dbe29b3
/usr/share/package-licenses/keepassxc/931598fba0b3756401d967c3a7bab7ceaeb259ca
/usr/share/package-licenses/keepassxc/a6d187f326922e8d9bcc1ce585e92fa8d1700c4e
/usr/share/package-licenses/keepassxc/b550c747927caf17f4a96cb188467315e5f0ca8a
/usr/share/package-licenses/keepassxc/f45ee1c765646813b442ca58de72e20a64a7ddba
