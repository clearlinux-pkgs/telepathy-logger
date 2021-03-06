#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x432705FACDD40325 (rishi.is@lostca.se)
#
Name     : telepathy-logger
Version  : 0.8.2
Release  : 8
URL      : http://telepathy.freedesktop.org/releases/telepathy-logger/telepathy-logger-0.8.2.tar.bz2
Source0  : http://telepathy.freedesktop.org/releases/telepathy-logger/telepathy-logger-0.8.2.tar.bz2
Source99 : http://telepathy.freedesktop.org/releases/telepathy-logger/telepathy-logger-0.8.2.tar.bz2.asc
Summary  : Telepathy framework logging daemon
Group    : Development/Tools
License  : LGPL-2.1
Requires: telepathy-logger-data = %{version}-%{release}
Requires: telepathy-logger-lib = %{version}-%{release}
Requires: telepathy-logger-libexec = %{version}-%{release}
Requires: telepathy-logger-license = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : glib-bin
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(telepathy-glib)
BuildRequires : pkgconfig(x11)
BuildRequires : python

%description
Telepathy-Logger
================
tp-logger is a headless Observer client that logs information received by the
Telepathy framework. It features pluggable backends to log different sorts of
messages, in different formats.

%package data
Summary: data components for the telepathy-logger package.
Group: Data

%description data
data components for the telepathy-logger package.


%package dev
Summary: dev components for the telepathy-logger package.
Group: Development
Requires: telepathy-logger-lib = %{version}-%{release}
Requires: telepathy-logger-data = %{version}-%{release}
Provides: telepathy-logger-devel = %{version}-%{release}
Requires: telepathy-logger = %{version}-%{release}

%description dev
dev components for the telepathy-logger package.


%package doc
Summary: doc components for the telepathy-logger package.
Group: Documentation

%description doc
doc components for the telepathy-logger package.


%package lib
Summary: lib components for the telepathy-logger package.
Group: Libraries
Requires: telepathy-logger-data = %{version}-%{release}
Requires: telepathy-logger-libexec = %{version}-%{release}
Requires: telepathy-logger-license = %{version}-%{release}

%description lib
lib components for the telepathy-logger package.


%package libexec
Summary: libexec components for the telepathy-logger package.
Group: Default
Requires: telepathy-logger-license = %{version}-%{release}

%description libexec
libexec components for the telepathy-logger package.


%package license
Summary: license components for the telepathy-logger package.
Group: Default

%description license
license components for the telepathy-logger package.


%prep
%setup -q -n telepathy-logger-0.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557100301
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static PYTHON=/usr/bin/python2
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1557100301
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/telepathy-logger
cp COPYING %{buildroot}/usr/share/package-licenses/telepathy-logger/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/TelepathyLogger-0.2.typelib
/usr/share/dbus-1/services/org.freedesktop.Telepathy.Client.Logger.service
/usr/share/dbus-1/services/org.freedesktop.Telepathy.Logger.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.freedesktop.Telepathy.Logger.gschema.xml
/usr/share/telepathy/clients/Logger.client

%files dev
%defattr(-,root,root,-)
/usr/include/telepathy-logger-0.2/telepathy-logger/call-event.h
/usr/include/telepathy-logger-0.2/telepathy-logger/entity.h
/usr/include/telepathy-logger-0.2/telepathy-logger/event.h
/usr/include/telepathy-logger-0.2/telepathy-logger/log-manager.h
/usr/include/telepathy-logger-0.2/telepathy-logger/log-walker.h
/usr/include/telepathy-logger-0.2/telepathy-logger/telepathy-logger.h
/usr/include/telepathy-logger-0.2/telepathy-logger/text-event.h
/usr/lib64/libtelepathy-logger.so
/usr/lib64/pkgconfig/telepathy-logger-0.2.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/telepathy-logger/TplCallEvent.html
/usr/share/gtk-doc/html/telepathy-logger/TplEntity.html
/usr/share/gtk-doc/html/telepathy-logger/TplEvent.html
/usr/share/gtk-doc/html/telepathy-logger/TplLogManager.html
/usr/share/gtk-doc/html/telepathy-logger/TplLogWalker.html
/usr/share/gtk-doc/html/telepathy-logger/TplTextEvent.html
/usr/share/gtk-doc/html/telepathy-logger/ch-public.html
/usr/share/gtk-doc/html/telepathy-logger/home.png
/usr/share/gtk-doc/html/telepathy-logger/index.html
/usr/share/gtk-doc/html/telepathy-logger/index.sgml
/usr/share/gtk-doc/html/telepathy-logger/left-insensitive.png
/usr/share/gtk-doc/html/telepathy-logger/left.png
/usr/share/gtk-doc/html/telepathy-logger/right-insensitive.png
/usr/share/gtk-doc/html/telepathy-logger/right.png
/usr/share/gtk-doc/html/telepathy-logger/style.css
/usr/share/gtk-doc/html/telepathy-logger/telepathy-logger.devhelp2
/usr/share/gtk-doc/html/telepathy-logger/up-insensitive.png
/usr/share/gtk-doc/html/telepathy-logger/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtelepathy-logger.so.3
/usr/lib64/libtelepathy-logger.so.3.3.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/telepathy-logger

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/telepathy-logger/COPYING
