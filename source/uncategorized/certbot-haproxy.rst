.. index:: linux, certbot, letsencrypt, renewal, hooks, renewal-hooks, deploy

.. meta::
   :keywords: linux, certbot, letsencrypt, renewal, hooks, renewal-hooks, deploy

.. _certbot-haproxy:

HAProxy and Letsencrypt
=======================

Для работы HAProxy с сертификатами Letsencrypt нужно объединять файлы сертификата и ключа ``cat fullchain.pem privkey.pem > haproxy.pem``. Естетсвенно, отслеживать каждый раз обновление сертификата и склеивать его неудобно.

Можно использовать deploy-hook. Для этого создаем файл `/etc/letsencrypt/renewal-hooks/deploy/10-haproxy.sh` с содержимым:

.. code-block:: bash

  #!/bin/sh
  cd $RENEWED_LINEAGE
  cat fullchain.pem privkey.pem > haproxy.pem

Где, вместо ``$RENEWED_LINEAGE`` будет подставляться путь до сертификата, например `/etc/letsencrypt/live/example.com`.

Теперь, каждый раз, когда сертификат будет обновляться, то автоматически будет создан файл haproxy.pem, который мы и подсунем для HAProxy.

Для проверки можно использовать или stage сервер получения сертификатов или сделать ``certbot certonly -d example.com --force-renewal``.
