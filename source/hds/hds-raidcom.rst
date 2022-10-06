.. index:: hds, raidcom

.. _hds-raidcom:

HDS Конфигурирование через RAIDcom 
==================================

.. note:: SSH Port on MidRange controllers = 20522


Настройка HORCM
---------------

Когда требуется настройка по профилю, при инсталляции, то делать это через Storage Navigator очень долго. Гораздо быстрее использовать CLI при помощи RAIDcom. Пример настройки подключения к массиву и последующий план настройки.

.. code-block:: none

    root@lpar:~# cat /etc/horcm601.conf
    HORCM_MON
    # configure service port in /etc/services or use fixed port
    # ip_address    service         poll(10ms)      timeout(10ms)
    #localhost       horcm601        1000            3000
    localhost       11002        1000            3000

    HORCM_CMD
    # 
    # For HDS HiEnd use IP of SVP
    # For HDS Gx00 use IP of CTRL-1 & CTRL-2
    #
    # dev_name dev_name dev_name
    # \\.\IPCMD-192.168.1.100-31001  \\.\IPCMD-192.168.1.101-31001
    \\.\IPCMD-10.0.0.16  \\.\IPCMD-10.0.0.17
     
    root@lpar:~#

Конфигурация массива
--------------------

Пример можно посмотреть в "Command Control Interface User and Reference Guide" на странице 5-26.

.. code-block:: bash

    *// Логинимся на массив
    raidcom -login USER01 PASSWORD01 -IH601
     
    *// Включаем блокировку
    raidcom lock resource -resource_grp_name meta_resource -IH601
     
    *// Включение Port Security
    raidcom modify port -port CL1-E -security_switch y -IH601
    raidcom modify port -port CL1-G -security_switch y -IH601
    raidcom modify port -port CL3-E -security_switch y -IH601
    raidcom modify port -port CL3-G -security_switch y -IH601
     
    // Создание HG
    raidcom add host_grp -port CL1-E -host_grp_name e880_vios201 -IH601
    raidcom add host_grp -port CL1-G -host_grp_name e880_vios201 -IH601
    raidcom add host_grp -port CL3-E -host_grp_name e880_vios201 -IH601
    raidcom add host_grp -port CL3-G -host_grp_name e880_vios201 -IH601
     
    // Изменение HG на типа AIX
    raidcom modify host_grp -port CL1-E e880_vios201 -host_mode 15 -IH601
    raidcom modify host_grp -port CL1-G e880_vios201 -host_mode 15 -IH601
    raidcom modify host_grp -port CL3-E e880_vios201 -host_mode 15 -IH601
    raidcom modify host_grp -port CL3-G e880_vios201 -host_mode 15 -IH601
    radicom get host_grp -port CL1-E -IH601
 
    // Добавление WWN в HG
    raidcom add hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269b6 -IH601
    raidcom add hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269b7 -IH601
    raidcom add hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269e6 -IH601
    raidcom add hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269e7 -IH601
    raidcom add hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b226989 -IH601
    raidcom add hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b22698a -IH601
    raidcom add hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269d4 -IH601
    raidcom add hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269d5 -IH601
    raidcom get hba_wwn -port CL1-E e880_vios201 -IH601
     
    // Создание alias для WWN
    raidcom set hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269b6 -IH601 -wwn_nickname e880_vios201_EXP1_P1_C2_T1 -IH601
    raidcom set hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269b7 -IH601 -wwn_nickname e880_vios201_EXP1_P1_C2_T2 -IH601
    raidcom set hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269e6 -IH601 -wwn_nickname e880_vios201_EXP1_P1_C6_T1 -IH601
    raidcom set hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269e7 -IH601 -wwn_nickname e880_vios201_EXP1_P1_C6_T2 -IH601
    raidcom set hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b226989 -IH601 -wwn_nickname e880_vios201_EXP1_P2_C2_T1 -IH601
    raidcom set hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b22698a -IH601 -wwn_nickname e880_vios201_EXP1_P2_C2_T2 -IH601
    raidcom set hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269d4 -IH601 -wwn_nickname e880_vios201_EXP1_P2_C6_T1 -IH601
    raidcom set hba_wwn -port CL1-E e880_vios201 -hba_wwn 100000109b2269d5 -IH601 -wwn_nickname e880_vios201_EXP1_P2_C6_T2 -IH601
     
    // Создание луна
    raidcom add ldev -pool 0 -ldev_id 02:01 -capacity 200G -IH601
    raidcom add ldev -pool 0 -ldev_id 02:02 -capacity 200G -IH601
     
    *// Форматирование луна (quick format)
    raidcom initialize ldev -ldev_id 02:01 -operation qfmt -IH601
    raidcom initialize ldev -ldev_id 02:02 -operation qfmt -IH601
 
    // Переименование луна
    raidcom modify ldev -ldev_id 02:01 -ldev_name e880-vios201_boot -IH601
    raidcom modify ldev -ldev_id 02:02 -ldev_name e880-vios202_boot -IH601
     
    // Маппинг лунов
    raidcom add lun -port CL1-E e880_vios201 -ldev_id 02:01 -IH601
    raidcom add lun -port CL1-G e880_vios201 -ldev_id 02:01 -IH601
    raidcom add lun -port CL3-E e880_vios201 -ldev_id 02:01 -IH601
    raidcom add lun -port CL3-G e880_vios201 -ldev_id 02:01 -IH601
     
    *// Снимаем блокировку
    raidcom unlock resource -resource_grp_name meta_resource -IH601
     
    *// Разлогиниваемся
    raidcom -logout -IH601
