.. index:: linux, error

.. meta::
   :keywords: linux, error

.. _linux-lc-all-unset:

LC_ALL = (unset)
================

Для решения ошибки вида

.. code-block:: none

   perl: warning: Setting locale failed.
   perl: warning: Please check that your locale settings:
       LANGUAGE = "en_US.UTF-8",
       LC_ALL = (unset),
       LANG = "en_US"
       are supported and installed on your system.
   perl: warning: Falling back to the standard locale ("C").

Необходимо добавить строчку в файле `/etc/environment`

.. code-block:: none

   LC_ALL=en_US.UTF-8
   LANG=en_US.UTF-8