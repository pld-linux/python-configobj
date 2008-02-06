Summary:	Reading and writing config files
Name:		python-configobj
Version:	4.5.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://www.voidspace.org.uk/cgi-bin/voidspace/downman.py?file=configobj-%{version}.zip
# Source0-md5:	0cc7989083b6030843f6600ca512bc9e
URL:		http://www.voidspace.org.uk/python/configobj.html
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reading and writing config files.

%prep
%setup -q -n configobj-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
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
