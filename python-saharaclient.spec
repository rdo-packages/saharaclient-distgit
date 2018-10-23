# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname saharaclient
%if 0%{?fedora}
%global with_python3 1
%endif

Name:             python-saharaclient
Version:          XXX
Release:          XXX
Summary:          Client library for OpenStack Sahara API
License:          ASL 2.0
URL:              https://launchpad.net/sahara
Source0:          https://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{upstream_version}.tar.gz

BuildArch:        noarch

%description
Python client library for interacting with OpenStack Sahara API.

%package -n python%{pyver}-%{sname}
Summary:	Client library for OpenStack Sahara API
BuildRequires:    python%{pyver}-setuptools
BuildRequires:    python%{pyver}-devel
BuildRequires:    python%{pyver}-pbr >= 2.0.0

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

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:    python-d2to1
%else
BuildRequires:    python%{pyver}-d2to1
%endif

%{?python_provide:%python_provide python%{pyver}-%{sname}}

%description -n python%{pyver}-%{sname}
Python client library for interacting with OpenStack Sahara API.

%prep
%setup -q -n %{name}-%{upstream_version}

rm -rf python_saharaclient.egg-info
rm -rf {,test-}requirements.txt

%build
%{pyver_build}


%install
%{pyver_install}

%check
# Building on koji with virtualenv requires test-requirements.txt and this
# causes errors when trying to resolve the package names, also turning on pep8
# results in odd exceptions from flake8.
# TODO mimccune fix up unittests
# sh run_tests.sh --no-virtual-env --no-pep8

%files -n python%{pyver}-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{pyver_sitelib}/saharaclient
%{pyver_sitelib}/*.egg-info

%changelog
