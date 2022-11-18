.. index:: ibm, bc, gw, switch

.. meta::
   :keywords: ibm, bc, gw, switch

.. _ibm-bch-switchgw:

План по коммутации BC с переводом их в GW
=========================================

.. code:: none

  0. Устанавливаем имя:
  switchname "Fabric1Switch1"
   
  1. Проверяем, что свитчи в Native mode
  switchShow
   
  2. Дисэйблим свитч
  switchdisable
   
  3. Переводим свитч в режим ag
  ag --modeenable
  Ждем загрузки свитча
   
  4. Проверка
  ag --modeshow
  switchshow
   
  5. Смотрим мапинг портов
  ag --mapshow
   
  6. Меняем мапинг на необходимый
  portdisable 1
  portdisable 2
  portdisable 3
  portdisable 4
  portdisable 5
  portdisable 6
  portdisable 7
  portdisable 8
  portdisable 9
  portdisable 10
  portdisable 11
  portdisable 12
  portdisable 13
  portdisable 14
  ag --mapdel для портов 1,2,3,4,5,6,7,8,9,10,11,12,13,14 в зависимости от текущего мапинга
  ag --mapdel 0 "1;2"
  ag --mapdel 15 "3;4"
  ag --mapdel 16 "5;6;7"
  ag --mapdel 17 "8;9"
  ag --mapdel 18 "10;11"
  ag --mapdel 19 "12;13;14"
   
   
  ag --mapadd 0 "1;3;5;7;9;11;13"
  ag --mapadd 15 "2;4;6;8;10;12;14"
  portenable 1
  portenable 2
  portenable 3
  portenable 4
  portenable 5
  portenable 6
  portenable 7
  portenable 8
  portenable 9
  portenable 10
  portenable 11
  portenable 12
  portenable 13
  portenable 14
   
  7. Для failover'а создаем порт-группу
  ag --pgshow
  ag --policyenable pg
  ag --pgcreate 2 "0;15" -n "№"fabric
   
  8. Проверяем политику failover
  ag --failovershow 0
  ag --failovershow 15
   
  Если необходимо
  ag --failoverenable 0
  ag --failoverenable 15
   
  9. Проверяем Failback policy
  ag --failbackshow 0
  ag --failbackshow 15
   
  Если необходимо
  ag --failbackenable 0
  ag --failbackenable 15
   
   
   
  Коммутация:
  bc01tk1
     bc01tk1-fc1.rs.ru
         Port     0 ->     1/4 (fc48k_44)
         Port     15 ->    2/16 (fc48k_44)
     bc01tk1-fc2.rs.ru
         Port    0 ->     1/4  (fc48k_47)
         Port    15 ->    2/16 (fc48k_47)
  bc02tk1
     bc02tk1-fc1.rs.ru
         Port    0 ->    4/10 (fc48k_44)
         Port    15 ->    7/0 (fc48k_44)
     bc02tk1-fc2.rs.ru
         Port    0 ->    4/10 (fc48k_47)
         Port    15 ->    7/0 (fc48k_47)