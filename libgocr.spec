Summary:	GOCR API library
Summary(pl):	Biblioteka GOCR API
Name:		libgocr
Version:	0.7.2
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/jocr/%{name}-%{version}.tar.gz
Patch0:		%{name}-doc.patch
Patch1:		%{name}-configure.patch
URL:		http://jocr.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	netpbm-devel
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOCR (GNU Optical Character Recognition) API is a library, released
under the LGPL, intended to make life easier to the developers of OCR
algorithms. It handles all the internal problems, structures, data,
images, etc, freeing the programmer of all this burden. All one has to
do is to write a plugin (using, for example, the Module Development
Kit), which "simply" processes the image of a character and returns
its value. Easy.

%description -l pl
GOCR (GNU OCR) API jest bibliotek± na licencji LGPL maj±c± za zadanie
u³atwiæ ¿ycie programistom algorytmów OCR. Biblioteka obs³uguje wiele
wewnêtrznych problemów, struktur, danych, obrazków - uwalniaj±c
programistê od tego ciê¿aru. Wszystko, co musi napisaæ programista, to
plugin (u¿ywaj±c np. Module Development Kit), który "tylko" obrabia
obraz znaku i zwraca jego warto¶æ.

%package devel
Summary:	Development package for GOCR API
Summary(pl):	Pakiet dla programistów u¿ywaj±cych GOCR API
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and developer's documentation for GOCR API.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do GOCR API.

%package static
Summary:	Static GOCR API library
Summary(pl):	Biblioteka statyczna GOCR API
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of GOCR API library.

%description static -l pl
Statyczna wersja biblioteki GOCR API.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gocrdir=%{_includedir}

gzip -9nf Changelog README STATUS TODO doc/developers.txt doc/api.ps

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/gocr

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
