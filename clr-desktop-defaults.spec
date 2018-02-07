#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-desktop-defaults
Version  : 11
Release  : 19
URL      : https://github.com/clearlinux/clr-desktop-defaults/archive/v11.tar.gz
Source0  : https://github.com/clearlinux/clr-desktop-defaults/archive/v11.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: clr-desktop-defaults-bin
Requires: clr-desktop-defaults-config
Requires: clr-desktop-defaults-data

%description
clr-desktop-defaults
=====================
Provides default configuration and startup assistance for the desktop experience within
the `os-utils-gui` bundle.

%package bin
Summary: bin components for the clr-desktop-defaults package.
Group: Binaries
Requires: clr-desktop-defaults-data
Requires: clr-desktop-defaults-config

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


%prep
%setup -q -n clr-desktop-defaults-11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517938105
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517938105
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-desktop-files.sh

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/logind.conf.d/80-lidswitch.conf

%files data
%defattr(-,root,root,-)
/usr/share/glib-2.0/schemas/10_gnome_settings.gschema.override
/usr/share/lightdm/lightdm-gtk-greeter.conf.d/clr-gtk-greeter.conf
/usr/share/lightdm/lightdm.conf.d/clr-lightdm.conf
/usr/share/lightdm/users.conf
/usr/share/xdg/autostart/clr-desktop-files.desktop
