.. index:: ibm, storage, fw, upgrade, v7000, storwize

.. meta::
   :keywords: ibm, storage, fw, upgrade, v7000, storwize

.. _ibm-storages-hdd-healthcheck:

Storwize V7000 HDD HealthCheck
==============================

.. code-block:: bash

  #!/bin/sh
  # Jeff Scrum
  # Version: 1
  echo "Checking Storwize-1..."
  ssh monitor@192.168.12.156 'lsdrive'| grep sas_hdd | grep -v online
  echo ""
  echo "Checking Storwize-2..."
  ssh monitor@192.168.12.152 'lsdrive'| grep sas_hdd | grep -v online
  echo ""
  echo "Checking Storwize-3..."
  ssh monitor@192.168.12.153 'lsdrive'| grep sas_hdd | grep -v online
  echo ""
  echo "Checking Storwize-4..."
  ssh monitor@192.168.12.259 'lsdrive'| grep sas_hdd | grep -v online
  echo ""
  echo "Checking Storwize-5..."
  ssh monitor@192.168.12.252 'lsdrive'| grep sas_hdd | grep -v online
  echo ""
  echo "Checking Storwize-6..."
  ssh monitor@192.168.12.251 'lsdrive'| grep sas_hdd | grep -v online
  echo ""
  echo "Checking Storwize-7..."
  ssh monitor@192.168.12.250 'lsdrive'| grep sas_hdd | grep -v online