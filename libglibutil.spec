Summary:	Library of glib utilities
Summary(pl.UTF-8):	Biblioteka narzędzi glib
Name:		libglibutil
Version:	1.0.67
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/sailfishos/libglibutil/tags
Source0:	https://github.com/sailfishos/libglibutil/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4cc4b99b9561edf309d89f844806c3d1
Patch0:		install.patch
URL:		https://github.com/sailfishos/libglibutil/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library of glib utilities.

%description -l pl.UTF-8
Biblioteka narzędzi glib.

%package devel
Summary:	Header files for glibutil library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki glibutil
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0

%description devel
Header files for glibutil library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki glibutil.

%prep
%setup -q
%patch0 -p1

%build
%{__make} release pkgconfig \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	LIBDIR=%{_libdir} \
	KEEP_SYMBOLS=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-dev \
	LIBDIR=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/libglibutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglibutil.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglibutil.so
%{_includedir}/gutil
%{_pkgconfigdir}/libglibutil.pc
