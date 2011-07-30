%define name gngb
%define beta 20060309
%define version 0.%{beta}
%define release %mkrel 2

Summary: Gngb - Color Gameboy emulator
Name: %{name}
Version: %{version}
Release: %{release}
BuildRequires: SDL-devel
BuildRequires: bzip2-devel
BuildRequires: zlib-devel
%if %mdkversion >= 200700
BuildRequires: mesagl-devel
BuildRequires: mesaglu-devel
%else
BuildRequires: X11-devel
BuildRequires: MesaGLU-devel
%endif
Source0: http://m.peponas.free.fr/gngb/download/%{name}-%{beta}.tar.bz2
Group: Emulators
License: GPLv2
URL: http://m.peponas.free.fr/gngb/
BuildRoot: %{_tmppath}/%{name}-build

%description
Gngb is a Color Gameboy emulator for Linux written in C with the SDL.
It support most of Gameboy and Color Gameboy games.

%prep
%setup -q -n %{name}-%{beta}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO sample_gngbrc
%attr(0755,root,games) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%clean
rm -rf %{buildroot}

