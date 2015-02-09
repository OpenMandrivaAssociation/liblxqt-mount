%define major 0
%define libname %mklibname lxqtmount %{major}
%define devname %mklibname lxqtmount -d
%define scm %nil

Summary:	Mounting related libraries for the LXQt desktop
Name:		liblxqt-mount
Version:	0.9.0
%if "%scm" != ""
Source0:	%{name}-%{scm}.tar.xz
Release:	0.%scm.1
%else
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Release:	1
%endif
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://lxqt.org/
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(Qt5Xdg)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5X11Extras)

%description
Mounting related libraries for the LXQt desktop.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Mounting related libraries for the LXQt desktop
Group:		System/Libraries
Conflicts:	%{_lib}lxqt-mount0 < 0.7.0-2
Obsoletes:	%{_lib}lxqt-mount0 < 0.7.0-2
Conflicts:	%{_lib}lxqtmount-qt5_0 < 0.9.0
%rename		%{_lib}lxqtmount-qt5_0

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
%rename		%{_lib}lxqtmount-qt5-devel

%description -n %{devname}
Development files (headers etc.) for %{name}.

%files -n %{devname}
%dir %{_libdir}/cmake/lxqtmount
%{_includedir}/*
%{_libdir}/liblxqtmount.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/cmake/lxqtmount
%{_libdir}/cmake/lxqtmount/*.cmake

#----------------------------------------------------------------------------

%prep
%if "%scm" != ""
%setup -q -n %{name}
%else
%setup -q -n %{name}-%{version}
%endif

%build
%cmake -DUSE_QT5:BOOL=ON
%make

%install
%makeinstall_std -C build

