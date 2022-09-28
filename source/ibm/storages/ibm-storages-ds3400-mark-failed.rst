.. index:: ibm, storage, ds3400

.. _ibm-storages-ds3400-mark-failed:

DS3400. Mark Disk As Failed
===========================

Самый простой способ инициировать выполнение скрипта системой – открыть DS staroge manager, щелкунть по требуемой системе правой клавишей и выбрать из контекстного меню “Execute Script”. В открывшемся окне пишем код и жмем по необходимости Verify или Execute.

.. code-block:: bash

   set drive [enclousure,slot]
   operationalState=failed;
