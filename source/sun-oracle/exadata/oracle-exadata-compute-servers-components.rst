.. index:: exadata, default, configuration, components, servers, compute, db

.. meta::
   :keywords: exadata, intel, amd, configuration, components, servers, compute, db, pmem

.. _oracle-exadata-compute-servers-components:

Oracle Exadata Database Server Hardware Components
==================================================

Oracle Exadata X10M Database Server Hardware Components
-------------------------------------------------------

- CPU: 2 x 96-core AMD EPYC 9J14 processors @ 2.6 GHz (up to 3.7 GHz)
- RAM: 512 GB RAM (16 x 32 GB DIMMs), 1.5 TB (24 x 64 GB DIMMs), 2.25 TB (24 x 96 GB DIMMs), or 3 TB (24 x 128 GB DIMMs)
- System storage: 2 x 3.84 TB PCIe 4.0 NVMe storage devices, expandable to 4 devices
- RDMA Network Fabric: 1 x dual-port CX7 RDMA Network Fabric card; PCIe 4.0, 2 x 100 Gb/s ports active-active (200 Gb/s combined throughput)
- Administration network: 1 x 1 GbE Base-T Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port
- Client and additional network connectivity:

  - Two factory-installed CX6-LX network cards. Each card contains 2 x SFP+/SFP28 ports (10/25 GbE)
  - Up to 3 optional network cards. Each card can be any of the following:

    - CX6-LX with 2 x SFP+/SFP28 ports (10/25 GbE)
    - CX6-DX with 2 x QSFP28 ports (100GbE). Each QSFP28 port can support one 10 GbE or 25 GbE link with appropriate breakout cables.
    - Fortpond RJ45 Ethernet with 4 x 10GBASE-T ports (10 GbE)


Oracle Exadata X9M-2 Database Server Hardware Components
--------------------------------------------------------

- CPU: 32-core Intel Xeon 8358 processors @ 2.6 GHz:

  - Flexible configuration: 2 CPUs
  - Eighth Rack: 1 CPU

- RAM:

  - Flexible configuration: 512 GB RAM (16 x 32 GB DIMMs), expandable to 1 TB (16 x 64 GB DIMMs), 1.5 TB (16 x 32 GB and 16 x 64 GB DIMMs), or 2 TB (32 x 64 GB DIMMs) with memory expansion kit
  - Eighth Rack: 384 GB RAM (12 x 32 GB DIMMs), expandable to 1 TB (16 x 64 GB DIMMs) with memory expansion kit

- System storage: 2 x 3.84 TB PCIe 4.0 NVMe storage drives, expandable to 4 drives
- RDMA Network Fabric: 1 x dual-port CX5 RDMA Network Fabric card; PCIe 4.0, 2 x 100 Gb/s ports active-active (200 Gb/s combined throughput)
- Administration network: 1 x 1 GbE Base-T Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port
- Client and additional network connectivity:

  - Flexible configuration options:

    - Two factory-installed network cards. Each card contains 2 x SFP+/SFP28 ports (10/25 GbE) or 4 x 10GBASE-T ports (10 GbE)
    - One optional field-installed network card containing 2 x SFP+/SFP28 ports (10/25 GbE) or 4 x 10GBASE-T ports (10 GbE) or 2 x QSFP28 ports (100GbE). Each QSFP28 port can support one 10 GbE or 25 GbE link with appropriate breakout cables.
  - Eighth Rack: Two factory-installed network cards only. Each card contains 2 x SFP+/SFP28 ports (10/25 GbE) or 4 x 10GBASE-T ports (10 GbE)


Oracle Exadata X9M-8 Database Server Hardware Components
--------------------------------------------------------

- CPU: 8 x 24-core Intel Xeon Platinum 8268 Processors @ 2.9GHz
- RAM: 3 TB (48 x 64 GB DIMMs), expandable to a maximum of 6 TB (96 x 64 GB DIMMs)
- System storage: 2 x 6.4 TB flash accelerator PCIe cards (Hot-Pluggable)
- RDMA Network Fabric: 4 x dual-port QSFP28 100 Gb/s PCIe 3.0 RDMA Network Fabric cards - all ports active
- Network connectivity:

  - 8 x 10GBASE-T ports (1/10 GbE) - 1 port used for the administration network
  - 8 x SFP+/SFP28 ports (10/25 GbE)

- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Oracle Exadata X8M-2 Database Server Hardware Components
--------------------------------------------------------

- CPU: 2 x 24-core Intel Xeon Platinum 8260 Processors @ 2.4 GHz
- RAM: 384 GB RAM (12 x 32 GB DIMMs), expandable to 1.5 TB (24 x 64 GB DIMMs) with memory expansion kit
- System storage: 4 x 1.2 TB boot drive/hard disks, hot swappable, expandable to 8 drives
- Disk controller HBA with 2 GB cache (no batteries)
- RDMA Network Fabric: 1 x dual-port QSFP28 100 Gb/s PCIe 3.0 RDMA Network Fabric card - both ports active
- Client network: 2 x SFP+/SFP28 ports (10/25 GbE) or 2 x 10GBASE-T ports (10 GbE)
- Backup/optional networks: 2 x SFP+/SFP28 ports (10/25 GbE) or 4 x 10GBASE-T ports (10 GbE)
- Administration network: 1 x 1 GbE Base-T Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Oracle Exadata X8M-8 Database Server Hardware Components
--------------------------------------------------------

- CPU: 8 x 24-core Intel Xeon Platinum 8268 Processors @ 2.9GHz
- RAM: 3 TB (48 x 64 GB DIMMs)
- System storage: 2 x 6.4 TB flash accelerator PCIe cards (Hot-Pluggable)
- RDMA Network Fabric: 4 x dual-port QSFP28 100 Gb/s PCIe 3.0 RDMA Network Fabric cards - all ports active
- 8 x 10GBASE-T ports (10 GbE) - 1 port used for the administration network
- 8 x SFP+/SFP28 ports (10/25 GbE)
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Oracle Exadata X8-2 Database Server Hardware Components
-------------------------------------------------------

- CPU: 2 x 24-core Intel Xeon Platinum 8260 Processors @ 2.4 GHz
- RAM: 384 GB RAM (12 x 32 GB DIMMs), expandable to 768 GB (12 x 64 GB DIMMs) or 1.5 TB (24 x 64 GB DIMMs) with memory expansion kit
- System storage: 4 x 1.2 TB boot drive/hard disks, hot swappable, expandable to 8 drives
- Disk controller HBA with 2 GB cache (no batteries)
- RDMA Network Fabric: 2 x InfiniBand 4X QDR (40 Gb/s) ports (PCIe 3.0) - both ports active
- Client network: 2 x SFP+/SFP28 ports (10/25 GbE) or 2 x 10GBASE-T ports (10 GbE)
- Backup/optional networks: 2 x SFP+/SFP28 ports (10/25 GbE) or 4 x 10GBASE-T ports (10 GbE)
- Administration network: 1 x 1 GbE Base-T Ethernet port
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Oracle Exadata X8-8 Database Server Hardware Components
-------------------------------------------------------

- CPU: 8 x 24-core Intel Xeon Platinum 8268 Processors @ 2.9GHz
- RAM: 3 TB (48 x 64 GB DIMMs) RAM, expandable to 6 TB (96 x 64 GB DIMMs) with memory expansion kit
- System storage: 2 x 6.4 TB flash accelerator PCIe cards (Hot-Pluggable)
- RDMA Network Fabric: 8 x InfiniBand 4X QDR (40 Gb/s) ports (PCIe 3.0) - all ports active
- 8 x 10GBASE-T ports (10 GbE) - 1 port used for the administration network
- 8 x SFP+/SFP28 ports (10/25 GbE)
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 1 GbE Base-T Ethernet port


Oracle Exadata X7-2 Database Server Hardware Components
-------------------------------------------------------

