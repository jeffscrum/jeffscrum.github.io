.. index:: exadata, default, configuration, components, servers, storage, cell

.. meta::
   :keywords: exadata, intel, amd, configuration, components, servers, storage, cell, compute, pmem

.. _oracle-exadata-cell-servers-components:


Exadata Storage Server X10M Extreme Flash
=========================================

- CPU: 2 x 32-core AMD EPYC 9334 processors @ 2.7 GHz (up to 3.9 GHz)
- RAM: 1.5 TB (24 x 64 GB DIMMs) including XRMEM cache
- Flash storage:
  - 4 x 30.72 TB capacity-optimized flash devices (for primary data storage)
  - 4 x 6.8 TB performance-optimized flash devices (primarily for high-performance low-latency caching using Exadata Smart Flash Cache and Exadata Smart Flash Log)
- System storage: 2 x 480 GB NVMe devices
- RDMA Network Fabric: 1 x dual-port CX7 RDMA Network Fabric card; PCIe 4.0, 2 x 100 Gb/s ports active-active (200 Gb/s combined throughput)
- Administration network: 1 x 1 GbE Base-T Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X10M High Capacity
=========================================

- CPU: 2 x 32-core AMD EPYC 9334 processors @ 2.7 GHz (up to 3.9 GHz)
- RAM: 1.5 TB (24 x 64 GB DIMMs) including XRMEM cache
- Disk storage: 12 x 22 TB hard disk drives (HDD)
- Flash storage: 4 x 6.8 TB performance-optimized flash devices
- System storage: 2 x 480 GB NVMe devices
- RDMA Network Fabric: 1 x dual-port CX7 RDMA Network Fabric card; PCIe 4.0, 2 x 100 Gb/s ports active-active (200 Gb/s combined throughput)
- Administration network: 1 x 1 GbE Base-T Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X10M Extended 
====================================

- CPU: 1 x 32-core AMD EPYC 9334 processor @ 2.7 GHz (up to 3.9 GHz)
- RAM: 128 GB (4 x 32 GB DIMMs)
- Disk storage: 12 x 22 TB hard disk drives (HDD)
- System storage: 2 x 480 GB NVMe devices
- RDMA Network Fabric: 1 x dual-port CX7 RDMA Network Fabric card; PCIe 4.0, 2 x 100 Gb/s ports active-active (200 Gb/s combined throughput)
- Administration network: 1 x 1 GbE Base-T Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X9M-2 Extreme Flash
==========================================

- CPU: 2 x 32-core Intel Xeon 8352Y processors @ 2.2 GHz
- RAM: 256 GB (16 x 16 GB DDR4 3200 MT/s DIMMs)
- Flash storage: 8 x 6.4 TB NVMe flash devices (PCIe 4.0)
- Persistent memory: 12 x 128 GB modules (Intel Optane Persistent Memory 200 Series, NMB1XXD128GPS)
- System storage: 2 x 240 GB M.2 devices
- RDMA Network Fabric: 1 x dual-port CX5 RDMA Network Fabric card; PCIe 4.0, 2 x 100 Gb/s ports active-active (200 Gb/s combined throughput)
- Administration network: 1 x 1 GbE Base-T Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X9M-2 High Capacity
==========================================

- CPU: 2 x 32-core Intel Xeon 8352Y processors @ 2.2 GHz, but only half of the CPU cores are enabled on Eighth Rack configurations
- RAM: 256 GB (16 x 16 GB DDR4 3200 MT/s DIMMs)
- Disk storage: 12 x 18 TB hard disk drives (HDD), but only 6 HDD on Eighth Rack configurations
- Disk controller Host Bus Adapter (HBA) with 2 GB cache
- Flash storage: 4 x 6.4 TB NVMe flash devices (PCIe 4.0), but only 2 flash devices on Eighth Rack configurations
- Persistent memory: 12 x 128 GB modules (Intel Optane Persistent Memory 200 Series, NMB1XXD128GPS), but only 6 modules on Eighth Rack configurations
- System storage: 2 x 240 GB M.2 devices
- RDMA Network Fabric: 1 x dual-port CX5 RDMA Network Fabric card; PCIe 4.0, 2 x 100 Gb/s ports active-active (200 Gb/s combined throughput)
- Administration network: 1 x 1 GbE Base-T Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X9M-2 Extended 
=====================================

