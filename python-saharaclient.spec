%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname saharaclient
%if 0%{?fedora}
%global with_python3 1
%endif

Name:             python-saharaclient
Version:          1.3.1
Release:          1%{?dist}
Summary:          Client library for OpenStack Sahara API
License:          ASL 2.0
URL:              https://launchpad.net/sahara
Source0:          https://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{upstream_version}.tar.gz

BuildArch:        noarch

%description
Python client library for interacting with OpenStack Sahara API.

%package -n python2-%{sname}
Summary:	Client library for OpenStack Sahara API
BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-d2to1
BuildRequires:    python-pbr >= 2.0.0

Requires:         python-babel >= 2.3.4
Requires:         python-keystoneauth1 >= 3.1.0
Requires:         python-openstackclient >= 3.3.0
Requires:         python-osc-lib >= 1.7.0
Requires:         python-oslo-i18n >= 2.1.0
Requires:         python-oslo-log >= 3.22.0
Requires:         python-oslo-serialization >= 1.10.0
Requires:         python-oslo-utils >= 3.20.0
Requires:         python-pbr
Requires:         python-requests >= 2.10.0
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
BuildRequires:    python3-pbr >= 2.0.0

Requires:         python3-babel >= 2.3.4
Requires:         python3-keystoneauth1 >= 3.1.0
Requires:         python3-openstackclient >= 3.3.0
Requires:         python3-osc-lib >= 1.7.0
Requires:         python3-oslo-i18n >= 2.1.0
Requires:         python3-oslo-log >= 3.22.0
Requires:         python3-oslo-serialization >= 1.10.0
Requires:         python3-oslo-utils >= 3.20.0
Requires:         python3-pbr
Requires:         python3-requests >= 2.10.0
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
%endif

%py2_install

%check
# Building on koji with virtualenv requires test-requirements.txt and this
# causes errors when trying to resolve the package names, also turning on pep8
# results in odd exceptions from flake8.
# TODO mimccune fix up unittests
# sh run_tests.sh --no-virtual-env --no-pep8

%files -n python2-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{python2_sitelib}/saharaclient
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{python3_sitelib}/saharaclient
%{python3_sitelib}/*.egg-info
%endif


%changelog
* Wed Mar 20 2019 RDO <dev@lists.rdoproject.org> 1.3.1-1
- Update to 1.3.1

* Mon Aug 21 2017 Alfredo Moralejo <amoralej@redhat.com> 1.3.0-1
- Update to 1.3.0

