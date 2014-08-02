%define major 0
%define libname %mklibname lxqtmount-qt5 %{major}
%define devname %mklibname lxqtmount-qt5 -d
%define qt4libname %mklibname lxqtmount %{major}
%define qt4devname %mklibname lxqtmount -d
%define scm 20140730

Summary:	Mounting related libraries for the LXQt desktop
Name:		liblxqt-mount
Version:	0.8.0
%if %scm
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
BuildRequires:	pkgconfig(lxqt-qt5)
BuildRequires:	pkgconfig(Qt5Xdg)

%description
Mounting related libraries for the LXQt desktop.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Mounting related libraries for the LXQt desktop
Group:		System/Libraries
Conflicts:	%{_lib}lxqt-mount0 < 0.7.0-2
Obsoletes:	%{_lib}lxqt-mount0 < 0.7.0-2
%rename	%{qt4libname}

%description -n %{libname}
Mounting related libraries for the LXQt desktop.

%files -n %{libname}
%{_libdir}/liblxqtmount-qt5.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Conflicts:	%{_lib}lxqt-mount-devel < 0.7.0-2
Obsoletes:	%{_lib}lxqt-mount-devel < 0.7.0-2
%rename	%{qt4devname}

%description -n %{devname}
Development files (headers etc.) for %{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/liblxqtmount-qt5.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/cmake/lxqtmount-qt5

#----------------------------------------------------------------------------

%prep
%if %scm
%setup -q -n %{name}
%else
%setup -q -c %{name}-%{version}
%endif

%build
%cmake -DUSE_QT5:BOOL=ON
%make

%install
%makeinstall_std -C build