- CPU: 1 x 32-core Intel Xeon 8352Y processor @ 2.2 GHz
- RAM: 96 GB (6 x 16 GB DDR4 3200 MT/s DIMMs)
- Disk storage: 12 x 18 TB hard disk drives (HDD)
- Disk controller Host Bus Adapter (HBA) with 2 GB cache
- System storage: 2 x 240 GB M.2 devices
- RDMA Network Fabric: 1 x dual-port CX5 RDMA Network Fabric card; PCIe 4.0, 2 x 100 Gb/s ports active-active (200 Gb/s combined throughput)
- Administration network: 1 x 1 GbE Base-T Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X8M-2 and X8-2 Extreme Flash
===================================================

- CPU: 2 x 16-core Intel Xeon 5218 Processors @ 2.3GHz
- RAM: 192 GB RAM (12 x 16 GB DIMMs)(full 6 channels)
- **X8M-2 only**: 12 x 128 GB Intel Optane DC Persistent Memory modules (NMA1XXD128GPS)
- Flash storage: 8 x 6.4 TB flash accelerator PCIe cards
- System storage: 2 x 240 GB M.2 devices for system partitions (partitioned as 150 GB devices)
- **X8M-2 only**: 1 dual-port (PCIe 3.0), both ports active, 100Gb/s RDMA Network Fabric Card
- **X8-2 only**: 2 x InfiniBand 4X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA)), all ports active
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X8M-2 and X8-2 High Capacity
===================================================

- CPU: 2 x 16-core Intel Xeon 5218 Processors @ 2.3GHz
- RAM: 192 GB RAM (12 x 16 GB DIMMs)(full 6 channels)
- **X8M-2 only**: 12 x 128 GB Intel Optane™ DC Persistent Memory modules (NMA1XXD128GPS)
- Disk storage: 12 x 14 TB High Capacity SAS disks, but only 6 drives on Eighth Rack configurations
- System storage: 2 x 240 GB M.2 devices for system partitions (partitioned to appear as 150 GB devices)
- Flash storage: 4 x 6.4 TB flash accelerator PCIe cards
- Disk controller HBA with 2 GB cache
- **X8M-2 only**: 1 dual-port (PCIe 3.0), both ports active, 100Gb/s RDMA Network Fabric Card
- **X8-2 only**: 2 x InfiniBand 4X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA)), all ports active
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X8M-2 and X8-2 Extended 
==============================================

- CPU: 1 x 16-core Intel Xeon 5218 Processor @ 2.3GHz
- RAM: 96 GB RAM (6 x 16 GB DIMMs)(full 6 channels)
- Disk storage: 12 x 14 TB High Capacity SAS disks
- System storage: 2 x 240 GB M.2 devices for system partitions
- Disk controller HBA with 2 GB cache
- **X8M-2 only**: 1 dual-port (PCIe 3.0), both ports active, 100Gb/s RDMA Network Fabric Card
- **X8-2 only**: 2 x InfiniBand 4X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA)), all ports active
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X7-2 Extreme Flash
=========================================

- CPU: 2 x Intel Xeon Silver 4114 Processors @ 2.20GHz
- RAM: 192 GB RAM (12 x 16 GB)(full 6 channels)
- Flash storage: 8 x 6.4 TB flash accelerator PCIe cards
- System storage: 2 x 150 GB M.2 devices for system partitions
- RDMA Network Fabric: 2 x InfiniBand 4X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA)), all ports active
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X7-2 High Capacity
=========================================

- CPU: 2 x Intel Xeon Silver 4114 Processors @ 2.20GHz
- RAM: 192 GB RAM (12 x 16 GB) – full 6 channels
- Disk storage: 12 x 10 TB High Capacity SAS disks
- System storage: 2 x 150 GB M.2 devices for system partitions
- Flash storage: 4 x 6.4 TB flash accelerator PCIe cards
- Disk controller HBA with 2 GB cache
- RDMA Network Fabric: 2 x InfiniBand 4X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA)), all ports active
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X6-2 Extreme Flash
=========================================

- CPU: 2 x 10-Core Intel Xeon CPU E5-2630 v4 @ 2.2 GHz
- RAM: 128 GB RAM (8 x 16 GB)
- Flash storage: 8 x 3.2 TB 2.5-inch flash accelerator F320 PCIe drives
- RDMA Network Fabric: 2 x InfiniBand 4X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA)), all ports active
- 4 embedded Gigabit Ethernet ports
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X6-2 High Capacity
=========================================

