.. index:: linux, kernel, centos, rhel

.. meta::
   :keywords: linux, kernel, centos, rhel

.. _linux-centos-install-kernel:

Установка свежего ядра в Centos
===============================

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
