.. index:: brocade, firmware, san, switch

.. meta::
   :keywords: brocade, firmware, switch, san

.. _brocade-fw-update:

Brocade FW Update
=================

План работ:

1. Подключить USB накопитель
2. Подключиться к свитчу пользователем admin
3. Подключить USB накопитель в ОС свитча: ``usbStorage -e``
4. Просмотреть список файлов: ``usbstorage -l``
5. Запустить обновление ОС: ``firmwaredownload -U /usb/usbstorage/brocade/firmware/v8.2.3a``
