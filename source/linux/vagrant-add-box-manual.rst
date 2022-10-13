.. index:: vagrant, box, manual, add

.. meta::
   :keywords: vagrant, box, manual, add

.. _vagrant-add-box-manual:

Add a downloaded .box file to Vagrant
=====================================

Можно запустить скачивание образа vagrant командой ``vagrant box add <name>``. Если образ скачивается медленно, то можно скачать его вручную, используя адрес который будет виден в выводе команды, а после добавить из локального файла при помощи `metadata.json`, который также создать.

.. code-block:: none

   $ vagrant box add centos/8
   ==> box: Adding box 'centos/8' (v2011.0) for provider: virtualbox
   box: Downloading: https://vagrantcloud.com/centos/boxes/8/versions/2011.0/providers/virtualbox.box

Дальше самостоятельно скачиваем

.. code-block:: none

   $ wget https://vagrantcloud.com/centos/boxes/8/versions/2011.0/providers/virtualbox.box

Создаем `metadata.json`:

.. code-block:: json

   {
     "name": "centos/8",
     "versions": [
       {
         "version": "2011.0",
         "providers": [
           {
             "name": "virtualbox",
             "url": "file:///Downloads/virtualbox.box"
           }
         ]
       }
     ]
   }

И добавляем ``vagrant box add centos/8 metadata.json``
