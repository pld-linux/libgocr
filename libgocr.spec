Summary:	GOCR API library
Summary(pl):	Biblioteka GOCR API
Name:		libgocr
Version:	0.7.2
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://prdownloads.sourceforge.net/jocr/%{name}-%{version}.tar.gz
URL:		http://jocr.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	netpbm-devel
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
u≥atwiÊ øycie programistom algorytmÛw OCR. Biblioteka obs≥uguje wiele
wewnÍtrznych problemÛw, struktur, danych, obrazkÛw - uwalniaj±c
programistÍ od tego ciÍøaru. Wszystko, co musi napisaÊ programista, to
plugin (uøywaj±c np. Module Development Kit), ktÛry "tylko" obrabia
obraz znaku i zwraca jego warto∂Ê.

%package devel
Summary:	Development package for GOCR API
Summary(pl):	Pakiet dla programistÛw uøywaj±cych GOCR API
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files and developer's documentation for GOCR API.

%description devel -l pl
Pliki nag≥Ûwkowe i dokumentacja programisty do GOCR API.

%package static
Summary:	Static GOCR API library
Summary(pl):	Biblioteka statyczna GOCR API
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static version of GOCR API library.

%description static -l pl
Statyczna wersja biblioteki GOCR API.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force --ltdl
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gocrdir=%{_includedir}

gzip -9nf Changelog README STATUS TODO doc/developers.txt

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
