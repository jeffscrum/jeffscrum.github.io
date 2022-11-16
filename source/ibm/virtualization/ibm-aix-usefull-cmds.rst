.. index:: ibm, aix, wwn, lpar, terminal, console, hmc

.. meta::
   :keywords: ibm, aix, wwn, lpar, terminal, console, hmc

.. _ibm-aix-usefull-cmds:

Полезные команды для AIX
========================

Посмотреть WWN порта ``lscfg -vl fcs0 |grep Addr``

Открыть и закрыть консоль LPARa

.. code-block:: none

  mkvterm -m p520 -p aix1
  rmvterm -m p520 -p aix1

Посмотреть список систем, заведенных в HMC ``lssyscfg -r sys -F name``
