.. index:: vmax, hds, migration

.. meta::
   :keywords: vmax, hds, migration

.. _vmax-to-g600:

.. TASK03580263

Миграция томов с VMAX на G600
=============================

План работ:

1. Проверить наличие бэкапов
2. Создание host-группы и лунов на массиве g600 аналогичные соответствующим лунам на массиве vmax
3. Делаем мапинг новых LUN на сервера
4. На сервере выполняем команды:

  .. code:: none
  
    -- p780-lp01 /oracle (hdisk3: 100gb) --
    cfgmgr
    extendvg data_vm3_bin hdisk#X
    mirrorvg -s -c 2 hdisk#X
    syncvg -P 4 -v data_vm3_bin

5. После успешного зеркалирования данных делаем unmirror дисковой группы и удаляем старые LUN из конфигурации системы

  .. code:: none

    unmirrorvg data_vm3_bin hdisk3
    reducevg data_vm3_bin hdisk3
    rmdev -dl hdisk3

6. На сервере выполняем команды:

  .. code:: none

    -- p780-lp01 /fio (hdisk4: 21gb; hdisk23: 500gb) --
    cfgmgr
    extendvg data_fio hdisk#Y hdisk#Z
    mirrorvg -s -c 2 hdisk#Y hdisk#Z
    syncvg -P 4 -v data_fio


7. После успешного зеркалирования данных делаем unmirror дисковой группы и удаляем старые LUN из конфигурации системы

  .. code:: none

    unmirrorvg fio_lv hdisk4 hdisk23
    reducevg data_fio hdisk4 hdisk23
    rmdev -dl hdsik4
    rmdev -dl hdsik23

8. На сервере выполняем команды:

  .. code:: none

    -- p795-2-lp20 /oracle (hdisk0: 100gb) --
    cfgmgr
    extendvg data_vm3_bin hdis#W
    mirrorvg -s -c 2 hdisk#W
    syncvg -P 4 -v data_vm3_bin
    
9. После успешного зеркалирования данных делаем unmirror дисковой группы и удаляем старые LUN из конфигурации системы

  .. code:: none

    unmirrorvg data_vm3_bin hdisk0
    reducevg -d data_vm3_bin hdisk0
    rmdev -dl hdsik0
