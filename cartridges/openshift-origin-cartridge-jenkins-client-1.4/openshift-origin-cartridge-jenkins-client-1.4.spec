%global cartridgedir %{_libexecdir}/openshift/cartridges/embedded/jenkins-client-1.4
%global frameworkdir %{_libexecdir}/openshift/cartridges/jenkins-client-1.4

Name: openshift-origin-cartridge-jenkins-client-1.4
Version: 1.1.1
Release: 1%{?dist}
Summary: Embedded jenkins client support for express 
Group: Network/Daemons
License: ASL 2.0
URL: https://openshift.redhat.com
Source0: http://mirror.openshift.com/pub/origin-server/source/%{name}/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Requires: openshift-origin-cartridge-abstract
Requires: rubygem(openshift-origin-node)
Requires: mysql-devel
Requires: wget
Requires: java-1.6.0-openjdk
Requires: rubygems
Requires: rubygem-json
Obsoletes: cartridge-jenkins-client-1.4

%description
Provides embedded jenkins client support


%prep
%setup -q


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
mkdir -p %{buildroot}/%{_sysconfdir}/openshift/cartridges
cp LICENSE %{buildroot}%{cartridgedir}/
cp COPYRIGHT %{buildroot}%{cartridgedir}/
cp -r info %{buildroot}%{cartridgedir}/
ln -s %{cartridgedir}/info/configuration/ %{buildroot}/%{_sysconfdir}/openshift/cartridges/%{name}
ln -s %{cartridgedir} %{buildroot}/%{frameworkdir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%attr(0750,-,-) %{cartridgedir}/info/hooks/
%attr(0750,-,-) %{cartridgedir}/info/build/
%config(noreplace) %{cartridgedir}/info/configuration/
%attr(0755,-,-) %{cartridgedir}/info/bin/
%attr(0755,-,-) %{frameworkdir}
%{_sysconfdir}/openshift/cartridges/%{name}
%{cartridgedir}/info/changelog
%{cartridgedir}/info/control
%{cartridgedir}/info/manifest.yml
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
* Thu Nov 08 2012 Adam Miller <admiller@redhat.com> 1.1.1-1
- Bumping specs to at least 1.1 (dmcphers@redhat.com)

* Tue Oct 30 2012 Adam Miller <admiller@redhat.com> 1.0.1-1
- bumping specs to at least 1.0.0 (dmcphers@redhat.com)

* Mon Oct 08 2012 Dan McPherson <dmcphers@redhat.com> 0.33.6-1
- renaming crankcase -> origin-server (dmcphers@redhat.com)

* Fri Oct 05 2012 Krishna Raman <kraman@gmail.com> 0.33.5-1
- new package built with tito

* Thu Oct 04 2012 Adam Miller <admiller@redhat.com> 0.33.4-1
- Typeless gear changes (mpatel@redhat.com)

* Mon Sep 24 2012 Adam Miller <admiller@redhat.com> 0.33.3-1
- Merge pull request #514 from pmorie/bz846971 (dmcphers@redhat.com)
- Downcase url of jenkins for curl POSTs (pmorie@gmail.com)

* Thu Sep 20 2012 Adam Miller <admiller@redhat.com> 0.33.2-1
- Bug 849950 - web_framework does not belong on jenkins client
  (ccoleman@redhat.com)

* Wed Sep 12 2012 Adam Miller <admiller@redhat.com> 0.33.1-1
- bump_minor_versions for sprint 18 (admiller@redhat.com)

* Wed Sep 12 2012 Adam Miller <admiller@redhat.com> 0.32.3-1
- Delete associated job upon jenkins-client removal. (pmorie@gmail.com)

* Fri Sep 07 2012 Adam Miller <admiller@redhat.com> 0.32.2-1
- Merge pull request #450 from smarterclayton/switch_to_newer_broker_tags
  (openshift+bot@redhat.com)
- Return display_name, description fields in RestCartridge model
  (rpenta@redhat.com)
- Use the agreed on newer broker tags for jenkins and jenkins-client
  (ccoleman@redhat.com)

* Wed Aug 22 2012 Adam Miller <admiller@redhat.com> 0.32.1-1
- bump_minor_versions for sprint 17 (admiller@redhat.com)

* Mon Aug 20 2012 Adam Miller <admiller@redhat.com> 0.31.5-1
- BZ848661 (bdecoste@gmail.com)

* Fri Aug 17 2012 Adam Miller <admiller@redhat.com> 0.31.4-1
- Removed bad newline (jhonce@redhat.com)

* Thu Aug 16 2012 Adam Miller <admiller@redhat.com> 0.31.3-1
- Patch for fix for BZ823720 (jhonce@redhat.com)

* Wed Aug 15 2012 Adam Miller <admiller@redhat.com> 0.31.2-1
- Runtime test Refactor (jhonce@redhat.com)
- Wait for jenkins server to become stable (jhonce@redhat.com)

* Thu Aug 02 2012 Adam Miller <admiller@redhat.com> 0.31.1-1
- bump_minor_versions for sprint 16 (admiller@redhat.com)

* Tue Jul 24 2012 Adam Miller <admiller@redhat.com> 0.30.3-1
- Add pre and post destroy calls on gear destruction and move unobfuscate and
  openshift-origin-proxy out of cartridge hooks and into node. (rmillner@redhat.com)

* Thu Jul 19 2012 Adam Miller <admiller@redhat.com> 0.30.2-1
- Refactor JBoss hot deployment support (ironcladlou@gmail.com)

* Wed Jul 11 2012 Adam Miller <admiller@redhat.com> 0.30.1-1
- bump_minor_versions for sprint 15 (admiller@redhat.com)

* Thu Jul 05 2012 Adam Miller <admiller@redhat.com> 0.29.2-1
- more cartridges have better metadata (rchopra@redhat.com)
- cart metadata work merged; depends service added; cartridges enhanced; unit
  tests updated (rchopra@redhat.com)

* Wed Jun 20 2012 Adam Miller <admiller@redhat.com> 0.29.1-1
- bump_minor_versions for sprint 14 (admiller@redhat.com)

* Thu Jun 14 2012 Adam Miller <admiller@redhat.com> 0.28.2-1
- Fix for bug 812046 (abhgupta@redhat.com)

* Fri Jun 01 2012 Adam Miller <admiller@redhat.com> 0.28.1-1
- bumping spec versions (admiller@redhat.com)

* Tue May 22 2012 Dan McPherson <dmcphers@redhat.com> 0.27.2-1
- Merge branch 'master' into US2109 (jhonce@redhat.com)
- Merge branch 'master' into US2109 (ramr@redhat.com)
- Merge branch 'master' into US2109 (ramr@redhat.com)
- Typeless gears - create app/ dir, rollback logs, manage repo, data and state.
  (ramr@redhat.com)

* Thu May 10 2012 Adam Miller <admiller@redhat.com> 0.27.1-1
- bumping spec versions (admiller@redhat.com)

* Mon May 07 2012 Adam Miller <admiller@redhat.com> 0.26.2-1
- remove old obsoletes (dmcphers@redhat.com)
- clean specs (whearn@redhat.com)

* Thu Apr 26 2012 Adam Miller <admiller@redhat.com> 0.26.1-1
- bumping spec versions (admiller@redhat.com)

* Mon Apr 23 2012 Adam Miller <admiller@redhat.com> 0.25.5-1
- cleaning up spec files (dmcphers@redhat.com)

* Sat Apr 21 2012 Dan McPherson <dmcphers@redhat.com> 0.25.4-1
- new package built with tito
