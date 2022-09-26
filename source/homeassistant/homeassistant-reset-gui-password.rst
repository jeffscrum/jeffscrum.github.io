.. index:: homeassistant, password

.. _homeassistant-reset-gui-password:

Reset Admin Password
====================

Чтобы восстановить доступ в случае утери пароля или логина от WEB UI в Homeassistant

1. Через SSH и sudo:

  .. code-block:: bash
  
    cd /usr/share/hassio/homeassistant/.storage
    rm auth
    rm auth_provider.homeassistant
    rm onboarding
    rm hassio
    reboot

2. После перезапуска, заходим в WEB UI создаём нового пользователя

3. Если не выходит, то делаем так

  .. code-block:: bash

    sudo ha core stop
    sudo rm -r /usr/share/hassio/homeassistant/.storage
    sudo ha core start

4. Заходим в WEB UI создаём нового пользователя
