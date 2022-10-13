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

Дальше самостоятельно скачиваем ``wget https://vagrantcloud.com/centos/boxes/8/versions/2011.0/providers/virtualbox.box``. Создаем `metadata.json`

.. code-block:: json

   {
     "name": "centos/8",
     "versions": [
       {
         "version": "2011.0",
         "providers": [
           {
             "name": "virtualbox",
             "url": "file:///Users/cfish/Downloads/virtualbox.box"
           }
         ]
       }
     ]
   }

И добавляем ``vagrant box add centos/8 metadata.json``











Для устновки свежего ядра 5.4.0 в Centos нужно подключить репозиторий `ELRepo <http://elrepo.org/tiki/HomePage>`_. После чего можно будет доступно новое ядро. 

Есть 2 варианта:

- **kernel-ml** - mainline kernels
- **kernel-lt** - long term kernels

Я буду ставить ядро `lt`.

.. code-block:: bash

   # Import the public key
   rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
   
   # To install ELRepo for RHEL-9
   yum install https://www.elrepo.org/elrepo-release-9.el9.elrepo.noarch.rpm
   
   # To install ELRepo for RHEL-8
   yum install https://www.elrepo.org/elrepo-release-8.el8.elrepo.noarch.rpm
   
   # To install ELRepo for RHEL-7
   yum install https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm
   
   # Update Metadata
   yum update
   
   # List and install available kernels
   yum --enablerepo="elrepo-kernel" list available | grep kernel
   yum --enablerepo=”elrepo-kernel” install kernel-lt.x86_64
   
   # Reboot
   shutdown -r now
