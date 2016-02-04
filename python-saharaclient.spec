Name:             python-saharaclient
Version:          0.11.1
Release:          3%{?dist}
Provides:         python-savannaclient = %{version}-%{release}
Obsoletes:        python-savannaclient <= 0.5.0-2
Summary:          Client library for OpenStack Sahara API
License:          ASL 2.0
URL:              https://launchpad.net/sahara
Source0:          http://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-d2to1
BuildRequires:    python-pbr >= 1.6


Requires:         python-babel >= 1.3
Requires:         python-cliff
Requires:         python-iso8601
Requires:         python-keystoneclient
Requires:         python-oslo-i18n
Requires:         python-oslo-log
Requires:         python-oslo-utils
Requires:         python-netaddr >= 0.7.12
Requires:         python-pbr
Requires:         python-prettytable
Requires:         python-requests >= 2.5.2
Requires:         python-six >= 1.9.0


%description
Python client library for interacting with OpenStack Sahara API.


%prep
%setup -q -n %{name}-%{version}

rm -rf python_saharaclient.egg-info
rm -rf {,test-}requirements.txt


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%check
# Building on koji with virtualenv requires test-requirements.txt and this
# causes errors when trying to resolve the package names, also turning on pep8
# results in odd exceptions from flake8.
# TODO mimccune fix up unittests
# sh run_tests.sh --no-virtual-env --no-pep8

%files
%doc LICENSE ChangeLog README.rst
%{_bindir}/sahara
%{python2_sitelib}/saharaclient
%{python2_sitelib}/*.egg-info


%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.11.1-2
- Add missing runtime dep on python-oslo-log

* Wed Sep 30 2015 Haikel Guemar <hguemar@fedoraproject.org> 0.11.1-1
- Update to upstream 0.11.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 02 2015 Ethan Gafford <egafford@redhat.com> 0.8.0-2
- Fixing dependency on python-oslo-i18n

* Wed Apr 01 2015 Ethan Gafford <egafford@redhat.com> 0.8.0-1
- Update to upstream 0.8.0

* Tue Dec 02 2014 Jakub Ruzicka <jruzicka@redhat.com> 0.7.6-1
- Update to upstream 0.7.6

* Wed Oct 08 2014 Michael McCune <mimccune@redhat.com> 0.7.4-1
- Update to upstream 0.7.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Michael McCune <mimccune@redhat> - 0.7.0-3
- Changing the version/release temp for patch

* Mon May 05 2014 Michael McCune <mimccune@redhat> - 0.7.0-2
- Adding patch to remove runtime pbr dep

* Thu Apr  3 2014 Michael McCune <mimccune@redhat> - 0.7.0-1
- 0.7.0 release and rename from python-savannaclient

* Sat Mar  1 2014 Matthew Farrellee <matt@redhat> - 0.5.0-1
- 0.5.0 release

* Fri Jan 17 2014 Matthew Farrellee <matt@redhat> - 0.4.1-1
- 0.4.1 release - introduced Savanna CLI

* Sun Oct 20 2013 Matthew Farrellee <matt@redhat> - 0.3-1
- 0.3 release

* Fri Oct 11 2013 Matthew Farrellee <matt@redhat> - 0.3-0.2
- 0.3 rc3 build

* Sat Aug 17 2013 Matthew Farrellee <matt@redhat> - 0.3-0.1.f816386git
- Initial package
