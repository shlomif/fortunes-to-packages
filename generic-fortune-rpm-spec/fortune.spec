# Base Macros which need to be set
%define packageprefix fortune-
%define packagebase joelkirchartz
%define archivebase fortune-joelkirchartz
%define version 0.0.1.20200409
%define fortunefilesprefix %{packagebase}
%define rel 1
%global tarball_ext xz

# Derived Macros
%define archivewithver %{archivebase}-%{version}
%define archivefull %{archivewithver}.tar.%{tarball_ext}

%define fortunedatadir %{_datadir}/games/fortunes

Name: %{packageprefix}-%{packagebase}
Version: %{version}
Release: %{rel}
License: Unlicense
Group: Toys

Source: %{archivefull}
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-root
URL: https://github.com/JKirchartz/fortunes
BuildRequires: fortune-mod
BuildRequires: perl
Requires: fortune-mod
Summary: Fortune Cookies Collection by Joel Kirchartz

%description
This package contains several collections of fortune cookies by Joel
Kirchartz.


%prep
%setup -n %{archivewithver}

%build

myprefix="%{fortunefilesprefix}"
rm -f *.dat
# For strfile
PATH="$PATH:/usr/sbin:/sbin"
for fn in $(perl -E 'print join" ",grep {(not /\A(?:Makefile|LICENSE|(?:README.*)|(?:.*\.dat))\z/)}glob("*")') ; do \
    mv "$fn" "$myprefix$fn" ; \
    strfile "${myprefix}$fn" "${myprefix}$fn.dat" ; \
done

%install

mkdir -p "%{buildroot}"/%{fortunedatadir}
for dat in *.dat ; do \
    cp "${dat}" "`echo "$dat" | sed 's/\.dat$//'`" \
        "%{buildroot}"/%{fortunedatadir}/ ; \
done

%files
%defattr(-,root,root)
%{fortunedatadir}/*
%doc README.md
%license LICENSE

%changelog
* Wed Oct 08 2008 Shlomi Fish <shlomif@iglu.org.il> 0.10.148-1
- Updated slightly.

* Sun Jul 21 2002 Shlomi Fish <shlomif@iglu.org.il> 0.2.4-7
- Applied Tzafrir's Suggestions:
- Created the macro %{fortunedatadir} to specify the locations of the files
- Broke up long lines.
- Added fortune-mod to the BuildRequires
- Made the script /bin/sh compatible
- Changed a mkdir loop to mkdir -p
- Removed the empty %post and %postun targets
- Added a README file.


* Fri May 31 2002 Shlomi Fish <shlomif@iglu.org.il> 0.2.2-2
- Added macros all over the place

* Thu May 30 2002 Shlomi Fish <shlomif@iglu.org.il> 0.2.2-1
- first release - testing.

