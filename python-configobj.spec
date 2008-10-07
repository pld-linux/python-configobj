Summary:	Reading and writing config files
Summary(pl.UTF-8):	Odczyt i zapis plików konfiguracyjnych
Name:		python-configobj
Version:	4.5.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/configobj/configobj-%{version}.zip
# Source0-md5:	abd4eec2ff08bea466018bccdcf91aab
URL:		http://www.voidspace.org.uk/python/configobj.html
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reading and writing config files.

%description -l pl.UTF-8
Odczyt i zapis plików konfiguracyjnych.

%prep
%setup -q -n configobj-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*
