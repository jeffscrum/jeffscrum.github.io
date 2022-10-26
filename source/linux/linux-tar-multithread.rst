.. index:: linux, tar, multithread

.. meta::
   :keywords: linux, tar, multithread

.. _linux-tar-multithread:

TAR Multithread
===============

How to use multiple CPU thread(core) to make tar compression faster

.. code-block:: none

   On many unix like systems, tar is a widely used tool to package and compress files, almost built-in in the all common Linux and BSD distribution, however, tar always spends a lot of time on file compression, because the programs itself doesn’t support multi-thread compressing, but fortunately, tar supports to use specified external program to compress file(s), which means we can use the programs support multi-thread compressing with higher speed!
   
   From the tar manual (man tar), we can see:
   -I, –use-compress-program PROG
   filter through PROG (must accept -d)
   
   With parameter -I or --use-compress-program, we can select the extermal compressor program we’d like to use.
   The three tools for parallel compression I will use today, all can be easy installed via apt install under Debian/Ubuntu based GNU/Linux distributions, here are the commands and corresponding apt package name, please note that new versions of Ubuntu and Debian no longer have pxz package, but pixz can do the similar thing:
   gz:   pigz
   bz2: pbzip2
   xz:   pxz, pixz
   
   Originally commands to tar with compression will be look like:
   gz:   tar -czf tarball.tgz files
   bz2: tar -cjf tarball.tbz files
   xz:   tar -cJf tarball.txz files
   
   The multi-thread version:
   gz:   tar -I pigz -cf tarball.tgz files
   bz2: tar -I pbzip2 -cf tarball.tbz files
   xz:   tar -I pixz -cf tarball.txz files
   xz:   tar -I pxz -cf tarball.txz files
   
   I am going to use Linux kernel v3.18.6 as compression example, threw the whole directory on the ramdisk to compress them, and then compare the difference!
