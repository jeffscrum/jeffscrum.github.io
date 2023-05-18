.. index:: vyos, wireguard, vpn, client, nat

.. meta::
   :keywords: vyos, wireguard, vpn, client, nat

.. _vyos-forwarding-single-host-wan-traffic-via-vpn:

Заворачиваем весь трафик от хоста в VPN
=======================================

Настройка нужна, если вам нужно заворачивать весь трафик с одного компьютера в VPN. В моем случае WireGuard. Настройку WireGuard туннеля можно посмотреть в другой статье (:ref:`vyos-wg-configure`).

Сеть 192.168.0.0/24
Весь трафик от адреса 192.168.0.5 будет заворачиваться в VPN.

.. code-block:: none

  interfaces {
      ethernet eth1 {
          address 192.168.0.13/24
          description LAN
          policy {
              route LAN-POLICY-BASED-ROUTING
          }
      }

  protocols {
      static {
          table 10 {
              interface-route 0.0.0.0/0 {
                  next-hop-interface wg0 {
                  }
              }
          }
      }
  }

  policy {
      route LAN-POLICY-BASED-ROUTING {
          rule 10 {
              set {
                  table 10
              }
              source {
                  address 192.168.0.5/32
              }
          }
      }
  }


.. code-block:: none

  set protocols static table 10 interface-route 0.0.0.0/0 next-hop-interface wg0

  set policy route LAN-POLICY-BASED-ROUTING rule 10 set table '10'
  set policy route LAN-POLICY-BASED-ROUTING rule 10 source address '192.168.0.5/32'

  set nat source rule 20 outbound-interface 'wg0'
  set nat source rule 20 translation address 'masquerade'

  set interfaces ethernet eth1 policy route 'LAN-POLICY-BASED-ROUTING'



Полезные ссылки
---------------

-  `Пост на форуме vyos <https://forum.vyos.io/t/solved-forwarding-single-host-wan-traffic-via-vpn/5192/2>`_
