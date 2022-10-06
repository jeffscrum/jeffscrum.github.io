.. meta::
   :keywords: vyos, influx, telegraf

.. index:: vyos, influx, telegraf

.. _vyos-cloud-influx:

VyOS and InfluxDB Cloud
=======================

После настройки telegraf через стандартный способ столкнулся с тем что в логе была вот такая ошибка:

::

  Apr 13 22:33:19 vyos telegraf[2096]: 2022-04-13T19:33:19Z E! [outputs.influxdb_v2] When writing to [https://europe-west1-1.gcp.cloud2.influxdata.com:8086]: 
  Post "https://europe-west1-1.gcp.cloud2.influxdata.com:8086/api/v2/write?bucket=vyos&org=myorg": context deadline exceeded (Client.Timeout exceeded while awaiting headers)

Похоже, что проблема проявляется только при использовании InfluxDB Cloud.

Проблема связана с тем, что в шаблоне конфигурационного файла подразумевается использование URL без указания порта. В случае InfluxDB Cloud требовалось вручную указать нужный порт.

Пришлось руками поправить шаблон по которому генерится конфиг -- */usr/share/vyos/templates/monitoring/telegraf.tmpl*

