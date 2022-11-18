.. index:: sun, solaris, vxvm, upgrade

.. meta::
   :keywords: sun, solaris, vxvm, upgrade

.. _solaris-vxvm-upgrade:

Upgrade Solaris u3 to Solaris u11 and VxVM 5.1 to 6.2
=====================================================

.. note:: Бэкап выполняется при помоще разрыва зеркала и демонтажа одного из дисков


План работ
----------

.. code-block:: none

   ---------------------
   Этап 0: Бэкапы 
   ---------------------
   1) Убедиться в наличии бэкапа
   2) Собрать explorer
    
   ---------------------
   Этап 1: Манипуляции с VxFS 
   ---------------------
   3) Поднимаем версию disk layout до v7
   # vxupgrade -n 7 <mount_point>
   4) Записываем загрузочную метку на оба диска
   # vxbootsetup -g rootdg vx-rootdisk
   # vxbootsetup -g rootdg vx-rootmirror
    
   ---------------------
   Этап 2: Проверки, разрыв зеркал, чистка плексов, АНинкапсуляция
   ---------------------
   5) Выключаем ОС
   # init 0
   6) Вытаскиваем физический диск HDD0
   7) Загружаемся с диска HDD1
   8) Выключаем ОС
   # init 0
   9) Вынимаем диск HDD1
   10) Вставляем диск HDD0
   11) Загружаем ОС и удаляем все плексы в состоянии failed
   vxplex -g rootdg -o rm dis crash-02
   vxplex -g rootdg -o rm dis home-02
   vxplex -g rootdg -o rm dis rootvol-02
   vxplex -g rootdg -o rm dis swapvol-02
   vxplex -g rootdg -o rm dis var-02
   12) Проводим АНинкапсуляцию рутового диска
   # vxunroot
   13) Перезагружаем ОС и проверяем что система работает на слайсах
   # df -h
    
   ---------------------
   Этап 3: Удаление VxVM и VCS
   ---------------------
   14) Удаляем VxVM 5.1 и VCS 5.1
   # /opt/VRTS/install/uninstallsf
   # /opt/VRTS/install/uninstallvcs
    
   ---------------------
   Этап 4: Установка нового релиза Solaris и обновление
   ---------------------
   15) Загружаем систему с cd-rom'a
   (ok) boot cdrom
   16) Апгрейдимся на релиз Solaris 10 u11
    
   ---------------------
   Этап 5: Установка патчей EIS
   ---------------------
   17.1) Монтируем EIS
   # lofiadm -a EIS.iso
   # mount -o ro -F hsfs /dev/lofi/1 /mnt
   17.2) Обновляем Explorer и другое служебное ПО
   # /mnt/sun/install/setup-standard.sh
   17.3) Перелогиниваемся
   # exit
   17.4) Установка патчей
   # init s
   # cd /mnt/sun/patch/10/
   # unpack-patches -rq /tmp
   18) Перезагружаемся
    
   ---------------------
   Этап 6: Установка VxVM 6.2 и патчей
   ---------------------
   19) Инсталлируем VxVM 6.2 и патчи
   # gunzip VRTS_SF_HA_Solutions_6.2_Solaris_SPARC.tar.gz
   # tar -xf VRTS_SF_HA_Solutions_6.2_Solaris_SPARC.tar
   # ./installer
   # shutdown -i6 -y -g0
   # gunzip sfha-sol10_sparc-MR-6.2.1.tar.gz
   # tar -xf sfha-sol10_sparc-MR-6.2.1.tar
   # ./installer
   # shutdown -i6 -y -g0
   # gunzip fs-sol10_sparc-Patch-6.2.1.100.tar.gz
   # tar -xf fs-sol10_sparc-Patch-6.2.1.100.tar
   # ./installVRTSvxfs621P1
   # shutdown -i6 -y -g0
    
   ---------------------
   Этап 7: Инкапсуляция рутового диска
   ---------------------
   20) Удаляем старую дисковую группу если она осталась(проверив что мы все еще на слайсах)
   # vxdisk list
   # df -h
   # vxdg destroy rootdg
   21) Инкапсулируем рутовый диск
   # vxdiskadm --> Encapsulate one or more disks
   22) Перезагружаемся и проверяем что системный диск под управлением VxVM
   # shutdown -i6 -y -g0
    
   ---------------------
   Этап 8: Зеркалирование
   ---------------------
   22) Вставляем физический диск HDD1
   23) Переводим диск HDD1 под управление VxVM и зеркалируем
   # vxdisksetup -i c1t1d0 format=sliced noreserve
   # vxdg -g rootdg adddisk rootmirror=c1t1d0
   # vxdiskadm --> Mirror volumes on a disk
   # eeprom use-nvramrc?=true
   # eeprom boot-device=rootdisk rootmirror
   24) Проверяем стутус синхронизации дисков
   #vxtask list

   	Риски: Неизвестные ошибки ПО, человечелский фактор, некорректная АНинкапсуляция, некорректная инкапсуляция.
   	В случае наступления рисков действуем по плану отката


План отката
-----------

.. code-block:: none

   1) Выключаем сервер
   # init 0
   2) Вынимаем диск HDD0
   3) Вставляем диск HDD1
   4) Загружаем ОС и удаляем все плексы в состоянии failed
   # vxplex -g rootdg -r rm dis <plex>
   5) Вставляем диск HDD0
   6) Переводим диск HDD0 под управление VxVM и зеркалируем
   # vxdisksetup -i c1t0d0 format=sliced noreserve
   # vxdg -g rootdg adddisk rootdisk=c1t0d0
   # vxdiskadm (Выбираем пункт №6)
   # eeprom use-nvramrc?=true
   # eeprom boot-device=rootdisk rootmirror




