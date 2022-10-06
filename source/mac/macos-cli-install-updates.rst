.. index:: macos, mac

.. meta::
   :keywords: macos, mac

.. _macos-cli-install-updates:

Installing Software Updates Mac OS X
=====================================

Перед тем как выполнять проверку или установку обновлений необходимо получить права root - ``sudo -s``

Проверка обновлений
-------------------

.. code-block:: none

   bash-3.2# softwareupdate --list
   Software Update Tool
   Copyright 2002-2010 Apple
   Software Update found the following new or updated software:
      * Safari6.1.4MountainLion-6.1.4
       Safari (6.1.4), 51692K [recommended]
      * Mac App Store Update-1.0
       Mac App Store Update (1.0), 3697K [recommended] [restart]
      * AirPortUtility-6.3.1
       AirPort Utility (6.3.1), 21104K [recommended]
      * SecUpd2014-002MtLion-1.0
       Security Update 2014-002 (1.0), 132404K [recommended] [restart]

Установка обновлений
--------------------

.. code-block:: none

   bash-3.2# softwareupdate --install -a
   Software Update Tool
   Copyright 2002-2010 Apple
    
   Downloading Safari
      2.7 MB of 213.9 MB
      6.8 MB of 213.9 MB — Less than a minute
      8.9 MB of 213.9 MB — Less than a minute
   ....
      44.8 MB of 213.9 MB — Less than a minute
      49.1 MB of 213.9 MB — Less than a minute
   Verifying Safari
   Waiting to install Safari
   Downloading Mac App Store Update
      55.9 MB of 213.9 MB — Less than a minute
   Verifying Mac App Store Update
   Waiting to install Mac App Store Update
   Downloading AirPort Utility
      59.7 MB of 213.9 MB — Less than a minute
      64.4 MB of 213.9 MB — Less than a minute
      69.5 MB of 213.9 MB — Less than a minute
      75.1 MB of 213.9 MB — Less than a minute
   Verifying AirPort Utility
   Waiting to install AirPort Utility
   Downloading Security Update 2014-002
      82.2 MB of 213.9 MB — Less than a minute
      87.5 MB of 213.9 MB — Less than a minute
   ....
      197.4 MB of 213.9 MB — About 5 seconds
      203.2 MB of 213.9 MB — About 5 seconds
      209 MB of 213.9 MB — About 5 seconds
   Verifying Security Update 2014-002
   Waiting to install Security Update 2014-002
      Checking packages...
   Installing
      About 3 minutes
      About 2 minutes
      About a minute
      Less than a minute
      About 10 seconds
      About 5 seconds
   Installed Safari
   Installed Mac App Store Update
   Installed AirPort Utility
   Installed Security Update 2014-002
   Done.
   You have installed one or more updates that requires that you restart your
   computer.  Please restart immediately.
