#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Test
%define		pnam	TCP
Summary:	Test::TCP - testing TCP program
Summary(pl.UTF-8):	Test::TCP - testowanie programów TCP
Name:		perl-Test-TCP
Version:	2.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d539ad6b16856e863a6b6b54fa58df33
URL:		http://search.cpan.org/dist/Test-TCP/
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-SharedFork >= 0.29
BuildRequires:	perl-Test-Simple >= 0.98
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::TCP is test utilities for TCP/IP programs.

%description -l pl.UTF-8
Test::TCP to narzędzia testowe dla programów TCP/IP.

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
%doc Changes README.md
%{perl_vendorlib}/Net/EmptyPort.pm
%{perl_vendorlib}/Test/TCP.pm
%{perl_vendorlib}/Test/TCP
%{_mandir}/man3/Net::EmptyPort.3pm*
%{_mandir}/man3/Test::TCP.3pm*
%{_mandir}/man3/Test::TCP::CheckPort.3pm*
