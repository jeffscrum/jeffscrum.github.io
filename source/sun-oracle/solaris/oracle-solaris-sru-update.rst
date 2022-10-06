.. index:: oracle, solaris, sru

.. meta::
   :keywords: oracle, solaris, sru

.. _oracle-solaris-sru-update:

Solaris 11 SRU Update
=====================

.. attention::

  В случае если мы прыгаем на другой релиз, то нужно дополнительно развернуть IPS репозиторий соответствующего релиза (соседний столбец)

1. Скачиваем последний SRU с сайта `support.oracle.com <https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=285495715497905&id=2045311.1&_afrWindowMode=0&_adf.ctrl-state=w7gl1t78o_4>`_

2. Закачиваем их на сервер:

.. code-block:: none

   # ls -l
   total 11254436
   -rwxr-xr-x   1 root     root       11612 Oct  3 07:50 install-repo.ksh
   -rw-r--r--   1 root     root     1458243926 Oct 18 18:19 p24757510_1100_SOLARIS64_1of4.zip
   -rw-r--r--   1 root     root     1501531286 Oct 18 18:16 p24757510_1100_SOLARIS64_2of4.zip
   -rw-r--r--   1 root     root     1433899884 Oct 18 18:13 p24757510_1100_SOLARIS64_3of4.zip
   -rw-r--r--   1 root     root     1364166940 Oct 18 18:10 p24757510_1100_SOLARIS64_4of4.zip
   -rw-r--r--   1 root     root         276 Oct  3 08:09 sol-11_3_13_4_0-incr-repo_md5sums.txt

3. Создаем каталог для будущего репозитория и запускаем его создание

.. code-block:: none

   # mkdir /repo11.3.13.4.0
   # ./install-repo.ksh -d /repo11.3.13.4.0/ -c -v

4. Добавляем репозиторий в систему (В моем случае понадобилось параллельно оставить репозиторий 11.3 LocalRepo из предыдущей главы [:ref:`oracle-solaris11_2-solaris11_3.rst`]):

.. code-block:: none

   # pkg set-publisher -g file:///repo11.3.13.4.0/ solaris
   # pkg publisher
   PUBLISHER                   TYPE     STATUS P LOCATION
   solaris                     origin   online F file:///repo11.3.13.4.0/
   solaris                     origin   online F file:///repo11.3/

5. Последняя проверка и установка самих патчей

.. code-block:: none

   # pkg update --be-name sol11_3_13_4_0 -nv
   # pkg update --be-name sol11_3_13_4_0 --accept

6. Теперь перезагружаемся и проверяем версию Solaris

.. code-block:: none

   # shutdown -i6 -g0 -y
   # pkg info entire
