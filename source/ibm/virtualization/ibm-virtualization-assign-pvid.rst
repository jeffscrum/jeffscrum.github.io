.. index:: imb, pvid

.. _ibm-virtualization-assign-pvid:

Assign PVID to a new disk
=========================

Команда используется для того чтобы AIX считал PVID с диска

.. code:block:: bash

   # lspv
   hdisk0          00c0e90dce6c290a                    rootvg          active              
   hdisk1          none                                None                                
   hdisk2          none                                None                              
    
             Disk name Attribute
            |         | 
   # chdev -l hdisk1 -a pv=yes
   hdisk1 changed
    
   # lspv
   hdisk0          00c0e90dce6c290a                    rootvg          active              
   hdisk1          00c4489d762b6769                    None
