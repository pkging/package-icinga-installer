Name:       icinga-installer
Version:    3.0.0
Release:    1%{?dist}
Summary:    OpenVox-based installer for Icinga
Group:      Applications/System
License:    ASL 2.0
URL:        https://github.com/lbetz/icinga-installer
Source0:    https://github.com/lbetz/icinga-installer/archive/refs/tags/v%{version}.tar.gz

BuildArch:  noarch

Requires:   curl
Requires:   openvox-agent >= 8
Requires:   openvox-agent < 9
Requires:   openvox-agent-kafo >= 7.5.0
Requires:   openvox-agent-kafo < 8

BuildRequires: openvox-agent >= 7.9.0
BuildRequires: openvox-agent < 9
BuildRequires: openbolt >= 4
BuildRequires: openvox-agent-kafo >= 7.5.0
BuildRequires: openvox-agent-kafo < 8
BuildRequires: openvox-agent-openvox-strings >= 7
BuildRequires: openvox-agent-openvox-strings < 8
BuildRequires: git

%description
Complete installer for Icinga software stack based on Puppet.

%prep
%setup -q -n %{name}-%{version}%{?prerelease:-}%{?prerelease}

%build
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export RUBYOPT="-KU -E utf-8:utf-8"
export PATH=/opt/puppetlabs/puppet/bin:$PATH:/opt/puppetlabs/bolt/bin

rake build \
  BUILDDIR=_build \
  LOCALSTATEDIR=%{_localstatedir} \
  PREFIX=%{_prefix} \
  SBINDIR=%{_sbindir} \
  SYSCONFDIR=%{_sysconfdir} \
  --trace

%install
export PATH=/opt/puppetlabs/puppet/bin:$PATH
rake install \
  BUILDDIR=_build \
  PREFIX=%{buildroot}%{_prefix} \
  LOCALSTATEDIR=%{buildroot}%{_localstatedir} \
  SBINDIR=%{buildroot}%{_sbindir} \
  SYSCONFDIR=%{buildroot}%{_sysconfdir} \
  --trace

