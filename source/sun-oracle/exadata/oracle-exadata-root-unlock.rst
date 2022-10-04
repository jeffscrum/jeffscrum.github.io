.. index:: exadata, lock, ssh

.. _oracle-exadata-root-unlock:

Temporary User Lockout On Exadata
=================================

По-умолчанию, после нескольких неудачных попыток ввода пароля root на Exadata, пользователь будет временно заблокирован.

Если нужно разблокировать пользователя root, то нужно зайти на сервер любым другим способом и получить привилегии root.

Проверяем что пользователь действительно заблокирован системой pam

.. code-block:: none

   [root@exadata-host]# pam_tally2 -u root
   Login           Failures Latest failure     From
   root                1    11/11/14 01:11:33  192.168.0.202

Как видно, была неудачная попытка входа с ip 192.168.0.202.

Разблокируем пользователя и проверим

.. code-block:: none

   [root@exadata-host]# pam_tally2 -u root -r 
   Login           Failures Latest failure     From
   root                1    11/11/14 01:11:33  192.168.0.202
    

   [root@exadata-host]# pam_tally2 -u root 
   Login           Failures Latest failure     From
   root 

Если излишняя безопасность вам не нужна, то эту настройку можно отключить на этапе конфигурирования в OEDA или *[статья в разработке]*