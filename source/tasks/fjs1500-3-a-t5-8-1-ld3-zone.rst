.. index:: oracle, solaris, ldom, migrate

.. meta::
   :keywords: oracle, solaris, ldom, migrate

.. _fjs1500-3-a-t5-8-1-ld3-zone:

.. TASK01690763

fjs1500-3-a --> t5-8-1-ld3-zone
===============================

Миграция домена fjs1500-3-a в зону t5-8-1-ld3-zone

.. code-block:: none

   =========================
   = Подготовка к миграции =
   =========================

   T5-8-1-Primary:
   ldm add-vnet vid=135 vnet3 pr-vsw-prod3 ld3
   ldm add-vnet vid=135 vnet4 pr-vsw-prod4 ld3
   ldm add-vnet vid=135 vnet5 sec-vsw-prod3 ld3
   ldm add-vnet vid=135 vnet6 sec-vsw-prod4 ld3
   ld3:
   dladm create-vlan -l net2 -v135
   dladm create-vlan -l vnet3 -v135
   dladm create-vlan -l net4 -v135
   dladm create-vlan -l net5 -v135
   ipadm create-ipmp ipmp135
   ipadm create-ip net135002
   ipadm create-ip vnet135003
   ipadm create-ip net135004
   ipadm create-ip net135005
   ipadm add-ipmp -i net135002 -i vnet135003 -i net135004 -i net135005 ipmp135
   ipadm create-addr -T static -a 10.4.28.204/24 ipmp135/prod
   ipadm set-ifprop -p standby=on -m ip vnet135003
   ipadm set-ifprop -p standby=on -m ip net135004
   ipadm set-ifprop -p standby=on -m ip net135005
   svccfg -s svc:/network/ipmp setprop config/transitive-probing=true
   route -p add default 10.4.28.1 -ifp ipmp135
   route -p delete default 192.168.132.1 -ifp ipmp0
    
   svccfg -s network/dns/client setprop config/search = astring: '("s.ru")'
   svccfg -s network/dns/client setprop config/domain = astring: '("s.ru")'
   svccfg -s network/dns/client setprop config/nameserver = net_address: '(10.4.27.6 10.4.27.7 10.30.33.100 10.30.33.152 10.30.33.154 10.30.33.156 192.168.134.190)'
   svccfg -s name-service/switch setprop config/host = astring: '("files dns")'
   svccfg -s network/dns/client listprop config
   svcadm refresh svc:/system/name-service/switch
    
   zfs create -o mountpoint=/zones rpool/zones
   zonecfg -z T5-8-1-ld3-zone
   create -t SYSsolaris10
   set zonepath=/zones/T5-8-1-ld3-zone
   set autoboot=true
   remove anet
   set ip-type=shared
   add net
   set physical=ipmp135
   set address=10.4.28.205/24
   end
   verify
   commit
   exit
   zoneadm list -cv
   zoneadm -z T5-8-1-ld3-zone install -a /root/flarsol10p2v.flar -u
   zoneadm -z T5-8-1-ld3-zone attach
   zoneadm -z T5-8-1-ld3-zone boot; zlogin -C T5-8-1-ld3-zone
   T5-8-1-ld3-zone:
   scp root@10.4.28.200:/root/SF_zone.tar .
   pkgadd -d VRTSvxfs.pkg all 
   pkgadd -d VRTSvlic.pkg all
   pkgadd -d VRTSodm.pkg all
   zoneadm -z T5-8-1-ld3-zone halt
   zonecfg -z T5-8-1-ld3-zone
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
   zoneadm -z T5-8-1-ld3-zone boot
   scp root@10.4.28.200:/root/sol11_sparc.tar .
   tar -xvf sol11_sparc.tar
   cd /root/sol11_sparc/storage_foundation
   ./installsf -configure
   scp root@10.4.28.200:/root/VRTSaslapm_Solaris_6.1.1.400.tar .
   tar -xvf VRTSaslapm_Solaris_6.1.1.400.tar
   pkg set-publisher -p /root/SPARC/Solaris_11/VRTSaslapm.p5p Symantec
   pkg update
   
   ==============================
   = Миграционная часть для ld3 =
   ==============================

   T5-8-1-Primary:
   ldm add-vds primary-data-ld3 primary
   ldm add-vds secondary-data-ld3 IO-domain
   vxdisk scandisks new
   vxdisk list
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_044fs2 volvsp0_044f@primary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0450s2 volvsp0_0450@primary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0451s2 volvsp0_0451@primary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0452s2 volvsp0_0452@primary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0453s2 volvsp0_0453@primary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0454s2 volvsp0_0454@primary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0455s2 volvsp0_0455@primary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0456s2 volvsp0_0456@primary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_044fs2 volvsp0_044f@secondary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0450s2 volvsp0_0450@secondary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0451s2 volvsp0_0451@secondary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0452s2 volvsp0_0452@secondary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0453s2 volvsp0_0453@secondary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0454s2 volvsp0_0454@secondary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0455s2 volvsp0_0455@secondary-data-ld3
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0456s2 volvsp0_0456@secondary-data-ld3
   ldm add-vdisk timeout=30 id=10 volvsp0_044f-p volvsp0_044f@primary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=11 volvsp0_0450-p volvsp0_0450@primary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=12 volvsp0_0451-p volvsp0_0451@primary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=13 volvsp0_0452-p volvsp0_0452@primary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=14 volvsp0_0453-p volvsp0_0453@primary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=15 volvsp0_0454-p volvsp0_0454@primary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=16 volvsp0_0455-p volvsp0_0455@primary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=17 volvsp0_0456-p volvsp0_0456@primary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=18 volvsp0_044f-s volvsp0_044f@secondary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=19 volvsp0_0450-s volvsp0_0450@secondary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=20 volvsp0_0451-s volvsp0_0451@secondary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=21 volvsp0_0452-s volvsp0_0452@secondary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=22 volvsp0_0453-s volvsp0_0453@secondary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=23 volvsp0_0454-s volvsp0_0454@secondary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=24 volvsp0_0455-s volvsp0_0455@secondary-data-ld3 ld3
   ldm add-vdisk timeout=30 id=25 volvsp0_0456-s volvsp0_0456@secondary-data-ld3 ld3
   ld3:
   vxdisk scandisks new
   vxdisk list
   vxdisk -o alldgs list
   vxdg import KS-ArchiveDG
   echo "/dev/vx/dsk/KS-ArchiveDG/bin            /dev/vx/rdsk/KS-ArchiveDG/bin           /cs-archive             vxfs    2       no      log" >> /etc/vfstab
   echo "/dev/vx/dsk/KS-ArchiveDG/db             /dev/vx/rdsk/KS-ArchiveDG/db            /cs-archive/db          vxfs    2       no      log" >> /etc/vfstab
   echo "/dev/vx/dsk/KS-ArchiveDG/save           /dev/vx/rdsk/KS-ArchiveDG/save          /cs-archive/save        vxfs    2       no      log" >> /etc/vfstab
   mount /zones/T5-8-1-ld3-zone/root/cs-archive
   mount /zones/T5-8-1-ld3-zone/root/cs-archive/db
   mount /zones/T5-8-1-ld3-zone/root/cs-archive/save
