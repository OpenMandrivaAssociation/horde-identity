%define prj    Horde_Identity

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-identity
Version:       0.0.2
Release:       %mkrel 3
Summary:       Horde Identity API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-auth
Requires:      horde-framework
Requires:      horde-prefs
Requires:      horde-util
Requires:      php-pear
Requires:      php-gettext
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
The Identity:: class provides an interface to all identities a user might have.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%{peardir}/Horde/Identity.php



%changelog
* Mon Jul 26 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2011.0
+ Revision: 560597
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 524849
- increased rel version to 2

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 509400
- removed BuildRequires; horde-framework
  replaced PreReq with Requires(pre)
- import horde-identity


* Tue Mar  3 2009 Richard Bos <rbos@opensuse.org> - 0.0.2
- Change dependency to horde-framework from just horde
* Tue Dec 23 2008 Richard Bos <rbos@opensuse.org> - 0.0.2
- Changed the pear install command, use package.xml instead of the tarbal
* Wed Nov 26 2008 Richard Bos <rbos@opensuse.org> - 0.0.2
- initial version
