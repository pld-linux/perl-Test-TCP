#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	TCP
%include	/usr/lib/rpm/macros.perl
Summary:	Test::TCP - testing TCP program
#Summary(pl.UTF-8):	
Name:		perl-Test-TCP
Version:	1.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f328b8b207ade2aba981bddb4cc2dd31
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Test-TCP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::SharedFork) >= 0.14
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::TCP is test utilities for TCP/IP programs.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
