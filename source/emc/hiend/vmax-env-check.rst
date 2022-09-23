.. index:: emc, vmax

.. _vmax-env-check:

VMAX. Просмотр состояния массива
================================

.. code-block:: terminal

  root@Server:~# symcfg discover
  root@Server:~# symcfg -sid 789 list -env_data
 
  Symmetrix ID               : 000123456789
  Timestamp of Status Data   : 02/18/2015 17:02:19
      System Bay
        Bay Name                             :    SB-1
        Number of Standby Power Supplies     :    8
        Number of Drive Enclosures           :    0
        Number of Enclosure Slots            :    4
        Number of MIBE Enclosures            :    4
        Summary Status of Contained Modules
          All Standby Power Supplies         :    Normal
          All Enclosures                     :    Normal
          All Link Control Cards             :    Normal
          All Power Supplies                 :    Normal
          All Enclosure Slots                :    Normal
          All Power Supplies                 :    Normal
          All Fans                           :    Normal
          All Management Modules             :    Normal
          All IO Module Carriers             :    Normal
          All Directors                      :    Normal
          All MIBE Enclosures                :    Normal
          All Power Supplies                 :    Normal
      Drive Bays
        Bay Name                             :    DB-1A
        Number of Standby Power Supplies     :    8
        Number of Drive Enclosures           :    16
        Summary Status of Contained Modules
          All Enclosures                     :    Normal
          All Link Control Cards             :    Normal
          All Power Supplies                 :    Normal
          All Standby Power Supplies         :    Normal
        Bay Name                             :    DB-1B
        Number of Standby Power Supplies     :    8
        Number of Drive Enclosures           :    16
        Summary Status of Contained Modules
          All Enclosures                     :    Normal
          All Link Control Cards             :    Normal
          All Power Supplies                 :    Normal
          All Standby Power Supplies         :    Normal
