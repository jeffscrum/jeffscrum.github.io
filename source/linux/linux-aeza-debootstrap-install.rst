.. index:: linux, debian, debootstrap, aeza, bullseye, bookworm

.. meta::
   :keywords: linux, debian, debootstrap, aeza, bullseye, bookworm

.. _linux-aeza-debootstrap-install:

Установка Linux при помощи debootstrap
======================================

Иногда по каким-то причинам хочется переустановить ОС на сервере не через скрипты хостера. Например, когда в дистрибутиве хостера много лишнего софта, а объем диска совсем небольшой.

При помощи `debootstrap <https://www.debian.org/releases/stable/i386/apds03.en.html>_` можно установить как Debian, так и Ubuntu. Я покажу на примере установки ОС на хостинге AEZA.

На многих хостингах можно загрузиться с `SystemRescue CD <https://www.system-rescue.org>_`. Ставим курсор на первый пункт "Boot SystemRescue using default options", жмем :kbd:`Tab`. Теперь нужно дописать опцию 'nofirewall' и жмем :kbd:`Enter`.

После того как ОС загрузилась, настраиваем сетевое подключение (в случае DHCP сеть будет настроена автоматически):

.. code-block:: bash

    nmcli c m "Wired connection 1" ipv4.addr 123.45.67.89/32
    nmcli c m "Wired connection 1" ipv4.gateway 10.0.0.1
    nmcli c m "Wired connection 1" ipv4.dns 1.1.1.1
    nmcli c m "Wired connection 1" ipv4.method manual
    nmcli c u "Wired connection 1"

Задаем пароль пользователя root: ``passwd``

Далее я рекомендую подключиться к серверу по SSH, чтобы удобнее было копировать команды: ``ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@123.45.67.89``

Затираем разметку диска: ``dd if=/dev/zero of=/dev/vda bs=1M count=50``

Создаем разделы диска. Я создам один раздел на весь диск, а swap будет либо в виде файла, либо использую zswap:

.. code-block:: none

    parted -s -a optimal -- /dev/vda \
      mklabel msdos \
      mkpart primary ext4 1MiB -0 \
      quit

Создаем ФС на разделе: ``mkfs.ext4 -m 2 /dev/vda1``

Скачиваем и устанавливаем программу debootstrap:

.. code-block:: bash

    wget -O /tmp/debootstrap_1.0.132_all.deb http://deb.debian.org/debian/pool/main/d/debootstrap/debootstrap_1.0.132_all.deb
    ar -p /tmp/debootstrap_1.0.132_all.deb data.tar.gz | tar -xz -C /

Создаем точку монтирования будущего корня и монтируем его:

.. code-block:: bash

    mkdir -p /mnt/debinst
    mount -o relatime /dev/vda1 /mnt/debinst

Запускаем установку пакетов:

.. code-block:: bash

    /usr/sbin/debootstrap --arch amd64 bullseye /mnt/debinst http://deb.debian.org/debian
    OR
    /usr/sbin/debootstrap --arch amd64 bookworm /mnt/debinst http://deb.debian.org/debian

После того как установка закончится, монтируем служебные разделы:

.. code-block:: bash

    mount --bind /dev /mnt/debinst/dev
    mount --bind /dev/pts /mnt/debinst/dev/pts
    mount -t sysfs sys /mnt/debinst/sys
    mount -t proc proc /mnt/debinst/proc

Редактируем файл репозиториев /mnt/debinst/etc/apt/sources.list:

.. code-block:: bash

    #!Debian11
    deb http://deb.debian.org/debian bullseye main non-free contrib
    #deb-src http://deb.debian.org/debian bullseye main non-free contrib
    
    deb http://deb.debian.org/debian bullseye-updates main contrib non-free
    #deb-src http://deb.debian.org/debian bullseye-updates main contrib non-free
    
    deb http://security.debian.org/ bullseye-security main
    #deb-src http://security.debian.org/ bullseye-security main

