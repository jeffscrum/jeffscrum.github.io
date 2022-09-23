.. index:: mediawiki, smtp

.. _mw-configure-smtp-server:

Настройка SMTP server
=====================

Устанавливаем необходимые пакеты для PHP

.. code-block:: bash

  $ apt-get install php-pear
  $ pear install mail
  $ pear install Net_SMTP
  $ pear install Auth_SASL
  $ pear install mail_mime

Вносим изменения в файл *LocalSettings.php*, секция $wgSMTP. В данном случае письма будут отправляться через сервис mandrillapp, а не напрямую с сервера.

.. code-block:: bash

  $wgSMTP = array(
   'host'     => "smtp.mandrillapp.com", // could also be an IP address. Where the SMTP server is located
   'IDHost'   => "dev.ksomov.ru",        // Generally this will be the domain name of your website (aka mywiki.org)
   'port'     => 587,                    // Port to use when connecting to the SMTP server
   'auth'     => true,                   // Should we use SMTP authentication (true or false)
   'username' => "login",                // Username to use for SMTP authentication (if being used)
   'password' => "password"              // Password to use for SMTP authentication (if being used)
  );
