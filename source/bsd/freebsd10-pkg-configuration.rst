.. index:: freebsd

.. _freebsd10-pkg-configuration:

Настройка пакетов FreeBSD 10
============================

- Cоздаем новый */usr/local/etc/pkg.conf* или оставляем тот что был

   .. code-block:: bash
   
       pkg_dbdir: "/var/db/pkg"
       pkg_cachedir: "/var/cache/pkg"
       portsdir: "/usr/ports"
       handle_rc_cripts: false
       assume_always_yes: false
   
       repos_dir: [
                       "/etc/pkg",
                       "/usr/local/etc/pkg/repos",
       ]
   
       syslog: true
       autodeps: true
       developer_mode: false
   
       alias: {
         origin: "info -qo",
         nonauto: "query -e '%a == 0' '%n-%v'"
       }

- Cоздаем директорию для конфигов разных репозиториев ``mkdir -p /usr/local/etc/pkg/repos``

- Создаем файл конфигурации официального репозитория */usr/local/etc/pkg/repos/FreeBSD.conf*

   .. code-block:: bash

       FreeBSD: {
         url: "pkg+http://pkg.freebsd.org/${ABI}/latest",
         enabled: true,
         signature_type: "none",
         mirror_type: "srv"
       }

- Обновляем список пакетов и проверяем

   .. code-block:: bash

       # pkg -v
       # pkg update
       # pkg search rar
