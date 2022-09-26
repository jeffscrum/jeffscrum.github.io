.. index:: emc, vmax

.. _vmax-heads-tracks-cylinder-gb:

VAMX. Calculations for Heads, Tracks, Cylinders, GB
===================================================

Symmetrix 8000/DMX/DMX-2 Series
-------------------------------

.. code-block:: none

  Enginuity Code: 5567, 5568, 5669, 5670, 5671
  Includes EMC Symmetrix 8130, 8230, 8430, 8530, 8730, 8830, DMX1000, DMX2000, DMX3000 and various different configurations within those models.
  GB = Cylinders * 15 * 64 * 512 / 1024 / 1024 / 1024
  eg: 6140 Cylinder devices equates to 2.81 GB of usable data
  6140 * 15 * 64 * 512 / 1024 / 1024 / 1024 = 2.81 GB
  
  Cylinders = GB / 15 / 64 / 512 * 1024 * 1024 * 1024
  
  Where
  15 = tracks per cylinder
  64 = blocks per track
  512 = bytes per block
  1024 = conversions of bytes to kb to mb to gb.


Symmetrix DMX-3/DMX-4 Series
----------------------------

.. code-block:: none

  Enginuity Code: 5771, 5772, 5773
  Includes EMC Symmetrix DMX-3, DMX-4 and various different configurations within those models.
  GB = Cylinders * 15 * 128 * 512 / 1024 / 1024 / 1024
  Eg: 65520 Cylinder device equates to 59.97 GB of usable data
  65540 * 15 * 128 * 512 / 1024 / 1024 / 1024 = 59.97 GB
  
  Cylinders = GB / 15 / 128 / 512 * 1024 * 1024 * 1024
  
  15 = tracks per cylinder
  128 = blocks per track
  512 = bytes per block
  1024 = conversions of bytes to kb to mb to gb


Symmetrix VMAX
--------------

.. code-block:: none

  Enginuity Code: 5874
  Includes EMC Symmetrix V-Max and various different configurations within this model.
  GB = Cylinders * 15 * 128 * 512 / 1024 / 1024 / 1024
  Eg: 262668 Cylinder device equates to 240.47 GB of usable data
  262668 * 15 * 128 * 512 / 1024 / 1024 / 1024 = 240.47 GB
  
  Cylinders = GB / 15 / 128 / 512 * 1024 * 1024 * 1024
  
  15 = tracks per cylinder
  128 = blocks per track
  512 = bytes per block
  8 bytes = 520-512 used for T10-DIF
  1024 = conversions of bytes to kb to mb to gb

Drive format on a V-Max is 520 bytes, out of which 8 bytes are used for `T10-DIF <http://storagenerve.com/2009/06/30/emc-symmetrix-dmx-4-and-symmetrix-v-max-basic-differences>`_ ( A post on DMX-4 and V-Max differences).
