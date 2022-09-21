.. index:: mikrotik

.. _mikrotik-port-forward-cli:

Mikrotik Port Forward
=====================

.. code-block:: bash

   /ip firewall nat add chain=dstnat action=dst-nat to-addresses=192.168.0.12 to-ports=8123 protocol=tcp dst-port=8123 comment="some-comment-here"
   /ip firewall nat add chain=dstnat action=dst-nat to-addresses=192.168.0.6 to-ports=445 protocol=tcp dst-port=445 comment="some-comment-here" in-interface-list=WAN
