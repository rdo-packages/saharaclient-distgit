%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:             python-saharaclient
Version:          0.13.0
Release:          1%{?dist}
Provides:         python-savannaclient = %{version}-%{release}
Obsoletes:        python-savannaclient <= 0.5.0-2
Summary:          Client library for OpenStack Sahara API
License:          ASL 2.0
URL:              https://launchpad.net/sahara
Source0:          http://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{version}%{?milestone}.tar.gz

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
%setup -q -n %{name}-%{upstream_version}

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
%license LICENSE
%doc ChangeLog README.rst
%{_bindir}/sahara
%{python2_sitelib}/saharaclient
%{python2_sitelib}/*.egg-info


%changelog
* Wed Mar 23 2016 RDO <rdo-list@redhat.com> 0.13.0-0.1
-  Rebuild for Mitaka 
