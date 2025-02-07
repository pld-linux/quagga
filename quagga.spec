Summary:	Routing Software Suite
Summary(pl.UTF-8):	Zestaw oprogramowania do routingu
Name:		quagga
Version:	0.99.23
Release:	10
License:	GPL v2+
Group:		Networking/Daemons
Source0:	http://download.savannah.gnu.org/releases/quagga/%{name}-%{version}.tar.xz
# Source0-md5:	92dff03272aa9127ac13c6bea9c66187
Source1:	%{name}.pam
Source2:	%{name}.tmpfiles
Source10:	%{name}-zebra.init
Source11:	%{name}-bgpd.init
Source12:	%{name}-ospf6d.init
Source13:	%{name}-ospfd.init
Source14:	%{name}-ripd.init
Source15:	%{name}-ripngd.init
Source16:	%{name}-isisd.init
Source17:	%{name}-babeld.init
Source20:	%{name}-zebra.sysconfig
Source21:	%{name}-bgpd.sysconfig
Source22:	%{name}-ospf6d.sysconfig
Source23:	%{name}-ospfd.sysconfig
Source24:	%{name}-ripd.sysconfig
Source25:	%{name}-ripngd.sysconfig
Source26:	%{name}-isisd.sysconfig
Source27:	%{name}-babeld.sysconfig
Source30:	%{name}-zebra.logrotate
Source31:	%{name}-bgpd.logrotate
Source32:	%{name}-ospfd.logrotate
Source33:	%{name}-ospf6d.logrotate
Source34:	%{name}-ripd.logrotate
Source35:	%{name}-ripngd.logrotate
Source36:	%{name}-isisd.logrotate
Source37:	%{name}-babeld.logrotate
Patch0:		%{name}-info.patch
Patch1:		%{name}-proc.patch
Patch2:		%{name}-vtysh-pam.patch
Patch3:		%{name}-readline.patch
Patch4:		snmp-api.patch
Patch5:		includes.patch
URL:		http://www.quagga.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gawk
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	net-snmp-devel
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	readline-devel >= 4.1
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	texinfo
Requires(post):	/bin/hostname
Requires(post):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	rc-scripts
Provides:	group(quagga)
Provides:	group(quaggavty)
Provides:	routingdaemon
Provides:	user(quagga)
Obsoletes:	bird
Obsoletes:	gated
Obsoletes:	mrt
Obsoletes:	quagga
Obsoletes:	zebra-xs26
Conflicts:	logrotate < 3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}
%define		_includedir	%{_prefix}/include/%{name}
%define		_localstatedir	%{_var}/run/%{name}

# better fix by proper linking
%define		skip_post_check_so	libzebra.so.* libospf.so.* libospfapiclient.so.*

%description
Quagga is a routing software suite, providing implementations of
OSPFv2, OSPFv3, RIP v1 and v2, RIPv3 and BGPv4 for Unix platforms,
particularly FreeBSD and Linux and also NetBSD, to mention a few.
Quagga is a fork of GNU Zebra which was developed by Kunihiro
Ishiguro. The Quagga tree aims to build a more involved community
around Quagga than the current centralised model of GNU Zebra.

%description -l pl.UTF-8
Quagga to zestaw oprogramowania do routingu, dostarczający
implementacje OSPFv2, OSPFv3, RIP v1 i v2, RIPv3 i BGPv4 dla platform
uniksowych, w szczególności FreeBSD, Linuksa, NetBSD - żeby wymienić
tylko kilka. Quagga to odgałęzienie projektu GNU Zebra, który był
rozwijany przez Kunihiro Ishiguro. Celem drzewa Quagga jest
zgromadzenie bardziej zaangażowanej społeczności wokół projektu, niż w
aktualnie scentralizowanym modelu GNU Zebry.

%package babeld
Summary:	BABEL wireless mesh routing daemon
Summary(pl.UTF-8):	Demon routingu BABEL
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description babeld
BABEL wireless mesh routing daemon. Includes IPv6 support.

%description babeld -l pl.UTF-8
Demon obsługi protokołu BABEL. Obsługuje także IPv6.

%package bgpd
Summary:	BGP routing daemon
Summary(pl.UTF-8):	Demon routingu BGP
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Obsoletes:	zebra-xs26-bgpd

%description bgpd
BGP routing daemon. Includes IPv6 support.

%description bgpd -l pl.UTF-8
Demon obsługi protokołu BGP. Obsługuje także IPv6.

