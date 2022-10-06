.. index:: oracle, solaris, suntrunk

.. meta::
   :keywords: oracle, solaris, suntrunk

.. _oracle-sw-suntrunk:

Port trunk при помощи SUN Trunking
==================================

1. Скачиваем Sun Trunking 1.3 (p10264589_130_SOLARIS64.zip)
2. Скачиваем Patch 121181-06: Sun Trunking Utility 1.3:maintenance patch
3. Устанавливаем Sun Trunking 1.3

  .. code-block:: none
  
     unzip p10264589_130_SOLARIS64.zip
     unzip Sun_Trunking_1.3_s10_2.zip
     cd Sun_Trunking_1.3_s10_2/
     ./install

4. Проверяем что пакет установился

  .. code-block:: none
  
     pkginfo -l SUNWtrku
     pkginfo -l SUNWtrkm

5. Устанавливаем патч 121181-06 и перезагружаемся

  .. code-block:: none

     patchadd /var/spool/patch/123456-07
     init 6

6. Пробуем собрать транк

  .. code-block:: none

     nettr -setup 10 device=ce members=2,3,4,5 policy=3

7. Проверяем

  .. code-block:: none

     nettr -conf
      
     Key: 10; Policy: 3;
     Aggr MAC address: 01:23:ab:45:c6:72
     Name    Original-Mac-Addr   Speed   Duplex   Link Status
     ----    -----------------   -----   ------   ---- ------
     ce2     01:23:ab:45:c6:72     1000    full     up    enb
     ce3     01:23:ab:45:c6:73     1000    full     up    enb
     ce4     01:23:ab:45:c6:74     1000    full     up    enb
     ce5     01:23:ab:45:c6:75     1000    full     up    enb

8. Если все собралось, то сразу записываем команду в файлик `/etc/opt/SUNWconn/bin/nettr.sh`

  .. code-block:: bash
  
     #Add Sun Trunking Configuration entries below.
     nettr -setup 10 device=ce members=2,3,4,5 policy=3 lacp=p ptimer=1

9. Теперь можно настраивать интерфесы

  .. code-block:: bash

     ifconfig ce2 plumb 10.1.35.35 up
