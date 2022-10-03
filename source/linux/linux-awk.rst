.. index:: linux, awk

.. _linux-awk:

Обработка строк при помощи awk
==============================

.. code-block:: bash

   ---------------------------------------
       Отрезаем символы при помощи awk
   ---------------------------------------
   # Выбираем второй столбец и отрезаем последний символ
   $ echo spamegg foobar | awk '{print substr($2, 1, length($2)-1) }'
    
   # Отрезаем первый символ (2 варианта)
   $ echo foobar | awk '{print substr($1,2); }'
   $ echo foobar | awk '{print substr($1,2,length($1)-1); }'