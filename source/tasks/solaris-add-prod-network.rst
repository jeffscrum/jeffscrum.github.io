.. index:: solaris, ipmp, network, zone, ldom, net, vnet

.. meta::
   :keywords: solaris, ipmp, network, zone, ldom, net, vnet

.. _solaris-add-prod-network:

How to add production network in LDom
=====================================

.. code:: none

   Проверяем разрешены ли нужные VLAN на виртуальных свитчах
   ldm list-services primary
   ldm list-services IO-domain
    
   Если требуется добавляем нужный vlan (при этом указывая все осльные если они есть)
   ldm set-vswitch vid=135,171,175 pr-vsw-prod3       
   ldm set-vswitch vid=135,171,175 pr-vsw-prod4
   ldm set-vswitch vid=135,171,175 sec-vsw-prod3      
   ldm set-vswitch vid=135,171,175 sec-vsw-prod4 
    
   Добавляем сетевые интерфейсы домену, указывая на них нужный VLAN
   ldm add-vnet vid=171 vnet2 pr-vsw-prod2 ld1
   ldm add-vnet vid=171 vnet3 pr-vsw-prod2 ld1
   ldm add-vnet vid=171 vnet4 sec-vsw-prod1 ld1
   ldm add-vnet vid=171 vnet5 sec-vsw-prod2 ld1
    
   В LD-1 домене проверяем что интерфейсы появились
   dladm show-link
    
   Конфигурим vlan
   dladm create-vlan -l net2 -v [171]
   dladm create-vlan -l net3 -v [171]
   dladm create-vlan -l net4 -v [vlan]
   dladm create-vlan -l net5 -v [vlan]
    
   Проверяем что новые интерфейсы появились
   dladm show-vlan
    
   Настройка IPMP:
   ipadm create-ipmp ipmp[vlan]
   ipadm create-ip net[vlan]002
   ipadm create-ip net[vlan]003
   ipadm create-ip net[vlan]004
   ipadm create-ip net[vlan]005
   ipadm add-ipmp -i net[vlan]002 -i net[vlan]003 -i net[vlan]004 -i net[vlan]005 ipmp[vlan]
   ipadm create-addr -T static -a 10.4.28.240/24 ipmp[vlan]/prod  
   ipadm set-ifprop -p standby=on -m ip net171003
   ipadm set-ifprop -p standby=on -m ip net171004
   ipadm set-ifprop -p standby=on -m ip net171005
     
   svccfg -s svc:/network/ipmp setprop config/transitive-probing=true
   svcadm refresh svc:/network/ipmp:default
   route -p add default 10.4.28.1 -ifp ipmp171
     
   svccfg -s svc:/network/dns/client setprop
   config/nameserver=net_address: '(10.30.33.152 10.30.33.100 10.30.33.156 10.4.27.7 10.30.33.154 10.4.27.6)'
   svccfg -s svc:/system/name-service/switch setprop config/host = '("files dns")'
   svcadm refresh svc:/system/name-service/switch
