%define upstream_name	 PerlIO-via-Bzip2
Name:		perl-%{upstream_name}
Version:	0.02
Release:	7

Summary:	PerlIO layer for Bzip2 (de)compression
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/PerlIO-via-Bzip2
Source0:	https://cpan.metacpan.org/authors/id/A/AR/ARJEN/PerlIO-via-Bzip2-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	bzip2-devel
BuildRequires:	perl(Compress::Bzip2)
BuildArch:	noarch

%description
This module implements a PerlIO layer which will let you handle bzip2
compressed files transparently.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files 
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 658874
- rebuild for updated spec-helper

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 407960
- rebuild using %0.02 Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.02-5mdv2009.0
+ Revision: 241815
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.02-3mdv2008.0
+ Revision: 25187
- rebuild


* Wed Jun 15 2005 Olivier Thauvin <nanardon@mandriva.org> 0.02-2mdk
- noarch

* Wed Jun 15 2005 Olivier Thauvin <nanardon@mandriva.org> 0.02-1mdk
- First mandriva spec

