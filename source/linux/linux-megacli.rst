.. index:: linux, raid, megacli

.. meta::
   :keywords: linux, raid, megacli

.. _linux-megacli:

Полезные команды для работы с MegaCLI
=====================================

.. code-block:: none

   # Быстрая проверка
   megacli -LdPdInfo -aALL | grep -E "(Id|State |Bad Blocks|Firmware state|Error Count|Predictive Failure Count)"

   # Просмотр журнала событий BBU, где можно найти информацию по проверкам и автоисправлению  битых секторов
   megacli -fwtermlog -dsply -aall > /tmp/ttylog.txt
   
   # Полная информация о всех адаптеров контроллера
   megacli -AdpAllInfo -aALL
   
   # Полная информация о настройках и дисках
   megacli -CfgDsply -aALL
   
   # Информация о последних событиях, где можно найти информацию о сбои в работе дисков
   megacli -AdpEventLog -GetLatest 4000 -f events.log -aALL
   megacli -AdpEventLog -GetEvents -f events.log -aALL
   
   # Информация о всех доступных корпусах контроллера
   megacli -EncInfo -aALL
   
   # Список всех логических дисков и типе RAID-а в котором они собраны
   megacli -LDInfo -Lall -aALL
   
   # Список всех физических дисков
   megacli -PDList -aALL
   
   # Информация о конкретном физическом диске
   # Типовая комманда megacli -pdinfo -physdrv [E1:S2] -aALL
   # E1 - Enclosure Device ID: 1, S2 - Slot Number: 2
   
   # To get it need to run - megacli -LdPdInfo -aALL | grep -E "ID|Slot"
   megacli -pdinfo -physdrv [32:9] -aALL
   
   # Подсветить диск (для поиска)
   #Start blinking
   megacli -PdLocate -start -physdrv\[4:3\]  -aALL
   megacli -PdLocate -start -physdrv\[4:2\]  -aALL
   megacli -PdLocate -start -physdrv\[4:1\]  -aALL
   #Stop blinking
   megacli -PdLocate -stop  -physdrv\[4:1\]  -aALL
   megacli -PdLocate -stop  -physdrv\[4:2\]  -aALL
   megacli -PdLocate -stop  -physdrv\[4:3\]  -aALL
    
   # Проверка состояния BBU (Battery Backup Unit)
   megacli -adpbbucmd -aall
   
   # Посмотреть прогресс добавления диска в RAID
   megacli -pdrbld -showprog -physdrv[4:0] -aAll

   # Create LogicalDisk 
   megacli -CfgLdAdd -r0[32:6,32:7,32:8] wb direct CachedBadBBU -a0 (или NoCachedBadBBU)
   
   # Список всех логических дисков и типе RAID-а в котором они собраны
   megacli -LDInfo -Lall -aALL
   
   # Посмотреть прогресс добавления диска в RAID 
   megacli -pdrbld -showprog -physdrv[32:14] -aAll

   # remove LogicalDisk
   megacli -CfgLdDel -L2 -a0

Ну небольшой скрипт для вывода информации в удобном виде :download:`megaraid_status.py </_static/megaraid_status.tar.gz>`

.. code-block:: bash

   root@s19:~# python megaraid_status.py
   -- Controller information --
   -- ID | H/W Model         | RAM    | Temp | Firmware
   c0    | LSI MegaRAID ROMB | 1024MB | 57C  | FW: 23.18.0-0013
    
   -- Array information --
   -- ID | Type   |    Size |  Strpsz |   Flags | DskCache |   Status |  OS Path | InProgress
   c0u0  | RAID-1 |    278G |   64 KB |   RA,WT |  Default |  Optimal | /dev/sda | None
   c0u1  | RAID-0 |    930G |   64 KB |   RA,WB |  Enabled |  Optimal | /dev/sdb | None
   c0u2  | RAID-5 |   2725G |   64 KB |   RA,WT |  Default |  Optimal | /dev/sdc | None
   c0u3  | RAID-0 |    111G |   64 KB | ADRA,WB |  Enabled |  Optimal | /dev/sdd | None
    
   -- Disk information --
   -- ID   | Type | Drive Model                                        | Size     | Status          | Speed    | Temp | Slot ID  | Device ID
   c0u0p0  | HDD  | SEAGATE ST300MM0026 0001S0K263T8                   | 278.4 Gb | Online, Spun Up | 6.0Gb/s  | 31C  | [252:0]  | 12
   c0u0p1  | HDD  | SEAGATE ST300MM0026 0001S0K23LQQ                   | 278.4 Gb | Online, Spun Up | 6.0Gb/s  | 30C  | [252:1]  | 13
   c0u1p0  | SSD  | S21CNXAG506746T Samsung SSD 850 EVO 1TB EMT01B6Q   | 930.3 Gb | Online, Spun Up | 6.0Gb/s  | N/A  | [252:3]  | 0
   c0u2p0  | HDD  | SEAGATE ST91000640SS 00049XG5VT6F                  | 930.3 Gb | Online, Spun Up | 6.0Gb/s  | 30C  | [252:4]  | 8
   c0u2p1  | HDD  | SEAGATE ST91000640SS 00049XG5VYP6                  | 930.3 Gb | Online, Spun Up | 6.0Gb/s  | 30C  | [252:5]  | 11
   c0u2p2  | HDD  | SEAGATE ST91000640SS 00049XG690HG                  | 930.3 Gb | Online, Spun Up | 6.0Gb/s  | 31C  | [252:6]  | 10
   c0u2p3  | HDD  | SEAGATE ST91000640SS 00049XG690W8                  | 930.3 Gb | Online, Spun Up | 6.0Gb/s  | 33C  | [252:7]  | 9
   c0u3p0  | SSD  | S1FZNEAG514429 SAMSUNG MZ7WD120HCFV-00003 DXM9203Q | 110.8 Gb | Online, Spun Up | 6.0Gb/s  | N/A  | [252:2]  | 2

-------

Related Links:
- `S.M.A.R.T. (часть 1). Мониторинг SCSI дисков под LSI 2108 (megaraid) RAID контроллером <http://sysadm.pp.ua/linux/monitoring-systems/smart-under-lsi-2108-kontroller.html>`_



