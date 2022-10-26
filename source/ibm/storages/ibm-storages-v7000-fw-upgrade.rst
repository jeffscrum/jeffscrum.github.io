.. index:: ibm, storage, fw, upgrade, v7000, storwize, firmware

.. meta::
   :keywords: ibm, storage, fw, upgrade, v7000, storwize, firmware

.. _storwize-firmware-upgrade:

Storwize V7000 firmware upgrade
===============================

Матрицу возможных апгрейдов смотреть тут: `Concurrent Compatibility and Code Cross Reference for Storwize V7000 <https://www.ibm.com/support/pages/node/5692850>`_

План работ по обновлению прошивки IBM Storwize V7000 Gen1

Обновление fw через GUI
-----------------------

0) Проверить наличие бэкапа данных.
1) Проверить наличие мультипасинга на серверах/SVC.
2) Скачиваем утилиту SwUpgradeTestUtility, которая покажет нужно ли обновлять fw дисков, нужен ли будет downtime и требуются ли еще какие либо действия до обновления.
3) Запускаем само обновление Settings -> General -> Upgrade Software -> Launch Upgrade Wizard.

Необходимые шаги для достижения целевого уровня firmware. Каждый шаг занимает приблизительно 2 часа, а так же требуется выждать не менее 12 часов после шага для внутренних обновлений массива в бэкграунде:

.. code-block:: none

   Storwize-1: 6.3.0.7 --> 7.1.0.12 --> 7.4.0.11 --> 7.8.1.0 --> Drive Microcode Package 20170509
   Storwize-2: 7.7.0.3 --> 7.8.1.0 --> Drive Microcode Package 20170509
   Storwize-3: 7.7.0.3 --> 7.8.1.0 --> Drive Microcode Package 20170509
   Storwize-4: 7.4.0.4 --> 7.8.1.0 --> Drive Microcode Package 20170509
   Storwize-5: 7.4.0.4 --> 7.8.1.0 --> Drive Microcode Package 20170509

Риски: Неизвестные ошибки ПО, некорректное отрабатываение ПО мультипасинга.

.. warning::

   | Во время обновления контроллеры массива перезагружаются поочередно.
   | При корректном отрабатывании мультипасинга прерываний операций ввода-вывода быть не должно.
   | Перед началом обновления ОБЯЗАТЕЛЬНО необходимо убедиться, что хосты и массивы к SVC залогинены через две ноды.
   | Так же перед проведением обновления необходимо закрыть все активные event'ы и очистить log.
   | Есть вероятность, что для массивов Storwize будет необходимо обновление FW дисков.
   | Во время проведения операции обновления FW дисков возможна просадка производительности, однако ввод-вывод останавливать не требуется.
   | В новой версии микрокода (актуально только для версий firmware массивов Storwize-1 и Storwize-15) переделана архитектура кэша, поэтому во время обновления кэш будет выключен, что сильно повлияет на производительность.


Обновление fw через CLI
-----------------------

0) Копируем SoftwareUpgradeTestUtility в /home/admin/upgrade: ``pscp IBM2076_INSTALL_upgradetest_22.5 superuser@192.168.134.132:/home/admin/upgrade/``.
1) Установка утилиты: ``svctask applysoftware -file IBM2145_INSTALL_upgradetest_X.X``.
2) Проверка возможности обновления: ``svcupgradetest -v 7.5.0.2 | svcupgrade -v 7.5.0.2 | svcupgradetest -f``.
3) Копируем прошивку в `/home/admin/upgrade/`: ``pscp IBM2076_INSTALL_7.7.0.3 superuser@192.168.134.132:/home/admin/upgrade/``.
4) Запуск обновления: ``applysoftware -file IBM2076_INSTALL_7.7.0.3``.
5) Просмотр прогресса обновления:

  - Если прошивка ниже 7.4.0, то статус смотрим: ``svcinfo lssoftwareupgradestatus`` (показывает inactive, когда прошивка закончена).
  - Если прошивка выше 7.4.0, то статус смотрим: ``lsupdate`` (показывает success, когда прошивка закончена).

6) Если обновление идет до версии 7.4.0, то вы получите сообщение `"system_completion_required"`. Требуется подтвердить установку командой ```applysoftware -complete```. Далее наблюдаем статус командой ```lsupdate```.
7) Проверить код можно командой ``lsnodecanistervpd <1|2|3|4>`` на каждой из нод и смотрим строку "code_level".
8) Проверяем что обновление завершилось:

   - Финальный статус <7.4: ``status inactive``
   - Финальный статус >7.4: ``status success``


Обновление fw дисков в CLI
--------------------------

.. code-block:: none

   pscp IBM2076_DRIVE_20170901 superuser@192.168.134.132:/home/admin/upgrade/
   svctask applydrivesoftware -all -file /home/admin/upgrade/IBM2076_DRIVE_20170901 -type firmware