%package isisd
Summary:	IS-IS routing daemon
Summary(pl.UTF-8):	Demon routingu IS-IS
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description isisd
IS-IS routing daemon.

%package ospfd
Summary:	OSPF routing daemon
Summary(pl.UTF-8):	Demon routingu OSPF
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description ospfd
OSPF routing daemon.

%description ospfd -l pl.UTF-8
Demon do obsługi protokołu OSPF.

%package ospf6d
Summary:	IPv6 OSPF routing daemon
Summary(pl.UTF-8):	Demon routingu OSPF w sieciach IPv6
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Obsoletes:	zebra-xs26-ospf6d

%description ospf6d
OSPF6 routing daemon for IPv6 networks.

%description ospf6d -l pl.UTF-8
Demon do obsługi protokołu OSPF w sieciach IPv6.

%package ripd
Summary:	RIP routing daemon
Summary(pl.UTF-8):	Demon routingu RIP
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description ripd
RIP routing daemon for zebra.

%description ripd -l pl.UTF-8
Demon obsługi protokołu RIP.

%package ripngd
Summary:	IPv6 RIP routing daemon
Summary(pl.UTF-8):	Demon routingu RIP w sieciach IPv6
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Obsoletes:	zebra-xs26-ripngd

%description ripngd
RIP routing daemon for IPv6 networks.

%description ripngd -l pl.UTF-8
Demon obsługi protokołu RIP w sieciach IPv6.

%package devel
Summary:	Header files for quagga libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek quagga
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for quagga libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek quagga.

%package static
Summary:	Static version of quagga libraries
Summary(pl.UTF-8):	Statyczne wersje bibliotek quagga
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of quagga libraries.

