.. index:: oracle, mx000, xscf

.. _oracle-hw-xscf-snapshot:

How to collect XSCF snapshot
==================================

Очень часто для диагностики требуется собрать снапшот с системного контроллера. Что бы его собрать, нужно зайти в XSCF и выполнить следующую команду:

Mx000
~~~~~

1. Собрать и выложить по сети

  .. code-block:: none
  
     XSCF> snapshot -L F -t <username>@<hostname or IP addr>:<location to write to>

2. Собрать и выложить на USB флешку

  .. code-block:: none

     XSCF> snapshot -L F -d usb0

M10-x
~~~~~

1. Собрать и выложить по сети

  .. code-block:: none
  
     XSCF> snapshot -a -L F -t <username>@<hostname or IP addr>:<location to write to>

2. Собрать и выложить на USB флешку

  .. code-block:: none

     XSCF> snapshot -a -L F -d usb0


.. tip::

   * Используйте IP-адрес, а не hostname
   * USB флешка должна быть с FAT32