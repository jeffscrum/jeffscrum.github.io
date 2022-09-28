.. index:: ibm, storage, ds3400

.. _ibm-storages-ds3400-resync-progress:

DS3400. Show Logical Drive Progress
===================================

Самый простой способ инициировать выполнение скрипта системой – открыть DS staroge manager, щелкунть по требуемой системе правой клавишей и выбрать из контекстного меню “Execute Script”. В открывшемся окне пишем код и жмем по необходимости Verify или Execute.

.. code-block:: bash

   show logicalDrive ["logical_drive_name"] actionProgress;

Просмотр списка дисков

.. code-block:: bash

   show allDrives summary;

Просмотр списка логических томов

.. code-block:: bash

   show allLogicalDrives summary;
