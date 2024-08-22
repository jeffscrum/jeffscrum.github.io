.. index:: linux, mail, debug

.. meta::
   :keywords: linux, mail, debug

.. _debug-email-server:

Debugging Email Server
======================

Нужно мне было перехватить одно письмо, которое отправлял скрипт. На скорую руку я нашел модуль для python, который слушает 25 порт, а само письмо записывает в txt файл

.. code-block:: none

   sudo python -m smtpd -n -c DebuggingServer 0.0.0.0:25

После чего на клиенте был настроен SMTP сервер-заглушка. Таким образом было получено то что отправлял скрипт

.. code-block:: none

   ---------- MESSAGE FOLLOWS ----------
   From: Sym..proc..gen..tor_@dell.com
   Subject: For Logistics Awareness - Upcoming 5876 Code Upgrade
   To: m***ry@dell.com, j***in@dell.com
   Date: Mon, 9 Nov 2020 10:55:02 +0300
   X-Priority: 3
   X-Library: Indy 9.00.10
   X-Peer: 192.168.0.21
   Customer:
   Serial Number: 2***4
   Service Request: 1****7
   Updrade Scheduled Date: 2020/11/17
   Upgrading to Code Level: 5876.309.196
   Note: This could be a duplicate email as EPG may have been run on more than one occasion while scheduling the upgrade.
   To determine the drive part numers configured in the System and if additional drives need to positioned in local depots.
   *   Go to CLM Reporting https://clm-reporting-prd.cfcp.isus.emc.com/clm-reporting/#/summary
   *   Search for the System Serial Number
   *   Select Disk Info from the drop down on the top left
   o  This provides a high level overview of the drives configured in the System
   *   If the TLA part number is required then the Disk Info Details can be exported to excel, the raw serial number can be copied and pasted into the Drive Nesting Site: https://pld-statuni02.lss.emc.com/   csdriveinfo/index.php or the MFG Genealogy Site: http://mfg/GPOBI/Applications/Genealogy/ to determine the TLA part number
   o  All the serials in the Drive SN column can be copied and pasted into the search at once.
   o  If using the MFG Genealogy Search scroll across to the right to get the TLA part number
   
   DELLEMC
   ------------ END MESSAGE ------------
