#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	XMLNews-HTMLTemplate
Summary:	XMLNews::HTMLTemplate Perl module - for converting NITF to HTML
Summary(pl):	Modu³ Perla XMLNews::HTMLTemplate - konwersja NITF do HTML-a
Name:		perl-XMLNews-HTMLTemplate
Version:	0.01
Release:	3
License:	free
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/DMEGG/%{pnam}-%{version}.tar.gz
# Source0-md5:	936eafa6325978be17cf6d94ff5fdf6f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XMLNews-Meta
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XMLNews::HTMLTemplate module provides a simple mechanism for
creating HTML pages from XML/NITF news stories and/or XML/RDF metadata
files based on a user-supplied template file. The template is a simple
HTML file (SGML or XML flavour) using special template commands.

%description -l pl
Modu³ XMLNews::HTMLTemplate udostêpnia prosty mechanizm do tworzenia
stron HTML z artyku³ów XML/NITF i/lub plików metadanych XML/RDF,
bazuj±c na podanym pliku z szablonem. Szablon jest prostym plikiem
HTML (w wersji SGML lub XML) ze specjalnymi poleceniami.

%prep
%setup -q -n %{pnam}-%{version}

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
%doc Changes README
%{perl_vendorlib}/XMLNews/HTMLTemplate.pm
%{_mandir}/man3/*
