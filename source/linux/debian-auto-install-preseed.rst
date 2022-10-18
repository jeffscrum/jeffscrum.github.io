.. index:: linux, debian, centos, rhel, kickstart, preseed, install

.. meta::
   :keywords: linux, debian, centos, rhel, kickstart, preseed, install

.. _debian-auto-install-preseed:

Файлы автоматической установки linux
====================================

На Github я выложил файлы для автоматической установки Debian 10, Centos 7, Centos 8, Centos 9 на GitHub Gists `preseed.cfg <https://gist.github.com/jeffscrum/ec80f4a2546e3032921fd594bfbc921c>`_

Для создания ISO с Debian, который содержит внутри себя файл установки можно использовать скрипт `debian-preseeded-iso.sh <https://gist.github.com/jeffscrum/b217c8628de2595039b138bd035a1083>`_

А для запуска kickstart установки CentOS и RHEL нужно выложить файл на доступный ресурс, а в GRUB нажать :kbd:`Tab` и дописать ``inst.ks=http://10.32.5.1/ks.cfg``

------

Related Links: `How Do You Perform a Kickstart Installation? <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/installation_guide/sect-kickstart-howto>`_