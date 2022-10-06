.. index:: matrix, bot

.. meta::
   :keywords: matrix, bot

.. _matrix-bot:

Matrix Bot
==========

Для работы потребуется установить пакет ``jq``

.. code-block:: none

   sudo apt install jq

Скрипт бота

.. code-block:: bash
   :caption: post_to_matrix.sh

   #!/bin/bash
   # Usage:
   # echo "Hello world" | ./post_to_matrix.sh
   msgtype=m.text
   homeserver=glasgow.social
   room=!BOrDFgeDdZZbUvfjjs:glasgow.social
   access_token=put_your_user_access_token_here
    
   curl -XPOST -d "$( jq -Rsc --arg msgtype "$msgtype" '{$msgtype, body:.}')" "https://$homeserver/_matrix/client/r0/rooms/$room/send/m.room.message?access_token=$access_token"