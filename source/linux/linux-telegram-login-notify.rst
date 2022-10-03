.. index:: linux, telegram, notyfy, ssh

.. _linux-telegram-login-notify:

Уведомление о логине в Telegram
===============================

Скрипт будет присылать вам уведомление в Telegram каждый раз как кто-то заходит на сервер по SSH

Для его работы нужно установить пакет `jq`: ``sudo apt-get install jq``

.. code-block:: bash

   USERID="-1071597155692"                                   # Channel ID
   KEY="514235123:AAGeYjt481234cRrZQ1234rhc4FBVfAaINU"       # Bot API key
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

Получившийся файл должен иметь расширение .sh. Его нужно разместить в каталог ``/etc/profile.d/``
