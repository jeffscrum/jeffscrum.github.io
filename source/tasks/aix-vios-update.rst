.. index:: ibm, aix, vios, update

.. meta::
   :keywords: ibm, aix, vios, update

.. _aix-vios-update:

Обновление VIOs
===============

.. code:: none

   Первоначальная информация:
   root@p795-6-vio1>lspv
   hdisk0          00c1d387a24464ab                    rootvg active
   hdisk1          00c1d387515959de                    rootvg active
   hdisk2          none                                None
   hdisk3          none                                None
    
   Что делать:
    
   unmirrorvg rootvg hdisk1
   reducevg rootvg hdisk1
   bosboot -ad hdisk0
   bootlist -m normal hdisk0
   alt_disk_copy -d hdisk1
   bootlist -m normal hdisk0
    
   Для проверки загрузки с hdisk1:
   bootlist -m normal hdisk1
   shutdown -restart
    
   После загрузки с hdisk1 должно отображаться:
   root@p795-3-vio1>lspv
   hdisk0          00c1d387a24464ab                    old_rootvg
   hdisk1          00c1d387515959de                    rootvg active
    
   Для проверки загрузки с hdisk0:
   bootlist -m normal hdisk0
   shutdown -restart
    
   После загрузки с hdisk0 должно отображаться::
   root@p795-6-vio1: / # lspv
   hdisk0          00c1d387a24464ab                    rootvg active
   hdisk1          00c1d387515959de                    altinst_rootvg
    
   Проводим патчевание на hdisk0.
    
   Если все прошло успешно и работа проверена,то:
   alt_rootvg_op -X altinst_rootvg
   chpv -c hdisk1
   extendvg -f rootvg hdisk1
   mirrorvg -S rootvg hdisk1
   lsvg rootvg | grep STALE
   После окончания зеркалирования.
   bosboot -ad hdisk0; bosboot -ad hdisk1
   bootlist -m normal hdisk0 hdisk1
