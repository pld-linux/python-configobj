# NOTE:
# Pollutes module namespace by
# %{py*_sitescriptdir}/_version.py*
# %{py*_sitescriptdir}/validate.py*

#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module		configobj
%define 	egg_name	configobj
Summary:	Reading and writing config files
Summary(pl.UTF-8):	Odczyt i zapis plików konfiguracyjnych
Name:		python-configobj
Version:	5.0.6
Release:	3
License:	MIT
Group:		Libraries/Python
## Source0:	https://github.com/DiffSK/configobj/archive/%{version}.tar.gz
Source0:	https://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	e472a3a1c2a67bb0ec9b5d54c13a47d6
URL:		https://github.com/DiffSK/configobj
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reading and writing config files.

%description -l pl.UTF-8
Odczyt i zapis plików konfiguracyjnych.

%package -n python3-%{module}
Summary:	Reading and writing config files
Summary(pl.UTF-8):	Odczyt i zapis plików konfiguracyjnych
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-six

%description -n python3-%{module}
Reading and writing config files.

%description  -n python3-%{module} -l pl.UTF-8
Odczyt i zapis plików konfiguracyjnych.

%prep
%setup -q -n configobj-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}.py[co]
# Import error without _version.py
%{py_sitescriptdir}/_version.py[co]
# from validate import VdtMissingValue
%{py_sitescriptdir}/validate.py[co]
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.*.pyc
# Import error without _version.py
%{py3_sitescriptdir}/_version.py
%{py3_sitescriptdir}/__pycache__/_version.*.pyc
# from validate import VdtMissingValue
%{py3_sitescriptdir}/validate.py
%{py3_sitescriptdir}/__pycache__/validate.*.pyc
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
