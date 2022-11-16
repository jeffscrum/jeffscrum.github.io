.. index:: emc, vmax, cmd, port, disk

.. meta::
   :keywords: emc, vmax, cmd, port, disk

.. _vmax-usefull-cmds:

VAMX. Usefull Commands
=======================

#. Посмотреть masking view ``symaccess -sid 966 list view``
#. Посмотреть содержимое port-группы ``symaccess -sid 966 show PG_Task1 -type port``
#. Добавить порты в группу ``symaccess -sid 966 -type port -name PG_Task1 add -dirport 8e:1,7f:0,10e:0``
#. Посмотреть информацию по диску ``symdev -sid 966 show 02E5``
#. Посмотреть состояние массива

  .. code-block:: none
  
     symcfg -sid 307 list -env_data -v |grep Failed
     symdisk list -sid 307 -failed
     symevent -sid 307 list