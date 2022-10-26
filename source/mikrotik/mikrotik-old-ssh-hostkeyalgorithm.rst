.. index:: mikrotik, ssh, ciphers

.. meta::
   :keywords: mikrotik, ssh, ciphers

.. _mikrotik-old-ssh-hostkeyalgorithm:

Mikrotik HostKeyAlgorithm
=========================

Есть у меня старющий Mikrotik с прошивкой 5.7. При подключении к нему я стал получать вот такую ошибку:

.. code-block:: bash

  cfish$ ssh admin@192.168.0.1
  Unable to negotiate with 192.168.0.1 port 22: no matching host key type found. Their offer: ssh-dss

После гугления, я нашел, что нужно изменить параметры подключения, но это мне тоже не помогло

.. code-block:: bash

   cfish$ ssh -oHostKeyAlgorithms=+ssh-dss -oPubKeyAcceptedKeyTypes=+dsa admin@192.168.0.1
   ssh_dispatch_run_fatal: Connection to 192.168.0.1 port 22: DH GEX group out of range

В итоге, решение нашлось вот такое -- в конфиг *.ssh/config* нужно дописать такие настройки:

.. code-block:: none

  Host 192.168.0.1
      KexAlgorithms diffie-hellman-group14-sha1
      PubkeyAcceptedKeyTypes +ssh-dss
      HostKeyAlgorithms=+ssh-dss
      Ciphers aes256-ctr,aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc
