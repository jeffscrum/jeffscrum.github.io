.. index:: mikrotik, bgp

.. meta::
   :keywords: mikrotik, bgp

.. _mikrotik-antifilter-configure:

Mikrotik и antifilter.download
==============================

Более подробную информацию о сервисе вы можете посмотреть на `страничке проекта <https://antifilter.download/>`_

Сервис предлагает несколько способов получния адресов -- BGP или скриптом.

BGP
---

.. code-block:: bash

  /ip route add dst-address=45.154.73.71/32 gateway=<GATEWAY_FOR_CONNECT>
  /routing bgp instance set default as=64522 ignore-as-path-len=yes router-id=<YOUR_IP_ADDRESS>
  /routing bgp peer add hold-time=4m in-filter=bgp_in keepalive-time=1m multihop=yes name=antifilter remote-address=45.154.73.71 remote-as=65432 ttl=default
  /routing filter add action=accept chain=bgp_in comment="Set nexthop to VPN" set-in-nexthop-direct=<GATEWAY_INTERFACE>
  # Or use only selected BGP Community
  #/routing filter add action=accept chain=bgp_in bgp-communities=65432:500 comment="Set nexthop to VPN" set-in-nexthop-direct=<GATEWAY_INTERFACE>
  /routing filter add chain=bgp_in action=discard comment="Discard other"


.. note:: Команды выше подходят для настройки роутеров с ROS 6. Для настройки ROS 7 они чуть изменятся.

Скрипт
------

Добавление листа
~~~~~~~~~~~~~~~~

Для скачивания и применения листа можно воспользоваться скриптом. Новый лист будет сохранен с именем "list-antifilter"

.. literalinclude:: getlist.script
   :language: none


Удаление листа
~~~~~~~~~~~~~~

Удалить адресный лист при в CLI можно командой::
  
  /ip firewall address-list remove [/ip firewall address-list find list=list-antifilter]
