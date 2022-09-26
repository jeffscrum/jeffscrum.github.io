.. index:: homeassistant

.. _homeassistant-small-meteo-sensors:

Small Meteo Sensors
===================

Мой термодатчик умеет возвращать значения в простой текстовой странице tiny.htm:

.. code-block:: none

  1#25.3
  2#
  3#-2.5
  4#75
  5#995
  6#747

Отсюда видно что:

- температура в квартире: 25.3 °C
- температура на улице: -2.5 °C
- влажность: 75 %
- давление: 995 hPa
- давление: 747 mmHg

Для того чтобы интегрировать эти датчики в Home Assistant можно получать и обрабатывать значения при помощи curl и awk:

.. code-block:: bash

  curl -v --silent http://192.168.0.254/tiny.htm 2>&1 | grep 3# | awk '{print $1}' | awk '{print substr($1,3); }' 

Полностью кусок кода будет выглядеть так

.. code-block:: yaml

  # Small Meteo Sensors
  sensor:
    - platform: command_line
      name: В комнате
      command: ssh cfish@192.168.0.11 bash temp.sh
      unit_of_measurement: "°C"
      scan_interval: 5
    - platform: command_line
      name: На улице
      command: curl -v --silent http://192.168.0.254/tiny.htm 2>&1 | grep 3# | awk '{print $1}' | awk '{print substr($1,3); }'
      unit_of_measurement: "°C"
      scan_interval: 5
    - platform: command_line
      name: На улице
      command: curl -v --silent http://192.168.0.254/tiny.htm 2>&1 | grep 4# | awk '{print $1}' | awk '{print substr($1,3); }'
      unit_of_measurement: "%"
      scan_interval: 5
    - platform: command_line
      name: Давление
      command: curl -v --silent http://192.168.0.254/tiny.htm 2>&1 | grep 6# | awk '{print $1}' | awk '{print substr($1,3); }'
      unit_of_measurement: "mmHg"
      scan_interval: 5
