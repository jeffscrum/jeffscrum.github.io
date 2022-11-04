.. index:: linux, raid, megacli

.. meta::
   :keywords: linux, raid, megacli

.. _linux-megacli:

Полезные команды для работы с MegaCLI
=====================================

.. code-block:: bash

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

-------

Related Links:
- `S.M.A.R.T. (часть 1). Мониторинг SCSI дисков под LSI 2108 (megaraid) RAID контроллером <http://sysadm.pp.ua/linux/monitoring-systems/smart-under-lsi-2108-kontroller.html>`_



