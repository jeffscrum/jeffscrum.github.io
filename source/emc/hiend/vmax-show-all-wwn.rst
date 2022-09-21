.. index:: emc, vmax, wwn

.. _vmax-show-all-wwn:

VMAX. Просмотр WWN всех портов
==============================

Для того чтобы получить список WWN всех портов массива нужно выполнить следующую команду на хосте, где установлен Solutions Enabler (SE)

.. code-block:: bash

  root@lp95:~# symcfg -sid 2222 list -fa all

  Symmetrix ID: 000222202222
             S Y M M E T R I X    F I B R E   D I R E C T O R S
      Dir    Port  WWN               ACLX     Volume Set   Pnt to Pnt
                                     Enabled  Addressing
      FA-7E   0    50000974082E2222  Yes      No           Yes
      FA-7E   1    50000974082E2222  Yes      No           Yes
      FA-8E   0    50000974082E2222  Yes      No           Yes
      FA-8E   1    50000974082E2222  Yes      No           Yes
      FA-9E   0    50000974082E2222  Yes      No           Yes
      FA-9E   1    50000974082E2222  Yes      No           Yes
      FA-10E  0    50000974082E2222  Yes      No           Yes
      FA-10E  1    50000974082E2222  Yes      No           Yes
      FA-7F   0    50000974082E2222  Yes      No           Yes
      FA-7F   1    50000974082E2222  Yes      No           Yes
      FA-8F   0    50000974082E2222  Yes      No           Yes
      FA-8F   1    50000974082E2222  Yes      No           Yes
      FA-9F   0    50000974082E2222  Yes      No           Yes
      FA-9F   1    50000974082E2222  Yes      No           Yes
      FA-10F  0    50000974082E2222  Yes      No           Yes
      FA-10F  1    50000974082E2222  Yes      No           Yes
      FA-7G   0    50000974082E2222  Yes      No           Yes
      FA-7G   1    50000974082E2222  Yes      No           Yes
      FA-8G   0    50000974082E2222  Yes      No           Yes
      FA-8G   1    50000974082E2222  Yes      No           Yes
      FA-9G   0    50000974082E2222  Yes      No           Yes
      FA-9G   1    50000974082E2222  Yes      No           Yes
      FA-10G  0    50000974082E2222  Yes      No           Yes
      FA-10G  1    50000974082E2222  Yes      No           Yes
      FA-7H   0    50000974082E2222  Yes      No           Yes
      FA-7H   1    50000974082E2222  Yes      No           Yes
      FA-8H   0    50000974082E2222  Yes      No           Yes
      FA-8H   1    50000974082E2222  Yes      No           Yes
      FA-9H   0    50000974082E2222  Yes      No           Yes
      FA-9H   1    50000974082E2222  Yes      No           Yes
      FA-10H  0    50000974082E2222  Yes      No           Yes
      FA-10H  1    50000974082E2222  Yes      No           Yes
