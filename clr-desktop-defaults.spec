#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-desktop-defaults
Version  : 21
Release  : 44
URL      : https://github.com/clearlinux/clr-desktop-defaults/archive/v21.tar.gz
Source0  : https://github.com/clearlinux/clr-desktop-defaults/archive/v21.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: clr-desktop-defaults-bin = %{version}-%{release}
Requires: clr-desktop-defaults-data = %{version}-%{release}
Requires: clr-desktop-defaults-libexec = %{version}-%{release}
Requires: clr-desktop-defaults-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : dconf-dev

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
%setup -q -n clr-desktop-defaults-21
cd %{_builddir}/clr-desktop-defaults-21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581452633
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/clr-desktop-defaults
cp %{_builddir}/clr-desktop-defaults-21/LICENSE %{buildroot}/usr/share/package-licenses/clr-desktop-defaults/f428a480500ff40c02bfb5959c374d46538e2895
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/lib/systemd/logind.conf.d/80-lidswitch.conf

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-desktop-files.sh

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-mimeapps.list
/usr/share/dconf/profile/user
/usr/share/defaults/clearlinux/dconf/clearlinux-defaults
/usr/share/defaults/fonts/conf.d/70-disable-x11-75-100-dpi.conf
/usr/share/glib-2.0/schemas/10_gnome_settings.gschema.override
/usr/share/glib-2.0/schemas/20_gnome_settings.gschema.override
/usr/share/xdg/autostart/clr-desktop-files.desktop
/usr/share/xdg/autostart/clr-migrate-settings.desktop
/usr/share/xdg/autostart/org.clearlinux.initFlathubRepo.desktop

%files libexec
%defattr(-,root,root,-)
/usr/libexec/clr-init-flathub-repo
/usr/libexec/clr-migrate-settings

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-desktop-defaults/f428a480500ff40c02bfb5959c374d46538e2895
