%define upstream_name    Devel-Refcount
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Obtain the REFCNT value of a referent
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/Devel-Refcount-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a single function which obtains the reference count of
the object being pointed to by the passed reference value.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.90.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Apr 21 2011 Götz Waschk <waschk@mandriva.org> 0.90.0-1
+ Revision: 656435
- update build deps
- update to new version 0.09

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 555238
- rebuild

* Thu Jan 21 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.1
+ Revision: 494441
- update to 0.07

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 395362
- update to 0.06

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 390464
- import perl-Devel-Refcount


* Mon Jun 29 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist


