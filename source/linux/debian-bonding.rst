.. index:: linux, debian, bonding

.. _debian-bonding:

Debian Bonding (active-backup)
==============================

.. code-block:: bash

   sudo apt-get install ifenslave
    
   Add to /etc/network/interfaces:
    
   # Frontend bond interface
   auto bond0
   iface bond0 inet static
     address 192.168.0.11/24
     gateway 192.168.0.1
     bond-slaves enp1s0 enp3s0
     bond-mode active-backup
     bond-miimon 100
     bond-primary enp1s0 enp3s0