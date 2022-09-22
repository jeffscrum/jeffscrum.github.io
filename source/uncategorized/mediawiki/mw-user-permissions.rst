.. index:: mediawiki

.. _mw-user-permissions:


User permissions
================

.. code-block:: php
    :caption: LocalSettings.php

  ################
  # Restrictions #
  ################
  $wgDisableAnonTalk = false;     // Disable talk pages for anonymous users (IPs)
  $wgShowIPinHeader = false;      // Show the IP in the user bar for anonymous users by default
