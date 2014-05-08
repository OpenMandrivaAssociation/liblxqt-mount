%define major 0
%define libname %mklibname lxqt-mount %{major}
%define devname %mklibname lxqt-mount -d

Name: liblxqt-mount
Version: 0.7.0
Release: 1
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Summary: Mounting related libraries for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(qtxdg)
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: qt4-devel
Requires: %{libname} = %{EVRD}

%description
Mounting related libraries for the LXQt desktop

%package -n %{libname}
Summary: Mounting related libraries for the LXQt desktop
Group: System/Libraries

%description -n %{libname}
Mounting related libraries for the LXQt desktop

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q -c %{name}-%{version}
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/lxqtmount
