.. index:: linux, telegram, notyfy, ssh, terminal

.. meta::
   :keywords: linux, telegram, notyfy, ssh, terminal

.. _linux-telegram-login-notify:

Уведомление о логине в Telegram
===============================

Скрипт будет присылать вам уведомление в Telegram каждый раз как кто-то заходит на сервер по SSH. Для его работы нужно установить пакет `jq`: ``sudo apt-get install jq``

Файл должен иметь расширение .sh. Разместить его нужно в каталоге ``/etc/profile.d/``

.. code-block:: bash

   USERID="-107159715...2"                                   # Channel ID
   KEY="514235123:AAG...some text...234rhfc4FBVfAaINU"       # Bot API key
   TIMEOUT="10"
   URL="https://api.telegram.org/bot$KEY/sendMessage"
   DATE_EXEC="$(date "+%d %b %Y %H:%M")"
   TMPFILE='/tmp/ipinfo-$DATE_EXEC.txt'
   if [ -n "$SSH_CLIENT" ]; then
       IP=$(awk '{print $1}' <<< $SSH_CLIENT)
       PORT=$(awk '{print $3}' <<< $SSH_CLIENT)
       HOSTNAME=$(hostname -f)
       IPADDR=$(hostname -I | awk '{print $1}')
       curl http://ipinfo.io/$IP -s -o $TMPFILE
       CITY=$(jq -r '.city' < $TMPFILE)
       REGION=$(cat $TMPFILE | jq '.region' | sed 's/"//g')
       COUNTRY=$(cat $TMPFILE | jq '.country' | sed 's/"//g')
       ORG=$(cat $TMPFILE | jq '.org' | sed 's/"//g')
       TEXT="$DATE_EXEC: Вход пользователя ${USER} по SSH на $HOSTNAME ($IPADDR) из $IP - $ORG - $CITY, $REGION, $COUNTRY через порт $PORT"
       curl -s --max-time $TIMEOUT -d "chat_id=$USERID&disable_web_page_preview=1&text=$TEXT" $URL > /dev/null
       rm $TMPFILE
   fi
