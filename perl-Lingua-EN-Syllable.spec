%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-EN-Syllable perl module
Summary(pl):	Modu³ perla Lingua-EN-Syllable
Name:		perl-Lingua-EN-Syllable
Version:	0.251
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-EN-Syllable-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Lingua-EN-Syllable estimates the number of syllables in the word passed to it. 

%description -l pl
Lingua-EN-Syllable szacuje liczbê sylab w wyrazach angielskich.

%prep
%setup -q -n Lingua-EN-Syllable-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Lingua/EN/Syllable
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Lingua/EN/Syllable.pm
%{perl_sitearch}/auto/Lingua/EN/Syllable

%{_mandir}/man3/*
