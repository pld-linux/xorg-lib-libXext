Summary:	X extension library
Summary(pl.UTF-8):	Biblioteka rozszerzeń X
Name:		xorg-lib-libXext
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2
# Source0-md5:	1bf6fa1c26f9957d7cc0bd90b038dfa6
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xextproto-devel
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
Requires:	xorg-lib-libX11-devel
Requires:	xorg-proto-xextproto-devel
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXext.so
%{_libdir}/libXext.la
%{_pkgconfigdir}/xext.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXext.a
