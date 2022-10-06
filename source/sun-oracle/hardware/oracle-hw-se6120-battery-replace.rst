.. index:: sun, se6120, battery

.. meta::
   :description: How to replace replace battery Sun StorEge 6120
   :keywords: sun, oracle, StorEge, 6120, battery

.. _oracle-hw-se6120-battery-replace:

Sun StorEdge 6120 Battery Replace
=================================

Недавно, меняя батарею на массиве Sun StorEge 6120 я столкнулся с хитростью. А именно с тем, что после замены батареи автоматически не сбросился ее статус и срок годности (см. u1b2):

.. code-block:: none

   SS6120:/:<2>refresh -s
   Current Date and Time:  Wed Aug 22 13:15:11 GMT 2012
   Next Scheduled Refresh: Mon Sep 24 02:21:30 GMT 2012
   Battery   State     Last Health Check              Warranty Expiration         
   -------   -------   ----------------------------   ----------------------------
   u1b1      normal    not tested                     Fri May 23 14:53:09 GMT 2014
   u1b2      failed    Mon Sep 22 09:51:15 GMT 2008   Fri Jun 29 06:33:32 GMT 2007
   u2b1      normal    Mon Aug 20 05:19:07 GMT 2012   Sat May 04 14:56:07 GMT 2013
   u2b2      normal    Mon Aug 20 08:38:46 GMT 2012   Thu May 23 11:07:17 GMT 2013

Для решения этой проблемы нужно перейти в сервисный режим командой "sun". Далее массив запросит сервисный пароль - вводим "arrayservice"

.. code-block:: none

   SS6120:/:<3>sun
   Password: *******
   sun: commands enabled

После этого для нас станут доступны сервисные команды. Нас интересует команда ".bat":

.. code-block:: none

   SS6120:/:<16>.bat help
   Usage :
       bat -c u[encid]pcu[1|2]       ----> clear battery status
       bat -d [u[encid]pcu[1|2]]     ----> complete debugging information
       bat -D [u[encid]pcu[1|2]]     ----> limited debugging information
       bat -f u[encid]pcu[1|2]       ----> mark battery as failed
       bat -i u[encid]pcu[1|2]       ----> initialize battery warranty date
       bat -m [norm|none|fast]       ----> battery management mode
       bat -r u[encid]pcu[1|2]       ----> set recharge date to current date
       bat -s u[encid]pcu[1|2]       ----> battery status information
       bat -u                        ----> update cache mode calculation

Для начала нам необходимо сбросить счетчик использования батареи:

.. code-block:: none

   SS6120:/:<17>.bat -i u1b2
   SS6120:/:<18>refresh -s
   Current Date and Time:  Wed Aug 22 13:26:11 GMT 2012
   Next Scheduled Refresh: Mon Sep 24 02:21:30 GMT 2012
   Battery   State     Last Health Check              Warranty Expiration         
   -------   -------   ----------------------------   ----------------------------
   u1b1      normal    not tested                     Fri May 23 14:53:09 GMT 2014
   u1b2      failed    not tested                     Wed Jun 25 13:23:01 GMT 2014
   u2b1      normal    Mon Aug 20 05:19:07 GMT 2012   Sat May 04 14:56:07 GMT 2013
   u2b2      normal    Mon Aug 20 08:38:46 GMT 2012   Thu May 23 11:07:17 GMT 2013

Теперь, когда счетчик сброшен нам нужно избавиться от статуса failed для батареи:

.. code-block:: none

   SS6120:/:<17>.bat -c u1b2
   SS6120:/:<18>refresh -s
   Current Date and Time:  Wed Aug 22 13:26:11 GMT 2012
   Next Scheduled Refresh: Mon Sep 24 02:21:30 GMT 2012
   Battery   State     Last Health Check              Warranty Expiration         
   -------   -------   ----------------------------   ----------------------------
   u1b1      normal    not tested                     Fri May 23 14:53:09 GMT 2014
   u1b2      charge    not tested                     Wed Jun 25 13:23:01 GMT 2014
   u2b1      normal    Mon Aug 20 05:19:07 GMT 2012   Sat May 04 14:56:07 GMT 2013
   u2b2      normal    Mon Aug 20 08:38:46 GMT 2012   Thu May 23 11:07:17 GMT 2013

Вот и все, теперь нам остается лишь дождаться когда батарея зарядится...