%files
%defattr(-,root,root,-)
%doc README.*
%license LICENSE
%dir %{_sysconfdir}/%{name}
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/custom-hiera.yaml
%dir %{_sysconfdir}/%{name}/scenarios.d
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/server-db-mysql.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/server-db-mysql-answers.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/server-db-pgsql.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/server-db-pgsql-answers.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/worker.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/worker-answers.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/agent.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/agent-answers.yaml
%{_sbindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Oct 25 2026 Lennart Betz <lbetz@prefork.de> 3.0.0-1
- Drop IDO support
- Use OpenVox 8, Drop Puppet support
- Add Ubuntu 26.04 support
- Drop Debian 11 support
- Add complete SELinux support
- Update Puppet modules

* Sat Aug 31 2024 Lennart Betz <lennart.betz@netways.de> 2.0.0-1
- Use Ruby of Puppet AIO package
- Add Puppet 8 support
- Drop EOL EL7 support
- Drop Puppet 6 support
- Add SELinux support for Icinga 2 (Agent, Worker)
- Update Puppet modules

* Sat Aug 17 2024 Lennart Betz <lennart.betz@netways.de> 1.3.2-1
- Replace Icinga Web 2 module packages

* Tue Jul 02 2024 Lennart Betz <lennart.betz@netways.de> 1.3.1-1
- Fix missing logdir in icingadb-redis-7.0.15-1 package

* Fri Jun 21 2024 Lennart Betz <lennart.betz@netways.de> 1.3.0-2
- Fix private key permission for tls files

* Fri Feb 16 2024 Lennart Betz <lennart.betz@netways.de> 1.3.0-1
- Add support for Debian bookworm#74

* Fri Jan 05 2024 Lennart Betz <lennart.betz@netways.de> 1.2.8-1
- Redis password isn't set in Icinga2 feature #84

* Tue Nov 21 2023 Lennart Betz <lennart.betz@netways.de> 1.2.7-1
- Add missing general monitoring settings #82
- Port for director db connection is not passed #80

* Wed Oct 04 2023 Lennart Betz <lennart.betz@netways.de> 1.2.6-1
- Some fixes to install only icingaweb2 with icingadb module #79

* Fri May 12 2023 Lennart Betz <lennart.betz@netways.de> 1.2.4-1
- Bugfix Release 1.2.4

* Wed Apr 19 2023 Lennart Betz <lennart.betz@netways.de> 1.2.3-1
- Bugfix Release 1.2.3

* Sat Apr 15 2023 Lennart Betz <lennart.betz@netways.de> 1.2.2-1
- Bugfix Release 1.2.2

* Mon Apr 03 2023 Lennart Betz <lennart.betz@netways.de> 1.2.1-1
- Bugfix Release 1.2.1

* Sat Mar 11 2023 Lennart Betz <lennart.betz@netways.de> 1.2.0-1
- Release 1.2.0
- Support PdfExport module for Icinga Web 2
- Prevent overwriting Icinga Web 2 roles by rerun the Installer
- Support additional resources, user and group backends
- Support additional Apache vhost configs

* Mon Mar 06 2023 Lennart Betz <lennart.betz@netways.de> 1.1.0-1
- Release 1.1.0
- Support Reporting

* Sat Feb 11 2023 Lennart Betz <lennart.betz@netways.de> 1.0.0-1
- Release 1.0.0
- Support IcingaDB

* Mon Aug 01 2022 Lennart Betz <lennart.betz@netways.de> 0.7.1-1
- Release 0.7.1

* Tue Jul 26 2022 Lennart Betz <lennart.betz@netways.de> 0.7.0-1
- Release 0.7.0
- Update puppet module
- Add Alma and Rocky Linux support
- Set a randomize initial icingaadmin password

* Wed Jun 08 2022 Lennart Betz <lennart.betz@netways.de> 0.6.3-1
- Bugfix Release 0.6.3
- update icinga-icinga2 puppet module to v3.3.1

* Tue May 31 2022 Lennart Betz <lennart.betz@netways.de> 0.6.2-1
- Bugfix Release 0.6.2

* Fri Jan 28 2022 Lennart Betz <lennart.betz@netways.de> 0.6.1-1
- Bugfix Release 0.6.1

* Fri Jan 14 2022 Lennart Betz <lennart.betz@netways.de> 0.6.0-1
- Release 0.6.0
- Drop Puppet 5 support, but add support for Puppet 7

* Mon Nov 08 2021 Lennart Betz <lennart.betz@netways.de> 0.5.0-2
- Security impact: remove world read permission from custom-hiera.yaml

* Mon Nov 08 2021 Lennart Betz <lennart.betz@netways.de> 0.5.0-1
- Release 0.5.0

* Fri Sep 03 2021 Lennart Betz <lennart.betz@netways.de> 0.4.5-1
- Release 0.4.5
- Fix puppet 5 problems with PostgreSQL databases

* Tue Aug 17 2021 Lennart Betz <lennart.betz@netways.de> 0.4.3-1
- Release 0.4.3
- Fix puppet 5 problems

* Fri Jul 16 2021 Lennart Betz <lennart.betz@netways.de> 0.4.2-1
- Release 0.4.2
- Rename scenario server-pgsql to server-ido-pgsql

* Mon Jun 21 2021 Lennart Betz <lennart.betz@netways.de> 0.4.1-1
- Release 0.4.1

* Fri Jun 18 2021 Lennart Betz <lennart.betz@netways.de> 0.4.0-1
- Release 0.4.0

* Mon Mar 15 2021 Lennart Betz <lennart.betz@netways.de> 0.3.0-1
- Release 0.3.0
- New scenario server-pgsql
- Puppet Agent >= 5.5.10 < 7

* Sat Mar 06 2021 Lennart Betz <lennart.betz@netways.de> 0.2.1-3
- fix missing parent_zone for agent

* Fri Mar 05 2021 Lennart Betz <lennart.betz@netways.de> 0.2.1-2
- fix missing parent_zone in puppet-icinga-installer

* Thu Mar 04 2021 Lennart Betz <lennart.betz@netways.de> 0.2.1-1
- Release 0.2.1 

* Thu Mar 04 2021 Lennart Betz <lennart.betz@netways.de> 0.2.0-1
- Release 0.2.0

* Fri Feb 26 2021 Lennart Betz <lennart.betz@netways.de> 0.1.3-1
- Release 0.1.3

* Fri Feb 12 2021 Lennart Betz <lennart.betz@netways.de> 0.1.1-1
- Release 0.1.1

* Wed Feb 10 2021 Lennart Betz <lennart.betz@netways.de> 0.1.0-1
- Initial setup
