.. index:: mikrotik, backup, restore

.. meta::
   :keywords: mikrotik, backup, restore

.. _mikrotik-backup-and-restore-configuration:

Backup and Restore Mikrotik Configuration
=========================================

Backup -- ``system backup save name=backup_20121030``

Restore -- ``system backup load name=backup_20121030``


Или делаем экспорт-импорт конфигурации:

Export  -- ``export file=config_backup_20121030.rsc``

Import -- ``import file=config_backup_20121030.rsc``

Можно делать экспорт только лишь одной из веток конфигурации

.. code-block:: bash

  ip address export file=ip.rsc
  ip firewall mangle export file=mangle.rsc
  ip firewall nat export file=nat.rsc
  ip firewall filter export file=filter.rsc
  queue simple export file=simple.rsc
  ip dns export file=dns.rsc
  files backup export file=backup.rsc
  system script export file=script.rsc
  system scheduler export file=scheduler.rsc
  tool e-mail export file=email.rsc
  ip firewall address-list export file=address-list.rsc
  ip route export file=route.rsc
  ip dhcp-server network export file=network.rsc
  queue type export file=type.rsc
  queue tree export file=tree.rsc
  queue simple export file=simple.rsc
  interface ethernet export file=ethernet.rsc
  ip pool export file=pool.rsc
  ppp profile export file=profile.rsc
  log export file=log.rsc

