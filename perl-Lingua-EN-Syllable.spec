#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Lingua
%define		pnam	EN-Syllable
Summary:	Lingua::EN::Syllable Perl module - estimating syllable count in words
Summary(pl.UTF-8):	Moduł Perla Lingua::EN::Syllable - szacowanie liczby sylab w słowach
Name:		perl-Lingua-EN-Syllable
Version:	0.251
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f44a056e92c1d9df89e190591879d84f
URL:		http://search.cpan.org/dist/Lingua-EN-Syllable/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Syllable estimates the number of syllables in the word
passed to it.

%description -l pl.UTF-8
Lingua::EN::Syllable szacuje liczbę sylab w wyrazach angielskich.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Lingua/EN/Syllable.pm
%{_mandir}/man3/Lingua::EN::Syllable.3pm*
