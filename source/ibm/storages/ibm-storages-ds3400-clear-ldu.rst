.. index:: ibm, storage, ds3400

.. meta::
   :keywords: ibm, storage, ds3400, drive, failed

.. _ibm-storages-ds3400-clear-ldu:

DS3400. Clear Logical Drive Unreadable Sectors
==============================================

Самый простой способ инициировать выполнение скрипта системой – открыть DS staroge manager, щелкунть по требуемой системе правой клавишей и выбрать из контекстного меню “Execute Script”. В открывшемся окне пишем код и жмем по необходимости Verify или Execute.

.. code-block:: bash

   clear allLogicalDrives unreadableSectors;