%description static -l pl.UTF-8
Statyczne wersje bibliotek quagga.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%{__autoheader}
%configure \
	--enable-ipv6 \
	--enable-vtysh \
	--enable-netlink \
	--enable-snmp \
	--enable-opaque-lsa \
	--enable-ospfapi=yes \
	--enable-ospfclient=yes \
	--enable-ospf-te \
	--enable-multipath=64 \
	--enable-user=quagga \
	--enable-group=quagga \
	--enable-vty-group=quaggavty \
	--enable-rtadv \
	--enable-isisd \
	--disable-isis-topology \
	--enable-irdp \
	--disable-watchquagga \
	--with-libpam

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{env.d,logrotate.d,pam.d,rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT/var/log/{archive,}/%{name} \
	$RPM_BUILD_ROOT%{_var}/run/%{name} \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/zebra
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

install -p %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/zebra
install -p %{SOURCE11} $RPM_BUILD_ROOT/etc/rc.d/init.d/bgpd
install -p %{SOURCE12} $RPM_BUILD_ROOT/etc/rc.d/init.d/ospf6d
install -p %{SOURCE13} $RPM_BUILD_ROOT/etc/rc.d/init.d/ospfd
install -p %{SOURCE14} $RPM_BUILD_ROOT/etc/rc.d/init.d/ripd
install -p %{SOURCE15} $RPM_BUILD_ROOT/etc/rc.d/init.d/ripngd
install -p %{SOURCE16} $RPM_BUILD_ROOT/etc/rc.d/init.d/isisd
install -p %{SOURCE17} $RPM_BUILD_ROOT/etc/rc.d/init.d/babeld

cp -p %{SOURCE20} $RPM_BUILD_ROOT/etc/sysconfig/zebra
cp -p %{SOURCE21} $RPM_BUILD_ROOT/etc/sysconfig/bgpd
cp -p %{SOURCE22} $RPM_BUILD_ROOT/etc/sysconfig/ospf6d
cp -p %{SOURCE23} $RPM_BUILD_ROOT/etc/sysconfig/ospfd
cp -p %{SOURCE24} $RPM_BUILD_ROOT/etc/sysconfig/ripd
cp -p %{SOURCE25} $RPM_BUILD_ROOT/etc/sysconfig/ripngd
cp -p %{SOURCE26} $RPM_BUILD_ROOT/etc/sysconfig/isisd
cp -p %{SOURCE27} $RPM_BUILD_ROOT/etc/sysconfig/babeld

cp -p %{SOURCE30} $RPM_BUILD_ROOT/etc/logrotate.d/zebra
cp -p %{SOURCE31} $RPM_BUILD_ROOT/etc/logrotate.d/bgpd
cp -p %{SOURCE32} $RPM_BUILD_ROOT/etc/logrotate.d/ospfd
cp -p %{SOURCE33} $RPM_BUILD_ROOT/etc/logrotate.d/ospf6d
cp -p %{SOURCE34} $RPM_BUILD_ROOT/etc/logrotate.d/ripd
cp -p %{SOURCE35} $RPM_BUILD_ROOT/etc/logrotate.d/ripngd
cp -p %{SOURCE36} $RPM_BUILD_ROOT/etc/logrotate.d/isisd
cp -p %{SOURCE37} $RPM_BUILD_ROOT/etc/logrotate.d/babeld

touch $RPM_BUILD_ROOT/var/log/%{name}/{zebra,babeld,bgpd,isisd,ospf6d,ospfd,ripd,ripngd}.log

touch $RPM_BUILD_ROOT%{_sysconfdir}/{vtysh,zebra,babeld,bgpd,isisd,ospf6d,ospfd,ripd,ripngd}.conf

echo '#VTYSH_PAGER="less -FX"' > $RPM_BUILD_ROOT/etc/env.d/VTYSH_PAGER

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 127 quagga
%groupadd -g 128 quaggavty
%useradd -u 127 -d /tmp -s /bin/false -c "Quagga User" -g quagga quagga

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig
/sbin/chkconfig --add zebra >&2
umask 027
if [ ! -s %{_sysconfdir}/zebra.conf ]; then
	echo "hostname `hostname`" > %{_sysconfdir}/zebra.conf
fi
%service zebra restart "main routing daemon"

%post babeld
/sbin/chkconfig --add babeld >&2
if [ ! -s %{_sysconfdir}/babeld.conf ]; then
        echo "hostname `hostname`" > %{_sysconfdir}/babeld.conf
fi
%service babeld restart "babeld routing daemon"

%post bgpd
/sbin/chkconfig --add bgpd >&2
if [ ! -s %{_sysconfdir}/bgpd.conf ]; then
	echo "hostname `hostname`" > %{_sysconfdir}/bgpd.conf
fi
%service bgpd restart "bgpd routing daemon"

%post isisd
/sbin/chkconfig --add isisd >&2
if [ ! -s %{_sysconfdir}/isisd.conf ]; then
	echo "hostname `hostname`" > %{_sysconfdir}/isisd.conf
fi
%service isisd restart "IS-IS routing daemon"

%post ospfd
/sbin/chkconfig --add ospfd >&2
if [ ! -s %{_sysconfdir}/ospfd.conf ]; then
	echo "hostname `hostname`" > %{_sysconfdir}/ospfd.conf
fi
%service ospfd restart "ospfd routing daemon"

%post ospf6d
/sbin/chkconfig --add ospf6d >&2
if [ ! -s %{_sysconfdir}/ospf6d.conf ]; then
	echo "hostname `hostname`" > %{_sysconfdir}/ospf6d.conf
fi
%service ospf6d restart "ospf6d routing daemon"

%post ripd
/sbin/chkconfig --add ripd >&2
if [ ! -s %{_sysconfdir}/ripd.conf ]; then
	echo "hostname `hostname`" > %{_sysconfdir}/ripd.conf
fi
%service ripd restart "ripd routing daemon"

%post ripngd
/sbin/chkconfig --add ripngd >&2
if [ ! -s %{_sysconfdir}/ripngd.conf ]; then
	echo "hostname `hostname`" > %{_sysconfdir}/ripngd.conf
fi
%service ripngd restart "ripngd routing daemon"

%preun
if [ "$1" = "0" ]; then
	%service zebra stop
	/sbin/chkconfig --del zebra >&2
fi

%preun babeld
if [ "$1" = "0" ]; then
        %service babeld stop
        /sbin/chkconfig --del babeld >&2
fi

%preun bgpd
if [ "$1" = "0" ]; then
	%service bgpd stop
	/sbin/chkconfig --del bgpd >&2
fi

%preun isisd
if [ "$1" = "0" ]; then
	%service isisd stop
	/sbin/chkconfig --del isisd >&2
fi

%preun ospfd
if [ "$1" = "0" ]; then
	%service ospfd stop
	/sbin/chkconfig --del ospfd >&2
fi

%preun ospf6d
if [ "$1" = "0" ]; then
	%service ospf6d stop
	/sbin/chkconfig --del ospf6d >&2
fi

%preun ripd
if [ "$1" = "0" ]; then
	%service ripd stop
	/sbin/chkconfig --del ripd >&2
fi

%preun ripngd
if [ "$1" = "0" ]; then
	%service ripngd stop
	/sbin/chkconfig --del ripngd >&2
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
if [ "$1" = "0" ]; then
	%userremove quagga
	%groupremove quagga
	%groupremove quaggavty
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README REPORTING-BUGS SERVICES TODO
%{_infodir}/*info*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/VTYSH_PAGER
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/zebra
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/zebra
%dir %attr(770,root,quagga) %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %attr(660,root,quagga) %{_sysconfdir}/vtysh.conf
%config(noreplace) %verify(not md5 mtime size) %attr(660,root,quagga) %{_sysconfdir}/zebra.conf
%{systemdtmpfilesdir}/%{name}.conf
%dir %attr(770,root,quagga) /var/run/%{name}
%dir %attr(750,quagga,quagga) /var/log/%{name}
%dir %attr(750,quagga,quagga) /var/log/archive/%{name}
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.0
%doc zebra/*sample*
%{_mandir}/man8/zebra*
%attr(755,root,root) %{_sbindir}/zebra
%attr(754,root,root) /etc/rc.d/init.d/zebra
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/zebra
%ghost /var/log/%{name}/zebra*

%files babeld
%defattr(644,root,root,755)
%doc babeld/*sample*
%attr(755,root,root) %{_sbindir}/babeld
%attr(754,root,root) /etc/rc.d/init.d/babeld
%config(noreplace) %verify(not md5 mtime size) %attr(660,root,quagga) %{_sysconfdir}/babeld.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/babeld
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/babeld
%ghost /var/log/%{name}/babeld*

%files bgpd
%defattr(644,root,root,755)
%doc bgpd/*sample*
%{_mandir}/man8/bgpd*
%attr(755,root,root) %{_sbindir}/bgpd
%attr(754,root,root) /etc/rc.d/init.d/bgpd
%config(noreplace) %verify(not md5 mtime size) %attr(660,root,quagga) %{_sysconfdir}/bgpd.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/bgpd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/bgpd
%ghost /var/log/%{name}/bgpd*

%files isisd
%defattr(644,root,root,755)
%doc isisd/*sample*
%{_mandir}/man8/isisd*
%attr(755,root,root) %{_sbindir}/isisd
%attr(754,root,root) /etc/rc.d/init.d/isisd
%config(noreplace) %verify(not md5 mtime size) %attr(660,root,quagga) %{_sysconfdir}/isisd.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/isisd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/isisd
%ghost /var/log/%{name}/isisd*

%files ospfd
%defattr(644,root,root,755)
%doc ospfd/*sample*
%{_mandir}/man8/ospfd*
%{_mandir}/man8/ospfclient*
%attr(755,root,root) %{_sbindir}/ospfd
%attr(755,root,root) %{_sbindir}/ospfclient
%attr(754,root,root) /etc/rc.d/init.d/ospfd
%config(noreplace) %verify(not md5 mtime size) %attr(660,root,quagga) %{_sysconfdir}/ospfd.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/ospfd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/ospfd
%ghost /var/log/%{name}/ospfd*

%files ospf6d
%defattr(644,root,root,755)
%doc ospf6d/*sample*
%{_mandir}/man8/ospf6d*
%attr(755,root,root) %{_sbindir}/ospf6d
%attr(754,root,root) /etc/rc.d/init.d/ospf6d
%config(noreplace) %verify(not md5 mtime size) %attr(660,root,quagga) %{_sysconfdir}/ospf6d.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/ospf6d
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/ospf6d
%ghost /var/log/%{name}/ospf6d*

%files ripd
%defattr(644,root,root,755)
%doc ripd/*sample*
%{_mandir}/man8/ripd*
%attr(755,root,root) %{_sbindir}/ripd
%attr(754,root,root) /etc/rc.d/init.d/ripd
%config(noreplace) %verify(not md5 mtime size) %attr(660,root,quagga) %{_sysconfdir}/ripd.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/ripd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/ripd
%ghost /var/log/%{name}/ripd*

%files ripngd
%defattr(644,root,root,755)
%doc ripngd/*sample*
%{_mandir}/man8/ripngd*
%attr(755,root,root) %{_sbindir}/ripngd
%attr(754,root,root) /etc/rc.d/init.d/ripngd
%config(noreplace) %verify(not md5 mtime size) %attr(660,root,quagga) %{_sysconfdir}/ripngd.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/sysconfig/ripngd
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) /etc/logrotate.d/ripngd
%ghost /var/log/%{name}/ripngd*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
