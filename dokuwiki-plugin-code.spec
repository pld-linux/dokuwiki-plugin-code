%define		plugin		code
Summary:	DokuWiki plugin: Syntax highlighting with optional line numbers
Name:		dokuwiki-plugin-%{plugin}
Version:	20080722
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dev.mwat.de/dw/syntax_plugin_code.zip
# Source0-md5:	79c8f4333dd9627f468062ce5309e06f
Patch0:		%{name}-geshi.patch
URL:		http://www.dokuwiki.org/plugin:code2
BuildRequires:	unzip
Requires:	dokuwiki >= 20050713
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir	/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
DokuWiki pluging that extends hiliting of code fragments by adding
caption/footer and line numbers support.

%prep
%setup -q -n %{plugin}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/img
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/*.xml
