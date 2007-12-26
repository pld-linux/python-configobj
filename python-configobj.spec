Summary:	Reading and writing config files
Name:		python-configobj
Version:	4.4.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/configobj/configobj-%{version}.zip
# Source0-md5:	9d222d8d583b9bdc5b5ecbae1be5177a
URL:		http://www.voidspace.org.uk/python/configobj.html
BuildRequires:	python-devel >= 1:2.3.0
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

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*
