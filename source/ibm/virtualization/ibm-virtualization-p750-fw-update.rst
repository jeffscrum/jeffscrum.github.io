.. index:: ibm, firmware, update, fw

.. meta::
   :keywords: ibm, firmware, update, fw

.. _ibm-virtualization-p750-fw-update:

Обновление микрокода сервера IBM p750
=====================================

Выдался случай обновить IBM p750 и записать этот процесс.

`YouTube <https://youtu.be/9Glf511xU3o>`_

Для проведения обновления через CLI:

#. Залить прошивку на HMC в каталог ``/home/hscroot/<fw_folder>`` используя SCP
#. Узнать имя обновляемой системы используя команду: ``lssyscfg -r sys -F name``
#. Запустить обновление сервера: ``updlic -m <system name> -o a -t sys -l latest -r mountpoint -d /home/hscroot/<fw_folder>``
