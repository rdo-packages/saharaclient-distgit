%global sname saharaclient


%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:             python-saharaclient
Version:          3.2.1
Release:          1%{?dist}
Summary:          Client library for OpenStack Sahara API
License:          ASL 2.0
URL:              https://launchpad.net/sahara
Source0:          https://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{upstream_version}.tar.gz

BuildArch:        noarch

%description
Python client library for interacting with OpenStack Sahara API.

%package -n python3-%{sname}
Summary:	Client library for OpenStack Sahara API
BuildRequires:    openstack-macros
BuildRequires:    python3-setuptools
BuildRequires:    python3-devel
BuildRequires:    python3-mock >= 2.0.0
BuildRequires:    python3-osc-lib >= 1.11.0
BuildRequires:    python3-osc-lib-tests >= 1.11.0
BuildRequires:    python3-oslotest >= 3.2.0
BuildRequires:    python3-oslo-log >= 3.36.0
BuildRequires:    python3-oslo-serialization >= 2.18.0
BuildRequires:    python3-pbr >= 2.0.0
BuildRequires:    python3-requests-mock >= 1.2.0
BuildRequires:    python3-stestr >= 1.0.0

Requires:         python3-keystoneauth1 >= 3.4.0
Requires:         python3-openstackclient >= 5.2.0
Requires:         python3-osc-lib >= 2.0.0
Requires:         python3-oslo-i18n >= 3.15.3
Requires:         python3-oslo-log >= 3.36.0
Requires:         python3-oslo-serialization >= 2.18.0
Requires:         python3-oslo-utils >= 3.33.0
Requires:         python3-pbr >= 2.0.0
Requires:         python3-requests >= 2.14.2
Requires:         python3-six >= 1.10.0

%{?python_provide:%python_provide python3-%{sname}}

%description -n python3-%{sname}
Python client library for interacting with OpenStack Sahara API.

%prep
%setup -q -n %{name}-%{upstream_version}

rm -rf python_saharaclient.egg-info
%py_req_cleanup

%build
%{py3_build}


%install
%{py3_install}

%check
# Remove hacking tests, we don't need them
rm saharaclient/tests/unit/test_hacking.py
export PYTHON=%{__python3}
stestr-3 run

%files -n python3-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{python3_sitelib}/saharaclient
%{python3_sitelib}/*.egg-info

%changelog
* Mon Sep 21 2020 RDO <dev@lists.rdoproject.org> 3.2.1-1
- Update to 3.2.1

