.. index:: mediawiki

.. _mw-tiny-url:

ЧПУ в MediaWiki
================

Адреса страниц по-умолчанию имеют вид: ``wikisite.ru/index.php?title=Название_страницы``. Для поисковых ботов это не проблема, но гораздо удобнее настроить Человеко-Понятные Урлы (ЧПУ), чтобы страницы имели красивый вид: ``wikisite.ru/Название_страницы``


Настройка ЧПУ
-------------

Есть хороший и автоматизированный инструмент - http://shorturls.redwerks.org

От вас требуется указать адрес вашей вики, система сама автоматически просканирует ваш сайт и предложит указать дополнительные параметры:

* Article Path — как должны выглядеть адреса страниц вашей вики в адресной строке браузера, например /wiki/$1
* Include 404 thumbnail handler config — включить обработчик 404 ошибки для ваших превьюшек, включим

Затем выбираем, какой конфиг нам нужен — в файлах .htacces или сразу конфиг для апача.

Кроме апача, можно сгенерировать конфиги под LiteSpeed, Nginx, Lighttpd, IIS

В конце не забываем указать физический путь к вашему index.php в корне вики.

Генератор выдает фрагменты настроек сервера и LocalSettings.php


----

Если ваша wiki недоступна снаружи, то вот примерный конфиг для nginx

.. code-block:: bash

   server {
       listen 80;
       server_name dev.ksomov.ru;
       root /websrv/dev.ksomov.ru;
       index index.html index.htm index.php;
       access_log /var/log/nginx/dev.ksomov.ru_sh_.access.log;
       error_log /var/log/nginx/dev.ksomov.ru_su_.error.log;
       # Location for the wiki's root
       location / {
           try_files $uri $uri/ @mediawiki;
           # Do this inside of a location so it can be negated
           location ~ \.php$ {
               try_files $uri $uri/ =404; # Don't let php execute non-existent php files
               include /etc/nginx/fastcgi_params;
               fastcgi_pass unix:/var/run/php5-fpm.sock;
           }
       }
       location /images {
           # Separate location for images/ so .php execution won't apply
           location ~ ^/images/thumb/(archive/)?[0-9a-f]/[0-9a-f][0-9a-f]/([^/]+)/([0-9]+)px-.*$ {
               # Thumbnail handler for MediaWiki
               # This location only matches on a thumbnail's url
               # If the file does not exist we use @thumb to run the thumb.php script
               try_files $uri $uri/ @thumb;
           }
       }
       location /images/deleted {
           # Deny access to deleted images folder
           deny    all;
       }
       # Deny access to folders MediaWiki has a .htaccess deny in
       location /cache       { deny all; }
       location /languages   { deny all; }
       location /maintenance { deny all; }
       location /serialized  { deny all; }
       # Just in case, hide .svn and .git too
       location ~ /.(svn|git)(/|$) { deny all; }
       # Hide any .htaccess files
       location ~ /.ht { deny all; }
       # Uncomment the following code if you wish to hide the installer/updater
       ## Deny access to the installer
       location /mw-config { deny all; }
       # Handling for the article path
       location @mediawiki {
           include /etc/nginx/fastcgi_params;
           # article path should always be passed to index.php
           fastcgi_param SCRIPT_FILENAME   $document_root/index.php;
           fastcgi_pass  unix:/var/run/php5-fpm.sock;
       }
       # Thumbnail 404 handler, only called by try_files when a thumbnail does not exist
       location @thumb {
           # Do a rewrite here so that thumb.php gets the correct arguments
           rewrite ^/images/thumb/[0-9a-f]/[0-9a-f][0-9a-f]/([^/]+)/([0-9]+)px-.*$ /thumb.php?f=$1&width=$2;
           rewrite ^/images/thumb/archive/[0-9a-f]/[0-9a-f][0-9a-f]/([^/]+)/([0-9]+)px-.*$ /thumb.php?f=$1&width=$2&archived=1;
           # Run the thumb.php script
           include /etc/nginx/fastcgi_params;
           fastcgi_param SCRIPT_FILENAME   $document_root/thumb.php;
           fastcgi_pass  unix:/var/run/php5-fpm.sock;
       }
   }

В файл *LocalSettings.php* дописать:

.. code-block:: bash

   $wgScriptPath = "";
   $wgScriptExtension = ".php";
   $wgArticlePath = "/$1";
   $wgUsePathInfo = true;
