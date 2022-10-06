.. index:: oracle, solaris, wget, patch

.. meta::
   :keywords: oracle, solaris, wget, patch

.. _oracle-sw-wget-oracle-patches:

Using WGET to Download MOS Patches
==================================

1. For getting the Link Address to download the patch please goto

  .. code-block:: none
  
     For eg; to download Patch 8836308 for Sun Solaris SPARC (64-bit) follow below instructions :
      
      From My Oracle Support Portal :
      - Login to "My Oracle Support"
      - Search for the patch
      - Go to the download page
     - Click to Select the Row for Patch to be downloaded
      - Click "Download"
      - Right Click on Patch Zip file displayed
      - Copy URL
      
      Directly from Browser :
      
      https://updates.oracle.com/download/8836308.html
      In Platform or Language : choose Sun Solaris SPARC (64-bit)
      On the same page on the Download Button->Right Click on the Download->Copy link location
     
     or
     
     - Login to "My Oracle Support"
      - Search for the patch
      - Go to the download page
     - Click to Select the Row for Patch to be downloaded
      - Click "Download"
     - At Bottom Click "WGET options"
     - Click on Download .sh. You will get wget.sh file

2. Enter the following command where username and password are your My Oracle Support login and password and filename is the patch file name that you copied from the Properties window

  .. code-block:: none
  
     wget --http-user=username --http-password=password --no-check-certificate --output-document=filename "paste the above copied address here in quotes"
      
      ie;
      
     wget --http-user=username --http-password=password --no-check-certificate --output-document=filename "https://updates.oracle.com/Orion/Download/download_patch/filename" 
   
     For example, to download patch 8836308 for Sun Solaris SPARC (64-bit) where the patch file name is p8836308_10204_Solaris-64.zip, enter:
      
     wget --http-user=firstname.lastname@oracle.com --http-password=password --no-check-certificate --output-document=p8836308_10204_Solaris-64.zip "https://updates.oracle.com/Orion/Download/download_patch/p8836308_10204_Solaris-64.zip"
   
  
     For example, to download a password protected patch, enter the patch  password at the end of the URL as follows, where patch_password is the password for the patch:
   
     wget --http-user=firstname.lastname@oracle.com --http-password=password --no-check-certificate --output-document=p8836308_10204_Solaris-64.zip "https://updates.oracle.com/Orion/Download/download_patch/p8836308_10204_Solaris-64.zip?patch_password=patch_password"

.. tip::

  If your download breaks or is interrupted before finishing, you can resume/continue it from the partially-downloaded file by providing "-c" option to wget:

  .. code-block:: none

     wget -c --http-user=username --http-password=password --no-check-certificate --output-document=filename "https://updates.oracle.com/Orion/Download/download_patch/"
