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

%package -n python2-%{sname}
Summary:	Client library for OpenStack Sahara API
BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-d2to1
BuildRequires:    python-pbr >= 2.0.0
# test requirements
BuildRequires:    python-hacking
BuildRequires:    python-os-testr
BuildRequires:    python-oslotest
BuildRequires:    python-requests-mock
BuildRequires:    python-reno
BuildRequires:    python-openstackdocstheme
BuildRequires:    python-mock
BuildRequires:    python-sphinx
BuildRequires:    python-testrepository
BuildRequires:    python-oslo-serialization
BuildRequires:    python-oslo-log
BuildRequires:    python-osc-lib
BuildRequires:    python-osc-lib-tests
BuildRequires:    python-testtools

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
%{__python2} setup.py test

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
