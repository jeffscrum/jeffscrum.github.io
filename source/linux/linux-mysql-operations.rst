.. index:: linux, mysql

.. _linux-mysql-operations:

Шпаргалка по MySQL
==================

Заведение базы, пользователя и права на базу
--------------------------------------------

.. code-block:: sql

   $ mysql -u root -p
   Enter password: *****
   > CREATE DATABASE `db_name` CHARACTER SET `utf8` COLLATE `utf8_bin`;
   > GRANT ALL ON db_name.* TO 'user'@'localhost' IDENTIFIED BY 'super_secret_password';
   > FLUSH PRIVILEGES;
   > \q

Проверка базы есть и ее типа
----------------------------

.. code-block:: sql

   SHOW CREATE DATABASE `db_name`;
    
   USE db_name;
   show variables like "character_set_database";
   show variables like "collation_database";

Бекап и рестор базы
-------------------

.. code-block:: bash

   Backup:
   mysqldump -u USER -p PASSWORD DATABASE | gzip > /path/to/outputfile.sql.gz
    
   Restore:
   gunzip < /path/to/outputfile.sql.gz | mysql -u USER -p PASSWORD DATABASE