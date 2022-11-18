.. index:: vmax, tasks

.. meta::
   :keywords: vmax, tasks

.. _vmax-svalka:


VMAX. Свалка планов
=====================================

.. note:: Какие-то ошметки, но мало ли пригодятся


TASK01869498
------------

.. code:: none

   =================================================================================
   Миграция /rmod, /rmod/archlog, /rmod/db
   =================================================================================
   Переразбивка массива и показывание девайсов на сервер.
   1. Создаем тонкий пул:
   symconfigure -sid 307 -cmd "create pool RMOD_STB_FC, type=thin;" -v prepare
   symconfigure -sid 307 -cmd "create pool RMOD_STB_FC, type=thin;" -v commit
   2. Создаем data-устройства:
   symconfigure -sid 307 -cmd "create dev count=1000, size=32060, 
   emulation=fba, data_member_count=7, config=RAID-5, disk_group=4, 
   attribute=datadev;" -v prepare
   symconfigure -sid 307 -cmd "create dev count=1000, size=32060, 
   emulation=fba, data_member_count=7, config=RAID-5, disk_group=4, 
   attribute=datadev;" -v commit
   Записываем номера созданных устройств: datadev1:datadev1000
   3. Добавляем data-устройства:
   symconfigure -sid 307 -cmd "add dev datadev1:datadev1000 to pool 
   RMOD_STB_FC type=thin, member_state=ENABLE;" -v prepare
   symconfigure -sid 307 -cmd "add dev datadev1:datadev1000 to pool 
   RMOD_STB_FC type=thin, member_state=ENABLE;" -v commit
   4. Создаем thin-устройства для тома db:
   symconfigure -sid 307 -cmd "create dev count=16, size=91000, 
   config=TDEV, emulation=fba;" -v prepare
   symconfigure -sid 307 -cmd "create dev count=16, size=91000, 
   config=TDEV, emulation=fba;" -v commit
   Записываем номера созданных устройств: thindevdb1:thindevdb16
   Создаем meta-устройства
   symconfigure -sid 307 -cmd "form meta from dev thindevdb1, 
   config=striped, count=16;" -v prepare
   symconfigure -sid 307 -cmd "form meta from dev thindevdb1, 
   config=striped, count=16;" -v commit
   -------------------------------------------
   Создаем thin-устройства для тома archlogs:
   symconfigure -sid 307 -cmd "create dev count=16, size=34134, 
   config=TDEV, emulation=fba;" -v prepare
   symconfigure -sid 307 -cmd "create dev count=16, size=34134, 
   config=TDEV, emulation=fba;" -v commit
   Записываем номера созданных устройств: thindevarc1:thindevarc16
   Создаем meta-устройства
   symconfigure -sid 307 -cmd "form meta from dev thindevarc1, 
   config=striped, count=16;" -v prepare
   symconfigure -sid 307 -cmd "form meta from dev thindevarc1, 
   config=striped, count=16;" -v commit
   -------------------------------------------
   Создаем thin-устройства для тома bin:
   symconfigure -sid 307 -cmd "create dev count=8, size=68268, config=TDEV, 
   emulation=fba;" -v prepare
   symconfigure -sid 307 -cmd "create dev count=8, size=68268, config=TDEV, 
   emulation=fba;" -v commit
   Записываем номера созданных устройств: thindevarc1:thindevarc8
   Создаем meta-устройства
   symconfigure -sid 307 -cmd "form meta from dev thindevbin1, 
   config=striped, count=8;" -v prepare
   symconfigure -sid 307 -cmd "form meta from dev thindevbin1, 
   config=striped, count=8;" -v commit
   5.1 Повторяем шаг 4 (том db) для создания 20 meta-устройств. Записываем их номера:
   5.2 Повторяем шаг 4 (том archlogs) для создания 2 meta-устройств. Записываем их номера:
   5.3 Повторяем шаг 4 (том bin) для создания 1 meta-устройств. Записываем их номера:
   6. Биндим metadev в пул:
   Создаем файл "bind.txt" с содержанием:
   bind tdev thindevdb1 to pool RMOD_STB_FC, preallocate size=ALL;
   bind tdev thindevdb2 to pool RMOD_STB_FC, preallocate size=ALL;
   bind tdev thindevdb3 to pool RMOD_STB_FC, preallocate size=ALL;
   bind tdev thindevdb4 to pool RMOD_STB_FC, preallocate size=ALL;
   bind tdev thindevdb5 to pool RMOD_STB_FC, preallocate size=ALL;
   bind tdev thindevdb6 to pool RMOD_STB_FC, preallocate size=ALL;
   ...

