.. index:: ibm, storage, v7000, cli, commands, cluster, password, clusterid, CMMVC8020E

.. meta::
   :keywords: ibm, storage, v7000, cli, commands, cluster, password, clusterid, CMMVC8020E

.. _ibm-storages-v7000-commands:

Storwize V7000. Полезные команды
================================

Команды, которые могут пригодиться при работе с IBM Storwize V7000


1. Создание кластера. Можно вставить содержимое в файл `satask.txt` на USB, а можно подключиться к сервисному ip и выпонить в CLI. Команда создаст кластер и настроит кластерный ip. После этого, перейдя по этому адресу вы попадете в Wizard настройки остальных параметров (пароль, дата, оповещения и тд)

``satask mkcluster -clusterip 192.168.134.179 -gw 192.168.134.1 -mask 255.255.255.0``

2. Сброс пароля пользователя `superuser`. Команда вписывается в файле `satask.txt` на USB, после чего втыкаем флешку в USB порт любого из контроллеров. Пароль сменится на дефолтный `passw0rd`.

``satask resetpassword``

3. Удаление старого clusterid. В моем случае кластер никак не хотел создаваться, ругаясь ошибкой `CMMVC8020E Attempting to create cluster while there is a stored cluster ID.`. Процедура по полному удалению кластера не помогала. Помогло только это. После, создаем кластер по стандартной процедуре с флешки или как указано в п.1

``satask chenclosurevpd -resetclusterid``