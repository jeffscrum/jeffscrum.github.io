.. index:: asterisk, dongle, linux

.. meta::
   :keywords: asterisk, dongle, linux

.. _asterisk-debian10-installation:

Установка Asterisk 18
=====================

Процесс сборки и инсталляции Asterisk 18 из исходников на OS Debian 10


.. code-block:: bash

  apt-get update
  apt-get upgrade
  apt-get install unzip git gnupg2 curl libnewt-dev libssl-dev libncurses5-dev libsqlite3-dev build-essential libjansson-dev libxml2-dev uuid-dev subversion iptables-persistent fail2ban
  wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz
  tar zxf asterisk-18-current.tar.gz
  cd asterisk-18.*/
  contrib/scripts/get_mp3_source.sh
  contrib/scripts/install_prereq install
  ./configure
  make menuselect
  make -j2
  make install
  make samples
  make config
  ldconfig
  groupadd asterisk
  useradd -r -d /var/lib/asterisk -g asterisk asterisk
  usermod -aG audio,dialout asterisk
  chown -R asterisk.asterisk /etc/asterisk
  chown -R asterisk.asterisk /var/{lib,log,spool}/asterisk
  chown -R asterisk.asterisk /usr/lib/asterisk
  vi /etc/default/asterisk
  ---
  AST_USER="asterisk"
  AST_GROUP="asterisk"
  ---
  vi /etc/asterisk/asterisk.conf
  ---
  runuser = asterisk              ; The user to run as.
  rungroup = asterisk             ; The group to run as.
  ---
  sed -i 's";\[radius\]"\[radius\]"g' /etc/asterisk/cdr.conf
  sed -i 's";radiuscfg => /usr/local/etc/radiusclient-ng/radiusclient.conf"radiuscfg => /etc/radcli/radiusclient.conf"g' /etc/asterisk/cdr.conf
  sed -i 's";radiuscfg => /usr/local/etc/radiusclient-ng/radiusclient.conf"radiuscfg => /etc/radcli/radiusclient.conf"g' /etc/asterisk/cel.conf
  systemctl restart asterisk
  systemctl enable asterisk
  systemctl status asterisk
