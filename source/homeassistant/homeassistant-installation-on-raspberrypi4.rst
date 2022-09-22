.. index:: homeassistant

.. _homeassistant-installation-on-raspberrypi4:

Home Assistant на RaspberriPi4
==============================

Предполагается что загрузка происходит с SSD диска, а не SD-карты.

.. code-block:: bash

   # boot from SD without USB drive
   sudo apt update
   sudo apt upgrade -y
   sudo vcgencmd bootloader\_version
   sudo vi /etc/default/rpi-eeprom-update
   # change to 'stable'
   # show available versions
   ls -la /lib/firmware/raspberrypi/bootloader/stable/
   #install version 2020-07-31 or past
   sudo rpi-eeprom-update -d -f /lib/firmware/raspberrypi/bootloader/stable/pieeprom-2020-07-31.bin 
   # install latest version
   sudo rpi-eeprom-update -d -a
   sudo shutdown -r now
   # update Raspberry firmware
   sudo rpi-update
   # configure to use USB as boot-device
   sudo raspi-config
       Advanced Options --> Boot Order --> B1. Boot from USB device if SD card boot fails --> Finish --> Reboot
    
   # connect USB drive (image has to be flashed)
   sudo mkdir /mnt/ssddisk
   sudo mount /dev/sda1 /mnt/ssddisk
   sudo cp /boot/\*.elf /mnt/ssddisk/
   sudo cp /boot/\*.dat /mnt/ssddisk/
   sudo halt
    
   # remove SD
   # boot
   sudo apt update
   sudo apt upgrade -y
   sudo adduser cfish
   sudo usermod -a -G adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,gpio,i2c,spi cfish

   ## Security
   # relogin and check user cfish
   # lock pi user
   sudo usermod -L pi
   # OR remove pi user

   sudo pkill -u pi
   sudo deluser -remove-home pi
   sudo vi /etc/sudoers.d/010\_pi-nopasswd
   # change to 'cfish ALL=(ALL) PASSWD: ALL'
   sudo vi /etc/ssh/sshd\_config
   # edit "AllowUsers alice bob" or
   # edit "DenyUsers jane john"
   sudo systemctl restart ssh

   # change size of SWAP
   sudo dphys-swapfile swapoff
   sudo vi /etc/dphys-swapfile
   # change CONF_SWAPSIZE=2048
   sudo dphys-swapfile swapon
   /etc/init.d/dphys-swapfile restart
   sudo apt install ufw
   sudo echo "IPv6=off" >> /etc/ufw/ufw.conf
   sudo ufw allow 22
   sudo ufw enable
   sudo apt install fail2ban
   sudo vi /etc/fail2ban/jail.local
   ----
   [DEFAULT]
   ignoreip = 192.168.0.170 172.16.0.0/23
   findtime = 3600
   maxretry = 3
   bantime = 86400
   [sshd]
   enabled = true
   port = 22
   [asterisk]
   enabled  = true
   port = 5060
   filter = asterisk
   logpath = /var/log/asterisk/security
   action = iptables-allports\[name=ASTERISK, protocol=all]
    
   ----
   service fail2ban restart
    
   # configure network
   sudo vi /etc/network/interfaces
   ----
   auto lo
   iface lo inet loopback
   #iface eth0 inet manual
   allow-hotplug eth0
   iface eth0 inet static
       address 192.168.88.30
       netmask 255.255.255.0
       gateway 192.168.88.1
   ----

   # Locale settings
   sudo raspi-config
       Localisation Options --> Locale --> en_US.UTF-8
       Localisation Options --> Timezone --> Europe --> Moscow
   
   # Update channel
   sudo vi /etc/default/rpi-eeprom-update
   # change to 'stable'
   ## Hassio install
   sudo apt update && sudo apt dist-upgrade -y && sudo apt autoremove -y
   sudo -i
   apt-get install -y software-properties-common apparmor-utils apt-transport-https ca-certificates curl dbus jq network-manager
   systemctl disable ModemManager
   systemctl stop ModemManager
   shutdown -r now
   curl -sSL https://get.docker.com | sh
   # Link: https://github.com/home-assistant/supervised-installer
   curl -Lo installer.sh https://raw.githubusercontent.com/home-assistant/supervised-installer/master/installer.sh
   bash installer.sh --machine raspberrypi4
   curl -sL https://raw.githubusercontent.com/home-assistant/supervised-installer/master/installer.sh | bash -s -- -m qemuarm-64
