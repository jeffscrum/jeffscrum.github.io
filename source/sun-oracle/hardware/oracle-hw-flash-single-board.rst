.. index:: sun, oracle, sunfire, v1280, e2900, 3800, 4800, 4810, 6800, e4900, e6900, netra 1280, 1290, flashupdate, firmware

.. meta::
   :keywords: sun, oracle, sunfire, v1280, e2900, 3800, 4800, 4810, 6800, e4900, e6900, netra 1280, 1290, flashupdate, firmware

.. _oracle-hw-flash-single-board:

How to Flashupdate a Single board on Sun Fire servers
=====================================================

Симптомы
--------

После замены системной платы в логах системного контроллера вы можете увидеть вот такое сообщение: "Cpu boards have mixed or old firmware."

Эта ошибка говорит о том, что какая-то из плат (чаще всего новая) имеет микрокод, отличный от остальных. Работа в конфигурация со смещанным микрокодом не поддерживается, поэтому потребуется или обновить его до более свежего, либо понизить версию.

Проверить текущий микрокод плат можно командой ``showboards -p v``

.. code-block:: none

   schostname:SC> showboards -p v
   
   Component   Compatible Version
   ---------   ---------- -------
   SSC0        Reference  5.20.4 Build_01
   /N0/IB6     Yes        5.20.4 Build_01
   /N0/IB7     Yes        5.20.4 Build_01
   /N0/IB8     Yes        5.20.4 Build_01
   /N0/IB9     Yes        5.20.4 Build_01
   /N0/SB0     Yes        5.20.6 Build_03  <<<<
   /N0/SB1     Yes        5.20.4 Build_01
   /N0/SB2     Yes        5.20.4 Build_01
   /N0/SB3     Yes        5.20.4 Build_01
   /N0/SB4     Yes        5.20.4 Build_01
   /N0/SB5     Yes        5.20.4 Build_01


Как обновить микрокод
---------------------

1. Убеждаемся что плата включена. В примере выше видно, что плата SB0 включена и имеет микрокод выше, чем остальные.

2. Запустить обновление платы одним из способов

   - Скопировать микрокод с другой платы (для нашего случая): ``flashupdate -c SB2 SB0``

   - Запустить обновление с внешнего источника: ``flashupdate -f``

3. При помощи команды ``showboards`` снова проверить версию микрокода платы. Возможно потребуется выключить/включить, если её статус "Failed".

4. Теперь можно добавить плату в домен.



Добавление платы для серверов non-DR
------------------------------------

1. Выполните команду ``showboards -p version -v`` чтобы убедиться что микрокоды плат идентичны

2. Выключите домен командами: ``halt`` или ``init 0``

3. Выключите все процессорные и платы ввода-вывода: ``schostname:A> setkeyswitch off``

4. Добавьте плату в домен: ``schostname:SC> addboard -d a sb1`` (плата SB1 добавится в домен А)

5. Выключите домен с новой платой: ``schostname:A> setkeyswitch on``

6. Запустите Solaris

.. tip::

   * Sun Fire 3800 Server
   * Sun Fire 4800 Server
   * Sun Fire 6800 Server
   * Sun Fire 4810 Server
   * Sun Fire v1280 Server
   * Sun Fire E2900 Server
   * Sun Fire E4900 Server
   * Sun Fire E6900 Server
   * Netra 1280 Server
   * Netra 1290 Server
