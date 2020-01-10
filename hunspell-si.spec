Name: hunspell-si
Summary: Sinhala hunspell dictionaries
Version: 0.2.1
Release: 8%{?dist}
Source: http://www.sandaru1.com/si-LK.tar.gz
Group: Applications/Text
#Following URL is down since few months informed to upstream
URL: http://www.sandaru1.com/2009/08/29/sinhala-spell-checker-for-firefox/
License: GPLv2+
BuildArch: noarch
Requires: hunspell

%description
Sinhala hunspell dictionaries.

%prep
%setup -q -c -n hunspell-si

%build
#nothing to build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/si-LK.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/si_LK.aff
cp -p dictionaries/si-LK.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/si_LK.dic

%files
%doc LICENSE README
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Parag Nemade <pnemade AT redhat.com> - 0.2.1-7
- Resolves:rh#879152 - spec cleanup for recent packaging guidelines 

* Thu Aug 23 2012 Parag Nemade <pnemade AT redhat.com> - 0.2.1-6
- Resolves:rh#848847:-Source URL not working

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 09 2010 Parag Nemade <pnemade AT redhat.com> - 0.2.1-2
- Resolves: rh#571710: Fix license tag in spec file with new upstream release
- Removed CREDITS file as upstream provides now README and LICENSE files.

* Wed Feb 24 2010 Parag Nemade <pnemade AT redhat.com> - 0.2.1-1
- Resolves: rh#567895: Fix license tag in spec file with new upstream release

* Wed Nov 25 2009 Caolan McNamara <caolanm@redhat.com> - 0.2-1
- initial version
