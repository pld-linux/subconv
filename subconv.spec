Summary:	Subtitle formats converter
Name:		subconv
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	%{name}.py
# Source0-md5:	e6c8ad11b6e4c8dd21a823c68b65ef42
URL:		http://cvs.pld-linux.org/cgi-bin/cvsweb.cgi/packages/subconv/
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subtitle formats converter.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -D %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/subconv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/subconv
