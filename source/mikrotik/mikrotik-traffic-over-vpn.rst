.. index:: mikrotik, vpn, list, l2tp

.. meta::
   :keywords: mikrotik, vpn, list, l2tp

.. _mikrotik-traffic-over-vpn:

Направляем траффик через VPN
============================

Может сложиться ситуация, когда траффик до какого-то сервера (группы серверов) нужно направить в туннель, а не через шлюз по-умолчанию.

В моем примере настраивается L2TP-туннель до удаленного сервера, после чего пакеты до серверов из определенного адресного листа перенаправляются в этот туннель. 

.. code-block:: bash

  /interface l2tp-client
  add name="apu_l2tp" connect-to=123.45.67.8 user="my_vpn_user" password="vpn_user_password" profile=default-encryption add-default-route=no allow=pap,chap,mschap1,mschap2 disabled=no

  /ip firewall mangle
  add action=mark-routing chain=prerouting dst-address-list=2VPN new-routing-mark=Through_VPN passthrough=no
  
  /ip route
  add distance=1 gateway=apu_l2tp routing-mark=Through_VPN
  
  /ip route rule
  add action=lookup-only-in-table routing-mark=Through_VPN table=Through_VPN
  
  /ip firewall nat
  add action=masquerade chain=srcnat out-interface=apu_l2tp src-address=192.168.88.0/24
  
  /ip firewall address-list
  add address=2ip.ru list=2VPN comment="2ip.ru for testing"

В список можно добавлять как IP-адреса, так и hostname сервера, а роутер сам подставит IP.

Если потребуется добавить ещё один адрес, то достаточно будет выполнить ``add address 8.8.8.8 disabled=no list=2VPN comment="google.com"``. Добавлять нужно в тот же лист, так как пакеты именно до серверов из него будут отправляться в туннель.

.. note::
  
  Не забудь настроить masquerade на удаленном сервере ;)
