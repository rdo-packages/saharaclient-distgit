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

%package -n       python3-%{sname}-tests
Summary:          Tests for OpenStack Sahara API client library
Requires:         python3-%{sname} = %{version}-%{release}

BuildRequires:    python3-os-testr
BuildRequires:    python3-hacking
BuildRequires:    python3-oslotest
BuildRequires:    python3-requests-mock
BuildRequires:    python3-reno
BuildRequires:    python3-openstackdocstheme
BuildRequires:    python3-mock
BuildRequires:    python3-sphinx
BuildRequires:    python3-testrepository
BuildRequires:    python3-oslo-serialization
BuildRequires:    python3-oslo-log
BuildRequires:    python3-osc-lib
BuildRequires:    python3-osc-lib-tests
BuildRequires:    python3-testtools

Requires:    python3-os-testr
Requires:    python3-hacking
Requires:    python3-oslotest
Requires:    python3-requests-mock
Requires:    python3-reno
Requires:    python3-openstackdocstheme
Requires:    python3-mock
Requires:    python3-sphinx
Requires:    python3-testrepository
Requires:    python3-oslo-serialization
Requires:    python3-oslo-log
Requires:    python3-osc-lib
Requires:    python3-osc-lib-tests
Requires:    python3-testtools

%description -n python3-%{sname}-tests
Python client library for interacting with OpenStack Sahara API.

These are the unit tests for the OpenStack Sahara client library.
%endif

%package -n       python2-%{sname}-tests
Summary:          Tests for OpenStack Sahara API client library
Requires:         python2-%{sname} = %{version}-%{release}

BuildRequires:    python-os-testr
BuildRequires:    python-oslotest
BuildRequires:    python-hacking
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

Requires:    python-os-testr
Requires:    python-oslotest
Requires:    python-hacking
Requires:    python-requests-mock
Requires:    python-reno
Requires:    python-openstackdocstheme
Requires:    python-mock
Requires:    python-sphinx
Requires:    python-testrepository
Requires:    python-oslo-serialization
Requires:    python-oslo-log
Requires:    python-osc-lib
Requires:    python-osc-lib-tests
Requires:    python-testtools

%description -n python2-%{sname}-tests
Python client library for interacting with OpenStack Sahara API.

These are the unit tests for the OpenStack Sahara client library.


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
OS_TEST_PATH=./sahara/tests/unit ostestr -c 2

%files -n python2-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{python2_sitelib}/saharaclient
%exclude %{python2_sitelib}/%{sname}/tests
%{python2_sitelib}/*.egg-info

%files -n python2-%{sname}-tests
%license LICENSE
%{python2_sitelib}/%{sname}/tests

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{python3_sitelib}/saharaclient
%exclude %{python3_sitelib}/%{sname}/tests
%{python3_sitelib}/*.egg-info

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests
%endif


%changelog
