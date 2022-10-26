.. index:: linux, strongswan, mschapv2, vpn

.. meta::
   :keywords: linux, strongswan, mschapv2, vpn

.. _linux-strongswan-eap-mschapv2:

StrongSwan with eap-mschapv2 enabled
====================================

Я долго не мог понять почему у меня не работает eap-mschapv2, а на консоль падает ссобщение "loading EAP_MSCHAPV2 method failed", хотя модуль, вроде бы, есть. Оказалось что модуль работает только если StrongSwan собран с поддержкой openssl. К тому же, в Debian 10 был все равно пакет старой версии, так что решил пересобрать самостоятельно.

Более подробно о плагинах написано `в документации <https://wiki.strongswan.org/projects/strongswan/wiki/Autoconf>`_. Я же собрал приблизительно так же. как ставится из репозитория, но добавил md4 и openssl, которые нужны для eap-mschapv2.

.. code-block:: bash

   apt-get update && apt-get upgrade -y
   apt-get install build-essential libgmp-dev libpam0g-dev libssl-dev wget
    
   cd /tmp
   wget https://download.strongswan.org/strongswan.tar.gz
   tar -xvf strongswan.tar.gz && cd strongswan-5.9.2
    
   ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --enable-shared \
    --enable-md4 \
    --enable-openssl \
    --enable-eap-mschapv2 \
    --enable-eap-aka \
    --enable-eap-gtc \
    --enable-eap-identity \
    --enable-eap-md5 \
    --enable-eap-peap \
    --enable-eap-tls \
    --enable-eap-tnc \
    --enable-eap-ttls \
    --enable-eap-radius \
    --enable-dhcp \
    --enable-lookip \
    --enable-led \
    --enable-unity \
    --enable-certexpire \
    --enable-addrblock \
    --enable-error-notify \
    --enable-xauth-pam \
    --enable-xauth-eap \
    --enable-farp \
    --enable-swanctl \
    --enable-eap-dynamic \
    --disable-des \
    --disable-cmac \
    --disable-vici \
    --disable-ikev1
    
   make && make install
