%define module	PerlIO-via-Bzip2
%define name	perl-%{module}
%define version	0.02
%define release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	PerlIO layer for Bzip2 (de)compression
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/F/FI/FITZNER/%{module}-%{version}.tar.bz2
Url:		http://www.cpan.org
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Buildrequires:	perl-devel
BuildRequires:  bzip2-devel
BuildRequires:  perl(Compress::Bzip2)
BuildArch: noarch

%description
This module implements a PerlIO layer which will let you handle bzip2
compressed files transparently.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%check
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*

