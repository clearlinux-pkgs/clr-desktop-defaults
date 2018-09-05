#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-desktop-defaults
Version  : 13
Release  : 22
URL      : https://github.com/clearlinux/clr-desktop-defaults/archive/v13.tar.gz
Source0  : https://github.com/clearlinux/clr-desktop-defaults/archive/v13.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: clr-desktop-defaults-bin
Requires: clr-desktop-defaults-config
Requires: clr-desktop-defaults-license
Requires: clr-desktop-defaults-data
BuildRequires : buildreq-meson

%description
clr-desktop-defaults
=====================
Provides default configuration and startup assistance for the desktop experience within
the `os-utils-gui` and `desktop` bundles.

%package bin
Summary: bin components for the clr-desktop-defaults package.
Group: Binaries
Requires: clr-desktop-defaults-data
Requires: clr-desktop-defaults-config
Requires: clr-desktop-defaults-license

%description bin
bin components for the clr-desktop-defaults package.


%package config
Summary: config components for the clr-desktop-defaults package.
Group: Default

%description config
config components for the clr-desktop-defaults package.


%package data
Summary: data components for the clr-desktop-defaults package.
Group: Data

%description data
data components for the clr-desktop-defaults package.


%package license
Summary: license components for the clr-desktop-defaults package.
Group: Default

%description license
license components for the clr-desktop-defaults package.


%prep
%setup -q -n clr-desktop-defaults-13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536144853
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/clr-desktop-defaults
cp LICENSE %{buildroot}/usr/share/doc/clr-desktop-defaults/LICENSE
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-desktop-files.sh
/usr/libexec/clr-init-flathub-repo

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/logind.conf.d/80-lidswitch.conf

%files data
%defattr(-,root,root,-)
/usr/share/glib-2.0/schemas/10_gnome_settings.gschema.override
/usr/share/xdg/autostart/clr-desktop-files.desktop
/usr/share/xdg/autostart/org.clearlinux.initFlathubRepo.desktop

%files license
%defattr(-,root,root,-)
/usr/share/doc/clr-desktop-defaults/LICENSE
