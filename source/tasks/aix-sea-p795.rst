.. index:: ibm, aix, sea, vio

.. meta::
   :keywords: ibm, aix, sea, vio

.. _aix-sea-p795:

План настройки SEA на p795-1
============================

Действия на VIOS01
------------------

.. code-block:: none

  1. Создаем EtherChannel из ent1 (U5803.001.88125Z6-P1-C1-T2) ==> ent8
  2. Для обслуживания LPAR'ов и control_channel'а используем уже существующие виртуальные адаптеры ent4(adapter_id 2) и ent7(adapter_id 64)
  3. Создаем SEA на основе etherchannel ent8, виртуального ent4, control_channel ent7 и PVID=1. ==> ent9
  # mkvdev -sea ent8 -vadapter ent4 -default ent4 -defaultid 1 -attr ha_mode=auto ctl_chan=ent7
  4. Назначаем IP адрес 192.168.134.250 на интерфейс en9
  $ mktcpip -hostname vios01 -interface en9 -inetaddr 192.168.134.250 -netmask 255.255.255.0 -gateway 192.168.134.1 -s
  5. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent4 устанавливаем галочку 802.1q и дабавляем VLAN 412, 413. Так же ставим галочку, разрешающую этому интерфейсу доступ во внешнюю сеть и Priority=1. VSwitch=ETHERNET0.
  6. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent7 устанавливаем PVID 99 (control_channel). VSwitch=ETHERNET0.
  7. Создаем вспомогательные интерфейсы VIOS для работы с VLAN 412, 413
  $ mkvdev –vlan ent9 –tagid 412 (==> ent10)
  $ mkvdev –vlan ent9 –tagid 413 (==> ent11)
  8. Из интерфейса HMC создаем новый виртуальный свитч - ETHERNET1.
  9. Создаем EtherChannel из ent2 (U5803.001.88125Z6-P1-C1-T3) ==> ent12
  10. Из интерфейса HMC создаем 2 новых виртуальных ethrenet-адаптера. ==> ent13 (для обслуживания LPAR'ов) и ent14 (control_channel)
  11. Создаем SEA на основе etherchannel ent12, виртуального ent13, control_channel ent14 и PVID=2. ==> ent15
  # mkvdev -sea ent12 -vadapter ent13 -default ent13 -defaultid 2 -attr ha_mode=auto ctl_chan=ent14
  12. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent13 устанавливаем галочку 802.1q и дабавляем VLAN 499. Так же ставим галочку, разрешающую этому интерфейсу доступ во внешнюю сеть и Priority=1. VSwitch=ETHERNET1.
  13. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent14 устанавливаем PVID 98 (control_channel). VSwitch=ETHERNET1.
  14. Создаем вспомогательные интерфейсы VIOS для работы с VLAN 499
  $ mkvdev –vlan ent15 –tagid 499 (==> ent16)
  15. Из интерфейса HMC создаем новый виртуальный свитч - ETHERNET2.
  16. Создаем EtherChannel из ent2 (U5803.001.88125Z6-P1-C1-T4) ==> ent17
  17. Из интерфейса HMC создаем 2 новых виртуальных ethrenet-адаптера. ==> ent18 (для обслуживания LPAR'ов) и ent19 (control_channel)
  18. Создаем SEA на основе etherchannel ent17, виртуального ent18, control_channel ent19 и PVID=3. ==> ent20
  # mkvdev -sea ent17 -vadapter ent18 -default ent18 -defaultid 3  -attr ha_mode=auto ctl_chan=ent19
  19. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent18 устанавливаем галочку 802.1q и дабавляем VLAN 411. Так же ставим галочку, разрешающую этому интерфейсу доступ во внешнюю сеть и Priority=1. VSwitch=ETHERNET2.
  20. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent19 устанавливаем PVID 97 (control_channel). VSwitch=ETHERNET2.
  21. Создаем вспомогательные интерфейсы VIOS для работы с VLAN 411
  $ mkvdev –vlan ent20 –tagid 411 (==> ent21)


Действия  на VIOS02
-------------------

.. code-block:: none

  1. Создаем EtherChannel из ent1 (U5803.001.881057Z-P1-C1-T2) ==> ent8
  2. Для обслуживания LPAR'ов и control_channel'а используем уже существующие виртуальные адаптеры ent6(adapter_id 22) и ent7(adapter_id 63)
  3. Создаем SEA на основе etherchannel ent8, виртуального ent6, control_channel ent7 и PVID=1. ==> ent9
  # mkvdev -sea ent8 -vadapter ent6 -default ent6 -defaultid 1  -attr ha_mode=auto ctl_chan=ent7
  4. Назначаем IP адрес 192.168.134.251 на интерфейс en9
  $ mktcpip -hostname vios01 -interface en9 -inetaddr 192.168.134.251 -netmask 255.255.255.0 -gateway 192.168.134.1 -s
  5. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent6 устанавливаем галочку 802.1q и дабавляем VLAN 412, 413. Так же ставим галочку, разрешающую этому интерфейсу доступ во внешнюю сеть и Priority=1. VSwitch=ETHERNET0.
  6. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent7 устанавливаем PVID 99 (control_channel). VSwitch=ETHERNET0.
  7. Создаем вспомогательные интерфейсы VIOS для работы с VLAN 412, 413
  $ mkvdev –vlan ent9 –tagid 412 (==> ent10)
  $ mkvdev –vlan ent9 –tagid 413 (==> ent11)
  8. Из интерфейса HMC создаем новый виртуальный свитч - ETHERNET1.
  9. Создаем EtherChannel из ent2 (U5803.001.881057Z-P1-C1-T3) ==> ent12
  10. Из интерфейса HMC создаем 2 новых виртуальных ethrenet-адаптера. ==> ent13 (для обслуживания LPAR'ов) и ent14 (control_channel)
  11. Создаем SEA на основе etherchannel ent12, виртуального ent13, control_channel ent14 и PVID=2. ==> ent15
  # mkvdev -sea ent12 -vadapter ent13 -default ent13 -defaultid 2  -attr ha_mode=auto ctl_chan=ent14
  12. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent13 устанавливаем галочку 802.1q и дабавляем VLAN 499. Так же ставим галочку, разрешающую этому интерфейсу доступ во внешнюю сеть и Priority=1. VSwitch=ETHERNET1.
  13. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent14 устанавливаем PVID 98 (control_channel). VSwitch=ETHERNET1.
  14. Создаем вспомогательные интерфейсы VIOS для работы с VLAN 499
  $ mkvdev –vlan ent15 –tagid 499 (==> ent16)
  15. Из интерфейса HMC создаем новый виртуальный свитч - ETHERNET2.
  16. Создаем EtherChannel из ent2 (U5803.001.881057Z-P1-C1-T4) ==> ent17
  17. Из интерфейса HMC создаем 2 новых виртуальных ethrenet-адаптера. ==> ent18 (для обслуживания LPAR'ов) и ent19 (control_channel)
  18. Создаем SEA на основе etherchannel ent17, виртуального ent18, control_channel ent19 и PVID=3. ==> ent20
  # mkvdev -sea ent17 -vadapter ent18 -default ent18 -defaultid 3  -attr ha_mode=auto ctl_chan=ent19
  19. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent18 устанавливаем галочку 802.1q и дабавляем VLAN 411. Так же ставим галочку, разрешающую этому интерфейсу доступ во внешнюю сеть и Priority=1. VSwitch=ETHERNET2.
  20. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent19 устанавливаем PVID 97 (control_channel). VSwitch=ETHERNET2.
  21. Создаем вспомогательные интерфейсы VIOS для работы с VLAN 411
  $ mkvdev –vlan ent20 –tagid 411 (==> ent21)


Действия  на lp08
-------------------

.. code-block:: none

  1. Создаем новый виртуальный ethernet-адаптер ent4
  2. Из интерфейса HMC для виртуального ethernet-адаптера, соответствующего ent4 устанавливаем VLAN 499 VSwitch=ETHERNET1.
  3. Удаляем текущий IP адрес
  # smit rmtcpip
  4. Назначаем IP адрес 192.168.134.xxx на интерфейс en4
  # smit mktcpip
  5. В случае, если сетевой доступ работает удаляем все интерфейсы, удерживающие карты 8Z-P2-C4 и K6-P2-C4
  # rmdev -dl enX
  # rmdev -dl entX
  6. Удаляем адаптеры 8Z-P2-C4 и K6-P2-C4 из профиля LPAR'а.
  7. Удаляем адаптеры 8Z-P2-C4 и K6-P2-C4 из динамических ресурсов LPAR'а.


Действия  на VIOS01
-------------------

.. code-block:: none

  1. Добавляем адаптер 8Z-P2-C4 в профиль VIOS'а
  2. Добавляем адаптер 8Z-P2-C4 в динамические ресурсы VIOS'а (==> ent22, ent23, ent24, ent25)
  3. Добавляем соответствующие пары backup-каналов для имеющихся SEA:
  /usr/lib/methods/ethchan_config -a -b ent8 ent23
  /usr/lib/methods/ethchan_config -a -b ent12 ent24
  /usr/lib/methods/ethchan_config -a -b ent17 ent25


Действия  на VIOS02
-------------------

.. code-block:: none

  1. Добавляем адаптер K6-P2-C4 в профиль VIOS'а
  2. Добавляем адаптер K6-P2-C4 в динамические ресурсы VIOS'а (==> ent22, ent23, ent24, ent25)
  3. Добавляем соответствующие пары backup-каналов для имеющихся SEA:
  /usr/lib/methods/ethchan_config -a -b ent8 ent23
  /usr/lib/methods/ethchan_config -a -b ent12 ent24
  /usr/lib/methods/ethchan_config -a -b ent17 ent25


Действия  на lp13
-------------------

.. code-block:: none

 1. Используем имеющиеся виртуальные ethernet-адаптеры ent0 (adapter_id 6) и ent1(adapter_id 7)
 2. Для виртуального адаптера, соответствующего ent0 устанавливаем VLAN 422. VSwitch=ETHERNET0
 3. Для виртуального адаптера, соответствующего ent1 устанавливаем VLAN 499. VSwitch=ETHERNET1


Действия  на lp14
-------------------

.. code-block:: none

  1. Используем имеющиеся виртуальные ethernet-адаптеры ent0 (adapter_id 6) и ent1(adapter_id 7)
  2. Для виртуального адаптера, соответствующего ent0 устанавливаем VLAN 411. VSwitch=ETHERNET2
  3. Для виртуального адаптера, соответствующего ent1 устанавливаем VLAN 499. VSwitch=ETHERNET1


Действия  на lp15
-------------------

.. code-block:: none

  1. Используем имеющиеся виртуальные ethernet-адаптеры ent0 (adapter_id 6) и ent1(adapter_id 7)
  2. Для виртуального адаптера, соответствующего ent0 устанавливаем VLAN 413. VSwitch=ETHERNET0
  3. Для виртуального адаптера, соответствующего ent1 устанавливаем VLAN 499. VSwitch=ETHERNET1


Действия  на lp16
-------------------

.. code-block:: none

  1. Используем имеющиеся виртуальные ethernet-адаптеры ent0 (adapter_id 6) и ent1(adapter_id 7)
  2. Для виртуального адаптера, соответствующего ent0 устанавливаем VLAN 411. VSwitch=ETHERNET2
  3. Для виртуального адаптера, соответствующего ent1 устанавливаем VLAN 499. VSwitch=ETHERNET1


Действия  на lp17
-------------------

.. code-block:: none

  1. Используем имеющиеся виртуальные ethernet-адаптеры ent0 (adapter_id 6) и ent1(adapter_id 7)
  2. Для виртуального адаптера, соответствующего ent0 устанавливаем VLAN 412. VSwitch=ETHERNET0
  3. Для виртуального адаптера, соответствующего ent1 устанавливаем VLAN 499. VSwitch=ETHERNET1
