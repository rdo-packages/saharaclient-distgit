%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x815AFEC729392386480E076DCC0DFE2D21C023C9
%global sname saharaclient


%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order sphinx openstackdocstheme

Name:             python-saharaclient
Version:          4.2.0
Release:          1%{?dist}
Summary:          Client library for OpenStack Sahara API
License:          Apache-2.0
URL:              https://launchpad.net/sahara
Source0:          https://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
# TODO(jcapitao): remove the condition below once
# https://review.opendev.org/c/openstack/python-saharaclient/+/894867 is merged and
# contained in a new tag.
%if %{lua:print(rpm.vercmp(rpm.expand("%{version}"), '4.2.0'));} >= 0
Patch0001:        0001-Remove-obsolete-whitelist_externals.patch
%endif

BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
Python client library for interacting with OpenStack Sahara API.

%package -n python3-%{sname}
Summary: Client library for OpenStack Sahara API

BuildRequires:    openstack-macros
BuildRequires:    python3-devel
BuildRequires:    pyproject-rpm-macros
# Required to run unit tests
BuildRequires:    python3-osc-lib-tests >= 1.11.0

%description -n python3-%{sname}
Python client library for interacting with OpenStack Sahara API.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version}

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel


%install
%pyproject_install

%check
# Remove hacking tests, we don't need them
rm saharaclient/tests/unit/test_hacking.py
%tox -e %{default_toxenv}

%files -n python3-%{sname}
%license LICENSE
%doc ChangeLog README.rst HACKING.rst
%{python3_sitelib}/saharaclient
%{python3_sitelib}/*.dist-info

%changelog
* Wed Sep 13 2023 RDO <dev@lists.rdoproject.org> 4.2.0-1
- Update to 4.2.0

