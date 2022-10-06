.. index:: macos, mac, install, nvidia, driver

.. meta::
   :keywords: macos, mac, install, nvidia, driver, apple

.. _macos-install-nvidia-drv:

How to install NVIDIA drivers on Mac OS
=======================================

.. code-block:: none

   # Check your OS build in Software section (about this mac)
   # and check drivers version for this build
   https://create.pro/nvidia_drivers
   
   
   # Disable SIP
   # Reboot with CMD + R
   csrutil disable 
   
   
   # Reboot
   csrutil status
   
   
   # Install Drivers
   bash <(curl -s https://vulgo.github.io/webdriver) 387.10.10.10.40.133
   
   
   # Enable SIP
   # Reboot with CMD + R
   csrutil enable 