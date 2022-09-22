.. index:: homeassistant

.. _homeassistant-downgrade:

Home Assistant Downgrade
========================

Если по какой-то причине требуется понизить версию Hassio.

1. Check available release at https://github.com/home-assistant/core/releases
2. Connect to CLI utility: ``docker exec -it hassio_cli bash``
3. Use: ``ha core update --version=x.y.z``
