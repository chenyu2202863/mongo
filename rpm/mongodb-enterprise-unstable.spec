Name: mongodb-enterprise-unstable
Conflicts: mongo-10gen, mongo-10gen-enterprise, mongo-10gen-enterprise-server, mongo-10gen-server, mongo-10gen-unstable, mongo-10gen-unstable-enterprise, mongo-10gen-unstable-enterprise-mongos, mongo-10gen-unstable-enterprise-server, mongo-10gen-unstable-enterprise-shell, mongo-10gen-unstable-enterprise-tools, mongo-10gen-unstable-mongos, mongo-10gen-unstable-server, mongo-10gen-unstable-shell, mongo-10gen-unstable-tools, mongo18-10gen, mongo18-10gen-server, mongo20-10gen, mongo20-10gen-server, mongodb, mongodb-server, mongodb-dev, mongodb-clients, mongodb-10gen, mongodb-10gen-enterprise, mongodb-10gen-unstable, mongodb-10gen-unstable-enterprise, mongodb-10gen-unstable-enterprise-mongos, mongodb-10gen-unstable-enterprise-server, mongodb-10gen-unstable-enterprise-shell, mongodb-10gen-unstable-enterprise-tools, mongodb-10gen-unstable-mongos, mongodb-10gen-unstable-server, mongodb-10gen-unstable-shell, mongodb-10gen-unstable-tools, mongodb-enterprise, mongodb-enterprise-mongos, mongodb-enterprise-server, mongodb-enterprise-shell, mongodb-enterprise-tools, mongodb-nightly, mongodb-org, mongodb-org-mongos, mongodb-org-server, mongodb-org-shell, mongodb-org-tools, mongodb-stable, mongodb18-10gen, mongodb20-10gen, mongodb-org-unstable, mongodb-org-unstable-mongos, mongodb-org-unstable-server, mongodb-org-unstable-shell, mongodb-org-unstable-tools
Obsoletes: mongodb-enterprise-unstable,mongo-enterprise-unstable
Version: 2.5.2
Release: mongodb_1%{?dist}
Summary: MongoDB cross-platform document-oriented database system (enterprise metapackage)
License: AGPL 3.0
URL: http://www.mongodb.org
Group: Applications/Databases
Requires: mongodb-enterprise-unstable-server, mongodb-enterprise-unstable-shell, mongodb-enterprise-unstable-mongos, mongodb-enterprise-unstable-tools

Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
MongoDB (from "huMONGOus") is a schema-free document-oriented database.
It features dynamic profileable queries, full indexing, replication
and fail-over support, efficient storage of large binary data objects,
and auto-sharding.

This package provides the mongo shell, import/export tools, other
client utilities, server software, default configuration, and
init.d scripts.

%package server
Summary: MongoDB database server (enterprise)
Requires: cyrus-sasl, net-snmp-libs
Conflicts: mongo-10gen, mongo-10gen-enterprise, mongo-10gen-enterprise-server, mongo-10gen-server, mongo-10gen-unstable, mongo-10gen-unstable-enterprise, mongo-10gen-unstable-enterprise-mongos, mongo-10gen-unstable-enterprise-server, mongo-10gen-unstable-enterprise-shell, mongo-10gen-unstable-enterprise-tools, mongo-10gen-unstable-mongos, mongo-10gen-unstable-server, mongo-10gen-unstable-shell, mongo-10gen-unstable-tools, mongo18-10gen, mongo18-10gen-server, mongo20-10gen, mongo20-10gen-server, mongodb, mongodb-server, mongodb-dev, mongodb-clients, mongodb-10gen, mongodb-10gen-enterprise, mongodb-10gen-unstable, mongodb-10gen-unstable-enterprise, mongodb-10gen-unstable-enterprise-mongos, mongodb-10gen-unstable-enterprise-server, mongodb-10gen-unstable-enterprise-shell, mongodb-10gen-unstable-enterprise-tools, mongodb-10gen-unstable-mongos, mongodb-10gen-unstable-server, mongodb-10gen-unstable-shell, mongodb-10gen-unstable-tools, mongodb-enterprise, mongodb-enterprise-mongos, mongodb-enterprise-server, mongodb-enterprise-shell, mongodb-enterprise-tools, mongodb-nightly, mongodb-org, mongodb-org-mongos, mongodb-org-server, mongodb-org-shell, mongodb-org-tools, mongodb-stable, mongodb18-10gen, mongodb20-10gen, mongodb-org-unstable, mongodb-org-unstable-mongos, mongodb-org-unstable-server, mongodb-org-unstable-shell, mongodb-org-unstable-tools

