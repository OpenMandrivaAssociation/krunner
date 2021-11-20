%define major 5
%define libname %mklibname KF5Runner %{major}
%define devname %mklibname KF5Runner -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: krunner
Version: 5.88.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Parallelized query system
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5ThreadWeaver)
BuildRequires: cmake(KF5Activities)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}

%description
Parallelized query system.

%package -n %{libname}
Summary: Parallelized query system
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Parallelized query system.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Runner library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Runner library.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories5/krunner.*categories
%{_libdir}/qt5/qml/org/kde/runnermodel
%{_datadir}/kservicetypes5/*
%{_datadir}/dbus-1/interfaces/kf5_org.kde.krunner1.xml

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/*
%{_datadir}/kdevappwizard

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
