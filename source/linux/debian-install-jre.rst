.. index:: linux, debian, java, jre

.. meta::
   :keywords: linux, debian, java, jre

.. _debian-install-jre:

Install Oracle JRE on Debian
============================

У Oracle есть готовый пакет для RPM систем, но нет для Debian. Поэтому поставим сами бинарники вручную.

:download:`JRE from oracle <https://www.oracle.com/java/technologies/downloads/>`

.. code-block:: bash

   sudo mkdir -p /usr/lib/jvm
   sudo tar -xf jre-8u311-linux-x64.tar.gz -C /usr/lib/jvm
   sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/<имя папки>/bin/java 1