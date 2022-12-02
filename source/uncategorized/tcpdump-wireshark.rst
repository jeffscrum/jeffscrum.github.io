.. index:: tcpdump, wireshark, capture, log

.. meta::
   :keywords: tcpdump, wireshark, capture, log

.. _tcpdump-wireshark:

Capturing with 'tcpdump' for viewing with Wireshark
===================================================

It’s often more useful to capture packets using tcpdump rather than wireshark. For example, you might want to do a remote capture and either don’t have GUI access or don’t have Wireshark installed on the remote machine.

Older versions of tcpdump truncate packets to 68 or 96 bytes. If this is the case, use -s to capture full-sized packets:

.. code-block:: none

   $ tcpdump -i <interface> -s 65535 -w <file>

You will have to specify the correct interface and the name of a file to save into. In addition, you will have to terminate the capture with ``^C`` when you believe you have captured enough packets.
