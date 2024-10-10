.. index:: emc, vmax, service

.. meta::
   :keywords: emc, vmax, service

.. _vmax-deffered-maintenance:

VMAX. Отключение Deferred Maintenance
=====================================

Опция "deferred maintenance" подразумевает, что массив откроет кейс, как только в системе появится сломанный диск, не покрываемый запасным (Spare). В этом случае открывается кейс на все диски, вышедшие из строя к этому времени.

В том случае, если вам это не подходит, то отключить можно так:

1. В SymmWin выберете: *Configuration > Site information > General*
2. Измените "Spare Replace" на "None".
3. Нажмите зеленую галочку наверху, для того что бы изменения применились.

.. image:: /images/vmax-deffered-maintenance.webp

После проделанных действий кейс будет открываться всякий раз, когда будет сломан новый диск.