%description server
MongoDB (from "huMONGOus") is a schema-free document-oriented database.

This package provides the mongo server software, default configuration
files, and init.d scripts.

%package shell
Summary: MongoDB shell client (enterprise)
Conflicts: mongo-10gen, mongo-10gen-enterprise, mongo-10gen-enterprise-server, mongo-10gen-server, mongo-10gen-unstable, mongo-10gen-unstable-enterprise, mongo-10gen-unstable-enterprise-mongos, mongo-10gen-unstable-enterprise-server, mongo-10gen-unstable-enterprise-shell, mongo-10gen-unstable-enterprise-tools, mongo-10gen-unstable-mongos, mongo-10gen-unstable-server, mongo-10gen-unstable-shell, mongo-10gen-unstable-tools, mongo18-10gen, mongo18-10gen-server, mongo20-10gen, mongo20-10gen-server, mongodb, mongodb-server, mongodb-dev, mongodb-clients, mongodb-10gen, mongodb-10gen-enterprise, mongodb-10gen-unstable, mongodb-10gen-unstable-enterprise, mongodb-10gen-unstable-enterprise-mongos, mongodb-10gen-unstable-enterprise-server, mongodb-10gen-unstable-enterprise-shell, mongodb-10gen-unstable-enterprise-tools, mongodb-10gen-unstable-mongos, mongodb-10gen-unstable-server, mongodb-10gen-unstable-shell, mongodb-10gen-unstable-tools, mongodb-enterprise, mongodb-enterprise-mongos, mongodb-enterprise-server, mongodb-enterprise-shell, mongodb-enterprise-tools, mongodb-nightly, mongodb-org, mongodb-org-mongos, mongodb-org-server, mongodb-org-shell, mongodb-org-tools, mongodb-stable, mongodb18-10gen, mongodb20-10gen, mongodb-org-unstable, mongodb-org-unstable-mongos, mongodb-org-unstable-server, mongodb-org-unstable-shell, mongodb-org-unstable-tools

%description shell
MongoDB (from "huMONGOus") is a schema-free document-oriented database.

This package provides the mongo shell

%package mongos
Summary: MongoDB sharding router (enterprise)
Conflicts: mongo-10gen, mongo-10gen-enterprise, mongo-10gen-enterprise-server, mongo-10gen-server, mongo-10gen-unstable, mongo-10gen-unstable-enterprise, mongo-10gen-unstable-enterprise-mongos, mongo-10gen-unstable-enterprise-server, mongo-10gen-unstable-enterprise-shell, mongo-10gen-unstable-enterprise-tools, mongo-10gen-unstable-mongos, mongo-10gen-unstable-server, mongo-10gen-unstable-shell, mongo-10gen-unstable-tools, mongo18-10gen, mongo18-10gen-server, mongo20-10gen, mongo20-10gen-server, mongodb, mongodb-server, mongodb-dev, mongodb-clients, mongodb-10gen, mongodb-10gen-enterprise, mongodb-10gen-unstable, mongodb-10gen-unstable-enterprise, mongodb-10gen-unstable-enterprise-mongos, mongodb-10gen-unstable-enterprise-server, mongodb-10gen-unstable-enterprise-shell, mongodb-10gen-unstable-enterprise-tools, mongodb-10gen-unstable-mongos, mongodb-10gen-unstable-server, mongodb-10gen-unstable-shell, mongodb-10gen-unstable-tools, mongodb-enterprise, mongodb-enterprise-mongos, mongodb-enterprise-server, mongodb-enterprise-shell, mongodb-enterprise-tools, mongodb-nightly, mongodb-org, mongodb-org-mongos, mongodb-org-server, mongodb-org-shell, mongodb-org-tools, mongodb-stable, mongodb18-10gen, mongodb20-10gen, mongodb-org-unstable, mongodb-org-unstable-mongos, mongodb-org-unstable-server, mongodb-org-unstable-shell, mongodb-org-unstable-tools

