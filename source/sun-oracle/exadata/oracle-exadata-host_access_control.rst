.. index:: exadata, host_access_control, security, ssh, lock, deny, root, password, unsuccessful, login, banner, rootssh, access, pam

.. meta::
   :keywords: exadata, host_access_control, security, ssh, lock, deny, root, password, unsuccessful, login, banner, rootssh, access, pam

.. _oracle-exadata-host_access_control:

Настройки безопасности на Exadata при помощи host_access_control
================================================================

В Exadata существует утилита host_access_control, при помощи которой можно производить настройки безопасности.
В документации к Exadata о ней не написано, зато описано в `документации <https://docs.oracle.com/cd/E58626_01/html/E58630/gqeje.html>`_ к Supercluster.
Расположена утилита по адресу `/opt/oracle.cellos/host_access_control`.

При запуске утилиты с ключом "-h" будет показана помощь:

.. code-block:: none

    /opt/oracle.cellos/host_access_control -h
     
    Usage: [-q|--quiet] command [argument]
         command is one of:
         access           - User access from hosts, networks, etc.
         access-ilomweb   - Control overall access from the ILOM Web Remote Console device (tty1)
         access-export    - Export access rules to a file
         access-import    - Import access rules via a supplied file
         audit-rules      - Import audit rules via a supplied file
         banner           - Login banner management
         fips-mode        - FIPS mode for openSSH
         grub-password    - GRUB password control
         idle-timeout     - Shell and SSH client idle timeout control
         ilom-configure   - ILOM settings control
         ilom-password    - ILOM root user password control
         kernel-dump      - kdump (kernel dump file creation) control
         maint-password   - Diagnostic ISO shell and Rescue password control
         pam-auth         - PAM authentication settings: pam_tally2 deny and lock_time, passwdqc, and password history values
         password-aging   - Adjust current users' password aging
         password-policy  - Adjust the system's password age policies
         rootssh          - Root user SSH access control
         sshciphers       - SSH cipher support control
         ssh-listen       - Control the SSHD service optional ListenAddress entries
         ssh-service      - Control the SSHD service and active connections
         sudo             - User privilege control through sudo
         sudodeny         - Manage the Exadata sudo users deny list
         get-runtime      - Maintenance command: import system configuration settings, storing them in host_access_control parameter settings files.
         restore          - Maintenance command: reapply settings previously set by this utility, as in after an upgrade

Посмотрим настройки pam-аутентификации:

.. code-block:: none

    /opt/oracle.cellos/host_access_control pam-auth -h
     
        Usage: host_access_control pam-auth [options] [arguments] [arguments]
        --deny {integer}
        --lock {integer}
        --passwdqc {comma-separated values}
        --remember {integer}
        --defaults
        --secdefaults
        --status
        --deny, --lock, --passwdqc, and --remember maybe be combined options

Мы можем изменить:

- Количество неудачных логинов (по-умолчанию: 5): ``--deny``
- Время блокировки пользователя, после неудачных логинов (по-умолчанию: 600 сек): ``--lock``
- Настроить сложность паролей: ``--passwdqc``
- И т.д.

Например, нам нужно изменить количество неудачных логинов и время блокировки пользователя (:ref:`oracle-exadata-root-unlock`).

Текущие настройки можно посмотреть так:

.. code-block:: none

    opt/oracle.cellos/host_access_control pam-auth --status
     
    [2023-03-08 12:10:54 +0300] [INFO] [IMG-SEC-0601] Deny on login failure count is deny=5
    [2023-03-08 12:10:54 +0300] [INFO] [IMG-SEC-0602] Account lock-out time is lock_time=600
    [2023-03-08 12:10:54 +0300] [INFO] [IMG-SEC-0603] Password strength, passwdqc setting is min=5,5,5,5,5
    [2023-03-08 12:10:54 +0300] [INFO] [IMG-SEC-0604] Password history depth setting is remember=10

Теперь изменяем параметры:

.. code-block:: none

    /opt/oracle.cellos/host_access_control pam-auth -d 10 -l 0

Проверяем:

.. code-block:: none

    /opt/oracle.cellos/host_access_control pam-auth --status
     
    [2018-10-08 15:10:54 +0200] [INFO] [IMG-SEC-0801] Deny on login failure count is deny=10
    [2018-10-08 15:10:54 +0200] [INFO] [IMG-SEC-0802] Account lock-out time is lock_time=0
    [2018-10-08 15:10:54 +0200] [INFO] [IMG-SEC-0803] Password strength, passwdqc setting is min=5,5,5,5,5
    [2018-10-08 15:10:54 +0200] [INFO] [IMG-SEC-0804] Password history depth setting is remember=10
