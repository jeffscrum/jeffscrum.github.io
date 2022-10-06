.. index:: oracle, solaris, eis

.. meta::
   :keywords: oracle, solaris, eis

.. _oracle-sw-eis-version:

How To Determinate Installation EIS Patches
===========================================

Часто возникает необходимость выяснить какой последний EIS ставили на Solaris. Увидеть это можно в файлике `/var/sun/EIS-CD.log`.

Пример вывода:

.. code-block:: none

   Mon Jan 31 12:42:49 MSK 2011: Ran setup-standard with EIS-DVD Vn 08-DEC-10

Отсюда видно, что последние установленный патч-кластер был с EIS от 8 декабря 2010 года.