.. index:: sun, oracle, ilom, password

.. meta::
   :description: How to reset ILOM password
   :keywords: sun, oracle, ilom, password

.. _oracle-hw-ilom-password-reset:

Сброс пароля ILOM
=================

Если получилось так что вы забыли пароль на ILOM, то сбросить его можно используя ipmitool из ОС

.. code-block:: none

   /usr/sbin/ipmitool user set password 0x02 changeme

После чего пароль будет сменен на changeme.

.. note::

   Сбросить пароль можно только из ОС. Извне сбросить пароль не получится.