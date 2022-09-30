.. index:: ibm, aix, missing, path

.. _ibm-virtualization-remove-failed-paths-mpio:

How To Remove The Failed Paths In MPIO
======================================

1. Смотрим список мертвые путей - ``lspath | grep -v Ena``

2. Далее выбираем один из дисков у которого есть мертвые пути

  .. code-block:: bash
  
     lspath -l hdisk23  -H -F"name parent path_id connection status"
     name    parent path_id connection                       status 
      
     hdisk23 fscsi0 0       50060482d53192c8,d89000000000000 Failed 
     hdisk23 fscsi1 1       5006048ad53192c8,17000000000000  Failed 
     hdisk23 fscsi2 2       50060482d53192c7,d89000000000000 Failed 
     hdisk23 fscsi3 3       5006048ad53192c7,17000000000000  Failed 
     hdisk23 fscsi0 4       50060482d53192cc,270000000000000 Enabled 
     hdisk23 fscsi0 5       5006048ad53192cc,270000000000000 Enabled 
     hdisk23 fscsi1 6       50060482d53192dc,270000000000000 Enabled 
     hdisk23 fscsi1 7       5006048ad53192dc,270000000000000 Enabled 
     hdisk23 fscsi2 8       50060482d53192c3,270000000000000 Enabled 
     hdisk23 fscsi2 9       5006048ad53192c3,270000000000000 Enabled 
     hdisk23 fscsi3 10      50060482d53192d3,270000000000000 Enabled 
     hdisk23 fscsi3 11      5006048ad53192d3,270000000000000 Enabled

3. Удаляем все мертвые пути используя скрипт

.. code-block:: bash

   for disk in `lspv |awk '{ print $1 }'` 
   do
   for path in `lspath -l $disk -F "status connection" |grep Failed |awk '{ print $2 }'` 
   do
   echo $disk 
   rmpath -l $disk -w $path -d 
   done
   done
