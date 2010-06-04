Summary:	libXext - library for common extensions to the X11 protocol
Summary(pl.UTF-8):	Biblioteka libXext powszechnych rozszerzeń protokołu X11
Name:		xorg-lib-libXext
Version:	1.1.2
Release:	1
Epoch:		1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2
# Source0-md5:	9e51f9cb7e0a38c7099ac1c0de1a1add
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libX11-devel >= 1.1.99.1
BuildRequires:	xorg-proto-xextproto-devel >= 1:7.1.0
BuildRequires:	xorg-proto-xproto-devel >= 7.0.13
BuildRequires:	xorg-util-util-macros >= 1.3
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
Requires:	xorg-lib-libXau-devel
Requires:	xorg-lib-libX11-devel >= 1.1.99.1
Requires:	xorg-proto-xextproto-devel >= 1:7.1.0
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

# in liblbxutil now
%{__rm} $RPM_BUILD_ROOT%{_includedir}/X11/extensions/lbx{buf,bufstr,image}.h

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
