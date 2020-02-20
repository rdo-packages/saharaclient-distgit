%global sname saharaclient

# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:             python-saharaclient
Version:          2.3.0
Release:          1%{?dist}
Summary:          Client library for OpenStack Sahara API
License:          ASL 2.0
URL:              https://launchpad.net/sahara
Source0:          https://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{upstream_version}.tar.gz

BuildArch:        noarch

%description
Python client library for interacting with OpenStack Sahara API.

%package -n python%{pyver}-%{sname}
Summary:	Client library for OpenStack Sahara API
BuildRequires:    openstack-macros
BuildRequires:    python%{pyver}-setuptools
BuildRequires:    python%{pyver}-devel
BuildRequires:    python%{pyver}-mock >= 2.0.0
BuildRequires:    python%{pyver}-osc-lib >= 1.11.0
BuildRequires:    python%{pyver}-osc-lib-tests >= 1.11.0
BuildRequires:    python%{pyver}-oslotest >= 3.2.0
BuildRequires:    python%{pyver}-oslo-log >= 3.36.0
BuildRequires:    python%{pyver}-oslo-serialization >= 2.18.0
BuildRequires:    python%{pyver}-pbr >= 2.0.0
%if %{pyver} == 2
BuildRequires:    python-requests-mock >= 1.2.0
%else
BuildRequires:    python%{pyver}-requests-mock >= 1.2.0
%endif
BuildRequires:    python%{pyver}-stestr >= 1.0.0

Requires:         python%{pyver}-babel >= 2.3.4
Requires:         python%{pyver}-keystoneauth1 >= 3.4.0
Requires:         python%{pyver}-openstackclient >= 3.12.0
Requires:         python%{pyver}-osc-lib >= 1.11.0
Requires:         python%{pyver}-oslo-i18n >= 3.15.3
Requires:         python%{pyver}-oslo-log >= 3.36.0
Requires:         python%{pyver}-oslo-serialization >= 2.18.0
Requires:         python%{pyver}-oslo-utils >= 3.33.0
Requires:         python%{pyver}-pbr >= 2.0.0
Requires:         python%{pyver}-requests >= 2.14.2
Requires:         python%{pyver}-six >= 1.10.0

%{?python_provide:%python_provide python%{pyver}-%{sname}}

%description -n python%{pyver}-%{sname}
Python client library for interacting with OpenStack Sahara API.

%prep
%setup -q -n %{name}-%{upstream_version}

rm -rf python_saharaclient.egg-info
%py_req_cleanup

%build
%{pyver_build}


%install
%{pyver_install}

%check
# Remove hacking tests, we don't need them
rm saharaclient/tests/unit/test_hacking.py
export PYTHON=%{pyver_bin}
stestr-%{pyver} run

%files -n python%{pyver}-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{pyver_sitelib}/saharaclient
%{pyver_sitelib}/*.egg-info

%changelog
* Fri Sep 20 2019 RDO <dev@lists.rdoproject.org> 2.3.0-1
- Update to 2.3.0

