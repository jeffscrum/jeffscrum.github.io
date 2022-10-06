.. index:: davinci

.. meta::
   :keywords: davinci, studio

.. _davinci-studio-trick:

Davinci Resolve Studio
======================

16.2.6
------

.. code-block:: perl

  perl -pi -e 's/\xB6\x43\x07\x0F\x1F\x44\x00\x00\x55/\xB6\x43\x07\x0F\x1F\x44\x00\x00\xC3/g' /Applications/DaVinci\ Resolve/DaVinci\ Resolve.app/Contents/MacOS/Resolve


16.1
----

.. code-block:: perl

  perl -pi -e 's/\x3D\x1B\x07\x0F\x1F\x44\x00\x00\x55/\x3D\x1B\x07\x0F\x1F\x44\x00\x00\xC3/g' /Applications/DaVinci\ Resolve/DaVinci\ Resolve.app/Contents/MacOS/Resolve


16.0
----

.. code-block:: perl

  perl -pi -e 's/\xFE\xCD\x06\x0F\x1F\x44\x00\x00\x55/\xFE\xCD\x06\x0F\x1F\x44\x00\x00\xC3/g' /Applications/DaVinci\ Resolve/DaVinci\ Resolve.app/Contents/MacOS/Resolve
