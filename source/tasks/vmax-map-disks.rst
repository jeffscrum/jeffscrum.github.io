.. index:: vmax, map, disks

.. meta::
   :keywords: vmax, map, disks

.. _vmax-map-disks:


VMAX. Отмапливание дисков
=========================

.. code:: none

   1. Создаем новые устройства
   symconfigure -sid 307 -cmd "create dev count=1, size=2294, config=TDEV, emulation=fba;" -v prepare
   symconfigure -sid 307 -cmd "create dev count=1, size=2294, config=TDEV, emulation=fba;" -v commit
   
   Записываем номера созданных устройств: [09EE]
   
   2. Биндим новые устройства в пул.
   Создаем файл "bind.txt" с содержанием:
   
     bind tdev 09EE to pool CFT_FC, preallocate size=ALL;
   
   symconfigure -sid 307 -file bind.txt -v prepare
   symconfigure -sid 307 -file bind.txt -v commit
   
   Проверяем, что у пула не появилась переподписка.
   
   symcfg -sid 307 list -pool -thin -detail -gb
   
   3. Добавляем созданные устройства в группу для сервера SG_CFT.
   
   symaccess -sid 307 -type storage -name SG_CFT add devs 09EE
   
   4. Говорим на серверах cfgmgr. И выставляем девайсам необходимые параметры, как у остальных.
