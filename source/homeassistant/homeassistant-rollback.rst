.. index:: homeassistant, unsupported

.. _homeassistant-rollback:

Rollback plan
=============

.. code-block:: bash

  docker pull homeassistant/qemux86-64-homeassistant:0.118.5
  docker pull homeassistant/qemux86-64-homeassistant:0.115.6
  docker pull homeassistant/amd64-addon-mariadb:2.2.1
  docker pull dwelch2101/zigbee2mqtt-amd64:1.16.2.2
  docker pull carldebilly/zigbee2mqttassistant:0.3.157
  docker pull homeassistant/amd64-addon-ssh:8.10.0
  docker pull homeassistant/amd64-addon-mosquitto:5.1
  docker pull homeassistant/amd64-addon-configurator:5.2.0
  docker pull esphome/esphome-hassio-amd64:1.15.3
  docker pull hassioaddons/appdaemon-amd64:0.3.2
   
  sudo systemctl stop hassio-supervisor.service
  sudo systemctl restart hassio-supervisor.service
