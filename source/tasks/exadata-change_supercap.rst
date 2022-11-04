.. index:: exadata, supercap, battery, change, raid

.. meta::
   :keywords: exadata, supercap, battery, change, raid

.. _exadata-change_supercap:


Exadata Change Internal RAID HBA SuperCap
=========================================

Работы проводятся согласно документу Doc ID 1969384.1

План работ:

1. Выключение CRS

2. Подготовительные шаги:
   * Установить политику кэша WriteThrough для всех логических дисков.
   ``/opt/MegaRAID/MegaCli/MegaCli64 -ldsetprop wt -lall -a0``

   * Проверить что настройки применились WriteThrough
   ``/opt/MegaRAID/MegaCli/MegaCli64 -ldpdinfo -a0 | grep BBU``

3. Выключить сервер `exadbadm01`

4. Физическая замена батареи RAID

5. После включения и загрузки ОС:

   * Проверить физические, логические тома и состояние батареи
     
     - ``/opt/MegaRAID/MegaCli/MegaCli64 -LdInfo -Lall -a0``
     - ``/opt/MegaRAID/MegaCli/MegaCli64 -PdList -a0 | grep "Slot\|Firmware\|Inq"``
     - ``/opt/MegaRAID/MegaCli/MegaCli64 -AdpBbuCmd -a0``

   * Переключить политику кэша в режим WriteBack
   ``/opt/MegaRAID/MegaCli/MegaCli64 -ldsetprop wb -lall -a0``

   * Проверить что настройки применились WriteBack
   ``/opt/MegaRAID/MegaCli/MegaCli64 -ldpdinfo -a0 | grep BBU``

6. Запустить CRS
