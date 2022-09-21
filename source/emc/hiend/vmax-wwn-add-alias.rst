.. index:: emc, vmax, alias, wwn

.. _vmax-wwn-add-alias:

VMAX. Добавление алаиса для WWN
===============================

Сделать это из GUI как-то сильно сложно, зато через CLI делается за 5 секунд::

  symaccess -sid 1234 -wwn 1000000000000001 rename -alias Host1/HBA01


..
	[GUI]: Graphical User Interface
	[CLI]: Command Line Interface
