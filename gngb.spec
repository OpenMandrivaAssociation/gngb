%define beta 20060309

Summary:	Color Gameboy emulator
Name:		gngb
Version:	0.%{beta}
Release:	5
License:	GPLv2+
Group:		Emulators
Url:		http://m.peponas.free.fr/gngb/
Source0:	http://m.peponas.free.fr/gngb/download/%{name}-%{beta}.tar.bz2
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)

%description
Gngb is a Color Gameboy emulator for Linux written in C with the SDL.
It support most of Gameboy and Color Gameboy games.

%files
%doc AUTHORS COPYING ChangeLog README TODO sample_gngbrc
%attr(0755,root,games) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{beta}

%build
%configure2_5x
%make

%install
%makeinstall_std

