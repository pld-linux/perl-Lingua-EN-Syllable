%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-Syllable
Summary:	Lingua::EN::Syllable perl module
Summary(pl):	Modu³ perla Lingua::EN::Syllable
Name:		perl-Lingua-EN-Syllable
Version:	0.251
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Syllable estimates the number of syllables in the word
passed to it.

%description -l pl
Lingua::EN::Syllable szacuje liczbê sylab w wyrazach angielskich.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Lingua/EN/Syllable.pm
%{_mandir}/man3/*
