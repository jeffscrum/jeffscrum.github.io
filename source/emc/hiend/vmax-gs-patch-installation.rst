.. index:: emc, vmax

.. _vmax-gs-patch-installation:

VMAX. Установка GSPatch
=======================

GSPatch нужен для включения поддержки новых дисков в массиве. Иногда, при замене дисков требуется предварительно установить свежий GSPatch.

Проверить текущую версию
------------------------

- Открываем ``O:\EMC\<System Serial Number>\SYMMWIN``
- Блокнотом открываем файл *GSINFO.ini* (если файлика нет, то патч не установлен)

  .. note:: Предположим, что текущая версия микрокода на массиве 5875.286.218 и в файле GSINFO.ini вы видите значение *1.0.0.11* --> В системе установлен патч GS5875-11

Скачивание патча
----------------

- Идем на сайт `support.emc.com <http://support.emc.com>`_
- Выбираем support by product
- Скачиваем патч под нужную версию прошивки (например GSPatch_Toolkit_5875.zip)


Установка патча
---------------

- Заливаете патч на USB флешку (GS5875-12.EXE)
- Копируете его на диск C:\\
- Запускаете инсталлятор

Активация патча
---------------

- 5876 (5876.163.105 and below): SymmWin -> Procedures -> Procedure Wizard -> Code Load and Firmware Upgrades -> Update Drive DB
- 5875: SymmWin -> Procedures -> Procedure Wizard -> Code Load and Firmware Upgrades -> Update Drive DB
- 5773: SymmWin -> Procedure Wizard -> D Disk Maintenance Utilities -> M Load Drive DB
