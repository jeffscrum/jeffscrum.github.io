.. index:: ibm, aix, vios, update

.. meta::
   :keywords: ibm, aix, vios, update

.. _aix-vios-update-22350:

Обновление VIOs до версии 2.2.3.50
==========================================

.. code:: none

   -----------------------
   Пункт второй:
   -----------------------
   
   Обновление VIO серверов до версии 2.2.3.50.
   Текущая версия 2.2.2.2.
   
   Обновление VIO серверов необходимо делать поочередно, при
   работающих клиентских партициях.
   
   Для данного релиза есть следующее предостережение:
   Notice: Please be aware of RSCT APAR IV73126 which can cause trace files to use up to 80MB of additional space in /var. Details can be found in the AIX 6.1 Installation Tips published to My Notifications on May 29, 2015 (https://www14.software.ibm.com/webapp/set2/subscriptions/onvdq).

   Для нормальной установки данной версии необходимо будет увеличить размер /var.
   Подробности можно прочитать тут:
   http://www-01.ibm.com/support/docview.wss?uid=isg1IV73126
   
   Перед обновлением необходимо удостовериться в наличии свободного места в группе rootvg:
   
   Please ensure that your rootvg contains at least 30GB and that there is at least 4GB free space before you attempt to update to Update Release 2.2.3.50. Run the lsvg rootvg command, and then ensure there is enough free space.
   Проверка:
   $ lsvg rootvg
   
   Согласно следующей ноте:
   NOTE: In order to update to Update Release 2.2.3.50 from a level between 2.2.1.1 and 2.2.3.1 in a single step, you can put the 2.2.3.1 and 2.2.3.50 updates in the same location and do the update using the updateios command.
   
   Для обновления до версии 2.2.3.50 с 2.2.2.2 необходимо скачать два дистрибутива и положить их в одну директорию,
   что может занять больше места на файловой системе.
   
   Для проверки пакетов обновления:
   $ oem_setup_env 
   Create a link to openssl 
   # ln -s /usr/bin/openssl /usr/ios/utils/openssl 
   Verify the link to openssl was created 
   # ls -alL /usr/bin/openssl /usr/ios/utils/openssl 
   Both files should display similar owner and size 
   # exit
   
   Само обновление:
   Переходим в окружение root
   $ oem_setup_env
   Создаем ФС для обновлений (возможно уже есть)
   # crfs -v jfs2 -g rootvg -m /updates -a size=<необходимый размер>
   Монтирование новой ФС
   # mount /updates
   Меняем владельца на padmin
   # chown padmin /updates
   Под пользователем padmin заливаем файлы обновлений по FTP в /updates.
   Заливаем файлы для двух дистрибутивов, как было написано ранее.
   Пересоздаем toc файл - ОБЯЗАТЕЛЬНО.
   Коммитим все предыдущие пакеты
   $ updateios -commit
   
   Проверяем скачанные пакеты
   $ cp /updates/ck_sum.bff /home/padmin 
   $ chmod 755 /home/padmin/ck_sum.bff 
   $ ck_sum.bff /updates 
   If there are missing updates or incomplete downloads, an error message is displayed.
   
   Согласно ноте:
   If your current level is 2.2.2.1, 2.2.2.2, 2.2.2.3, or 2.2.3.1, you need to run updateios command twice to get bos.alt_disk_install.boot_images fileset update problem fixed.
   
   Запускаем процесс обновления из под пользователя padmin
   $ updateios -accept -install -dev /updates
   $ updateios -accept -dev /updates
   Когда обновление завершится вновь принимаем лицензионное соглашение
   $ license -accept
   Перезагружаем VIOs
   $ shutdown -restart
   После перезагрузки проверяем версию VIOs
   $ ioslevel
   
   Перед проведением обновления обязательно необходимо сделать бэкап системы.
   
   Риски: Неизвестные ошибки ПО.
