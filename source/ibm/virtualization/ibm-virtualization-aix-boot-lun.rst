.. index:: ibm, aix, boot, emc, vmax

.. meta::
   :keywords: ibm, aix, boot, emc, vmax

.. _ibm-virtualization-aix-boot-lun:

Как узнать с какого из VMAX отдан лун
=====================================

Если нужно определить с которого из массивов EMC Symmetrix отдан лун (в случае если массивов несколько, а посмотреть с их стороны нельзя), то определить это можно из AIX.

Для этого необходимо на хосте, где установлен Symcli посмотреть список доступных массивов “symcfg list”. В этом выводе нас будут интересовать 4 последние цифры серийного номера массива – это SymmID.

.. code-block:: bash

  root@pServer-lp01:~# symcfg list
                                  S Y M M E T R I X
                                         Mcode    Cache      Num Phys  Num Symm
      SymmID       Attachment  Model     Version  Size (MB)  Devices   Devices
      000292603121 Local       VMAX10K   5876       57344        34      5748
      000292604212 Local       VMAX20K   5876       86016        33      3889
      000292601201 Local       VMAX40K   5876      172032        22      2573

Теперь, на AIX’е нам нужно посмотреть вывод команды “lscfg -vsp -l hdisk79”. Найдя нужный нам hdisk смотрим его “EC Level” и соответствующие ей цифры. Последние 4 цифры тоже будут указывать на SymmID.

.. code-block:: bash

  root@pServer-lp01:~# lscfg -vsp -l hdisk79
   hdisk79          U9119.FHB.00C0CC0-V10-C10-T1-W5000000001112222-L17000000000000
         EMC Symmetrix FCP MPIO VRAID
         Manufacturer................EMC
         Machine Type and Model......SYMMETRIX
         ROS Level and ID............5876
         Serial Number...............71V0D000
         Part Number.................000000000000400D49000292
         EC Level....................604212
         LIC Node VPD................0V0D
         Device Specific.(Z0)........10
         Device Specific.(Z1)........40
         Device Specific.(Z2)........000000300D9C09000260019C
         Device Specific.(Z3)........12000000
         Device Specific.(Z4)........54130000
         Device Specific.(Z5)........4F80
         Device Specific.(Z6)........45

Отсюда видно, что диск hdisk79 был отдан с массива VMAX20K с серийным номером CK292604212
