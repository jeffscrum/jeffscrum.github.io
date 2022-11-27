.. index:: linux, docker, error, resolving, failure, dns

.. meta::
   :keywords: linux, docker, error, resolving, failure, dns

.. _docker-temporary-failure-resolving:

===========================================================
Docker build "Temporary failure resolving 'deb.debian.org'"
===========================================================

Собирая один из образов для docker столкнулся с ошибкой

.. code-block:: none

   Err:1 http://deb.debian.org/debian bullseye InRelease
     Temporary failure resolving 'deb.debian.org'
   Err:2 http://deb.debian.org/debian-security bullseye-security InRelease
     Temporary failure resolving 'deb.debian.org'
   Err:3 http://deb.debian.org/debian bullseye-updates InRelease
     Temporary failure resolving 'deb.debian.org'

Решается такая проблема путем создания файла ``/etc/docker/daemon.json`` со следующим содержимым

.. code-block:: json

   {
       "dns": ["8.8.8.8", "1.1.1.1"]
   }

После чего перезапускаем демон docker ``sudo service docker restart`` и повторяем попытку.

Также, можно собирать вот таким образом ``docker build --network=host -t my-image-name .``