TASK01555851
------------

.. code:: none

   ------------------------------------------------------
   Расширение девайса на p795-lp04 - VMAX.
   ------------------------------------------------------
   Данная ФС расположена на страйпе из 7 девайсов:
   hdisk12
            EC Level....................602966
            LIC Node VPD................0B79
   hdisk10
            EC Level....................602966
            LIC Node VPD................06F3
   hdisk14
            EC Level....................602966
            LIC Node VPD................0B89
   hdisk15
            EC Level....................602966
            LIC Node VPD................111D
   hdisk13
            EC Level....................602966
            LIC Node VPD................0B81
   hdisk16
            EC Level....................602966
            LIC Node VPD................1125
   hdisk11
            EC Level....................602966
            LIC Node VPD................0B71
   1. Создаем Thin+BCV девайс, с помощью которого будет производиться расширение.
   symconfigure -sid 66 -cmd "create dev count=8, size=20075, 
   config=BCV+TDEV, emulation=fba;" -v prepare
   symconfigure -sid 66 -cmd "create dev count=8, size=20075, 
   config=BCV+TDEV, emulation=fba;" -v commit
   Записываем номера созданных устройств: ldev1:ldev8
   Создаем мета устройство.
   symconfigure -sid 66 -cmd "form meta from dev ldev1, config=striped, count=8;" -v prepare
   symconfigure -sid 66 -cmd "form meta from dev ldev1, config=striped, count=8;" -v commit
   2. В пуле TASK911 два террабайта свободного места. В нем будем проводить расширение.
   symconfigure -sid 66 -cmd "bind tdev ldev1 to pool Task911, preallocate size=ALL, allocate_type=persistent;" -v prepare
   symconfigure -sid 66 -cmd "bind tdev ldev1 to pool Task911, preallocate size=ALL, allocate_type=persistent;" -v commit
   3. Создаем девайсы для прикрепления.
   symconfigure -sid 66 -cmd "create dev count=4, size=20075, config=TDEV, emulation=fba;" -v prepare
   symconfigure -sid 66 -cmd "create dev count=4, size=20075, config=TDEV, emulation=fba;" -v commit
   Записываем номера созданных устройств: ldev2:ldev3
   4. Запускаем процедуру расширения устройства.
   symconfigure -sid 66 -cmd "add dev ldev2:ldev3 to meta 0B79, protect_data=TRUE, bcv_meta_head=ldev1;" -v prepare
   symconfigure -sid 66 -cmd "add dev ldev2:ldev3 to meta 0B79, protect_data=TRUE, bcv_meta_head=ldev1;" -v commit
   Запускать с managment станций, т.к. процесс достаточно долгий. Ждем ее окончания.
   Пункты 3 и 4 повторяем для остальных девайсов: 06F3; 0B89; 111D; 0B81; 1125; 0B71.
   Каждый последующий девайс необходимо расширять после окончания предыдущего, т.к. используется одно и то же BCV устройство.
   5. После завершения процедуры на массиве для всех устройств, идем на сервер p795-lp04:
   
   root@p795-lp04:~# lsvg cc-hist-vmax1
   VOLUME GROUP:       cc-hist-vmax             VG IDENTIFIER: 00c1d38700004c0000000142084c95d6
   VG STATE:           active                   PP SIZE:        128 megabyte(s)
   VG PERMISSION:      read/write               TOTAL PPs:      9400 (1203200 megabytes)
   MAX LVs:            256                      FREE PPs:       0 (0 megabytes)
   LVs:                3                        USED PPs:       9400 (1203200 megabytes)
   OPEN LVs:           3                        QUORUM:         5 (Enabled)
   TOTAL PVs:          8                        VG DESCRIPTORS: 8
   STALE PVs:          0                        STALE PPs:      0
   ACTIVE PVs:         8                        AUTO ON:        yes
   MAX PPs per VG:     32768                    MAX PVs:        1024
   LTG size (Dynamic): 1024 kilobyte(s)         AUTO SYNC:      no
   HOT SPARE:          no                       BB POLICY: relocatable


