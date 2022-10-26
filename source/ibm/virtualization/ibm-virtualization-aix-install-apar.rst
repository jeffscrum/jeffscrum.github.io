.. index:: ibm, aix, apar

.. meta::
   :keywords: ibm, aix, apar

.. _ibm-virtualization-aix-install-apar:

Installing a Interim Fix (APAR)
===============================

.. attention:: This procedure will require a system reboot.

1. Download the right ifix for your oslevel according to the APAR description (see APAR read me)
2. Check if an ifix is not already installed on the system

  .. code-block:: none
  
    # emgr -l
    There is no efix data on this system.

3. Get some information from the downloaded ifix about itself

  .. code-block:: none
  
    # emgr -d -e IV16587s02.epkg.Z
    +-----------------------------------------------------------------------------+
    Efix Manager Initialization
    +-----------------------------------------------------------------------------+
    Initializing log /var/adm/ras/emgr.log ...
    Efix package file is: /fixes/IV16587s02.epkg.Z
    MD5 generating command is /usr/bin/csum
    MD5 checksum is 65f36f7ae062de211d4a8d6bc4633282
    Accessing efix metadata ...
    Verifying efix control file ...
     
    +-----------------------------------------------------------------------------+
    Efix Attributes
    +-----------------------------------------------------------------------------+
    LABEL:            IV16587s02
    EFIX FILES:       3
     
    FILE NUMBER:      1
       LOCATION:      /usr/sbin/trustchk
     
    FILE NUMBER:      2
       LOCATION:      /usr/ccs/lib/libc.a
     
    FILE NUMBER:      3
       LOCATION:      /usr/bin/date
     
    +-----------------------------------------------------------------------------+
    Operation Summary
    +-----------------------------------------------------------------------------+
    Log file is /var/adm/ras/emgr.log
     
    EPKG NUMBER       LABEL               OPERATION              RESULT
    ===========       ==============      =================      ==============
    1                 IV16587s02          DISPLAY                SUCCESS           
     
    Return Status = SUCCESS

4. Run a preview installation (output omitted)

  .. code-block:: none
  
    emgr -p -e IV16587s02.epkg.Z
    *******************************************************************************
    EFIX MANAGER PREVIEW START
    *******************************************************************************
     
    +-----------------------------------------------------------------------------+
    Efix Manager Initialization
    +-----------------------------------------------------------------------------+
    Initializing log /var/adm/ras/emgr.log ...
    Efix package file is: /fixes/IV16587s02.epkg.Z
    MD5 generating command is /usr/bin/csum
    MD5 checksum is 65f36f7ae062de211d4a8d6bc4633282
    Accessing efix metadata ...
    Processing efix label "IV16587s02" ...
    Verifying efix control file ...
    ...
    ...
    ...
    ...
     
    EPKG NUMBER       LABEL               OPERATION              RESULT
    ===========       ==============      =================      ==============
    1                 IV16587s02          INSTALL PREVIEW        SUCCESS           
     
    ATTENTION: system reboot will be required by the actual (not preview) operation.
    Please see the "Reboot Processing" sections in the output above or in the
    /var/adm/ras/emgr.log file.
     
    Return Status = SUCCESS
    Now run the actuall installtion

