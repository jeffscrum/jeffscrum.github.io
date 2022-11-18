.. index:: vxvm, disable, remove, disks

.. meta::
   :keywords: vxvm, disable, remove, disks

.. _vxvm-remove-disks:

Отключение san-диска в VxVM
===========================

.. code:: none
   
   План работ по удалению диска:
   1. Отключение путей
   fas62400_0
   vxdmpadm -f disable path=c16t500A09849F62C312d108s2
   vxdmpadm -f disable path=c17t500A09819F62C312d108s2
   vxdmpadm -f disable path=c18t500A09849F62C312d108s2
   vxdmpadm -f disable path=c19t500A09819F62C312d108s2
    
   2. Удаление дисков
   vxdisk rm fas62400_0
    
   3. Отключение путей
   luxadm -e offline /dev/rdsk/c16t500A09849F62C312d108s2
   luxadm -e offline /dev/rdsk/c17t500A09819F62C312d108s2
   luxadm -e offline /dev/rdsk/c18t500A09849F62C312d108s2
   luxadm -e offline /dev/rdsk/c19t500A09819F62C312d108s2
    
   4. удаляется mapping на массиве:
   lun unmap /vol/vol_for_test_dump_tm/lun_for_test_dump_tm fjs1500-1-a
    
   5. Расконфигурирование устройств
   cfgadm -o unusable_SCSI_LUN -c unconfigure c16::500a09849f62c312
   cfgadm -o unusable_SCSI_LUN -c unconfigure c17::500a09819f62c312
   cfgadm -o unusable_SCSI_LUN -c unconfigure c18::500a09849f62c312
   cfgadm -o unusable_SCSI_LUN -c unconfigure c19::500a09819f62c312
    
   6. Очистка дерева устройств
   devfsadm -Cv
    
   7. Обновление конфигурации vxvm
   vxdctl enable
