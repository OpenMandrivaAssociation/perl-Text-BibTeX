%define upstream_name       Text-BibTeX
%define upstream_version 0.45

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Interface to read and parse BibTeX files 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	btparse
BuildRequires:	btparse-devel >= 0.34-2mdk
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Config::AutoConf)
BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Text::BibTeX module serves mainly as a high-level introduction to the
Text::BibTeX library, for both code and documentation purposes. The code loads
the two fundamental modules for processing BibTeX files (Text::BibTeX::File and
Text::BibTeX::Entry), and this documentation gives a broad overview of the
whole library that isn't available in the documentation for the individual
modules that comprise it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
perl -pi -e 's|#!/usr/local/bin/perl5?|#!/usr/bin/perl|' scripts/* examples/*

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}
#install -d -m 755 %{buildroot}%{_bindir}
#install -m 755 btformat btcheck btsort %{buildroot}%{_bindir}
mv %{buildroot}%{_bindir}/bibparse %{buildroot}%{_bindir}/bibparse-perl

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README examples
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text
%{_mandir}/*/*
%{_bindir}/*
/usr/lib/libbtparse.so