%description mongos
MongoDB (from "huMONGOus") is a schema-free document-oriented database.

This package provides mongos, the mongo sharding server

%package tools
Summary: MongoDB tools (enterprise)
Conflicts: mongo-10gen, mongo-10gen-enterprise, mongo-10gen-enterprise-server, mongo-10gen-server, mongo-10gen-unstable, mongo-10gen-unstable-enterprise, mongo-10gen-unstable-enterprise-mongos, mongo-10gen-unstable-enterprise-server, mongo-10gen-unstable-enterprise-shell, mongo-10gen-unstable-enterprise-tools, mongo-10gen-unstable-mongos, mongo-10gen-unstable-server, mongo-10gen-unstable-shell, mongo-10gen-unstable-tools, mongo18-10gen, mongo18-10gen-server, mongo20-10gen, mongo20-10gen-server, mongodb, mongodb-server, mongodb-dev, mongodb-clients, mongodb-10gen, mongodb-10gen-enterprise, mongodb-10gen-unstable, mongodb-10gen-unstable-enterprise, mongodb-10gen-unstable-enterprise-mongos, mongodb-10gen-unstable-enterprise-server, mongodb-10gen-unstable-enterprise-shell, mongodb-10gen-unstable-enterprise-tools, mongodb-10gen-unstable-mongos, mongodb-10gen-unstable-server, mongodb-10gen-unstable-shell, mongodb-10gen-unstable-tools, mongodb-enterprise, mongodb-enterprise-mongos, mongodb-enterprise-server, mongodb-enterprise-shell, mongodb-enterprise-tools, mongodb-nightly, mongodb-org, mongodb-org-mongos, mongodb-org-server, mongodb-org-shell, mongodb-org-tools, mongodb-stable, mongodb18-10gen, mongodb20-10gen, mongodb-org-unstable, mongodb-org-unstable-mongos, mongodb-org-unstable-server, mongodb-org-unstable-shell, mongodb-org-unstable-tools

%description tools
MongoDB (from "huMONGOus") is a schema-free document-oriented database.

This package provides tools for use with MongoDB

%package devel
Summary: Headers and libraries for mongo development.
Conflicts: mongo-10gen, mongo-10gen-enterprise, mongo-10gen-enterprise-server, mongo-10gen-server, mongo-10gen-unstable, mongo-10gen-unstable-enterprise, mongo-10gen-unstable-enterprise-mongos, mongo-10gen-unstable-enterprise-server, mongo-10gen-unstable-enterprise-shell, mongo-10gen-unstable-enterprise-tools, mongo-10gen-unstable-mongos, mongo-10gen-unstable-server, mongo-10gen-unstable-shell, mongo-10gen-unstable-tools, mongo18-10gen, mongo18-10gen-server, mongo20-10gen, mongo20-10gen-server, mongodb, mongodb-server, mongodb-dev, mongodb-clients, mongodb-10gen, mongodb-10gen-enterprise, mongodb-10gen-unstable, mongodb-10gen-unstable-enterprise, mongodb-10gen-unstable-enterprise-mongos, mongodb-10gen-unstable-enterprise-server, mongodb-10gen-unstable-enterprise-shell, mongodb-10gen-unstable-enterprise-tools, mongodb-10gen-unstable-mongos, mongodb-10gen-unstable-server, mongodb-10gen-unstable-shell, mongodb-10gen-unstable-tools, mongodb-enterprise, mongodb-enterprise-mongos, mongodb-enterprise-server, mongodb-enterprise-shell, mongodb-enterprise-tools, mongodb-nightly, mongodb-org, mongodb-org-mongos, mongodb-org-server, mongodb-org-shell, mongodb-org-tools, mongodb-stable, mongodb18-10gen, mongodb20-10gen, mongodb-org-unstable, mongodb-org-unstable-mongos, mongodb-org-unstable-server, mongodb-org-unstable-shell, mongodb-org-unstable-tools

