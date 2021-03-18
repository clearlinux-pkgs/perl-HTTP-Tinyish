#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Tinyish
Version  : 0.17
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/HTTP-Tinyish-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/HTTP-Tinyish-0.17.tar.gz
Summary  : 'HTTP::Tiny compatible HTTP client wrappers'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Tinyish-license = %{version}-%{release}
Requires: perl-HTTP-Tinyish-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Which)

%description
NAME
HTTP::Tinyish - HTTP::Tiny compatible HTTP client wrappers
SYNOPSIS
my $http = HTTP::Tinyish->new(agent => "Mozilla/4.0");

my $res = $http->get("http://www.cpan.org/");
warn $res->{status};

$http->post("http://example.com/post", {
headers => { "Content-Type" => "application/x-www-form-urlencoded" },
content => "foo=bar&baz=quux",
});

$http->mirror("http://www.cpan.org/modules/02packages.details.txt.gz", "./02packages.details.txt.gz");

%package dev
Summary: dev components for the perl-HTTP-Tinyish package.
Group: Development
Provides: perl-HTTP-Tinyish-devel = %{version}-%{release}
Requires: perl-HTTP-Tinyish = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Tinyish package.


%package license
Summary: license components for the perl-HTTP-Tinyish package.
Group: Default

%description license
license components for the perl-HTTP-Tinyish package.


%package perl
Summary: perl components for the perl-HTTP-Tinyish package.
Group: Default
Requires: perl-HTTP-Tinyish = %{version}-%{release}

%description perl
perl components for the perl-HTTP-Tinyish package.


%prep
%setup -q -n HTTP-Tinyish-0.17
cd %{_builddir}/HTTP-Tinyish-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Tinyish
cp %{_builddir}/HTTP-Tinyish-0.17/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Tinyish/036ac4fadad942c8dfc1c24119c25472ba94bb21
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Tinyish.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Tinyish/036ac4fadad942c8dfc1c24119c25472ba94bb21

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/HTTP/Tinyish.pm
/usr/lib/perl5/vendor_perl/5.32.1/HTTP/Tinyish/Base.pm
/usr/lib/perl5/vendor_perl/5.32.1/HTTP/Tinyish/Curl.pm
/usr/lib/perl5/vendor_perl/5.32.1/HTTP/Tinyish/HTTPTiny.pm
/usr/lib/perl5/vendor_perl/5.32.1/HTTP/Tinyish/LWP.pm
/usr/lib/perl5/vendor_perl/5.32.1/HTTP/Tinyish/Wget.pm
