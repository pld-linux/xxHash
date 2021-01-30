Summary:	xxHash - extremely fast hash algorithm
Summary(pl.UTF-8):	xxHash - bardzo szybki algorytm haszowania
Name:		xxHash
Version:	0.8.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/Cyan4973/xxHash/releases
Source0:	https://github.com/Cyan4973/xxHash/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	62310678857c30fcef4128f41f711f49
Patch0:		%{name}-pc.patch
URL:		https://github.com/Cyan4973/xxHash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch %{arm}
%define		archcflags	-DXXH_FORCE_MEMORY_ACCESS=1
%endif

%description
xxHash is an Extremely fast Hash algorithm, running at RAM speed
limits. It successfully completes the SMHasher test suite which
evaluates collision, dispersion and randomness qualities of hash
functions. Code is highly portable, and hashes are identical on all
platforms (little / big endian).

%description -l pl.UTF-8
xxHash to niezwykle szybki algorytm haszowania, dochodzący do
ograniczeń szybkości pamięci RAM. Przechodzi zestaw testów SMHasher,
oceniający współczynniki kolizji, dyspersji i losowości funkcji
haszujących. Kod jest przenośny, a wartości haszy identyczne na
wszystkich platformach (little- i big-endian).

%package devel
Summary:	Header files for xxHash library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki xxHash
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for xxHash library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki xxHash.

%package static
Summary:	Static xxHash library
Summary(pl.UTF-8):	Statyczna biblioteka xxHash
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static xxHash library.

%description static -l pl.UTF-8
Statyczna biblioteka xxHash.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" \
CPPFLAGS="%{rpmcflags} %{?archcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	prefix=%{_prefix} \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.md
%attr(755,root,root) %{_bindir}/xxhsum
%attr(755,root,root) %{_bindir}/xxh32sum
%attr(755,root,root) %{_bindir}/xxh64sum
%attr(755,root,root) %{_bindir}/xxh128sum
%attr(755,root,root) %{_libdir}/libxxhash.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxxhash.so.0
%{_mandir}/man1/xxhsum.1*
%{_mandir}/man1/xxh32sum.1*
%{_mandir}/man1/xxh64sum.1*
%{_mandir}/man1/xxh128sum.1*

%files devel
%defattr(644,root,root,755)
%doc doc/xxhash_spec.md
%attr(755,root,root) %{_libdir}/libxxhash.so
%{_includedir}/xxh3.h
%{_includedir}/xxhash.h
%{_pkgconfigdir}/libxxhash.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxxhash.a
