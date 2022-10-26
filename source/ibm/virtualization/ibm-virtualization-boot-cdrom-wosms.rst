.. index:: ibm, aix, boot, cdrom

.. meta::
   :keywords: ibm, aix, boot, cdrom

.. _ibm-virtualization-boot-cdrom-wosms:

Загрузка с CD-ROM без SMS
=========================

Понадобилось мне тут загрузиться с CD-ROM в AIX. Так как дело происходило на блейд-центре, то поймать момент когда нужно нажимать "1" я не мог.

В итоге помог вот такой вариант загрузки::

  # bootlist -m normal -o cd0 hdisk0