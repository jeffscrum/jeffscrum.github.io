.. index:: exadata, serial

.. meta::
   :keywords: exadata, serial

.. _oracle-exadata-get-serial:

Как найти серийный номер Exadata
================================

Exadata Machine
---------------

Просмотр серийного номера комплекса целиком

.. code-block:: none

  [root@exadbadm01 ~]# ipmitool sunoem cli "show /SP system_identifier" | grep "system_identifier ="
  system_identifier = Exadata Database Machine X8-2 AK00XXXXXX
  [root@exadbadm01 ~]#

Compute Nodes
-------------

Просмотр серийных номеров db-серверов

.. code-block:: none

  [root@exadbadm01 ~]# dcli -g /opt/oracle.SupportTools/onecommand/dbs_group -l root dmidecode -s system-serial-number
  exadbadm01: 1514NMXXXX
  exadbadm02: 1514NMXXXX
  [root@exadbadm01 ~]#

Storage Cells
-------------

Просмотр серийных номеров cell-серверов

.. code-block:: none

  [root@exadbadm01 ~]# dcli -g /opt/oracle.SupportTools/onecommand/cell_group -l root dmidecode -s system-serial-number
  exaceladm01: 1515NMXXXX
  exaceladm02: 1515NMXXXX
  exaceladm03: 1515NMXXXX
  [root@exadbadm01 ~]#


InfiniBand
----------

Просмотр серийных номеров infiniband-свитчей

.. code-block:: none

  [root@exadbadm01 ~]# dcli -g /opt/oracle.SupportTools/onecommand/ib_group -l root showfruinfo | grep -a Sun_Serial_Number
  exasw-iba01: Sun_Serial_Number : XXXXXXT+1512RRXXXX
  exasw-iba01: Sun_Serial_Number : AK0029XXXX
  exasw-ibb01: Sun_Serial_Number : XXXXXXT+1512RRXXXX
  exasw-ibb01: Sun_Serial_Number : AK0029XXXX
  [root@exadbadm01 ~]#
