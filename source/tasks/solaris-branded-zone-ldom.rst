.. index:: solaris, ldom, zone

.. meta::
   :keywords: solaris, ldom, zone

.. _solaris-branded-zone-ldom:

Install And Configure Solaris 10 Branded Zone In Ldom
=====================================================

.. code:: none

   For Solaris 10 Branded zones
   Install:
   * VRTSvlic
   * VRTSvxfs
   * VRTSodm
    
   zfs create -o mountpoint=/zones rpool/zones
   zonecfg -z T5-8-1-ld2-zone
   create -t SYSsolaris10
   set zonepath=/zones/T5-8-1-ld2-zone
   set autoboot=true
   remove anet
   set ip-type=shared
   add net
   set physical=ipmp175
   set address=10.4.28.241/24
   end
   verify
   commit
   exit
   zoneadm list -cv
   zoneadm -z T5-8-1-ld2-zone install -a /root/flarsol10p2v.flar -u
   zoneadm -z T5-8-1-ld2-zone attach
   zoneadm -z T5-8-1-ld2-zone boot; zlogin -C T5-8-1-ld2-zone
 
   // заливаем в зону пакеты необходимые для корректной работы VRTS
   scp root@192.168.135.18:/root/SF_zone_sfha62.tar .
    
   // Необходимые настройки зоны
   pkgadd -d /root/SF_zone_sfha62/VRTSvxfs.pkg
   pkgadd -d /root/SF_zone_sfha62/VRTSvlic.pkg
   pkgadd -d /root/SF_zone_sfha62/VRTSodm.pkg
   zoneadm -z T5-8-1-ld2-zone halt
   zonecfg -z T5-8-1-ld2-zone
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
   zoneadm -z T5-8-1-ld2-zone boot