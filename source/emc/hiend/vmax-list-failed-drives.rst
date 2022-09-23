.. index:: emc, vmax, failed

.. _vmax-list-failed-drives:

VMAX. Просмотр неисправных дисков
=================================

.. code-block:: bash

  symdisk -sid 1234 list -failed

Команду можно выполнить как на хосте с установленным Solutions Enabler (SE), так и на SP самого массива (в этом случае ``-sid`` не нужен).