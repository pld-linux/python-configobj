# NOTE:
# Pollutes module namespace by
# %{py_sitescriptdir}/_version.py*

%define         module  configobj
Summary:	Reading and writing config files
Summary(pl.UTF-8):	Odczyt i zapis plików konfiguracyjnych
Name:		python-configobj
Version:	5.0.6
Release:	1
License:	MIT
Group:		Libraries/Python
## Source0:	https://github.com/DiffSK/configobj/archive/%{version}.tar.gz
Source0:	https://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	e472a3a1c2a67bb0ec9b5d54c13a47d6
URL:		https://github.com/DiffSK/configobj
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	unzip
Requires:	python-modules
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reading and writing config files.

%description -l pl.UTF-8
Odczyt i zapis plików konfiguracyjnych.

%prep
%setup -q -n configobj-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/configobj.py*
# Import error without _version.p
%{py_sitescriptdir}/_version.py*
# Seems not be needed:
## %{py_sitescriptdir}/validate.py*
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
