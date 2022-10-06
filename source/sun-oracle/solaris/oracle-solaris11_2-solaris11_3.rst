.. index:: oracle, solaris11

.. meta::
   :keywords: oracle, solaris11

.. _oracle-solaris-eis-download:

Solaris 11.2 to Solaris 11.3
============================

.. attention::

   В случае если мы прыгаем на другой релиз, то нужно дополнительно развернуть базовый IPS репозиторий (Doc ID 1277964.1)

1. Скачиваем образы Solaris 11 Repo c сайта Oracle.com (`Create a Local Repository <http://www.oracle.com/technetwork/server-storage/solaris11/downloads/local-repository-2245081.html>`_)

2. Закачиваем пакеты на сервер и подготавливаем репозиторий

.. code-block:: none

   # chmod -x install-repo.ksh
   # mkdir /Solaris11_Repo/
   # ./install-repo.ksh -d /Solaris11_Repo/ -c -v -y
   Using sol-11_3-repo download.
    
   Comparing checksums of downloaded files...done. Checksums match.
    
   Uncompressing sol-11_3-repo_1of5.zip...done.
   Uncompressing sol-11_3-repo_2of5.zip...done.
   Uncompressing sol-11_3-repo_3of5.zip...done.
   Uncompressing sol-11_3-repo_4of5.zip...done.
   Uncompressing sol-11_3-repo_5of5.zip...done.
   Repository can be found in /Solaris11_Repo/.
   Initiating repository verification.

3. Добавляем репозиторий в систему

.. code-block:: none

   # pkg set-publisher -g file:///Solaris11_Repo/ solaris

4. Установка обновлений

.. code-block:: none

   # pkg update --accept
               
               Packages to remove:  28
              Packages to install:  84
               Packages to update: 485
               Packages to change:   1
              Mediators to change:   7
          Create boot environment: Yes
   Create backup boot environment:  No
   DOWNLOAD                                PKGS         FILES    XFER (MB)   SPEED
   Completed                            598/598   27955/27955  600.1/600.1    0B/s
    
   PHASE                                          ITEMS
   Removing old actions                       6058/6058
   Installing new actions                   18544/18544
   Updating modified actions                17208/17208
   Updating package state database                 Done 
   Updating package cache                       513/513
   Updating image state                            Done 
   Creating fast lookup database                   Done 
   Updating package cache                           1/1
    
   A clone of solaris-2 exists and has been updated and activated.
   On the next boot the Boot Environment solaris-3 will be
   mounted on '/'.  Reboot when ready to switch to this updated BE.
    
   Updating package cache                           1/1
    
   ---------------------------------------------------------------------------
   NOTE: Please review release notes posted at:
    
   https://support.oracle.com/rs?type=doc&id=1672221.1
   ---------------------------------------------------------------------------

5. Проверяем что новое окржение создано и будет активировано при загрузке, после чего перезагружаемся в него

.. code-block:: none

   # beadm list
   BE        Flags Mountpoint Space   Policy Created          
   --        ----- ---------- -----   ------ -------          
   solaris   -     -          8.29M   static 2015-02-18 19:38
   solaris-1 -     -          10.34M  static 2015-02-24 20:33
   solaris-2 N     /          111.63M static 2015-06-25 02:38
   solaris-3 R     -          46.22G  static 2016-11-08 11:06
    
   # shutdown -i6 -g0

6. После перезагрузки проверяем версию ПО и можем приступать к накату патчей для S11.3 (seealso: :ref:`oracle-solaris-sru-update`)

.. code-block:: none

   # pkg list entire
   NAME (PUBLISHER)                                  VERSION                    IFO
   entire                                            0.5.11-0.175.3.1.0.5.0     i--