- CPU: 2 x 24-core Intel Xeon Platinum 8160 Processors @ 2.10GHz
- RAM: 384 GB RAM, expandable to 768 GB (12 x 64 GB) or 1.5 TB (24 x 64GB) with memory expansion kit
- System storage: 4 x 600 GB 10K RPM SAS disks, hot swappable, expandable to 8 drives
- Disk controller HBA with 2 GB cache (no batteries)
- RDMA Network Fabric: 2 x InfiniBand 4X QDR (40 Gbps) ports (PCIe 3.0), both ports active
- Client network: 2 x 10 GbE Base-T Ethernet ports or 2 x 10GbE/25GbE Ethernet SFP28 Ports
- Backup/optional networks: 2 x 10GbE/25GbE Ethernet SFP28 Ports
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100/1000 BASE-T Ethernet port


Oracle Exadata X7-8 Database Server Hardware Components
-------------------------------------------------------

- CPU: 8 x 24-core Intel Xeon Platinum 8168 Processors @ 2.70GHz
- RAM: 3TB (48 x 64 GB) RAM, expandable to 6 TB (96 x 64 GB) with memory expansion kit
- RDMA Network Fabric: 8 x InfiniBand 4X QDR (40 Gbps) ports (PCIe 3.0) - all ports active
- 8 x 10 GbE Base-T Ethernet ports (8 embedded ports based on the Intel 722 1/10GbE Controller)
- 8 x 10GbE/25GbE Ethernet SFP28 Ports (4 Dual-port 10/25 GbE PCIe 3.0 network card based on the Broadcom BCM57414 10Gb/25Gb Ethernet Controller technology)
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100/1000 BASE-T Ethernet port


Oracle Exadata X6-2 Database Server Hardware Components
-------------------------------------------------------

- CPU: 2 x 22-core Intel Xeon E5-2699 v4 processors @ 2.2 GHz
- RAM: 256 GB (8 x 32 GB) RAM expandable to 512 GB (16 x 32 GB) or 768 GB (24 x 32 GB) with memory expansion kit
- System storage: 4 x 600 GB 10K RPM SAS disks, hot swappable, expandable to 8x
- Disk controller HBA with 1 GB cache (no more batteries)
- RDMA Network Fabric: 2 x InfiniBand 4X QDR (40 Gbps) ports (PCIe 3.0), both ports active
- 4 x 1 GbE/10 GbE Base-T Ethernet ports
- 2 x 10 GbE Ethernet SFP+ ports (1 dual-port 10 GbE PCIe 2.0 network card based on the Intel 82599 10 GbE controller technology)
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100/1000 BASE-T Ethernet port


Oracle Exadata X5-2 Database Server Hardware Components
-------------------------------------------------------

- CPU: 2 x 18-Core Intel Xeon E5-2699 v3 processors @ 2.3 GHz
- RAM: 256 GB (8 x 32 GB) RAM expandable to 768 GB with memory expansion kit
- System storage: 4 x 600 GB 10K RPM SAS disks
- Disk controller HBA with 1 GB supercap-backed write cache
- RDMA Network Fabric: 2 InfiniBand 4X QDR (40 Gb/s) ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA))
- 4 x 1 GbE/10GbE Base-T Ethernet ports
- 2 x 10 GbE Ethernet SFP+ ports (1 dual-port 10GbE PCIe 2.0 network card based on the Intel 82599 10 GbE controller technology)
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100/1000 BASE-T Ethernet port


Oracle Exadata X5-8 and X6-8 Database Server Hardware Components
----------------------------------------------------------------

- CPU: 8 x 18-Core Intel Xeon E7-8895 v3 processors @ 2.6 GHz
- RAM: 2 TB (64 x 32 GB) RAM, expandable to 6 TB (192 x 32 GB) with memory expansion kit
- System storage: 8 x 600 GB 10K RPM SAS disks (hot swappable)
- Disk controller HBA with 1 GB cache
- RDMA Network Fabric: 8 x InfiniBand 4X QDR (40 Gbps) ports (PCIe 3.0) - all ports active
- 10 x 1 GbE Base-T Ethernet ports (2 Quad-port PCIe 2.0 network card, and 2 embedded ports based on the Intel I350 1 GbE Controller technology)
- 8 x 10 GbE Ethernet SFP+ ports (4 Dual-port 10 GbE PCIe 2.0 network card based on the Intel 82599 10 GbE Controller technology)
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100/1000 BASE-T Ethernet port


