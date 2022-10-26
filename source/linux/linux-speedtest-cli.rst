.. index:: linux, speedtest, cli

.. meta::
   :keywords: linux, speedtest, cli

.. _linux-speedtest-cli:

Linux SpeedTest via CLI
=======================

Так как на сервере не GUI, то измерить скорость канала попробуем через CLI при помощи speedtest-cli

Устанавливаем утилиту и даем ей права на исполнение

.. code-block:: bash

   # wget -O speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
   # chmod +x speedtest-cli

Теперь смотрим список доступных серверов SpeedTest и выбираем тот который отвечает нашим хотелкам. Я выбрал сервера в России, так как мне нужно было узнать скорость канала до РФ.

.. code-block:: bash

   # ./speedtest-cli --list | egrep -i Russian
   13484) Ekran (Kaliningrad, Russian Federation) [1400.03 km]
   2598) Rostelecom (Kaliningrad, Russian Federation) [1404.16 km]
   4090) Etype (Kaliningrad, Russian Federation) [1404.16 km]
   1352) Tis-Dialog (Kaliningrad, Russian Federation) [1404.16 km]

Запускаем тест и указываем номер сервера

.. code-block:: bash

   # ./speedtest-cli --simple --server 2598
   Ping: 38.458 ms
   Download: 477.09 Mbit/s
   Upload: 481.75 Mbit/s
