.. index:: sublime, dropbox, sync

.. _sublime-session-file:

Синхронизация файла сессий Sublime
==================================

Для синхронизации незакрытых сессий Sublime будем использовать DropBox.

.. code-block:: bash

  ln -s /Users/cfish/Dropbox/Sync/Sublime/Session.sublime_session /Users/cfish/Library/Application\ Support/Sublime\ Text\ 3/Local/

Теперь, если вы не сохранили или не закрыли **файл**, а закрыли сам редактор и открыли его на другом компьютере, то увидите все то что было не закончено
