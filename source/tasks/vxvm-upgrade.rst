.. index:: solaris, vxvm, upgrade

.. meta::
   :keywords: solaris, vxvm, upgrade

.. _vxvm-upgrade:

Обновление Veritas SF на f3800-1
================================

.. code:: none

   ---------------------
   Этап 1: Разрыв зеркал 
   ---------------------
    
   vxbootsetup -g rootdg rootdisk
   vxbootsetup -g rootdg rootmirr
    
   Проверка корректности разбивки дисков + исправление в случае ошибок.
    
   prtvtoс /dev/rdsk/c0t1d0s2
   prtvtoс /dev/rdsk/c0t0d0s2
    
   vxplex -g rootdg -o rm dis opt-02
   vxplex -g rootdg -o rm dis rootvol-02
   vxplex -g rootdg -o rm dis swapvol-02
   vxplex -g rootdg -o rm dis var-02
    
   vxdg -g rootdg rmdisk rootmirr
    
   Проверка всех слайсов с помощью fsck.
   fsck -y /dev/rdsk/c0t1d0s0
   fsck -y /dev/rdsk/c0t1d0s1
   fsck -y /dev/rdsk/c0t1d0s5
   fsck -y /dev/rdsk/c0t1d0s6
    
   mount /dev/dsk/c0t1d0s0 /mnt
   # cd /mnt/etc
   # cp -p system system.orig
   # cp -p vfstab vfstab.orig
   # cp -p vfstab.prevm vfstab
    
   vi /mnt/etc/vfstab
    
   touch /mnt/etc/vx/reconfig.d/state.d/install-db
    
   vi /mnt/etc/system
       * rootdev ..
       * set vxio ..
    
   umount /mnt
    
   ------------------------------------------
   Этап 2: Деинкапсулирование рутового диска 
   ------------------------------------------
    
   Остановка всех приложений и отмонтирование FS.
   umount /opt/openv
   umount /support
   umount /tm1-back/oradata
    
   Депортирование групп:
   vxdg deport NB_6_dg
   vxdg deport supportdg
   vxdg deport tm1-back_dg
    
   Комментирование в vfstab всех строк *vx*
   cp /etc/vfstab /etc/vfstab.backup.20022014
    
   Деинкапсулирование:
   /etc/vx/bin/vxunroot
    
   Перезагрузка со слайсов.
    
   Проверка состояния системы и окончания загрузки.
    
   -----------------------------
   Этап 3: Обновление Veritas SF 
   -----------------------------
    
   Удаление старой версии.
   cd /opt/VRTS/install
   ./uninstallsf
    
   Установка новой верси:
   gunzip VRTS_SF_HA_Solutions_5.1_Solaris_SPARC.tar.gz
   tar -xf VRTS_SF_HA_Solutions_5.1_Solaris_SPARC.tar.gz
    
   ./installer
    
   3)Install all Storage Foundation packages
   2)SF Enterprise
    
   После установки обновление ASL:
    
   Копируем файл "/var/sadm/install/admin/default"
   # cp /var/sadm/install/admin/default /var/sadm/install/admin/aslapm_admin
    
   Редактируем файл /var/sadm/install/admin/aslapm_admin
   # vi /var/sadm/install/admin/aslapm_admin
                   - modify the "instance" line to be:
                       "instance=overwrite"
   # pkgadd -a /var/sadm/install/admin/aslapm_admin -d VRTSaslapm.pkg
    
   Обновление конфигурации.
   # vxdctl enable
    
   Проверка версии.
    
   # vxddladm listsupport [all]
   # vxddladm listsupport libname=<libname>
    
   # vxdmpadm listapm [all | apmname]
    
   # pkginfo -l VRTSaslapm
    
   ---------------------------------------
   Этап 4: Инкапсулирование рутового диска 
   ---------------------------------------
    
   vxdiskadm
    
   Encapsulate one or more disks
    
   Инкапсулируем в группу rootdg диск c0t0d0 (sliced) как rootdisk.
   Перезагружаемся два раза : init 6
    
   -------------------------------------------------------------------
   Этап 5: Проверка инкапсуляции, импортирование групп, зеркалирование 
   -------------------------------------------------------------------
    
   Импортирование всех групп и запуск приложений.
    
   Если все прошло удачно, то зеркалируем рутовый диск.
    
   vxdg -g rootdg adddisk rootmirror=<disk_acc_name>
   vxmirror -g rootdg rootdisk rootmirror
    
   Если что-то пошло не так, то загружаемся со второго диска
   и возвращаем все в первоначальное состояние.
    
   vxiod set 10
   vxdconfigd -m disable
   vxdctl init
   vxdisk -f init c0t0d0 format=sliced
   vxdctl enable
   rm /etc/vx/reconfig.d/state.d/install-db
   vxdiskadm => option 2 Encapsulate one or more disks => choose c0t1d0 (old rootmirror) => put under rootdg
   shutdown -i6 -g0 -y
    
   /etc/vx/bin/vxrootmir -g rootdg rootdisk
   /etc/vx/bin/vxmirror -g rootdg rootmirror rootdisk
    
   Проверка состояния группы и дисков.
    
   Работы достаточно продолжительны по времени и могут занять более 3-х часов.
   Риски: Неизвестные ошибки ПО, человеческий фактор, паника системы.
