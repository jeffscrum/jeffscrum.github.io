.. index:: linux, journal, logs

.. _linux-var-log-journal-clean:

Чистим логи /var/log/journal/
=============================

Директория `/var/log/journal` - стала заниматься слишком много места и ее нужно очистить:

До очистки: ``# journalctl --disk-usage``
Archived and active journals take up 900.2M on disk.

Делаем чистку: ``journalctl --vacuum-size=50M && journalctl --verify ``

После очистки получаем результат: 

.. code-block:: bash

   # journalctl --disk-usage
   Archived and active journals take up 56.0M on disk.

Для того, чтобы логи своевременно удалялись вносим изменения в файл `/etc/systemd/journald.conf` и перезагружаем сервис

.. code-block:: bash

   SystemMaxUse=50M
   SystemMaxFileSize=12M
   
   # systemctl restart systemd-journald