TASK01555480
------------

.. code:: none

  ------------------------------------------------------
  Расширение девайса на p795-3-lp03 - Vmax-1.
  ------------------------------------------------------
 
  Данная ФС расположена на девайсе:
  hdisk2
          EC Level....................602966
          LIC Node VPD................15A1
 
  1. Создаем Thin+BCV девайс, с помощью которого будет производиться расширение.
 
  symconfigure -sid 66 -cmd "create dev count=8, size=27307, config=BCV+TDEV, emulation=fba;" -v prepare
  symconfigure -sid 66 -cmd "create dev count=8, size=27307, config=BCV+TDEV, emulation=fba;" -v commit
  Записываем номера созданных устройств: ldev1:ldev8
 
  Создаем мета устройство.
  symconfigure -sid 66 -cmd "form meta from dev ldev1, config=striped, count=8;" -v prepare
  symconfigure -sid 66 -cmd "form meta from dev ldev1, config=striped, count=8;" -v commit
 
  2. В пуле TASK911 три террабайта свободного места. В нем будем проводить расширение.
 
  symconfigure -sid 66 -cmd "bind tdev ldev1 to pool Task911, preallocate size=ALL, allocate_type=persistent;" -v prepare
  symconfigure -sid 66 -cmd "bind tdev ldev1 to pool Task911, preallocate size=ALL, allocate_type=persistent;" -v commit
 
  3. Создаем девайсы для прикрепления.

  symconfigure -sid 66 -cmd "create dev count=5, size=27307, config=TDEV, emulation=fba;" -v prepare
  symconfigure -sid 66 -cmd "create dev count=5, size=27307, config=TDEV, emulation=fba;" -v commit
  Записываем номера созданных устройств: ldev2:ldev3
  
  4. Запускаем процедуру расширения устройства.
  
  symconfigure -sid 66 -cmd "add dev ldev2:ldev3 to meta 15A1, protect_data=TRUE, bcv_meta_head=ldev1;" -v prepare
  symconfigure -sid 66 -cmd "add dev ldev2:ldev3 to meta 15A1, protect_data=TRUE, bcv_meta_head=ldev1;" -v commit
  Запускать с managment станций, т.к. процесс достаточно долгий. Ждем ее окончания.
  
  5. После завершения процедуры на массиве, идем на сервер p795-lp03:
  
  root@p795-lp03:~# lsvg cc-front-vmax1
  VOLUME GROUP:       cc-front-vmax1           VG IDENTIFIER: 00c1d38700004c0000000141ff551411
  VG STATE:           active                   PP SIZE:        128 megabyte(s)
  VG PERMISSION:      read/write               TOTAL PPs:      1599 (204672 megabytes)
  MAX LVs:            256                      FREE PPs:       0 (0 megabytes)
  LVs:                4                        USED PPs:       1599 (204672 megabytes)
  OPEN LVs:           4                        QUORUM:         2 (Enabled)
  TOTAL PVs:          1                        VG DESCRIPTORS: 2
  STALE PVs:          0                        STALE PPs:      0
  ACTIVE PVs:         1                        AUTO ON:        yes
  MAX PPs per VG:     32768                    MAX PVs:        1024
  LTG size (Dynamic): 1024 kilobyte(s)         AUTO SYNC:      no
  HOT SPARE:          no                       BB POLICY: relocatable
  PV RESTRICTION:     none                     INFINITE RETRY: no
  
  root@p795-lp03:~# lslv fscc-front-save
  LOGICAL VOLUME:     fscc-front-save        VOLUME GROUP: cc-front-vmax1
  LV IDENTIFIER:      00c1d38700004c0000000141ff551411.4 
  PERMISSION:     read/write
  VG STATE:           active/complete        LV STATE: opened/syncd
  TYPE:               jfs2                   WRITE VERIFY:   off
  MAX LPs:            512                    PP SIZE:        128 
  megabyte(s)
  COPIES:             1                      SCHED POLICY: parallel
  LPs:                399                    PPs:            399
  STALE PPs:          0                      BB POLICY:
