.. index:: sun, oracle, exadata, ib, infiniband, AutomaticHighErrorRate, error, disabled

.. meta::
   :keywords: sun, oracle, exadata, ib, infiniband, AutomaticHighErrorRate, error, disabled

.. _exadata-ib-AutomaticHighErrorRate:

.. TASK08718144

Exadata. Разблокировка IB порта AutomaticHighErrorRate
======================================================

На коммутаторе exasw-ibb01 порт 8 (14B) заблокирован вследствие накопленных ошибок. Давайте сбросим счетчик ошибок, разблокируем порт и через помониторим сервер пару недель на предмет появления ошибок вновь. 

.. code-block:: none

   ibqueryerrors.out:
   Errors for "exa2dbadm01 S 192.168.11.110,192.168.11.111 HCA-1"
      GUID 0x10e0000192ab51 port 1: [VL15Dropped == 232] [PortXmitWait == 4294967295]
   
   @conf@disabledports.conf:
   Switch 8 AutomaticHighErrorRate
   
   @usr@local@diag@listlinkup.out:
   Connector 14B Present <-> Switch Port 08 is down (AutomaticHighErrorRate)


Для того чтобы снова включить его проделайте следующее:

.. code-block:: none

   Команды выполняются на свитче exasw-ibb01 под пользователем root:
   
   	  1. Удалите порт из листа автоблокировки:
   	  # autodisable del 14B H
   	  # autodisable del 14B L
   	
   	  2. Проверьте что порт 14B удален:
   	  # autodisable list
   	  
   	  3. Очистка ошибок в фабрике
   	  # ibdiagnet -pc
   	  
   	  4. Добавление порта в список автоблокировки
   	  # autodisable add 14B H
   	  # autodisable add 14B L
   	  
   	  5. Проверьте что порт 14B добавлен:
   	  # autodisable list
   	  
   	  6. Включение порта обратно
   	  # enableswitchport --automatic 14B
   	  
   	  7. Проверка статуса порта (AdminState и LinkState должны быть "Active", а PhysLinkState должен быть "LinkUp".)
   	  # getportstatus 14B
   
   Команды выполняются на сервере exa2dbadm01:
   
   	  8. Зайдите на сервер exa2dbadm01 и проверьте стутус обоих портов (оба должны быть "Active" и "LinkUp").
   	  # ibstat


----

Related Links:
 - Compute Node/Storage Nodes IB Ports State Shown as "Down" Along with Infiniband Switch Ports Status Showing "Switch Port <X> down (AutomaticHighErrorRate)" Message (Doc ID 2399231.1)
 - Data Collection For Troubleshooting Symbol Errors, Cabling, Switch Port Issues On Infiniband Switches (Doc ID 2413588.1)