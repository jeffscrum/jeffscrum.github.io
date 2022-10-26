.. index:: mikrotik, cloud, install

.. meta::
   :keywords: mikrotik, cloud, install

.. _mikrotik-install-cloud-router:

Install Mikrotik Cloud Router
=============================

.. code-block:: bash

   # Configure LiveCD network
   ifconfig ens3 123.45.67.89 netmask 255.255.255.0 up
   ip route add default via 123.45.67.1
   echo "nameserver 8.8.8.8" >> /etc/resolv.conf
   /sbin/sshd
   passwd root


   # Install RouterOS
   cd /tmp
   wget https://download.mikrotik.com/routeros/7.2/chr-7.2.img.zip
   unzip chr-7.2.img.zip
   dd if=chr-7.2.img of=/dev/vda bs=4M oflag=sync
   /ip address add address=123.45.67.89/24 interface="ether1"
   /ip route add check-gateway=ping distance=1 gateway=123.45.67.1
   /ip dns set servers=8.8.8.8,1.1.1.1

После чего не забываем добавить :ref:`mikrotik-default-fw-rules`
