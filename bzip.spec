Summary:	Efficient compression program
Summary(pl):	Skuteczny program kompresuj±cy
Name:		bzip
Version:	0.21
Release:	4
Source0:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/%{name}-%{version}.tar.gz
License:	GPL, but see description for restrictions
Group:		Applications/Archiving
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	bzip-man
Obsoletes:	bzip-man-gz

%description
bzip is a compression program which uses some wild new `block sorting
algorithm' with `arithmetic encoding'. The fundamental point is that
it makes your files smaller than gzip does, sometimes by up to 30%.
The other fundamental point is that it may have algorithm patents
against it, so stick to gzip for public releases and commercial use
(especially in the States.. some of us live in less repressive
countries so we don't need to worry so much.)

If you want to do something about the problem of Algorithm patents,
contact the League for Programming Freedom to see what you can do to
help. http://www.lpf.org/

%description -l pl
bzip jest programem kompresuj±cym u¿ywaj±cym algorytmu sortowania
blokowego wraz z kodowaniem arytmetycznym. Kompresuje lepiej od gzipa,
czasem nawet do 30%. Jednak na kodowanie arytmetyczne obowi±zuje
patent w niektórych krajach (np. w USA).

Je¿eli chcesz zrobiæ co¶ z problemem patentowania algorytmów, zajrzyj
na stronê http://www.lpf.org/ .

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags} -fomit-frame-pointer"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install bzip ${RPM_BUILD_ROOT}%{_bindir}
install bzip.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
ln -sf bzip ${RPM_BUILD_ROOT}%{_bindir}/bunzip
gzip -9nf ALGORITHMS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ALGORITHMS,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
