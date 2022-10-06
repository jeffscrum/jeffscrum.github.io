.. index:: ibm, hmc, update

.. _ibm-virtualization-hmc-upgrade-network:

HMC Update over network
=======================

Подготовка к работам
~~~~~~~~~~~~~~~~~~~~
1. Если нужно повысить релиз на несколько версий, то смотрим матрицу `HMC Code Upgrades <http://www-01.ibm.com/support/docview.wss?uid=nas8N1021840>`_ на сайте IBM. Для каждой версии HMC указаны требования по апгрейду (например установка патчей перед апгрейдом) и поддерживается ли тот или иной релиз самой моделью сервера.
2. Прочитать release notes к целевой версии HMC
3. По матрице `POWER code matrix <https://www-304.ibm.com/support/customercare/sas/f/power5cm/supportedcodep8.html>`_ проверить можно ли с текущим микрокодом сервера провести обновление HMC
4. Скачиваем обновления HMC `c FTP IBM <ftp://public.dhe.ibm.com/software/server/hmc/network/>`_ и читаем как ими пользоваться `на страничке <http://www-01.ibm.com/support/docview.wss?uid=nas8N1020108>`_.
5. На всякий случай скачиваем HMC_Recovery_DVD под нужную нам версию. С него же можно и обновиться и проинсталлировать HMC с нуля, но нужно будет записывать болванку и иметь физический доступ к HMC.

.. attention::

   * Server managed by dual (redundant) HMCs require that both HMCs be upgraded to the same release
   * When a server is managed by dual (or redundant) HMCs, both HMCs must be upgraded to the same release.
   * When upgrading multiple HMCs that are part of a Power Enterprise Pool (PEP) from 8.8.5 to 8.8.6, its recommended to upgrade a backup HMC first, set the upgraded HMC as the master, then upgrade the previous master. This ensures a master is always available.
   * After one HMC is upgraded the servers on the redundant HMC may go to a "Version Mismatch" state, with reference code "Save area version mismatch". This state will clear when the redundant HMC is upgraded.

Копирование обновлений
~~~~~~~~~~~~~~~~~~~~~~

1. Собрать на всякий случай конфигурацию через `HMC Scanner <https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Power+Systems/page/HMC+Scanner>`_. (в моем случае помог, так как пришлось заливать HMC с нуля, а бэкап не хотел читаться)
2. Залить файлы на ftp-сервер
3. Сделать бэкап конфигурации

   * Вставить USB-flash и выполнить: ``saveupgdata -r diskusb``
   * Сделать копию на локальный диск: ``saveupgdata -r disk``

6. Запустить скачивание нового образа: ``getupgfiles -h <FTP server> -u <user id> --passwd <pwd> -d <directory>``
7. После скачивания обновлений перевести HMC в режим обновления: ``chhmc -c altdiskboot -s enable --mode upgrade``
8. Перезагрузить HMC: ``hmcshutdown -r -t now``


Установка обновлений
~~~~~~~~~~~~~~~~~~~~

1. Выкладываем обновления на ftp-сервер прямо в виде .iso файла
2. Логинимся на HMC через ssh и запускам обновление: ``updhmc -t ftp -h 192.168.0.100 -u testftp -f /8860SP2/MH01716.iso -r``
3. После установки обновления HMC уйдет в перезагрузку (ключик -r)
4. После перезагрузки проверяем что обновление установилось: ``lshmc -V``

.. note:: Большинство обновлений можно устанавливать через GUI, но некоторые требуют установки именно через CLI. Внимательно читайте Readme к обновлению.
