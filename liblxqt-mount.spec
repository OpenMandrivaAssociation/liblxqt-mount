%define major 0
%define libname %mklibname lxqtmount %{major}
%define devname %mklibname lxqtmount -d

Summary:	Mounting related libraries for the LXQt desktop
Name:		liblxqt-mount
Version:	0.7.0
Release:	2
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://lxqt.org/
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(qtxdg)

%description
Mounting related libraries for the LXQt desktop.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Mounting related libraries for the LXQt desktop
Group:		System/Libraries
Conflicts:	%{_lib}lxqt-mount0 < 0.7.0-2
Obsoletes:	%{_lib}lxqt-mount0 < 0.7.0-2

%description -n %{libname}
Mounting related libraries for the LXQt desktop.

%files -n %{libname}
%{_libdir}/liblxqtmount.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Conflicts:	%{_lib}lxqt-mount-devel < 0.7.0-2
Obsoletes:	%{_lib}lxqt-mount-devel < 0.7.0-2

%description -n %{devname}
Development files (headers etc.) for %{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/liblxqtmount.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/cmake/lxqtmount

#----------------------------------------------------------------------------

%prep
%setup -q -c %{name}-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

