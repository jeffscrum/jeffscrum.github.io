.. index:: oracle, solaris, ldom, migrate

.. meta::
   :keywords: oracle, solaris, ldom, migrate

.. _fjs1500-3-a-t5-8-1-ld4-zone:

.. TASK01690711

fjs1500-3-a --> t5-8-1-ld4-zone
===============================

Миграция домена fjs1500-3-a в зону t5-8-1-ld4-zone

.. code-block:: none

   =========================
   = Подготовка к миграции =
   =========================

   T5-8-1-Primary:
   ldm add-vnet vid=135 vnet3 pr-vsw-prod3 ld4
   ldm add-vnet vid=135 vnet4 pr-vsw-prod4 ld4
   ldm add-vnet vid=135 vnet5 sec-vsw-prod3 ld4
   ldm add-vnet vid=135 vnet6 sec-vsw-prod4 ld4
   ld4:
   dladm create-vlan -l net2 -v135
   dladm create-vlan -l net3 -v135
   dladm create-vlan -l net4 -v135
   dladm create-vlan -l net5 -v135
   ipadm create-ipmp ipmp135
   ipadm create-ip net135002
   ipadm create-ip net135003
   ipadm create-ip net135004
   ipadm create-ip net135005
   ipadm add-ipmp -i net135002 -i net135003 -i net135004 -i net135005 ipmp135
   ipadm create-addr -T static -a 10.4.28.202/24 ipmp135/prod
   ipadm set-ifprop -p standby=on -m ip net135003
   ipadm set-ifprop -p standby=on -m ip net135004
   ipadm set-ifprop -p standby=on -m ip net135005
   svccfg -s svc:/network/ipmp setprop config/transitive-probing=true
   route -p add default 10.4.28.1 -ifp ipmp135
   route -p add default 192.168.132.1 -ifp ipmp0
   svccfg -s svc:/network/dns/client setprop config/nameserver=net_address: "(10.30.33.154 10.30.33.152 10.4.27.7 10.4.27.6 10.30.33.100 10.30.33.156)"
   svccfg -s svc:/system/name-service/switch setprop config/host = '("files dns")'
   svcadm refresh svc:/system/name-service/switch
   zfs create -o mountpoint=/zones rpool/zones
   zonecfg -z T5-8-1-ld4-zone
   create -t SYSsolaris10
   set zonepath=/zones/T5-8-1-ld4-zone
   set autoboot=true
   remove anet
   set ip-type=shared
   add net
   set physical=ipmp135
   set address=10.4.28.203/24
   end
   verify
   commit
   exit
   zoneadm list -cv
   zoneadm -z T5-8-1-ld4-zone install -a /root/flarsol10p2v.flar -u
   zoneadm -z T5-8-1-ld4-zone attach
   zoneadm -z T5-8-1-ld4-zone boot; zlogin -C T5-8-1-ld4-zone
   T5-8-1-ld4-zone:
   scp root@10.4.28.200:/root/SF_zone.tar .
   pkgadd -d VRTSvxfs.pkg all
   pkgadd -d VRTSvlic.pkg all
   pkgadd -d VRTSodm.pkg all
   zoneadm -z T5-8-1-ld4-zone halt
   zonecfg -z T5-8-1-ld4-zone
   add device
   set match=/dev/vxportal
   end
   add device
   set match=/dev/fdd
   end
   add device
   set match=/dev/odm
   end
   add fs
   set dir=/etc/vx/licenses/lic
   set special=/etc/vx/licenses/lic
   set type=lofs
   end
   set fs-allowed=vxfs,odm
   verify
   commit
   exit
   zoneadm -z T5-8-1-ld4-zone boot
   scp root@10.4.28.200:/root/sol11_sparc.tar .
   tar -xvf sol11_sparc.tar
   cd /root/sol11_sparc/storage_foundation
   ./installsf -configure
   scp root@10.4.28.200:/root/VRTSaslapm_Solaris_6.1.1.400.tar .
   tar -xvf VRTSaslapm_Solaris_6.1.1.400.tar
   pkg set-publisher -p /root/SPARC/Solaris_11/VRTSaslapm.p5p Symantec
   pkg update
   
   ==============================
   = Миграционная часть для ld4 =
   ==============================
   
   T5-8-1-ld4:
   ifconfig ipmp135 addif 10.4.28.104 netmask 255.255.255.0 zone T5-8-1-ld4-zone up
   ifconfig ipmp135 addif 10.4.28.103 netmask 255.255.255.0 zone T5-8-1-ld4-zone up
   ifconfig ipmp135 addif 10.4.28.107 netmask 255.255.255.0 zone T5-8-1-ld4-zone up
   T5-8-1-Primary:
   ldm add-vds primary-data-ld4 primary
   ldm add-vds secondary-data-ld4 IO-domain
   vxdisk scandisks new
   vxdisk list
   * KS-Iridium_98-1 *
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0459s2 volvsp0_0459@primary-data-ld4
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0459s2 volvsp0_0459@secondary-data-ld4
   ldm add-vdisk timeout=30 id=10 volvsp0_0459-p volvsp0_0459@primary-data-ld4 ld4
   ldm add-vdisk timeout=30 id=11 volvsp0_0459-s volvsp0_0459@secondary-data-ld4 ld4
   * KS-Iridium_98-2 *
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0457s2 volvsp0_0457@primary-data-ld4
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0458s2 volvsp0_0458@primary-data-ld4
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0457s2 volvsp0_0457@secondary-data-ld4
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0458s2 volvsp0_0458@secondary-data-ld4
   ldm add-vdisk timeout=30 id=12 volvsp0_0457-p volvsp0_0457@primary-data-ld4 ld4
   ldm add-vdisk timeout=30 id=13 volvsp0_0458-p volvsp0_0458@primary-data-ld4 ld4
   ldm add-vdisk timeout=30 id=14 volvsp0_0457-s volvsp0_0457@secondary-data-ld4 ld4
   ldm add-vdisk timeout=30 id=15 volvsp0_0458-s volvsp0_0458@secondary-data-ld4 ld4
   ld4:
   vxdisk scandisks new
   vxdisk list
   vxdisk -o alldgs list
   vxdg import KS-Iridium_98-1
   vxdg import KS-Iridium_98-2
   * KS-Iridium_98-2 *
   echo "/dev/vx/dsk/KS-Iridium_98-2/bin         /dev/vx/rdsk/KS-Iridium_98-2/bin        /iridium        vxfs    2       yes     -" >> /etc/vfstab
   * KS-Iridium_98-1 *
   echo "/dev/vx/dsk/KS-Iridium_98-2/kbdb        /dev/vx/rdsk/KS-Iridium_98-2/kbdb       /iridium/kbdb   vxfs    2       yes     -" >> /etc/vfstab
   echo "/dev/vx/dsk/KS-Iridium_98-1/save        /dev/vx/rdsk/KS-Iridium_98-1/save       /iridium/save   vxfs    2       yes     -" >> /etc/vfstab
    
   mkdir /zones/T5-8-1-ld4-zone/root/iridium
   mount /zones/T5-8-1-ld4-zone/root/iridium
   mount /zones/T5-8-1-ld4-zone/root/iridium/save
   mount /zones/T5-8-1-ld4-zone/root/iridium/kbdb
