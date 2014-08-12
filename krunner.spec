%define major 5
%define libname %mklibname KF5Runner %{major}
%define devname %mklibname KF5Runner -d
%define debug_package %{nil}

Name: krunner
Version: 5.1.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/portingAids/%{name}-%{version}.tar.xz
Summary: Parallelized query system
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5ThreadWeaver)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
Parallelized query system

%package -n %{libname}
Summary: Parallelized query system
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Parallelized query system

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Runner library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Runner library

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_libdir}/qml/org/kde/runnermodel
%{_datadir}/kservicetypes5/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_prefix}/mkspecs/*
