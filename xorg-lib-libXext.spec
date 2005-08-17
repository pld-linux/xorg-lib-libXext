
#
Summary:	X extension library
Summary(pl):	Biblioteka rozszerzeñ X
Name:		xorg-lib-libXext
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXext-%{version}.tar.bz2
# Source0-md5:	b45858152e10c5271a71f7048cc27e85
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-proto-xextproto-devel
Obsoletes:	libXext
BuildRoot:	%{tmpdir}/libXext-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X extension library.

%description -l pl
Biblioteka rozszerzeñ X.


%package devel
Summary:	Header files libXext development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXext
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXext = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-proto-xextproto-devel
Obsoletes:	libXext-devel

%description devel
X extension library.

This package contains the header files needed to develop programs that
use these libXext.

%description devel -l pl
Biblioteka rozszerzeñ X.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXext.


%package static
Summary:	Static libXext libraries
Summary(pl):	Biblioteki statyczne libXext
Group:		Development/Libraries
Requires:	xorg-lib-libXext-devel = %{version}-%{release}
Obsoletes:	libXext-static

%description static
X extension library.

This package contains the static libXext library.

%description static -l pl
Biblioteka rozszerzeñ X.

Pakiet zawiera statyczn± bibliotekê libXext.


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
%doc AUTHORS ChangeLog
%attr(755,root,wheel) %{_libdir}/libXext.so.*


%files devel
%defattr(644,root,root,755)
%{_libdir}/libXext.la
%attr(755,root,wheel) %{_libdir}/libXext.so
%{_pkgconfigdir}/xext.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXext.a
