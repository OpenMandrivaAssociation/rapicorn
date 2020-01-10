%define _disable_ld_no_undefined 1

%define api_version	1307
%define major		0
%define libname		%mklibname %{name} %{api_version} %{major}
%define develname	%mklibname %{name} -d

%define custom_dsp 0
%{?dsp_device: %global custom_dsp 1}

%define custom_midi 0
%{?midi_device: %global custom_midi 1}

Name:		rapicorn
Summary:	Rapid development toolkit
Version:	13.07.0
Release:	2
Source0:	http://rapicorn.org/dist/%{name}/%{name}-%{version}.tar.bz2
Patch0:		rapicorn-13.07.0-libpng.patch
URL:		https://testbit.eu/wiki/Rapicorn_Home
License:	GPLv2+
Group:		Sound
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(python)
BuildRequires:	intltool
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libxml2-utils
BuildRequires:	readline-devel

Requires:	%{libname} = %{version}-%{release}

%description
Rapicorn is a toolkit for rapid development of graphical user interfaces using 
C++ and Python. Rapicorn is developed with the aim to significantly improve 
developer efficiency and user experience. 

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
License:	LGPLv2+

%description -n %{libname}
BEAST (the BEdevilled Audio System) is a GTK+/GNOME-based frontend to
BSE (the Bedevilled Sound Engine). BSE comes with the abilities to
load/store songs and synthesis networks (in .bse files), play them
modify them, etc. BEAST provides the necessary GUI to make actual
use of BSE. Synthesis filters (BseSources) are implemented in shared
library modules, and get loaded on demand.

You must install this library before running %{name}.

%package -n %{develname}
Summary:	Header files and static libraries from %{name}
Group: 		Development/C
License:	LGPLv2+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%autopatch -p1

%build
export CFLAGS="$CFLAGS -D_GLIBCXX_USE_NANOSLEEP -D_GLIBCXX_USE_SCHED_YIELD"
export CXXFLAGS="$CFLAGS -D_GLIBCXX_USE_NANOSLEEP -D_GLIBCXX_USE_SCHED_YIELD"
export LIBS="-lrt -lcairo"
%configure2_5x 
%make

%install
%makeinstall_std

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README AUTHORS COPYING* NEWS
%{_docdir}/rapicorn%{api_version}
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/aidacc-%{api_version}
%{py_puresitedir}/Aida%{api_version}
%{py_puresitedir}/Rapicorn%{api_version}

%files -n %{libname}
%{_libdir}/librapicorn%{api_version}.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so


