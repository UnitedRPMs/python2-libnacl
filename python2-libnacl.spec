%global srcname libnacl
%global sum Python bindings for libsodium based on ctypes

Name:           python2-%{srcname}
Version:        1.6.1
Release:        7%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://libnacl.readthedocs.org/
Source0:        https://github.com/saltstack/libnacl/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2 python2-devel 
BuildRequires:  libsodium
Requires:       libsodium
%{?python_provide:%python_provide python2-%{srcname}}

%description

python-libnacl is used to gain direct access to the functions exposed by
Daniel J. Bernstein’s nacl library via libsodium. It has been constructed
to maintain extensive documentation on how to use nacl as well as being
completely portable.

%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf %{name}.egg-info

%build
%py2_build

%install
%py2_install

%check
%{__python2} setup.py test

%files 
%license LICENSE
%doc AUTHORS
%doc libnacl.egg-info/PKG-INFO
%doc README.rst
%{python2_sitelib}/*

%changelog

* Mon Feb 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.6.1-7
- Upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Sérgio Basto <sergio@serjux.com> - 1.6.1-1
- Update to 1.6.1

* Thu Oct 05 2017 Sérgio Basto <sergio@serjux.com> - 1.6.0-1
- Update python-libnacl to 1.6.0
- Fix FTBFS with new libsodium

* Mon Oct 02 2017 Remi Collet <remi@fedoraproject.org> - 1.5.2-3
- rebuild for libsodium

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2 (#1463028)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Jonny Heggheim <jonnyheggheim@sigaint.org> - 1.5.0-1
- inital package

