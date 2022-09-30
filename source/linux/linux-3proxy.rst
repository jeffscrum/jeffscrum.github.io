.. index:: linux, debian, 3proxy, proxy, socks

.. _linux-3proxy:

Настройка SOCKS5 прокси сервера
===============================

Дистрибутив под вашу ОС можно скачать с официального сайта `3proxy <https://3proxy.ru/download/>`_ или `GitHub <https://github.com/3proxy/3proxy/releases>`_.

Установка

.. code-block:: bash

   adduser --system --disabled-login --no-create-home --group proxy3
   mkdir -p /var/log/3proxy
   mkdir /etc/3proxy
   cp tmp/3proxy /usr/bin/
   chmod +x /usr/bin/3proxy
   chown proxy3:proxy3 -R /etc/3proxy
   chown proxy3:proxy3 /usr/bin/3proxy
   chown proxy3:proxy3 /var/log/3proxy

Конфиг `/etc/3proxy/3proxy.cfg`

.. code-block:: none
 
   # Use "id proxy3" to know UID and GUID
   setgid 112
   setuid 107
    
   nserver 8.8.8.8
   nserver 8.8.4.4
    
   nscache 65536
   timeouts 1 5 30 60 180 1800 15 60
    
   daemon
    
   log /var/log/3proxy/3proxy.log D
   logformat "- +_L%t.%. %N.%p %E %U %C:%c %R:%r %O %I %h %T"
    
   auth strong
   users user1:CL:password1
   users user2:CL:password2
    
   allow *
    
   maxconn 700
   socks -p1080 -a

Для запуска прокси нужно написать файл-сервиса `/etc/systemd/system/3proxy.service`

.. code-block:: none

   [Unit]
   Description=3proxy Proxy Server
    
   [Service]
   Type=simple
   ExecStart=/usr/bin/3proxy /etc/3proxy/3proxy.cfg
   ExecStop=/bin/kill `/usr/bin/pgrep -u proxy3`
   RemainAfterExit=yes
   Restart=on-failure
    
   [Install]
   WantedBy=multi-user.target

Теперь запускаем службу и проверяем

.. code-block:: bash

   systemctl daemon-reload
   systemctl enable 3proxy
   systemctl start 3proxy
