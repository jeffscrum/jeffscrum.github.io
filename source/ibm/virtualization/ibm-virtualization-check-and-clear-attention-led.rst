.. index:: ibm, hmc, alarm

.. _ibm-virtualization-check-and-clear-attention-led:

Check And Clear Attention LED
=============================

To list the various LED states issue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. For the physical managed system (I'll call it managed_system, please replace with your actual name) ``lsled -m managed_system -r sa -t phys``
2. For the virtual partitions ``lsled -m managed_system -r sa -t virtuallpar``. Output will be ``state=off`` or ``state=on`` (for -t virtuallpar accompanied by lpar id and name)


To change the state of an attention LED to "off" issue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. For the physical managed system ``chled -m managed_system -r sa -o off -t phys``
2. For a virtual partition (I'll call it partition_name, please replace with your actual name) ``chled -m managed_system -r sa -o off -t virtuallpar -p partition_name``
