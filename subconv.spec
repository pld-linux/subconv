Summary:	Subtitle formats converter
Name:		subconv
Version:	0.2.2
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://linux.bydg.org/~yogin/%{name}-%{version}.tar.gz
# Source0-md5:	e6c8ad11b6e4c8dd21a823c68b65ef42
Patch0:		%{name}-pld.patch
URL:		http://linux.bydg.org/~yogin
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subtitle formats converter.

%prep
%setup -q -n %{name}
%patch0 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT

install -D subconv $RPM_BUILD_ROOT%{_bindir}/subconv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
