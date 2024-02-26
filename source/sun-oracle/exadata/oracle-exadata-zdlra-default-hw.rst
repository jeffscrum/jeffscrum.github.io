.. index:: zdlra, defaut, configuration, exadata

.. _oracle-exadata-zdlra-default-hw:

ZDLRA & Exadata Default Hardware 
================================

ZDLRA RA21
~~~~~~~~~~

Compute Server (Oracle Server X9-2)

- 2 x 32-core Intel(R) Xeon(R) Platinum 8358 CPU @ 2.60GHz
- 384 Gb RAM (12 x 32 GB DDR4-3200)
- 2 x 3.84 TB NVMe SSD (2.5'')
- 1 Dual Port QSFP28 100GbE Adapter Gen 4
- 1 Dual 10/25-Gigabit SFP28 Ethernet Card
- 1 Dual 10/25-Gigabit SFP28 Ethernet Card (optional)

Storage Server (Oracle Server X9-2L)

- 1 x Intel(R) Xeon(R) Platinum 8352Y CPU @ 2.20GHz
- 128 Gb RAM (8 x 16 Gb DDR4-3200)
- 1 Raid HBA (MegaRAID SAS 9361-16i)
- 12 x 18 TB HDD (7200 RPM SAS-3)
- 2 x 6.4 TB Flash Accelerator F640 v3
- 2 x 240 GB M.2 SSD
- 1 Dual Port QSFP28 100GbE Adapter

ZDLRA X9M
~~~~~~~~~

Storage Server (Oracle Server X9-2L)

- 1 x 32-core Intel(R) Xeon(R) 8352Y processor (2.2 GHz)
- 128 GB RAM
- 12 x 18 TB 7,200 RPM disks
- 2 x NVMe PCIe4.0 Flash Cards


Exadata X9M
~~~~~~~~~~~

Storage Server Extreme Flash (EF) (Oracle Server X9-2L):

- 2 x 32-core Intel(R) Xeon(R) 8352Y processors (2.2 GHz)
- 256 GB RAM
- 1.5 TB Persistent Memory
- 8 x 6.4 TB NVMe PCIe4.0 Flash cards

Storage Server High Capacity (HC) (Oracle Server X9-2L):

- 2 x 32-core Intel(R) Xeon(R) 8352Y processors (2.2 GHz)
- 256 GB RAM
- 1.5 TB Persistent Memory
- 12 x 18 TB 7,200 RPM disks
- 4 x 6.4 TB NVMe PCIe4.0 Flash cards


.. Для переделки сервера от ZDLRA X9M под Exadata X9M Extreme Flash:
     - Установить дополнительный процессор 2.2GHz 32-Core Intel Xeon 8352Y (pn 8207510)
     - Установить дополнительный радиатор для процессора (pn 8200986)
     - Установить 8 x 16GB DDR4-3200 (+128 GB RAM)(pn 8201155)
     - Установить 12 x 128GB Intel Optane PMEM [NMB1XXD128GPS](1.5 TB Persistent Memory)(pn 8206414)
     - Установить 6 x 6.4TB Flash Accelerator F640 v3 NVMe PCIe Card (pn 8204597)
     - Демонтировать 12 x 18 TB 7,200 RPM disks 3.5'' и на их место установить заглушки (у заглушек не вижу pn)

.. Для переделки сервера от ZDLRA X9M под Exadata X9M High Capacity:
     - Установить дополнительный процессор 2.2GHz 32-Core Intel Xeon 8352Y (pn 8207510)
     - Установить дополнительный радиатор для процессора (pn 8200986)
     - Установить 8 x 16GB DDR4-3200 (+128 GB RAM)(pn 8201155)
     - Установить 12 x 128GB Intel Optane PMEM [NMB1XXD128GPS](1.5 TB Persistent Memory)(pn 8206414)
     - Установить 2 x 6.4TB Flash Accelerator F640 v3 NVMe PCIe Card (pn 8204597)
