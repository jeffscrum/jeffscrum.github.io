.. index:: oracle, solaris, ldom, migrate

.. meta::
   :keywords: oracle, solaris, ldom, migrate

.. _fjs1500-3-a-t5-8-1-ld5-zone:

.. TASK01656372

fjs1500-3-a --> t5-8-1-ld5-zone
===============================

Миграция домена fjs1500-3-a в зону t5-8-1-ld5-zone

.. code-block:: none

   =========================
   = Подготовка к миграции =
   =========================
   
   T5-8-1-Primary:
   ldm add-vsw net-dev=net4 vid=135 pr-vsw-prod3 primary
   ldm add-vsw net-dev=net10 vid=135 pr-vsw-prod4 primary
   ldm add-vsw net-dev=net6 vid=135 sec-vsw-prod3 IO-domain
   ldm add-vsw net-dev=net8 vid=135 sec-vsw-prod4 IO-domain
   ldm add-vnet vid=135 vnet3 pr-vsw-prod3 ld5
   ldm add-vnet vid=135 vnet4 pr-vsw-prod4 ld5
   ldm add-vnet vid=135 vnet5 sec-vsw-prod3 ld5
   ldm add-vnet vid=135 vnet6 sec-vsw-prod4 ld5
   ld5:
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
   ipadm create-addr -T static -a 10.4.28.200/24 ipmp135/prod
   ipadm set-ifprop -p standby=on -m ip net135003
   ipadm set-ifprop -p standby=on -m ip net135004
   ipadm set-ifprop -p standby=on -m ip net135005
   svccfg -s svc:/network/ipmp setprop config/transitive-probing=true
   route -p add default 10.4.28.1 -ifp ipmp135
   route -p add 192.168.132.1 -ifp ipmp0
   svccfg -s svc:/network/dns/client setprop config/nameserver=net_address: "(10.30.33.154 10.30.33.152 10.4.27.7 10.4.27.6 10.30.33.100 10.30.33.156)"
   svccfg -s svc:/system/name-service/switch setprop config/host = '("files dns")'
   svcadm refresh svc:/system/name-service/switch
   zfs create -o mountpoint=/zones rpool/zones
   zonecfg -z T5-8-1-ld5-zone
   create -t SYSsolaris10
   set zonepath=/zones/T5-8-1-ld5-zone
   set autoboot=true
   remove anet
   set ip-type=shared
   add net
   set physical=ipmp135
   set address=10.4.28.201/24
   end
   verify
   commit
   exit
   zoneadm list -cv
   zoneadm -z T5-8-1-ld5-zone install -a /root/flarsol10p2v.flar -u
   zoneadm -z T5-8-1-ld5-zone attach
   zoneadm -z T5-8-1-ld5-zone boot; zlogin -C T5-8-1-ld5-zone
 
   scp root@10.4.28.200:/root/SF_zone.tar .
   pkgadd -d VRTSvxfs.pkg all
   pkgadd -d VRTSvlic.pkg all
   pkgadd -d VRTSodm.pkg all
   zoneadm -z T5-8-1-ld5-zone halt
   zonecfg -z T5-8-1-ld5-zone
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
   zoneadm -z T5-8-1-ld5-zone boot
 
   ==============================
   = Миграционная часть для ld5 =
   ==============================
   
   fjs1500-3-a:
   ifconfig fjgi0:3 unplumb
   ifconfig fjgi0:2 unplumb
   ifconfig fjgi0:6 unplumb
   \\ Удаляем старые адреса из /etc/hostname.fjgi0
   \\ addif cs-prokrust netmask + broadcast + up
   \\ addif cs-reffer-new netmask + broadcast + up
   \\ addif 10.4.28.107 netmask + broadcast + up
   vxdg deport KS-Reffer_98-1
   vxdg deport KS-Stafford_98-2_new
   vxdg deport ProkrustDG
    
   T5-8-1-ld5:
   ifconfig ipmp135 addif 10.4.28.104 netmask 255.255.255.0 zone T5-8-1-ld5-zone up
   ifconfig ipmp135 addif 10.4.28.103 netmask 255.255.255.0 zone T5-8-1-ld5-zone up
   ifconfig ipmp135 addif 10.4.28.107 netmask 255.255.255.0 zone T5-8-1-ld5-zone up
   T5-8-1-Primary:
   ldm add-vds primary-data-ld5 primary
   ldm add-vds secondary-data-ld5 IO-domain
   vxdisk scandisks new
   vxdisk list
   vxdisk -o alldgs list
   * ProkrustDG *
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_046as2 volvsp0_046a@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0467s2 volvsp0_0467@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0468s2 volvsp0_0468@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0469s2 volvsp0_0469@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_046as2 volvsp0_046a@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0467s2 volvsp0_0467@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0468s2 volvsp0_0468@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_0469s2 volvsp0_0469@secondary-data-ld5
   ldm add-vdisk timeout=30 id=10 volvsp0_046a-p volvsp0_046a@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=11 volvsp0_0467-p volvsp0_0467@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=12 volvsp0_0468-p volvsp0_0468@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=13 volvsp0_0469-p volvsp0_0469@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=14 volvsp0_046a-s volvsp0_046a@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=15 volvsp0_0467-s volvsp0_0467@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=16 volvsp0_0468-s volvsp0_0468@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=17 volvsp0_0469-s volvsp0_0469@secondary-data-ld5 ld5
   * KS-Reffer_98-1 *
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_046bs2 volvsp0_046b@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_046cs2 volvsp0_046c@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_046ds2 volvsp0_046d@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_046bs2 volvsp0_046b@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_046cs2 volvsp0_046c@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/hitachi_vsp0_046ds2 volvsp0_046d@secondary-data-ld5
   ldm add-vdisk timeout=30 id=18 volvsp0_046b-p volvsp0_046b@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=19 volvsp0_046c-p volvsp0_046c@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=20 volvsp0_046d-p volvsp0_046d@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=21 volvsp0_046b-s volvsp0_046b@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=22 volvsp0_046c-s volvsp0_046c@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=23 volvsp0_046d-s volvsp0_046d@secondary-data-ld5 ld5
   * KS-Stafford_98-2_new *
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000ads2 volsan_vc1_0000ad@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000aes2 volsan_vc1_0000ae@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000afs2 volsan_vc1_0000af@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b0s2 volsan_vc1_0000b0@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b1s2 volsan_vc1_0000b1@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b2s2 volsan_vc1_0000b2@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b5s2 volsan_vc1_0000b5@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b6s2 volsan_vc1_0000b6@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b7s2 volsan_vc1_0000b7@primary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000ads2 volsan_vc1_0000ad@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000aes2 volsan_vc1_0000ae@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000afs2 volsan_vc1_0000af@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b0s2 volsan_vc1_0000b0@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b1s2 volsan_vc1_0000b1@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b2s2 volsan_vc1_0000b2@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b5s2 volsan_vc1_0000b5@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b6s2 volsan_vc1_0000b6@secondary-data-ld5
   ldm add-vdsdev /dev/vx/dmp/san_vc1_0000b7s2 volsan_vc1_0000b7@secondary-data-ld5
   ldm add-vdisk timeout=30 id=24 volsan_vc1_0000ad-p volsan_vc1_0000ad@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=25 volsan_vc1_0000ae-p volsan_vc1_0000ae@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=26 volsan_vc1_0000af-p volsan_vc1_0000af@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=27 volsan_vc1_0000b0-p volsan_vc1_0000b0@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=28 volsan_vc1_0000b1-p volsan_vc1_0000b1@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=29 volsan_vc1_0000b2-p volsan_vc1_0000b2@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=30 volsan_vc1_0000b5-p volsan_vc1_0000b5@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=31 volsan_vc1_0000b6-p volsan_vc1_0000b6@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=32 volsan_vc1_0000b7-p volsan_vc1_0000b7@primary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=33 volsan_vc1_0000ad-s volsan_vc1_0000ad@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=34 volsan_vc1_0000ae-s volsan_vc1_0000ae@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=35 volsan_vc1_0000af-s volsan_vc1_0000af@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=36 volsan_vc1_0000b0-s volsan_vc1_0000b0@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=37 volsan_vc1_0000b1-s volsan_vc1_0000b1@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=38 volsan_vc1_0000b2-s volsan_vc1_0000b2@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=39 volsan_vc1_0000b5-s volsan_vc1_0000b5@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=40 volsan_vc1_0000b6-s volsan_vc1_0000b6@secondary-data-ld5 ld5
   ldm add-vdisk timeout=30 id=41 volsan_vc1_0000b7-s volsan_vc1_0000b7@secondary-data-ld5 ld5
    
   ld5:
   vxdisk scandisks new
   vxdisk list
   vxdisk -o alldgs list
   vxdg import ProkrustDG
   vxdg -n RefferDG import KS-Reffer_98-1
   vxdg -n StaffordDG import KS-Stafford_98-2_new
   * ProkrustDG *
   echo "/dev/vx/dsk/ProkrustDG/bin        /dev/vx/rdsk/ProkrustDG/bin       /zones/T5-8-1-ld5-zone/root/prokrust       vxfs    2       yes     log" >> /etc/vfstab
   echo "/dev/vx/dsk/ProkrustDG/save        /dev/vx/rdsk/ProkrustDG/save       /zones/T5-8-1-ld5-zone/root/prokrust/save       vxfs    2       yes     log" >> /etc/vfstab
   echo "/dev/vx/dsk/ProkrustDG/haribdadb        /dev/vx/rdsk/ProkrustDG/haribdadb       /zones/T5-8-1-ld5-zone/root/prokrust/db       vxfs    2       yes     log" >> /etc/vfstab
   * RefferDG *
   echo "/dev/vx/dsk/RefferDG/bin        /dev/vx/rdsk/RefferDG/bin       /zones/T5-8-1-ld5-zone/root/reffer       vxfs    2       yes     log" >> /etc/vfstab
   echo "/dev/vx/dsk/RefferDG/save        /dev/vx/rdsk/RefferDG/save       /zones/T5-8-1-ld5-zone/root/reffer/save       vxfs    2       yes     log" >> /etc/vfstab
   echo "/dev/vx/dsk/RefferDG/bookdb        /dev/vx/rdsk/RefferDG/bookdb       /zones/T5-8-1-ld5-zone/root/reffer/bookdb       vxfs    2       yes     log" >> /etc/vfstab
   * StaffordDG *
   echo "/dev/vx/dsk/StaffordDG/bin            /dev/vx/dsk/StaffordDG/bin            /zones/T5-8-1-ld5-zone/root/stafford               vxfs    2       no      -" >> /etc/vfstab
   echo "/dev/vx/dsk/StaffordDG/stafforddb     /dev/vx/dsk/StaffordDG/stafforddb     /zones/T5-8-1-ld5-zone/root/stafford/ase-data      vxfs    2       no      -" >> /etc/vfstab
   echo "/dev/vx/dsk/StaffordDG/rs-data        /dev/vx/dsk/StaffordDG/rs-data        /zones/T5-8-1-ld5-zone/root/stafford/rs-data       vxfs    2       no      -" >> /etc/vfstab
   echo "/dev/vx/dsk/StaffordDG/save           /dev/vx/dsk/StaffordDG/save           /zones/T5-8-1-ld5-zone/root/stafford/save          vxfs    2       no      -" >> /etc/vfstab
   
   mount /zones/T5-8-1-ld5-zone/root/prokrust
   mount /zones/T5-8-1-ld5-zone/root/prokrust/save
   mount /zones/T5-8-1-ld5-zone/root/prokrust/db
   mount /zones/T5-8-1-ld5-zone/root/reffer
   mount /zones/T5-8-1-ld5-zone/root/reffer/save
   mount /zones/T5-8-1-ld5-zone/root/reffer/bookdb
   mount /zones/T5-8-1-ld5-zone/root/stafford
   mount /zones/T5-8-1-ld5-zone/root/stafford/ase-data
   mount /zones/T5-8-1-ld5-zone/root/stafford/rs-data
   mount /zones/T5-8-1-ld5-zone/root/stafford/save