Oracle Exadata X4-2 Database Server Hardware Components
-------------------------------------------------------

- CPU: 2 x 12-Core Intel Xeon E5-2697 v2 processors @ 2.7 GHz
- RAM: 256 GB (16 x 16 GB) RAM expandable to 512 GB (16 x 32 GB) with memory expansion kit
- System storage: 4 x 600 GB 10K RPM SAS disks
- Disk controller HBA with 512 MB battery-backed write cache, and swappable battery backup unit (BBU)
- RDMA Network Fabric: 2 InfiniBand 4X QDR (40 Gb/s) ports (1 dual-port PCIe 3.0 Host Channel Adapter (HCA))
- 4 x 1 GbE/10GbE Base-T Ethernet ports
- 2 x 10 GbE Ethernet SFP+ ports (1 dual-port 10GbE PCIe 2.0 network card based on the Intel 82599 10 GbE controller technology)
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port


Oracle Exadata X4-8 Database Server Hardware Components
-------------------------------------------------------

- CPU: 8 x 15-Core Intel Xeon E5-8895 v2 processors @ 2.8 GHz
- RAM: 2 TB (64 x 32 GB) RAM expandable to 4 TB or 6 TB with memory expansion kit
- System storage: 7 x 600 GB 10K RPM SAS disks
- Disk controller HBA with 512 MB battery-backed write cache, and swappable battery backup unit (BBU)
- RDMA Network Fabric: 8 InfiniBand 4X QDR (40 Gb/s) ports
- 10 x 1 GbE Base-T Ethernet ports
- 8 x 10 GbE Ethernet SFP+ ports (4 dual-port 10GbE PCIe 2.0 network card based on the Intel 82599 10 GbE controller technology)
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100/1000 BASE-T Ethernet port


Oracle Exadata X3-2 Database Server Hardware Components
-------------------------------------------------------

- CPU: 2 x 8-Core Eight-Core Intel Xeon E5-2690 processors @ 2.9 GHz
- RAM: 256 GB (16 x 16 GB) RAM expandable to 512 GB with memory expansion kit
- System storage: 4 x 300 GB 10K RPM SAS disks
- Disk controller HBA with 512 MB battery-backed write cache
- RDMA Network Fabric: 2 InfiniBand 4X QDR (40 Gb/s) ports (1 dual-port PCIe 2.0 Host Channel Adapter (HCA))
- 4 x 1 GbE/10GbE Base-T Ethernet ports
- 2 x 10 GbE Ethernet SFP+ ports (1 dual-port 10GbE PCIe 2.0 network card based on the Intel 82599 10 GbE controller technology)
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port


Oracle Exadata X3-8 Database Server Hardware Components
-------------------------------------------------------

- CPU: 8 x 10-Core Intel Xeon E7-8870 Processors @ 2.40 GHz
- RAM: 2 TB RAM (128 x 16 GB)
- System storage: 8 x 300GB 10K RPM SAS Disks
- Disk Controller HBA with 512MB Battery-backed cache
- RDMA Network Fabric: 8 x InfiniBand QDR (40 Gb/s) Ports
- 2 Network Express Modules (NEM) providing the following:
  - 8 x 10 Gb Ethernet network ports using SFP+ connectors (based on Intel 82599 10 GbE controller)
  - 8 x 1 Gb Ethernet network ports
- Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port


Oracle Exadata X2-2 Database Server Hardware Components
-------------------------------------------------------

