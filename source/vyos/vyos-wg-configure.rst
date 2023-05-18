.. index:: vyos, wireguard, vpn, client, site-to-site

.. meta::
   :keywords: vyos, wireguard, vpn, client, site-to-site

.. _vyos-wg-configure:

Клиент WireGuard в vyos
=======================

1. Создаем публичный и приватный ключи для нашего клиента

.. code-block:: none

  generate wireguard named-keypairs my-wg-client  // <-- 'my-wg-client' имя ключа


2. Настройка клиента WireGuard в VyOS 

.. code-block:: none

  set interfaces wireguard wg0 address '172.16.26.2/24'
  set interfaces wireguard wg0 description 'VPN-to-YOGA'
  set interfaces wireguard wg0 mtu '1420'
  set interfaces wireguard wg0 peer yoga address '12.345.678.90'  // <-- VPN server address
  set interfaces wireguard wg0 peer yoga allowed-ips '0.0.0.0/0'
  set interfaces wireguard wg0 peer yoga persistent-keepalive '25'
  set interfaces wireguard wg0 peer yoga port '51820'
  set interfaces wireguard wg0 peer yoga pubkey 'K3/mcVPjcM4Fg7vL1YZyALodMgE0bi2vgTUIGRGe31o='
  set interfaces wireguard wg0 port '51820'
  set interfaces wireguard wg0 private-key 'my-wg-client'

.. note::  Если требуется импортировать уже готовую пару ключей, то сделать это можно положив их в каталог `/config/auth/wireguard/my-wg-client` (seealso: `vyos-forum <https://forum.vyos.io/t/import-wireguard-private-key/6214>`_)

3. Проверяем работу туннеля при помощи команд

.. code-block:: none

  $ show interfaces wireguard
  $ show interfaces wireguard wg0


Полезные ссылки
---------------

-  `Официальная документация VyOS <https://docs.vyos.io/en/equuleus/configuration/interfaces/wireguard.html>`_
-  `Пост на форуме про импорт ключей <https://forum.vyos.io/t/import-wireguard-private-key/6214/2>`_
