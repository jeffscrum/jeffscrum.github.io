.. index:: zdlra, exadata, lvm, extend, resize, increase, root, fs

.. _oracle-exadata-zdlra-extend-fs:

How to extend filesystem on Exadata & ZDLRA
===========================================

.. note::
    
    Oracle Exadata System Software release 11.2.3.2.1 or later

root (/) partition
~~~~~~~~~~~~~~~~~~

* Use the df command to identify the amount of free and used space in the root partition (/):

.. code:: bash

    df -h /

* Use the lvs command to display the current volume configuration:

.. code:: bash

    lvs -o lv_name,lv_path,vg_name,lv_size

* Use the df command to identify the file system type that is used in the root partition (/):

.. code:: bash

    df -hT /

* Verify there is available space in the volume group VGExaDb using the vgdisplay command:

.. code:: bash

    vgdisplay -s

* Resize both LVDbSys1 and LVDbSys2 logical volumes using the lvextend command:

.. code:: bash

    lvextend -L +10G /dev/VGExaDb/LVDbSys1
    lvextend -L +10G /dev/VGExaDb/LVDbSys2
    or
    lvextend -L 60G /dev/VGExaDb/LVDbSys1
    lvextend -L 60G /dev/VGExaDb/LVDbSys2

* Resize the file system within the logical volume:

.. code:: bash

    For ext3 and ext4:
    resize2fs /dev/VGExaDb/LVDbSys1
    resize2fs /dev/VGExaDb/LVDbSys2

    For the xfs:
    xfs_growfs /
    mkdir -p /tmp/mnt/root
    mount -t xfs /dev/VGExaDb/LVDbSys2 /tmp/mnt/root
    xfs_growfs /tmp/mnt/root
    umount /tmp/mnt/root

* Verify the space was extended using the df command

non-root (/u01) partition
~~~~~~~~~~~~~~~~~~~~~~~~~

* Use the df command to identify the amount of free and used space in the /u01 partition:

.. code:: bash

    df -h

* Use the lvs command to display the current logical volume configuration used by the /u01 file system:

.. code:: bash

    lvs -o lv_name,lv_path,vg_name,lv_size

* Use the df command to identify the file system type that is used in the /u01 partition:

.. code:: bash

    df -hT /u01

* Verify there is available space in the volume group VGExaDb using the vgdisplay command:

.. code:: bash

    vgdisplay -s

* Resize the logical volume using the lvextend command:

.. code:: bash

    lvextend -L +10G /dev/VGExaDb/LVDbOra1
    or
    lvextend -L 60G /dev/VGExaDb/LVDbOra1

* Resize the file system within the logical volume:

.. code:: bash

    For ext3 and ext4:
    resize2fs /dev/VGExaDb/LVDbOra1

    For the xfs:
    xfs_growfs /u01

* Verify the space was extended using the df command



------------

Link: `Maintaining Exadata Database Servers <https://docs.oracle.com/en/engineered-systems/exadata-database-machine/dbmmn/maintaining-exadata-database-servers.html#GUID-490E2BFC-82AF-4AC8-8AB1-FE389C074501>`_
