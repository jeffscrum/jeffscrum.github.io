.. index:: tourism, poi, garmin, gazprom

.. meta::
   :keywords: tourism, poi, garmin, gazprom

.. _garmin-gpnbonus-poi:

POI с заправками газпромнефть для Garmin
========================================

.. attention:: Дизайн сайта изменился, теперь невозможно получить координаты точек таким способом

Получаем базу точек с сайта
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Для получения базы переходим на сайт www.gpnbonus.ru в раздел "Наши АЗС", после чего в выпадающем списке выбираем "показать АЗС всех регионов".
Нам нужно скопировать URL этой странички, после чего подставить его для программы CURL.
На выходе получим CSV файл с точками.

.. code-block:: bash

   curl "https://www.gpnbonus.ru/our_azs/?region_id=all&region_name=%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C+%D0%90%D0%97%D0%A1+%D0%B2%D1%81%D0%B5%D1%85+%D1%80%D0%B5%D0%B3%D0%B8%D0%BE%D0%BD%D0%BE%D0%B2&CenterLon=38.929526&CenterLat=55.531728&city=" | grep -A 1 GPS | grep -v GPS | egrep [[:digit:]] | awk '{print $1 "," $2 ",Газпромнефть"}' > gaz.csv


Загрузка точек в прибор
~~~~~~~~~~~~~~~~~~~~~~~

Далее все что нам нужно - это воспользовавшись программой Garmin POI Loader, загрузить точки из CSV файла в навигатор.
Если нужна особая иконка для точек, то ее нужно положить в тот же каталог что и CSV с тем же именем.

Требования для иконки следующие:

- Format .bmp file type
- 8 or 16 bit RGB color palette
- 24x24 pixels in size (HiRes = 38x38)
- Transparency color is magenta RGB: R=255, G=0, B=255
- The name must be identical to the .csv or .gpx file