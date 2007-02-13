Summary:	GOCR API library
Summary(pl.UTF-8):	Biblioteka GOCR API
Name:		libgocr
Version:	0.7.2
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/jocr/%{name}-%{version}.tar.gz
# Source0-md5:	1b4747f02a0f2eadf31228f19c120265
Patch0:		%{name}-doc.patch
Patch1:		%{name}-configure.patch
URL:		http://jocr.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	netpbm-devel
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOCR (GNU Optical Character Recognition) API is a library, released
under the LGPL, intended to make life easier to the developers of OCR
algorithms. It handles all the internal problems, structures, data,
images, etc, freeing the programmer of all this burden. All one has to
do is to write a plugin (using, for example, the Module Development
Kit), which "simply" processes the image of a character and returns
its value. Easy.

%description -l pl.UTF-8
GOCR (GNU OCR) API jest biblioteką na licencji LGPL mającą za zadanie
ułatwić życie programistom algorytmów OCR. Biblioteka obsługuje wiele
wewnętrznych problemów, struktur, danych, obrazków - uwalniając
programistę od tego ciężaru. Wszystko, co musi napisać programista, to
plugin (używając np. Module Development Kit), który "tylko" obrabia
obraz znaku i zwraca jego wartość.

%package devel
Summary:	Development package for GOCR API
Summary(pl.UTF-8):	Pakiet dla programistów używających GOCR API
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and developer's documentation for GOCR API.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty do GOCR API.

%package static
Summary:	Static GOCR API library
Summary(pl.UTF-8):	Biblioteka statyczna GOCR API
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of GOCR API library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki GOCR API.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gocrdir=%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog README STATUS TODO doc/developers.txt doc/api.ps
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/gocr

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
