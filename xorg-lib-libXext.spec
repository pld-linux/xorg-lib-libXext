Summary:	libXext - library for common extensions to the X11 protocol
Summary(pl.UTF-8):	Biblioteka libXext powszechnych rozszerzeń protokołu X11
Name:		xorg-lib-libXext
Version:	1.3.3
Release:	2
Epoch:		1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2
# Source0-md5:	52df7c4c1f0badd9f82ab124fb32eb97
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	docbook-dtd412-xml
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-proto-xextproto-devel >= 1:7.1.99
BuildRequires:	xorg-proto-xproto-devel >= 7.0.13
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
Requires:	xorg-lib-libX11 >= 1.6
Obsoletes:	libXext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libXext - library for common extensions to the X11 protocol.

%description -l pl.UTF-8
Biblioteka libXext powszechnych rozszerzeń protokołu X11.

%package devel
Summary:	Header files for libXext library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXext
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-lib-libXau-devel
Requires:	xorg-proto-xextproto-devel >= 1:7.1.99
Requires:	xorg-proto-xproto-devel >= 7.0.13
Obsoletes:	libXext-devel

%description devel
libXext - library for common extensions to the X11 protocol.

This package contains the header files needed to develop programs that
use libXext.

%description devel -l pl.UTF-8
Biblioteka libXext powszechnych rozszerzeń protokołu X11.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXext.

%package static
Summary:	Static libXext library
Summary(pl.UTF-8):	Biblioteka statyczna libXext
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libXext-static

%description static
libXext - library for common extensions to the X11 protocol.

This package contains the static libXext library.

%description static -l pl.UTF-8
Biblioteka libXext powszechnych rozszerzeń protokołu X11.

Pakiet zawiera statyczną bibliotekę libXext.

%prep
%setup -q -n libXext-%{version}

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' man/*.man

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--without-fop
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXext.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXext.so.6

%files devel
%defattr(644,root,root,755)
%doc specs/*.html
%attr(755,root,root) %{_libdir}/libXext.so
%{_libdir}/libXext.la
%{_includedir}/X11/extensions/MITMisc.h
%{_includedir}/X11/extensions/XEVI.h
%{_includedir}/X11/extensions/XLbx.h
%{_includedir}/X11/extensions/XShm.h
%{_includedir}/X11/extensions/Xag.h
%{_includedir}/X11/extensions/Xcup.h
%{_includedir}/X11/extensions/Xdbe.h
%{_includedir}/X11/extensions/Xext.h
%{_includedir}/X11/extensions/Xge.h
%{_includedir}/X11/extensions/dpms.h
%{_includedir}/X11/extensions/extutil.h
%{_includedir}/X11/extensions/multibuf.h
%{_includedir}/X11/extensions/security.h
%{_includedir}/X11/extensions/shape.h
%{_includedir}/X11/extensions/sync.h
%{_includedir}/X11/extensions/xtestext1.h
%{_pkgconfigdir}/xext.pc
%{_mandir}/man3/DBE.3*
%{_mandir}/man3/DPMS*.3*
%{_mandir}/man3/XShape*.3*
%{_mandir}/man3/XShm*.3*
%{_mandir}/man3/Xcup*.3*
%{_mandir}/man3/Xdbe*.3*
%{_mandir}/man3/Xevi*.3*
%{_mandir}/man3/Xmbuf*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXext.a
