.. index:: oracle, sun, solaris, zfs

.. meta::
   :keywords: oracle, sun, solaris, zfs

.. _oracle-hw-zfs-disk-replace:

ZFS disk replacement on Solaris
===============================

.. code-block:: bash

   =====
   BAD DISK
   /SYS/DBP/HDD0      c0t5000CCA02F1B6454d0
   =====
    
   # zpool status -lx
   # zpool status -v
   # zpool detach rpool c0t5000CCA02F1B6454d0s0          <--- Плохой диск
   # cfgadm -alv | grep c0t5000CCA02F1B6454d0
   # cfgadm -c unconfigure c7::w5000cca02f1b6455,0
   <Physically remove failed disk c1t0d0>
   <Physically insert replacement disk c1t0d0>
   # cfgadm -al
   # devfsadm -Cv
   # cfgadm -c configure c7::w5000cca02f1ba63d,0          <--- Имя нового диска
   # prtvtoc /dev/rdsk/c0t5000CCA02F1B6E2Cd0s0          <---- Проверяем метку на хорошем диске
   # format
   # format -e          <--- Для установки EFI (SMI) метки
   # prtvtoc /dev/dsk/c0t5000CCA02F1B6E2Cd0s2 | fmthard -s - /dev/rdsk/<newdisk>s2
    
   # zpool attach rpool c0t5000CCA02F1B6E2Cd0s0 <newdisk>s0          <-- живой диск & новый диск
   # zpool status rpool
   # zpool status -lx
    
   SPARC# installboot -F zfs /usr/platform/`uname -i`/lib/fs/zfs/bootblk /dev/rdsk/c1t0d0s0    <-- bootblk на новый диск

--------

Related Links:
  * How to Replace a Disk in a ZFS rpool for a SPARC Solaris System (:download:`Doc ID 2328288.1 <https://app.box.com/s/ps29ulil1itg4lhavjiwr8dt4k8gibzx>`)