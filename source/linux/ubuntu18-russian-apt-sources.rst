.. index:: linux, ubuntu, apt

.. _ubuntu18-russian-apt-sources:

Russian apt-sources in Ubuntu 18
================================

Для добавления русских каналов нужно дописать/изменить файл ``/etc/apt/sources.lis``

.. code-block:: bash

   # RU sources
   deb http://ru.archive.ubuntu.com/ubuntu/ bionic main restricted
   deb http://ru.archive.ubuntu.com/ubuntu/ bionic-updates main restricted
   deb http://ru.archive.ubuntu.com/ubuntu/ bionic universe
   deb http://ru.archive.ubuntu.com/ubuntu/ bionic-updates universe
   deb http://ru.archive.ubuntu.com/ubuntu/ bionic multiverse
   deb http://ru.archive.ubuntu.com/ubuntu/ bionic-updates multiverse
   deb http://ru.archive.ubuntu.com/ubuntu/ bionic-backports main restricted universe multiverse
   #