%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname saharaclient
%if 0%{?fedora}
%global with_python3 1
%endif

Name:             python-saharaclient
Version:          0.14.0
Release:          2%{?dist}
Summary:          Client library for OpenStack Sahara API
License:          ASL 2.0
URL:              https://launchpad.net/sahara
Source0:          http://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{upstream_version}.tar.gz

BuildArch:        noarch

%description
Python client library for interacting with OpenStack Sahara API.

%package -n python2-%{sname}
Summary:	Client library for OpenStack Sahara API
BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-d2to1
BuildRequires:    python-pbr >= 1.6

Requires:         python-babel >= 1.3
Requires:         python-cliff
Requires:         python2-iso8601
Requires:         python-keystoneauth1 >= 2.1.0
Requires:         python-keystoneclient
Requires:         python-oslo-i18n
Requires:         python-oslo-log
Requires:         python-oslo-serialization >= 1.10.0
Requires:         python-oslo-utils
Requires:         python-netaddr >= 0.7.12
Requires:         python-pbr
Requires:         python-prettytable
Requires:         python-requests >= 2.5.2
Requires:         python-six >= 1.9.0


%{?python_provide:%python_provide python2-%{sname}}

%description -n python2-%{sname}
Python client library for interacting with OpenStack Sahara API.

%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:	Client library for OpenStack Sahara API
BuildRequires:    python3-setuptools
BuildRequires:    python3-devel
BuildRequires:    python3-d2to1
BuildRequires:    python3-pbr >= 1.6

Requires:         python3-babel >= 1.3
Requires:         python3-cliff
Requires:         python3-iso8601
Requires:         python3-keystoneauth1 >= 2.1.0
Requires:         python3-keystoneclient
Requires:         python3-oslo-i18n
Requires:         python3-oslo-log
Requires:         python3-oslo-serialization >= 1.10.0
Requires:         python3-oslo-utils
Requires:         python3-netaddr >= 0.7.12
Requires:         python3-pbr
Requires:         python3-prettytable
Requires:         python3-requests >= 2.5.2
Requires:         python3-six >= 1.9.0

%{?python_provide:%python_provide python3-%{sname}}

%description -n python3-%{sname}
Python client library for interacting with OpenStack Sahara API.
%endif


%prep
%setup -q -n %{name}-%{upstream_version}

rm -rf python_saharaclient.egg-info
rm -rf {,test-}requirements.txt


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/sahara %{buildroot}%{_bindir}/sahara-%{python3_version}
ln -s ./sahara-%{python3_version} %{buildroot}%{_bindir}/sahara-3
%endif

%py2_install
mv %{buildroot}%{_bindir}/sahara %{buildroot}%{_bindir}/sahara-%{python2_version}
ln -s ./sahara-%{python2_version} %{buildroot}%{_bindir}/sahara-2

ln -s ./sahara-2 %{buildroot}%{_bindir}/sahara

%check
# Building on koji with virtualenv requires test-requirements.txt and this
# causes errors when trying to resolve the package names, also turning on pep8
# results in odd exceptions from flake8.
# TODO mimccune fix up unittests
# sh run_tests.sh --no-virtual-env --no-pep8

%files -n python2-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{_bindir}/sahara
%{_bindir}/sahara-2
%{_bindir}/sahara-%{python2_version}
%{python2_sitelib}/saharaclient
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{_bindir}/sahara-3
%{_bindir}/sahara-%{python3_version}
%{python3_sitelib}/saharaclient
%{python3_sitelib}/*.egg-info
%endif


%changelog
* Thu Jun 23 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.14.0-2
- Conditionalize python3 on Fedora only
- Update requirements

* Tue May 31 2016 Charalampos Stratakis <cstratak@redhat.com> 0.14.0-1
- Update to 0.14.0
- Modernize SPEC file
- Provide Python 3 subpackage

* Wed Mar 23 2016 RDO <rdo-list@redhat.com> 0.13.0-0.1
-  Rebuild for Mitaka 
