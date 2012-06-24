Summary:	X extension library
Summary(pl):	Biblioteka rozszerze� X
Name:		xorg-lib-libXext
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/libXext-%{version}.tar.bz2
# Source0-md5:	30d1c7c035b059fca09ac3c0c1505a2f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X extension library.

%description -l pl
Biblioteka rozszerze� X.

%package devel
Summary:	Header files libXext development
Summary(pl):	Pliki nag��wkowe do biblioteki libXext
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-proto-xextproto-devel
Obsoletes:	libXext-devel

%description devel
X extension library.

This package contains the header files needed to develop programs that
use these libXext.

%description devel -l pl
Biblioteka rozszerze� X.

Pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania program�w
u�ywaj�cych biblioteki libXext.

%package static
Summary:	Static libXext library
Summary(pl):	Biblioteka statyczna libXext
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXext-static

%description static
X extension library.

This package contains the static libXext library.

%description static -l pl
Biblioteka rozszerze� X.

Pakiet zawiera statyczn� bibliotek� libXext.

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
	libmandir=%{_mandir}/man3 \
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
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXext.a
