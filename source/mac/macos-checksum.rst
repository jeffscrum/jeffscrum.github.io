.. index:: macos, mac, sha, md5

.. meta::
   :keywords: macos, mac, sha, md5, apple

.. _macos-checksum:

Get Checksum
============

MD5 checksum
~~~~~~~~~~~~

In order to find the MD5 checksum value of a file using the following command in the terminal.

.. code-block:: none

   $ md5 </path/to/file>


Using OpenSSL to check MD5
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following command to get the MD5 checksum using openssl command.

.. code-block:: none

   $ openssl md5 </path/to/file>


SHA1 checksum
~~~~~~~~~~~~~

To find the SHA1 checksum value use the following command in the terminal.

.. code-block:: none

   $ shasum -a 1 </path/to/file>


Using OpenSSL to check SHA1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following command to get the SHA256 checksum using openssl command in the terminal.

.. code-block:: none

   $ openssl sha1 </path/to/file>


SHA256 checksum
~~~~~~~~~~~~~~~

To find the SHA256 checksum use the following command in the terminal.

.. code-block:: none

   $ shasum -a 256 </path/to/file>


Using OpenSSL to check SHA256
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following command to get the SHA256 checksum using openssl command in the terminal.

.. code-block:: none

   $ openssl sha256 </path/to/file>


SHA512 checksum
~~~~~~~~~~~~~~~

To find the SHA512 checksum use the following command.

.. code-block:: none

   $ shasum -a 512 </path/to/file>


Using OpenSSL to check SHA512
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following command to get the SHA512 checksum using openssl command in the terminal.

.. code-block:: none

   $ openssl sha512 </path/to/file>
