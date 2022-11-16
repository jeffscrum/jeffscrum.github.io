.. index:: emc, vmax, check

.. meta::
   :keywords: emc, vmax, check

.. _vmax-checkscript:

VMAX. Скрипт проверки состояния массивов
========================================

.. code-block:: bash

   #!/bin/sh
   # Jeff Scrum
   # Version: 1
   VMAX1=906
   VMAX2=129
   VMAX3=157
   #symcfg discover
   echo "++++++++++++++++++++++++++++++++++++++++++++++++"
   echo "+ VMAX-1 (CK292503906) checking in progress... + "
   echo "+++++++++++++++++++1+++++++++++++++++++++++++++++"
   echo "Failed disks:"
   symdisk list -sid $VMAX1 -failed
   echo "Failed components:"
   symcfg -sid $VMAX1 list -env_data -v |grep Failed
   #symevent -sid $VMAX1 list | tail -25
   echo
   echo
   echo "++++++++++++++++++++++++++++++++++++++++++++++++"
   echo "+ VMAX-2 (CK292503129) checking in progress... + "
   echo "++++++++++++++++++++++++++++++++++++++++++++++++"
   echo "Failed disks:"
   symdisk list -sid $VMAX2 -failed
   echo "Failed components:"
   symcfg -sid $VMAX2 list -env_data -v |grep Failed
   #symevent -sid $VMAX2 list | tail -25
   echo
   echo
   echo "++++++++++++++++++++++++++++++++++++++++++++++++"
   echo "+ VMAX-3 (CK292503157) checking in progress... + "
   echo "++++++++++++++++++++++++++++++++++++++++++++++++"
   echo "Failed disks:"
   symdisk list -sid $VMAX3 -failed
   echo "Failed components:"
   symcfg -sid $VMAX3 list -env_data -v |grep Failed
   #symevent -sid $VMAX3 list | tail -25