- CPU: 2 x 10-Core Intel Xeon CPU E5-2630 v4 @ 2.2 GHz
- RAM: 128 GB RAM (8 x 16 GB)
- Disk storage: 12 x 8 TB 7.2 K RPM High Capacity SAS disks (in earlier releases, the high capacity disks were 4 TB)
- Flash storage: 4 x 3.2 TB flash accelerator F320 PCIe card
- Disk controller HBA with 1 GB cache
- RDMA Network Fabric: 2 x InfiniBand 4X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA)) - all ports active
- 4 embedded Gigabit Ethernet ports
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X5-2 Extreme Flash
=========================================

- CPU: 2 x 8-Core Intel Xeon CPU E5-2630 v3 @ 2.40GHz
- RAM: 64 GB RAM (8x 8 GB)
- Flash storage: 8 x 1.6 TB NVMe PCIe 3.0 SSD Extreme Flash disks
- RDMA Network Fabric: 2 InfiniBand 4 X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA))
- 4 embedded Gigabit Ethernet ports
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X5-2 High Capacity
=========================================

- CPU: 2 x 8-Core Intel Xeon CPU E5-2630 v3 (2.40GHz)
- RAM: 96 GB RAM (4x 8 GB and 4x 16 GB)
- Disk storage: 12 x 8 TB 7.2 K RPM High Capacity SAS disks (in earlier releases, the high capacity disks were 4 TB)
- Flash storage: 4 x 1.6 TB flash accelerator F160 PCIe cards
- Disk controller HBA with 1 GB supercap-backed write cache
- RDMA Network Fabric: 2 InfiniBand 4 X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA))
- 4 embedded Gigabit Ethernet ports
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Exadata Storage Server X4-2
===========================

- CPU: 2 x 6-Core Intel Xeon E5-2630 v2 processors (2.6 GHz)
- RAM: 96 GB RAM (4 x 8 GB, and 4 x 16 GB))
- Disk storage: 12 x 1.2 TB 10 K RPM High Performance SAS disks or 12 x 4 TB 7.2 K RPM High Capacity SAS disks
- Flash storage: 4 x 800 GB Sun Flash Accelerator F80 PCIe Cards
- Disk controller HBA with 512 MB battery-backed write cache, and swappable BBU
- RDMA Network Fabric: 2 InfiniBand 4 X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA))
- 4 embedded Gigabit Ethernet ports
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port


Exadata Storage Server X3-2
===========================

- CPU: 2 x 6-Core Intel Xeon E5-2630L processors (2 GHz)
- RAM: 64 GB RAM (8 x 8 GB)
- Disk storage: 12 x 600 GB 15 K RPM High Performance SAS disks or 12 x 3 TB 7.2 K RPM High Capacity SAS disks
- Flash storage: 4 x 400 GB Sun Flash Accelerator F40 PCIe Cards
- Disk controller HBA with 512 MB battery-backed write cache
- RDMA Network Fabric: 2 InfiniBand 4 X QDR (40 Gb/s) InfiniBand ports (1 dual-port PCIe 2.0 Host Channel Adapter (HCA))
- 4 embedded Gigabit Ethernet ports
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port


Exadata Storage Server Sun Fire X4270 M2
========================================

- CPU: 2 x 6-Core Intel Xeon L5640 processors (2.26 GHz)
- RAM: 24 GB RAM
- Disk storage: 12 x 600 GB 15 K RPM High Performance SAS disks or 12 x 3 TB 7.2 K RPM High Capacity SAS disks (in earlier releases, the high capacity disks were 2 TB)
- Flash storage: 4 x 96 GB Sun Flash Accelerator F20 PCIe Cards
- Disk controller HBA with 512 MB battery-backed write cache
- Dual-port 4X QDR (40 Gb/s) InfiniBand Host Channel Adapter (HCA)
- 1 embedded Gigabit Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port


Exadata Storage Server Sun Fire X4275
=====================================

- CPU: 2 x 4-Core Intel Xeon E5540 processors (2.53 GHz)
- RAM: 24 GB RAM
- Disk storage: 12 x 600 GB 15 K RPM High Performance SAS disks or 12 x 2 TB 7.2 K RPM SATA disks
- Flash storage: 4 x 96 GB Sun Flash Accelerator F20 PCIe Cards
- Disk controller HBA with 512 MB battery-backed write cache
- Dual-port 4X QDR (40 Gb/s) InfiniBand Host Channel Adapter (HCA)
- 1 embedded Gigabit Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port


----
Parent topic: `Hardware Components of Oracle Exadata <https://docs.oracle.com/en/engineered-systems/exadata-database-machine/dbmso/hardware-components-exadata-db-machine.html>`_
