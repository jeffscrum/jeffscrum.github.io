.. index:: exadata, intel, optane, PMEM, Persistent Memory Module

.. meta::
   :keywords: exadata, intel, optane, PMEM, Persistent Memory Module

.. _oracle-exadata-optane-pmem:

Optane Persistent Memory Module
===============================

Уже несколько раз попадал в неприятную ситуацию, когда на площадку привозят модуль PMEM, а он оказывается не тот.

Настало время прояснить ситуацию:

- pn: 8206414 это 128GB Intel Optane Persistent Memory Module (NMB1XXD128GPS). Синие. Такие стоят в Oracle Exadata X9M-2/X9M-8.
- pn: 8201297 это 128GB Intel Optane DC Persistent Memory Module (NMA1XXD128GPS). Черные. Такие стоят в Oracle Exadata X8-2/X8-8/X8M-2/X8M-8

Они отличаются одной буквой в модели NMA и NMB. 
Внешне они специально сделаны с радиаторами разного цвета: черные -- модули старого поколения (NMA), синие -- нового (NMB).
