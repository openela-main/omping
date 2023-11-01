Name: omping
Version: 0.0.4
Release: 18%{?dist}
Summary: Utility to test IP multicast functionality
License: ISC
URL: https://github.com/jfriesse/omping
Source0: https://github.com/jfriesse/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc

%description
Omping (Open Multicast Ping) is tool to test IP multicast functionality
primarily in local network.

%prep
%setup -q

%build
%set_build_flags
make %{?_smp_mflags}

%install
make DESTDIR="%{buildroot}" PREFIX="%{_prefix}" install

%files
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/*

%changelog
* Tue Apr 28 2020 Jan Friesse <jfriesse@redhat.com> - 0.0.4-18
- Resolves: rhbz#1828305

- Add explicit omping dependency for revdeps CI test

* Mon May 13 2019 Jan Friesse <jfriesse@redhat.com> - 0.0.4-17
- Related rhbz#1682115

- Add gating tests

* Wed Mar 20 2019 Jan Friesse <jfriesse@redhat.com> - 0.0.4-16
- Use license and set_build_flags macro
- Fix URL and source

- Related rhbz#1682115

* Tue Jul 10 2018 Jan Friesse <jfriesse@redhat.com> - 0.0.4-15
- Modernize spec file a bit
- Fix spec file changelog dates
- Add gcc build requirement

- Related rhbz#1682115

* Mon Jul  9 2018 Florian Weimer <fweimer@redhat.com> - 0.0.4-14
- Use LDFLAGS from redhat-rpm-config

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Jan Friesse <jfriesse@redhat.com> - 0.0.4-1
- Update to version 0.0.4

* Mon May 02 2011 Jan Friesse <jfriesse@redhat.com> - 0.0.3-1
- Update to version 0.0.3

* Thu Apr 14 2011 Jan Friesse <jfriesse@redhat.com> - 0.0.2-3
- Resolves rhbz#696509

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Jan Friesse <jfriesse@redhat.com> - 0.0.2-1
- Update to upstream release 0.0.2

* Tue Nov 30 2010 Jan Friesse <jfriesse@redhat.com> - 0.0.1-3
- Display error if only one host is specified

* Wed Nov 24 2010 Jan Friesse <jfriesse@redhat.com> - 0.0.1-2
- Change hard coded prefix path to macro

* Fri Nov 19 2010 Jan Friesse <jfriesse@redhat.com> - 0.0.1-1
- Initial package for Fedora
