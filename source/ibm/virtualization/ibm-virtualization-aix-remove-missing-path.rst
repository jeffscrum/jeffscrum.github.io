.. index:: ibm, aix, missing, path

.. _ibm-virtualization-aix-remove-missing-path:

How To Remove Missing Paths In AIX
==================================

Смотрим список пропавших путей
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   root@server:~# lspath
   ...
   Missing hdisk1   fscsi1
   Missing hdisk4   fscsi1
   Missing hdisk5   fscsi1
   ...


Собираем дополнительную информацию
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   root@server:~# lspath  -H -F"name parent path_id connection status" |grep Missing
   ...
   hdisk1   fscsi1 3       50060e80100d2a62,0              Missing
   hdisk4   fscsi1 3       50060e80100d2a62,2000000000000  Missing
   hdisk5   fscsi1 3       50060e80100d2a62,3000000000000  Missing
   ...


Удаляем пути
~~~~~~~~~~~~

.. code-block:: bash

   root@server:~# rmpath -dl hdisk1 -p fscsi1 -w 50060e80100d2a62,0
   path Deleted


Возможные ошибки
~~~~~~~~~~~~~~~~

В случае, если вы получаете вот такую ошибку

.. code-block:: none

   root@server:~# rmpath -dl hdisk1 -p fscsi1 -w 50060e80100d2a62,0
   Method error (/usr/lib/methods/undefine):
   0514-076 Cannot perform the requested function because the specified paths include all paths for the device.

то значит это был последний пути и можно просто удалить устройство

.. code-block:: none

   root@server:~# rmdev -Rdl hdisk1
   hdisk1 deleted
