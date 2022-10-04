.. index:: exadata, lacp

.. _oracle-exadata-lacp:

Exadata LACP Configure
======================

Для того чтобы собрать LACP (Link Aggregation Control Protocol) необходимо изменить параметр BONDING_OPTS в файле `/etc/sysconfig/network-scripts/ifcfg-bondeth0`

.. code-block:: bash

   BONDING_OPTS="mode=802.3ad xmit_hash_policy=layer2 miimon=100 downdelay=200 updelay=5000 num_grat_arp=100 lacp_rate=1"

После чего необходимо перезапустить службу сети - ``service network restart``

Чтобы посмотреть статус и то как собрался LACP

.. code-block:: none

   cat /proc/net/bonding/bondeth0
    
   802.3ad info
   LACP rate: fast
   Aggregator selection policy (ad_select): stable
   Active Aggregator Info:
   Aggregator ID: 1
   Number of ports: 2
   Actor Key: 33
   Partner Key: 34627
   Partner Mac Address: 00:23:04:ee:be:c8

Если же LACP не собрался, то в вывод будет примерно таким

.. code-block:: none

   cat /proc/net/bonding/bondeth0
    
   802.3ad info
   LACP rate: slow
   Aggregator selection policy (ad_select): stable
   bond bondeth0 has no active aggregator
