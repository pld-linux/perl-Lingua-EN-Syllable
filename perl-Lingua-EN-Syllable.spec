%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-EN-Syllable perl module
Summary(pl):	Modu� perla Lingua-EN-Syllable
Name:		perl-Lingua-EN-Syllable
Version:	0.251
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-EN-Syllable-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua-EN-Syllable estimates the number of syllables in the word
passed to it.

%description -l pl
Lingua-EN-Syllable szacuje liczb� sylab w wyrazach angielskich.

%prep
%setup -q -n Lingua-EN-Syllable-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Lingua/EN/Syllable.pm
%{_mandir}/man3/*
