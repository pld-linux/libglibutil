Summary:	Library of glib utilities
Name:		libglibutil
Version:	1.0.67
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	https://github.com/sailfishos/libglibutil/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4cc4b99b9561edf309d89f844806c3d1
Patch0:		install.patch
URL:		https://github.com/sailfishos/libglibutil/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library of glib utilities.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q
%patch0 -p1

%build
%{__make} release pkgconfig \
	CFLAGS="%{rpmcflags}" \
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
%doc README
%attr(755,root,root) %{_libdir}/%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}.so
%{_includedir}/gutil
%{_pkgconfigdir}/%{name}.pc
