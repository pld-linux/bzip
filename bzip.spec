Summary:	Efficient compression program
Summary(pl.UTF-8):   Skuteczny program kompresujący
Name:		bzip
Version:	0.21
Release:	4
License:	GPL, but see description for restrictions
Group:		Applications/Archiving
Source0:	ftp://custom.lab.unb.br/pub/compression/bzip/%{name}-%{version}.tar.gz
# Source0-md5:	03a7fe24ced5ac4401a32092409c78be
Obsoletes:	bzip-man
Obsoletes:	bzip-man-gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
bzip jest programem kompresującym używającym algorytmu sortowania
blokowego wraz z kodowaniem arytmetycznym. Kompresuje lepiej od gzipa,
czasem nawet do 30%. Jednak na kodowanie arytmetyczne obowiązuje
patent w niektórych krajach (np. w USA).

Jeżeli chcesz zrobić coś z problemem patentowania algorytmów, zajrzyj
na stronę <http://www.lpf.org/>.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -fomit-frame-pointer"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install bzip ${RPM_BUILD_ROOT}%{_bindir}
install bzip.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
ln -sf bzip ${RPM_BUILD_ROOT}%{_bindir}/bunzip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ALGORITHMS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
