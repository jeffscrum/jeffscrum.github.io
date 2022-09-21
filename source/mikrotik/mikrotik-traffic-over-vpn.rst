.. _mikrotik-traffic-over-vpn:

Направляем траффик через VPN
============================

Может сложиться ситуация, когда траффик до какого-то сервера (группы серверов) нужно направить в туннель, а не через шлюз по-умолчанию.

В моем примере настраивается L2TP-туннель до удаленного сервера, после чего пакеты до серверов из определенного адресного листа перенаправляются в этот туннель

.. code-block:: bash

  /interface l2tp-client
  add name="apu_l2tp" connect-to=123.45.67.8 user="my_vpn_user" password="vpn_user_password" profile=default-encryption add-default-route=no allow=pap,chap,mschap1,mschap2 disabled=no
    
  /ip firewall address-list
  add address 8.8.8.8 disabled=no list=2VPN comment="nakarte.me"
   
  /ip firewall mangle
  add chain=prerouting dst-address-list=2VPN action=mark-routing new-routing-mark=Through_VPN comment=2VPN
   
  /ip route
  add dst-address=0.0.0.0/0 gateway=apu_l2tp routing-mark=Through_VPN
   
  /ip firewall nat 
  add chain=srcnat src-address=192.168.0.0/24 out-interface=apu_l2tp action=masquerade

В список можно добавлять как IP-адреса, так и hostname сервера, а роутер сам подставит IP.

Если потребуется добавить ещё один сервер, то достаточно будет выполнить ``add address 8.8.8.8 disabled=no list=2VPN comment="google.com"``. Добавлять нужно в тот же лист, так как пакеты именно до серверов из него будут отправляться в туннель.

.. note::
  
  Не забудь настроить masquerade на удаленном сервере ;)