5. Now run the actuall installtion

  .. code-block:: none
  
  
    # emgr -e IV16587s02.epkg.Z
    +-----------------------------------------------------------------------------+
    Efix Manager Initialization
    +-----------------------------------------------------------------------------+
    Initializing log /var/adm/ras/emgr.log ...
    Efix package file is: /fixes/IV16587s02.epkg.Z
    MD5 generating command is /usr/bin/csum
    MD5 checksum is 65f36f7ae062de211d4a8d6bc4633282
    Accessing efix metadata ...
    Processing efix label "IV16587s02" ...
    Verifying efix control file ...
     
    +-----------------------------------------------------------------------------+
    Installp Prerequisite Verification
    +-----------------------------------------------------------------------------+
    Verifying prerequisite file ...
    Checking prerequisites ...
   
    Prerequisite Number: 1
       Fileset: bos.rte.libc
       Minimal Level: 6.1.7.1
       Maximum Level: 6.1.7.1
       Actual Level: 6.1.7.1
       Type: PREREQ
       Requisite Met: yes
     
    All prerequisites have been met.
     
    +-----------------------------------------------------------------------------+
    Processing APAR reference file
    +-----------------------------------------------------------------------------+
    ATTENTION: Interim fix is enabled for automatic removal by installp.
     
    +-----------------------------------------------------------------------------+
    Efix Attributes
    +-----------------------------------------------------------------------------+
    LABEL:            IV16587s02
    PACKAGING DATE:   Fri Mar  2 10:50:15 CST 2012
    ABSTRACT:         Ifix for IV16587@6.1TL7SP2
    PACKAGER VERSION: 7
    VUID:             00CCCC5B4C00030210031412
    REBOOT REQUIRED:  yes
    BUILD BOOT IMAGE: yes
    PRE-REQUISITES:   yes
    SUPERSEDE:        no
    PACKAGE LOCKS:    no
    E2E PREREQS:      no
    FIX TESTED:       no
    ALTERNATE PATH:   None
    EFIX FILES:       3
     
    Install Scripts:
       PRE_INSTALL:   no
       POST_INSTALL:  no
       PRE_REMOVE:    no
       POST_REMOVE:   no
     
    File Number:      1
       LOCATION:      /usr/sbin/trustchk
       FILE TYPE:     Standard (file or executable)
       INSTALLER:     installp
       SIZE:          1064
       ACL:           DEFAULT
       CKSUM:         35802
       PACKAGE:       bos.rte.security
       MOUNT INST:    no
     
    File Number:      2
       LOCATION:      /usr/ccs/lib/libc.a
       FILE TYPE:     Standard (file or executable)
       INSTALLER:     installp
       SIZE:          23176
       ACL:           DEFAULT
       CKSUM:         50144
       PACKAGE:       bos.rte.libc
       MOUNT INST:    no
     
    File Number:      3
       LOCATION:      /usr/bin/date
       FILE TYPE:     Standard (file or executable)
       INSTALLER:     installp
       SIZE:          32
       ACL:           DEFAULT
       CKSUM:         26421
       PACKAGE:       bos.rte.date
       MOUNT INST:    no
     
    +-----------------------------------------------------------------------------+
    Efix Description
    +-----------------------------------------------------------------------------+
    Ifix for IV16587@6.1TL7SP2
    Notes:
    IV16587 - Date command is failing while switching over day light saving
     
    +-----------------------------------------------------------------------------+
    Efix Lock Management
    +-----------------------------------------------------------------------------+
    Checking locks for file /usr/sbin/trustchk ...
    Checking locks for file /usr/ccs/lib/libc.a ...
    Checking locks for file /usr/bin/date ...
     
    All files have passed lock checks.
     
    +-----------------------------------------------------------------------------+
    Space Requirements
    +-----------------------------------------------------------------------------+
    Checking space requirements ...
     
    Space statistics (in 512 byte-blocks):
    File system: /usr, Free: 839248, Required: 57689, Deficit: 0.
    File system: /tmp, Free: 877464, Required: 97715, Deficit: 0.
     
    +-----------------------------------------------------------------------------+
    Efix Installation Setup
    +-----------------------------------------------------------------------------+
    Unpacking efix package file ...
    Initializing efix installation ...
     
    +-----------------------------------------------------------------------------+
    Efix State
    +-----------------------------------------------------------------------------+
    Setting efix state to: INSTALLING
     
    +-----------------------------------------------------------------------------+
    File Archiving
    +-----------------------------------------------------------------------------+
    Saving all files that will be replaced ...
    Save directory is: /usr/emgrdata/efixdata/IV16587s02/save
    File 1: Saving /usr/sbin/trustchk as EFSAVE1 ...
    File 2: Saving /usr/ccs/lib/libc.a as EFSAVE2 ...
    File 3: Saving /usr/bin/date as EFSAVE3 ...
     
    +-----------------------------------------------------------------------------+
    Efix File Installation
    +-----------------------------------------------------------------------------+
    Installing all efix files:
    Installing efix file #1 (File: /usr/sbin/trustchk) ...
    Installing efix file #2 (File: /usr/ccs/lib/libc.a) ...
    Installing efix file #3 (File: /usr/bin/date) ...
     
    Total number of efix files installed is 3.
    All efix files installed successfully.
     
    +-----------------------------------------------------------------------------+
    Package Locking
    +-----------------------------------------------------------------------------+
    Processing package locking for all files.
    File 1: locking installp fileset bos.rte.security.
    File 2: locking installp fileset bos.rte.libc.
    File 3: locking installp fileset bos.rte.date.
     
    All package locks processed successfully.
     
    +-----------------------------------------------------------------------------+
    Reboot Processing
    +-----------------------------------------------------------------------------+
     
    *** NOTICE ***
    This efix package requires the target system to be rebooted after the current
    operation is complete. It is recommended that you reboot the target system as
    soon as possible after installation to avoid disruption of current functionality.
     
    +-----------------------------------------------------------------------------+
    Efix State
    +-----------------------------------------------------------------------------+
    Setting efix state to: REBOOT REQUIRED
     
    +-----------------------------------------------------------------------------+
    Boot Image Processing
    +-----------------------------------------------------------------------------+
    Rebuilding boot image ...
    bosboot: Boot image is 49180 512 byte blocks.
    Successfully rebuilt boot image.
     
    +-----------------------------------------------------------------------------+
    Operation Summary
    +-----------------------------------------------------------------------------+
    Log file is /var/adm/ras/emgr.log
     
    EPKG NUMBER       LABEL               OPERATION              RESULT
    ===========       ==============      =================      ==============
    1                 IV16587s02          INSTALL                SUCCESS           
     
    ATTENTION: system reboot is required. Please see the "Reboot Processing"
    sections in the output above or in the /var/adm/ras/emgr.log file.
     
    Return Status = SUCCESS

6. Now view the ifix status

  .. code-block:: none
  
    # emgr -l
   
    ID  STATE LABEL      INSTALL TIME      UPDATED BY ABSTRACT
    === ===== ========== ================= ========== ======================================
    1   *Q*   IV16587s02 03/06/12 04:08:29            Ifix for IV16587@6.1TL7SP2          
     
    STATE codes:
     S = STABLE
     M = MOUNTED
     U = UNMOUNTED
     Q = REBOOT REQUIRED
     B = BROKEN
     I = INSTALLING
     R = REMOVING
     T = TESTED
     P = PATCHED
     N = NOT PATCHED
     SP = STABLE + PATCHED
     SN = STABLE + NOT PATCHED
     QP = BOOT IMAGE MODIFIED + PATCHED
     QN = BOOT IMAGE MODIFIED + NOT PATCHED
     RQ = REMOVING + REBOOT REQUIRED

7. Reboot the system when possible, and check again the ifix status

  .. code-block:: none
  
    # emgr -l
     
    ID  STATE LABEL      INSTALL TIME      UPDATED BY ABSTRACT
    === ===== ========== ================= ========== ======================================
    1    S    IV16587s02 03/06/12 04:08:29            Ifix for IV16587@6.1TL7SP2
     
    STATE codes:
    S = STABLE
