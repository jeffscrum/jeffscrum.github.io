.. index:: linux, postfix, mail, relay, gmail

.. meta::
   :keywords: linux, postfix, mail, relay, gmail

.. _ubuntu-postfix-gmail-relay:

Postfix Relay для Gmail в Ubuntu
================================

.. attention:: SMTP Сервер от Gmail имеет ограничение — `500 писем в день <https://support.google.com/a/answer/166852?hl=en&topic=28609&ctx=topic>`_. Используйте его с умом!


.. note::

   Для отправки писем через smtp.gmail.com нужно:

   * Иметь учетку в gmail через которую мы будем отправлять письма
   * Включить Less secure app access для этой учетки https://myaccount.google.com/u/2/lesssecureapps?utm_source=google-account&utm_medium=web

1. Устанавливаем postfix и утилиты

  .. code-block:: bash
  
     sudo aptitude install postfix mailutils

2. Добавляем в конец `/etc/postfix/main.cf`

  .. code-block:: bash
  
     # Relaying Postfix SMTP via GMAIL
     relayhost = [smtp.gmail.com]:587
     smtp_sasl_auth_enable = yes
     smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
     smtp_sasl_security_options = noanonymous
     smtp_tls_CAfile = /etc/postfix/cacert.pem
     smtp_use_tls = yes

  Сертификат *cacert.pem* можно скачать на `GitHub <https://github.com/google/certificate-transparency/blob/master/test/testdata/ca-cert.pem>`_

3. Файл с паролем для авторизации gmail - `/etc/postfix/sasl_passwd`

  .. code-block:: bash

     [smtp.gmail.com]:587 user@gmail.com:password

4. Расставляем права на файлы и перезагружаем postfix

  .. code-block:: bash

     sudo chmod 400 /etc/postfix/sasl_passwd
     sudo postmap /etc/postfix/sasl_passwd
     sudo service postfix restart

5. Проверяем отправляются ли письма

  .. code-block:: bash

     echo "Hello World" | mail -s "Test Message" user@gmail.com

6. Заглядываем в лог `/var/log/mail.log` и смотрим ушло ли письмо.
