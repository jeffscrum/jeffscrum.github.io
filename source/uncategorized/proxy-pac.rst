.. index:: linux, proxy, pac, socks

.. meta::
   :keywords: linux, proxy, pac, socks

.. _proxy-pac:

proxy.pac
=========

Для того чтобы каждый раз не переключать proxy-сервер для доступа к системам я написал .pac-файл. 

На серверах sun.t.ru, moon.t.ru и mngmnt.t.ru запущен SOCKS5-proxy. Если никакое из условий не выполняется, то запрос уходит на HTTP-proxy сервер srvisa.t.ru.

Сам файлик лежит в C:/\www/\ на grandma и доступен через http

.. code-block:: javascript
   :caption: proxy.pac

   function FindProxyForURL(url, host) {
       if (isInNet(host, "127.0.0.1", "255.255.255.0")) {
       return "DIRECT;";
       }
        
       if (isInNet(host, "192.168.21.0", "255.255.255.0")) {
       return "SOCKS5 sun.t.ru:1080;";
       }
    
       if (isInNet(host, "192.168.31.0", "255.255.255.0")) {
       return "SOCKS5 moon.t.ru:1080;";
       }
    
       if (isInNet(host, "192.168.41.0", "255.255.255.0")) {
       return "SOCKS5 mngmnt.t.ru:1080;";
       }
    
   return "PROXY srvisa.t.ru:8080;";
   }


