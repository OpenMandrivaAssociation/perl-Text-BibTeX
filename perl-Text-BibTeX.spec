%define upstream_name    Text-BibTeX%define upstream_version 0.69
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Interface to read and parse BibTeX files 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Config::AutoConf)
BuildRequires:	perl(ExtUtils::LibBuilder)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl-devel

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
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}
#install -d -m 755 %{buildroot}%{_bindir}
#install -m 755 btformat btcheck btsort %{buildroot}%{_bindir}
mv %{buildroot}%{_bindir}/bibparse %{buildroot}%{_bindir}/bibparse-perl

%files
%doc  README examples
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text
%{_mandir}/*/*
%{_bindir}/*
%{_libdir}/libbtparse.so

%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.580.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.580.0-1
+ Revision: 687004
- update to new version 0.58

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.560.0-1
+ Revision: 684826
- update to new version 0.56

* Fri Apr 29 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.550.0-1
+ Revision: 660539
- new version

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.530.0-2
+ Revision: 654087
- fix installation of native library on x86_64 (#63052)

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.530.0-1
+ Revision: 644800
- update to new version 0.53

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.520.0-2
+ Revision: 640783
- rebuild to obsolete old packages

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.520.0-1
+ Revision: 638970
- update to new version 0.52

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.510.0-1
+ Revision: 635597
- update to new version 0.51

* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.480.0-1mdv2011.0
+ Revision: 596686
- update to 0.48

* Sat Aug 28 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.460.0-1mdv2011.0
+ Revision: 573804
- update to 0.46

* Thu Jul 22 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.450.0-3mdv2011.0
+ Revision: 556821
- bump mkrel
- fix upstream rt#59602 - remove unwanted buildrequires
- rebuild for perl 5.12
- update to 0.45

* Sun Mar 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.430.0-1mdv2010.1
+ Revision: 526035
- new version

* Wed Mar 17 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.420.0-1mdv2010.1
+ Revision: 523440
- update to 0.42

* Mon Mar 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.410.0-1mdv2010.1
+ Revision: 519961
- update to 0.41

* Fri Mar 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.400.0-2mdv2010.1
+ Revision: 518459
- ship debug files in -debug

* Wed Mar 10 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.1
+ Revision: 517550
- adding missing buildrequires:
- adding missing buildrequires:
- update to 0.40

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.380.0-1mdv2010.0
+ Revision: 419928
- new perl version macro
- update Makefile patch for fuziness

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2009.1
+ Revision: 292356
- update to new version 0.38

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.37-6mdv2009.0
+ Revision: 258611
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.37-5mdv2009.0
+ Revision: 246624
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.37-3mdv2008.1
+ Revision: 152328
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.37-2mdv2008.1
+ Revision: 123760
- kill re-definition of %%buildroot on Pixel's request


* Thu Nov 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-2mdv2007.0
+ Revision: 84655
- bump release
- fix x86_64 build
- new version
- Import perl-Text-BibTeX

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-3mdv2007.0
- Rebuild

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.36-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdk
- New release 0.36
- buildrequires
- rediff patches

* Tue Jun 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdk 
- first mdk release



