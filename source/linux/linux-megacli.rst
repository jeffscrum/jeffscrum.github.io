.. index:: linux, raid, megacli

.. meta::
   :keywords: linux, raid, megacli

.. _linux-megacli:

Установка и работа с MegaCLI
============================

Установка
---------

Для установки в Debian 12 или Proxmox:

.. code-block:: bash

   apt-get install libncurses5
   wget -O /tmp/megacli_8.07.14-2_all.deb "https://kb.ksomov.ru/_static/megacli_8.07.14-2_all.deb" && dpkg -i /tmp/megacli_8.07.14-2_all.deb

Команды
-------

Полезные команды (исполняемый файл /opt/MegaRAID/MegaCli/MegaCli64 ):

.. code-block:: none

   # Быстрая проверка
   ./MegaCli64 -LdPdInfo -aALL | grep -E "(Id|State |Bad Blocks|Firmware state|Error Count|Predictive Failure Count)"

   # Просмотр журнала событий BBU, где можно найти информацию по проверкам и автоисправлению  битых секторов
   ./MegaCli64 -FwTermLog -Dsply -aALL > /tmp/ttylog.txt
   
   # Полная информация о всех адаптеров контроллера
   ./MegaCli64 -AdpAllInfo -aALL
   
   # Полная информация о настройках и дисках
   ./MegaCli64 -CfgDsply -aALL
   
   # Информация о последних событиях, где можно найти информацию о сбои в работе дисков
   ./MegaCli64 -AdpEventLog -GetLatest 4000 -f events.log -aALL
   ./MegaCli64 -AdpEventLog -GetEvents -f events.log -aALL
   
   # Информация о всех доступных корпусах контроллера
   ./MegaCli64 -EncInfo -aALL

   # Включение Disk Cache Policy для диска L0
   ./MegaCli64 -LDSetProp -EnDskCache -L0 -a0

   # Выключение Disk Cache Policy для диска L0
   ./MegaCli64 -LDSetProp -DisDskCache -L0 -a0

   # Список всех логических дисков и типе RAID-а в котором они собраны
   ./MegaCli64 -LDInfo -Lall -aALL
   
   # Список всех физических дисков
   ./MegaCli64 -PDList -aALL
   
   # Информация о конкретном физическом диске
   # Типовая комманда ./MegaCli64 -pdInfo -Physdrv [E1:S2] -aALL
   # E1 - Enclosure Device ID: 1, S2 - Slot Number: 2
   
   # To get it need to run - ./MegaCli64 -LdPdInfo -aALL | grep -E "ID|Slot"
   ./MegaCli64 -pdInfo -Physdrv [32:9] -aALL
   
   # Подсветить диск (для поиска)
   #Start blinking
   ./MegaCli64 -PdLocate -start -Physdrv\[4:3\]  -aALL
   ./MegaCli64 -PdLocate -start -Physdrv\[4:2\]  -aALL
   ./MegaCli64 -PdLocate -start -Physdrv\[4:1\]  -aALL
   #Stop blinking
   ./MegaCli64 -PdLocate -stop  -Physdrv\[4:1\]  -aALL
   ./MegaCli64 -PdLocate -stop  -Physdrv\[4:2\]  -aALL
   ./MegaCli64 -PdLocate -stop  -Physdrv\[4:3\]  -aALL
    
   # Проверка состояния BBU (Battery Backup Unit)
   ./MegaCli64 -AdpBbuCmd -aALL
   
   # Посмотреть прогресс добавления диска в RAID
   ./MegaCli64 -PDRbld -ShowProg -Physdrv[32:14] -aAll

   # Создание логического диска (Logical Disk)
   ./MegaCli64 -CfgLdAdd -r0[32:6,32:7,32:8] wb direct CachedBadBBU -a0 (или NoCachedBadBBU)
   
   # Список всех логических дисков и типе RAID-а в котором они собраны
   ./MegaCli64 -LDInfo -Lall -aALL

   # Удаление логического диска (Logical Disk)
   ./MegaCli64 -CfgLdDel -L2 -a0

   ## Expand Logical Disk
      1. First gather information:
         ./MegaCli64 -getLdExpansionInfo -L0 -a0
 
      2. From here you should have enough information to use the default command:
         ./MegaCli64 -LdExpansion -pN -dontExpandArray -Lx|-L0,1,2|-Lall -aN|-a0,1,2|-aALL
 
         For example, if my controller were 0, my PD I wanted to add was PD 4 and my Logical drive was 0;
         ./MegaCli64 -LdExpansion -p4 -L0 -a0



Скрипт мониторинга
------------------

Небольшой скрипт для вывода информации в удобном виде :download:`megaraid_status.py </_static/megaraid_status.tar.gz>`

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
   c0u1p0  | SSD  | Samsung SSD 850 EVO 1TB EMT51B6Q                   | 930.3 Gb | Online, Spun Up | 6.0Gb/s  | N/A  | [252:3]  | 0
   c0u2p0  | HDD  | SEAGATE ST91000640SS 00049XG5VT6F                  | 930.3 Gb | Online, Spun Up | 6.0Gb/s  | 30C  | [252:4]  | 8
   c0u2p1  | HDD  | SEAGATE ST91000640SS 00049XG5VYP6                  | 930.3 Gb | Online, Spun Up | 6.0Gb/s  | 30C  | [252:5]  | 11
   c0u2p2  | HDD  | SEAGATE ST91000640SS 00049XG690HG                  | 930.3 Gb | Online, Spun Up | 6.0Gb/s  | 31C  | [252:6]  | 10
   c0u2p3  | HDD  | SEAGATE ST91000640SS 00049XG690W8                  | 930.3 Gb | Online, Spun Up | 6.0Gb/s  | 33C  | [252:7]  | 9
   c0u3p0  | SSD  | SAMSUNG MZ7WD120HCFV-0003 DXM4203Q                 | 110.8 Gb | Online, Spun Up | 6.0Gb/s  | N/A  | [252:2]  | 2

Если запустить скрипт с параметром ``--nagios``, то будут показаны только проблемы:

.. code-block:: bash

   root@s11:~# python megaraid_status.py --nagios
   RAID ERROR - Arrays: OK:2 Bad:1 - Disks: OK:11 Bad:1

-------

Related Links:
- `S.M.A.R.T. (часть 1). Мониторинг SCSI дисков под LSI 2108 (megaraid) RAID контроллером <http://sysadm.pp.ua/linux/monitoring-systems/smart-under-lsi-2108-kontroller.html>`_
- `wikitech.wikimedia.org <https://wikitech.wikimedia.org/wiki/MegaCli>`_