.. code-block:: bash

    #Debian12
    deb http://deb.debian.org/debian bookworm main non-free-firmware
    #deb-src http://deb.debian.org/debian bookworm main non-free-firmware
    
    deb http://security.debian.org/ bookworm-security main
    #deb-src http://security.debian.org/ bookworm-security main
    
    deb http://deb.debian.org/debian bookworm-updates main non-free-firmware
    #deb-src http://deb.debian.org/debian bookworm-updates main non-free-firmware
    
    deb http://deb.debian.org/debian bookworm-backports main non-free-firmware
    #deb-src http://deb.debian.org/debian bookworm-backports main non-free-firmware

Выполняем chroot для того чтобы попасть в новое окружение: ``LANG=C.UTF-8 chroot /mnt/debinst /bin/bash``

Обновляем все установленные пакеты: ``apt-get update && apt-get upgrade``

Устанавливаем пакет locale и генерируем необходимые локали:

.. code-block:: bash

    apt-get install -y man locales
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    locale-gen
    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale
    echo 'LANGUAGE="en_US:en"' >> /etc/default/locale

Настройка часового пояса: ``dpkg-reconfigure tzdata``

При помощи 'blkid' смотрим UUID раздела / и редактируем /etc/fstab:

.. code-block:: bash

    # /etc/fstab: static file system information.
    #
    # Use 'blkid' to print the universally unique identifier for a
    # device; this may be used with UUID= as a more robust way to name devices
    # that works even if disks are added and removed. See fstab(5).
    #
    # <file system> <mount point>   <type>  <options>       <dump>  <pass>
    UUID="fa821b1b-321a-4d88-a285-d8912b05ff59" / ext4 errors=remount-ro 0 1

Перемонтируем разделы: ``mount -a``

Устанавливаем пакеты ядра и необходимые утилиты. Я буду использовать ядро cloud, но можно установить и обычное 'linux-image-amd64':

.. code-block:: bash

    apt-get install -y linux-image-amd64
    OR 
    apt-get install -y linux-image-cloud-amd64
    
    tasksel install ssh-server
    apt-get install -y net-tools htop wget curl dnsutils file aptitude python3 sudo make
    apt-get install -y grub2

Записываем загрузчик на диск и уменьшаем таймер GRUB:

.. code-block:: bash

    grub-install --recheck /dev/vda
    sed -i 's/^GRUB_TIMEOUT=.*$/GRUB_TIMEOUT=3/g' /etc/default/grub
    update-grub

Задаем новой системе hostname и настройки DNS:

.. code-block:: bash

    echo "my-debian" > /etc/hostname
    
    echo "nameserver 1.1.1.1" > /etc/resolv.conf
    echo "nameserver 2606:4700::1111" >> /etc/resolv.conf

Редактируем файл '/etc/hosts':

.. code-block:: none

    127.0.0.1       localhost my-debian
    123.45.67.89    my-debian
    
    # The following lines are desirable for IPv6 capable hosts
    ::1     ip6-localhost ip6-loopback
    fe00::0 ip6-localnet
    ff00::0 ip6-mcastprefix
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters
    ff02::3 ip6-allhosts

Смотрим mac-адрес сетевой карты: ``ip a | grep ether``

Редактируем файл '/etc/network/interfaces' с сетевыми настройками:

.. code-block:: none

    # The loopback network interface
    auto lo
    iface lo inet loopback
    
    # The primary network interface
    auto ens3
    iface ens3 inet static
        address   123.45.67.89
        netmask   255.255.255.0
        gateway   10.0.0.1
        hwaddress ether 52:54:00:12:41:d8
        dns-nameservers 1.1.1.1 8.8.8.8
    
    iface ens3 inet6 static
        address   2a12:5122:b2e5::2
        netmask   48
        gateway   2a12:5122:b2e5::1
        dns-nameservers 2606:4700::1111


Задавем пароль root и разрешаем ему подключение по паролю:

.. code-block:: bash

    passwd
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

Включаем BBR:

.. code-block:: bash

    echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf

Если требуется, то устанавливаем агента QEMU:

.. code-block:: bash

    apt-get install qemu-guest-agent
    systemctl start qemu-guest-agent
    systemctl enable --now qemu-guest-agent
    systemctl status qemu-guest-agent

