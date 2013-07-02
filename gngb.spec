%define version 0.%{beta}

Summary: Color Gameboy emulator
Name:    gngb
Version: 0.%{beta}
Release: 3
BuildRequires: SDL-devel
BuildRequires: bzip2-devel
BuildRequires: zlib-devel
BuildRequires: mesagl-devel
BuildRequires: mesaglu-devel
Source0: http://m.peponas.free.fr/gngb/download/%{name}-%{beta}.tar.bz2
Group: Emulators
License: GPLv2
URL: http://m.peponas.free.fr/gngb/

%description
Gngb is a Color Gameboy emulator for Linux written in C with the SDL.
It support most of Gameboy and Color Gameboy games.

%prep
%setup -q -n %{name}-%{beta}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog INSTALL README TODO sample_gngbrc
%attr(0755,root,games) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%clean



%changelog
* Sat Jul 30 2011 Andrey Bondrov <abondrov@mandriva.org> 0.20060309-2mdv2012.0
+ Revision: 692424
- imported package gngb


* Sun Jul 24 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.20060309-2mdv2011.0
- Import from PLF
- Remove PLF reference

* Tue Mar 27 2007 Guillaume Bedot <littletux@zarb.org> 0.20060309-1plf2007.1
- New (ok, say lastest) release

* Sun Sep 03 2006 Anssi Hannula <anssi@zarb.org> 0.20060204-6plf2007.0
- fix buildrequires again

* Wed Aug 30 2006 Anssi Hannula <anssi@zarb.org> 0.20060204-5plf2007.0
- fix buildrequires

* Wed Aug 30 2006 Anssi Hannula <anssi@zarb.org> 0.20060204-4plf2007.0
- fix buildrequires

* Sat Jul 22 2006 Guillaume Bedot <littletux@zarb.org> 0.20060204-3plf2007.0
- reup

* Sat Jul 22 2006 Guillaume Bedot <littletux@zarb.org> 0.20060204-2plf2007.0
- Dropped empy NEWS file, clean install, space instead of tabs

* Wed Feb 22 2006 Guillaume Bedot <littletux@zarb.org> 0.20060204-1plf
- First package
