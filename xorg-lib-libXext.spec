Summary:	X extension library
Summary(pl.UTF-8):	Biblioteka rozszerzeń X
Name:		xorg-lib-libXext
Version:	1.0.99.4
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2
# Source0-md5:	24da44888b87c66edb326acec35b85aa
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libX11-devel >= 1.1.99.1
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.3
BuildRequires:	xorg-proto-xproto-devel >= 7.0.13
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	libXext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X extension library.

%description -l pl.UTF-8
Biblioteka rozszerzeń X.

%package devel
Summary:	Header files for libXext library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXext
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXau-devel
Requires:	xorg-lib-libX11-devel >= 1.1.99.1
Requires:	xorg-proto-xextproto-devel >= 7.0.99.3
Requires:	xorg-proto-xproto-devel >= 7.0.13
Obsoletes:	libXext-devel

%description devel
X extension library.

This package contains the header files needed to develop programs that
use libXext.

%description devel -l pl.UTF-8
Biblioteka rozszerzeń X.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXext.

%package static
Summary:	Static libXext library
Summary(pl.UTF-8):	Biblioteka statyczna libXext
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXext-static

%description static
X extension library.

This package contains the static libXext library.

%description static -l pl.UTF-8
Biblioteka rozszerzeń X.

Pakiet zawiera statyczną bibliotekę libXext.

%prep
%setup -q -n libXext-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXext.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXext.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXext.so
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXext.la
%{_pkgconfigdir}/xext.pc
%{_mandir}/man3/DBE.3x*
%{_mandir}/man3/DPMS*.3x*
%{_mandir}/man3/XShape*.3x*
%{_mandir}/man3/XShm*.3x*
%{_mandir}/man3/Xcup*.3x*
%{_mandir}/man3/Xdbe*.3x*
%{_mandir}/man3/Xevi*.3x*
%{_mandir}/man3/Xmbuf*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXext.a
