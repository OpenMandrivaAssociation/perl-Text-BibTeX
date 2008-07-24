%define module	Text-BibTeX
%define name	perl-%{module}
%define version 0.37
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Interface to read and parse BibTeX files 
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
Patch0:		%{name}-0.36.Makefile.PL.patch
Patch1:		%{name}-0.36.tests.patch
BuildRequires:	btparse
BuildRequires:	perl-devel
BuildRequires:	btparse-devel >= 0.34-2mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Text::BibTeX module serves mainly as a high-level introduction to the
Text::BibTeX library, for both code and documentation purposes. The code loads
the two fundamental modules for processing BibTeX files (Text::BibTeX::File and
Text::BibTeX::Entry), and this documentation gives a broad overview of the
whole library that isn't available in the documentation for the individual
modules that comprise it.

%prep
%setup -q -n %{module}-%{version}
%patch0
%patch1
perl -pi -e 's|#!/usr/local/bin/perl5?|#!/usr/bin/perl|' btformat btcheck btsort examples/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor MYEXTLIB='%{_libdir}/libbtparse.so'
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 btformat btcheck btsort %{buildroot}%{_bindir}

%check
make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README examples
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text
%{_mandir}/*/*
%{_bindir}/*


