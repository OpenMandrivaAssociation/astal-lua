%global astal_commit 69efb4c91e590adcb5a3d8938454f987982e3891
%global astal_shortcommit %(c=%{astal_commit}; echo ${c:0:7})
%global bumpver 1

%global _vpath_srcdir lang/lua

%define libname %mklibname astal-lua

Name:       astal-lua
Version:    1~%{bumpver}.git%{astal_shortcommit}
Release:    2
Source0:    https://github.com/aylur/astal/archive/%{astal_commit}/%{name}-%{astal_shortcommit}.tar.gz
Summary:    Lua bindings for libastal
URL:        https://github.com/aylur/astal
License:    LGPL-2.1-only
Group:      System/Libraries

BuildArch:      noarch

BuildRequires:  lua-devel

Requires:       astal
Requires:       astal-io
Requires:       lua-lgi

%description
%{summary}.

%package -n %{libname}
Summary:    %summary
Group:      System/Libraries
Provides:   %{libname} = %{EVRD}
Provides:   %{name}

%description -n %{libname}

%prep
%autosetup -n astal-%{astal_commit} -p1

%build

%install
pushd %{_vpath_srcdir}
mkdir -p %{buildroot}/usr/share/lua/5.4.7
cp -pr astal %{buildroot}/usr/share/lua/5.4.7/

%files -n %{libname}
%license LICENSE
%{_datadir}/*



