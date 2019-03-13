#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBFF2F5A2CA201B84 (ikey.doherty@intel.com)
#
Name     : clr-desktop-defaults
Version  : 18
Release  : 35
URL      : https://github.com/clearlinux/clr-desktop-defaults/releases/download/v18/clr-desktop-defaults-18.tar.xz
Source0  : https://github.com/clearlinux/clr-desktop-defaults/releases/download/v18/clr-desktop-defaults-18.tar.xz
Source99 : https://github.com/clearlinux/clr-desktop-defaults/releases/download/v18/clr-desktop-defaults-18.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: clr-desktop-defaults-bin = %{version}-%{release}
Requires: clr-desktop-defaults-data = %{version}-%{release}
Requires: clr-desktop-defaults-libexec = %{version}-%{release}
Requires: clr-desktop-defaults-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : dconf-dev
Patch1: 0001-schemas-Allow-GNOME-sound-to-be-pushed-beyond-100-vo.patch
Patch2: 0002-Add-keyboard-shortcut-for-launching-terminal.patch
Patch3: 0003-fontconfig-ban-75-100-dpi-fonts.patch
Patch4: 0004-schemas-dash-to-dock-set-dash-max-icon-size-to-42.patch

%description
clr-desktop-defaults
=====================
Provides default configuration and startup assistance for the desktop experience within
the `os-utils-gui` and `desktop` bundles.

%package bin
Summary: bin components for the clr-desktop-defaults package.
Group: Binaries
Requires: clr-desktop-defaults-data = %{version}-%{release}
Requires: clr-desktop-defaults-libexec = %{version}-%{release}
Requires: clr-desktop-defaults-license = %{version}-%{release}

%description bin
bin components for the clr-desktop-defaults package.


%package data
Summary: data components for the clr-desktop-defaults package.
Group: Data

%description data
data components for the clr-desktop-defaults package.


%package libexec
Summary: libexec components for the clr-desktop-defaults package.
Group: Default
Requires: clr-desktop-defaults-license = %{version}-%{release}

%description libexec
libexec components for the clr-desktop-defaults package.


%package license
Summary: license components for the clr-desktop-defaults package.
Group: Default

%description license
license components for the clr-desktop-defaults package.


%prep
%setup -q -n clr-desktop-defaults-18
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552435279
export LDFLAGS="${LDFLAGS} -fno-lto"
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/clr-desktop-defaults
cp LICENSE %{buildroot}/usr/share/package-licenses/clr-desktop-defaults/LICENSE
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/lib/systemd/logind.conf.d/80-lidswitch.conf

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-desktop-files.sh

%files data
%defattr(-,root,root,-)
/usr/share/dconf/profile/user
/usr/share/defaults/clearlinux/dconf/clearlinux-defaults
/usr/share/defaults/fonts/conf.d/70-disable-x11-75-100-dpi.conf
/usr/share/glib-2.0/schemas/10_gnome_settings.gschema.override
/usr/share/xdg/autostart/clr-desktop-files.desktop
/usr/share/xdg/autostart/clr-migrate-settings.desktop
/usr/share/xdg/autostart/org.clearlinux.initFlathubRepo.desktop

%files libexec
%defattr(-,root,root,-)
/usr/libexec/clr-init-flathub-repo
/usr/libexec/clr-migrate-settings

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-desktop-defaults/LICENSE
