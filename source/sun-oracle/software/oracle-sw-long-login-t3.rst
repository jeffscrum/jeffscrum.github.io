.. index:: oracle, solaris, login, ssh

.. meta::
   :keywords: oracle, solaris, login, ssh

.. _oracle-sw-long-login-t3:

Long Login Problem With T3
==========================

Заказчик жаловался, что при открытии консоли через SP (Service Processor) на T3-1 и ввода логина/пароля "вход" происходит очень долго (~50-60 секунд).

Проблема оказалась в драйвере виртуального USB, который подключается при логине.
Решение простое - нужо закомментировать несколько строк в /etc/logindevperm, после чего время логина сократилось до 4-5 секунд.
Закомментировать нужно вот эти строки:

.. code-block:: none

   /dev/console   0600    /dev/usb/hid[0-9]+      # hid devices should have the same permission with conskbd and consms
   /dev/console   0600    /dev/usb/[0-9a-f]+[.][0-9a-f]+/[0-9]+/* driver=scsa2usb,usb_mid,usbprn,ugen     #libusb/ugen devices