.. _mikrotik-remove-huge-addresslist:

Удаление больших адресных листов
================================

В этом примере удаляется большой адресный список с именем "list-antifilter"

.. code-block:: bash

  /ip firewall address-list remove [/ip firewall address-list find list=list-antifilter]