%description devel
MongoDB (from "huMONGOus") is a schema-free document-oriented database.

This package provides the mongo static library and header files needed
to develop mongo client software.

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr
cp -rv BINARIES/usr/bin $RPM_BUILD_ROOT/usr
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
cp debian/*.1 $RPM_BUILD_ROOT/usr/share/man/man1/
# FIXME: remove this rm when mongosniff is back in the package
rm -v $RPM_BUILD_ROOT/usr/share/man/man1/mongosniff.1*
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
cp -v rpm/init.d-mongod $RPM_BUILD_ROOT/etc/rc.d/init.d/mongod
chmod a+x $RPM_BUILD_ROOT/etc/rc.d/init.d/mongod
mkdir -p $RPM_BUILD_ROOT/etc
cp -v rpm/mongod.conf $RPM_BUILD_ROOT/etc/mongod.conf
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
cp -v rpm/mongod.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/mongod
mkdir -p $RPM_BUILD_ROOT/var/lib/mongodb
mkdir -p $RPM_BUILD_ROOT/var/log/mongodb
mkdir -p $RPM_BUILD_ROOT/var/run/mongodb
touch $RPM_BUILD_ROOT/var/log/mongodb/mongod.log

%clean
rm -rf $RPM_BUILD_ROOT

%pre server
if ! /usr/bin/id -g mongodb &>/dev/null; then
    /usr/sbin/groupadd -r mongodb
fi
if ! /usr/bin/id mongodb &>/dev/null; then
    /usr/sbin/useradd -M -r -g mongodb -d /var/lib/mongodb -s /bin/false 	-c mongodb mongodb > /dev/null 2>&1
fi

%post server
if test $1 = 1
then
  /sbin/chkconfig --add mongod
fi

%preun server
if test $1 = 0
then
  /sbin/chkconfig --del mongod
fi

%postun server
if test $1 -ge 1
then
  /sbin/service mongod condrestart >/dev/null 2>&1 || :
fi

%files

%files server
%defattr(-,root,root,-)
%config(noreplace) /etc/mongod.conf
%{_bindir}/mongod
%{_mandir}/man1/mongod.1*
/etc/rc.d/init.d/mongod
/etc/sysconfig/mongod
%attr(0755,mongodb,mongodb) %dir /var/lib/mongodb
%attr(0755,mongodb,mongodb) %dir /var/log/mongodb
%attr(0755,mongodb,mongodb) %dir /var/run/mongodb
%attr(0640,mongodb,mongodb) %config(noreplace) %verify(not md5 size mtime) /var/log/mongodb/mongod.log

%files shell
%defattr(-,root,root,-)
%{_bindir}/mongo
%{_mandir}/man1/mongo.1*

%files mongos
%defattr(-,root,root,-)
%{_bindir}/mongos
%{_mandir}/man1/mongos.1*

%files tools
%defattr(-,root,root,-)
#%doc README GNU-AGPL-3.0.txt

%{_bindir}/bsondump
%{_bindir}/mongodump
%{_bindir}/mongoexport
%{_bindir}/mongofiles
%{_bindir}/mongoimport
%{_bindir}/mongooplog
%{_bindir}/mongoperf
%{_bindir}/mongorestore
%{_bindir}/mongotop
%{_bindir}/mongostat

%{_mandir}/man1/bsondump.1*
%{_mandir}/man1/mongodump.1*
%{_mandir}/man1/mongoexport.1*
%{_mandir}/man1/mongofiles.1*
%{_mandir}/man1/mongoimport.1*
%{_mandir}/man1/mongooplog.1*
%{_mandir}/man1/mongoperf.1*
%{_mandir}/man1/mongorestore.1*
%{_mandir}/man1/mongotop.1*
%{_mandir}/man1/mongostat.1*

%changelog
* Thu Jan 28 2010 Richard M Kreuter <richard@10gen.com>
- Minor fixes.

* Sat Oct 24 2009 Joe Miklojcik <jmiklojcik@shopwiki.com> -
- Wrote mongo.spec.