- Components of Sun Fire X4170 Oracle Database Servers

  - CPU: 2 x 4-Core Intel Xeon E5540 processors @ 2.53 GHz
  - RAM: 72 GB RAM expandable to 144 GB with memory expansion kit
  - System storage: 4 x 146 GB 10K RPM SAS disks
  - Disk controller HBA with 512 MB battery-backed write cache
  - RDMA Network Fabric: Dual-port 4X QDR (40 Gb/s) InfiniBand Host Channel Adapter (HCA)
  - 4 embedded Gigabit Ethernet ports
  - Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port

- Components of Sun Fire X4170 M2 Oracle Database Servers

  - CPU: 2 x 6-Core Intel Xeon X5675 processors @ 3.06 GHz
  - RAM: 96 GB RAM (12 x 8 GB) expandable to 288 GB with memory expansion kit
  - System storage: 4 x 300 GB 10 K RPM SAS disks
  - Disk controller HBA with 512 MB battery-backed write cache
  - RDMA Network Fabric: Dual-port 4X QDR (40 Gb/s) InfiniBand Host Channel Adapter (HCA)
  - 4 embedded Gigabit Ethernet ports
  - Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port
  - 1 dual-port 10 GbE PCIe 2.0 network card with Intel 82599 10 GbE controller

.. note::

   Sun Fire X4170 M2 Oracle Database Servers ship from the factory with 96 GB of memory with 12 of the 18 DIMM slots populated with 8 GB DIMMs. The optional X2-2 Memory Expansion Kit can be used to populate the remaining 6 empty slots with 16 GB DIMMs to bring the total memory to 192 GB (12 x 8 GB and 6 x 16 GB), or replace the existing 8 GB DIMMs with 16 GB DIMMs and add memory to bring the total memory to 288 GB (18 x 16 GB).

   The memory expansion kit is primarily for consolidation workloads where many databases are run on each database server. In this scenario, the CPU usage is often low while the memory usage is very high.

   However, there is a downside to populating all the memory slots as the frequency of the memory DIMMs drop to 800 MHz from 1333 MHz. The performance effect of the slower memory appears as increased CPU utilization. The average measured increase in CPU utilization is typically between 5% and 10%. The increase varies greatly by workload. In test workloads, several workloads had almost zero increase, while one workload had as high as a 20% increase.


Oracle Exadata X2-8 Database Server Hardware Components
-------------------------------------------------------

- Components of Sun Fire X4800 Oracle Database Servers

  - CPU: 8 x 8-core Intel Xeon X7560 Processors @ 2.26 GHz
  - RAM: 1 TB RAM
  - System storage: 8 x 300GB 10K RPM SAS Disks
  - Disk Controller HBA with 512MB Battery-backed cache
  - RDMA Network Fabric: 4 dual-port 4X QDR InfiniBand PCIe 2.0 Express Modules (EM)
  - 2 Network Express Modules (NEM) providing the following:

    - 8 x 10 Gb Ethernet network ports using SFP+ connectors (based on Intel 82599 10 GbE controller)
    - 8 x 1 Gb Ethernet network ports

  - Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port


- Components of Sun Server X2-8 Oracle Database Server (Sun Fire X4800 M2)

  - CPU: 8 x 10-core Intel Xeon E7-8870 Processors (2.40 GHz)
  - RAM: 2 TB RAM (128 x 16 GB)
  - System storage: 8 x 300GB 10K RPM SAS Disks
  - Disk Controller HBA with 512MB Battery-backed cache
  - RDMA Network Fabric: 4 dual-port 4X QDR InfiniBand PCIe 2.0 Express Modules (EM)
  - 2 Network Express Modules (NEM) providing the following:

    - 8 x 10 Gb Ethernet network ports using SFP+ connectors (based on Intel 82599 10 GbE controller)
    - 8 x 1 Gb Ethernet network ports

  - Integrated Lights Out Manager (ILOM) port for remote management: 1 x 10/100 BASE-T Ethernet port


----

Parent topic: `Hardware Components of Oracle Exadata <https://docs.oracle.com/en/engineered-systems/exadata-database-machine/dbmso/hardware-components-exadata-db-machine.html>`_
