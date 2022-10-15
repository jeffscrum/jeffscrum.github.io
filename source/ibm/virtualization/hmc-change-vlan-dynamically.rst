.. index:: ibm, dlpar, rmc, vlan, sea, hmc

.. meta::
   :keywords: ibm, dlpar, rmc, vlan, sea, hmc

.. _hmc-change-vlan-dynamically:

Сhange VLAN on HMC dynamically (SEA)
====================================

.. note:: Сменить VLAN в профиле можно без проблем, но применится он только после перезагрузки. Поэтому, если нужно сменить VLAN для прохождения через SEA без перезагрузки, то нужно делать это из HMC CLI.

With the Virtual I/O Server Version 2.2, or later, you can add, change, or remove the existing set of VLANs for a virtual Ethernet adapter that is assigned to an active partition on a POWER7® processor-based server by using the Hardware Management Console (HMC).

Before you perform this task, ensure that you meet the following requirements:

- The server must be a POWER7 processor-based server, or later.
- The server firmware level must be at least AH720_064+ for high end servers, AM720_064+ for midrange servers, and AL720_064+ for low end servers.
  .. note:: The AL720_064+ server firmware level is only supported on POWER7 processor-based servers, or later.
- The Virtual I/O Server must be at Version 2.2, or later.
- The HMC must be at Version 7.7.2.0, with mandatory efix MH01235, or later.

You can use the HMC graphical interface or the chhwres command from the HMC command-line interface to add, remove, or modify VLANs for a virtual Ethernet adapter that is assigned to an active partition. You can also edit the IEEE standard of the virtual Ethernet adapter dynamically. To specify additional VLANs, you must set the virtual Ethernet adapter to the IEEE 802.1Q standard.


.. tip:: Смотрим список систем -- ``lssyscfg -r sys -F name``

To add, remove, or modify VLANs on the Virtual I/O Server, complete the following steps:

1. Run the lssyscfg command to verify if the managed system supports adding, removing, or modifying VLANs on the Virtual I/O Server. 
  | For example, ``lssyscfg -r sys -m <managed system> -F capabilities``. If the managed server supports adding, removing, or modifying VLANs, this command returns the virtual_eth_dlpar_capable value.

2. Use the chhwres command to add, remove, or modify additional VLANs to the virtual Ethernet adapter that is assigned to an active partition. You can also edit the IEEE standard of the virtual Ethernet adapter dynamically by using the chhwres command. For example,
   
   - In this example, the VLAN ID 5 is added to the existing VLAN IDs for the virtual Ethernet adapter, and the virtual Ethernet adapter is set to the IEEE 802.1Q standard.

    ``chhwres -r virtualio --rsubtype eth -m <managed system> -o s {-p <partition name> | --id <partition ID>} -s <virtual slot number> -a "addl_vlan_ids+=5,ieee_virtual_eth=1"``
  
  - In this example, the VLAN ID 6 is removed from the existing VLAN IDs for the virtual Ethernet adapter.

    ``chhwres -r virtualio --rsubtype eth -m <managed system> -o s {-p <partition name> | --id <partition ID>} -s <virtual slot number> -a "addl_vlan_ids-=6"``

  - In this example, the VLAN IDs 2, 3, and 5 are assigned to the virtual Ethernet adapter instead of the existing VLAN IDs.

    ``chhwres -r virtualio --rsubtype eth -m <managed system> -o s {-p <partition name> | --id <partition ID>} -s <virtual slot number> -a "addl_vlan_ids=2,3,5"``

    You can provide a comma-separated list of VLANs to the attributes, ``addl_vlan_ids=``, ``addl_vlan_ids+=``, and ``addl_vlan_ids-=``.

3. Use the lshwres command to query the virtual Ethernet adapter.
   
   ``lshwres -m <server> -r virtualio --rsubtype eth --level lpar -F``

.. note:: Example

   ``chhwres -r virtualio --rsubtype eth -m Server-9119-FHB-3-SN841D387 -o s --id 1 -s 24 -a "addl_vlan_ids+=226"``


------

Related Links: https://www.ibm.com/support/knowledgecenter/en/8247-21L/p8hb1/p8hb1_vios_managing_vlans.htm
