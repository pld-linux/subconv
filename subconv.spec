Summary:	Subtitle formats converter
Name:		subconv
Version:	0.3
Release:	2
License:	GPL
Group:		Applications/System
Source0:	%{name}.py
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
