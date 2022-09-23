.. index:: emc, vmax, token

.. _vmax-recreate-emergency-token:

VMAX. How to recreate emergency token
=====================================

.. note::

  To access Central Manager off of EMC’s network use url: https://slc.emc.com/psscm

Validate Failed Tokens in Credential Management
-----------------------------------------------

#. Log in to Central Manager using one of the links above. 
#. Select Token Manager > Installed Token Viewer.
#. Enter the Symmetrix serial number and select Search.
#. The list of installed token types will be displayed along with their expiration dates. Make a note of the types that have expired. These are the tokens that will need to be replaced.

Validate Tokens on the Service Processor
----------------------------------------

1. Log in to the Service Processor using the default user name and password.
  
  - User: Admin
  - Password: EMC2Admin
  - Domain: Local Host

2. Select the SSC Key Client icon on the Service Processor desktop.
3. Select List Installed Tokens. Confirm the tokens listed on the Service Processor match those displayed in Credential Manager.
4. Select OK.
5. On the Service Processor in the SSC Key Client in the  Secure Service Credentials Tasks screen select Back  then Provision Tokens >  Next.
6. Select Disconnected.
7. Select Export Token Request File. Save the file on your portable USB media device for uploading to Credential Manager. This is an example for the file format: ``<sn>_KS_<datetime>.enc (e.g., 192604321_KS_20140204131709UTC.enc)``.

Deleting Tokens on the Service Processor
----------------------------------------

#. Return to Central Manager from your laptop.
#. Go to Token Manager > Token Provisioning Request > Manual Provisioning for Disconnected sites (SP File available) and select Next.
#. Enter the Symmetrix serial number of the system and select Search.
#. The “Service Processor File Upload” prompt will appear.
#. Browse your USB device and select the file saved from running the SSC Key Client on the Service Processor from Step 7 above.
#. Select Request Delete Transaction.
#. Select the check box to the left of each token type. This is required to be removed.
#. Select Get Token File.
#. The Save file dialog box will appear. Be patient. This may take longer than expected. 
#. Save this file on your portable USB device. Here is an example of the file: ``<sn>_KC_<datetime>.enc  (e.g., 192604321_KC_20140204_082319.enc)``.
#. Select the SSC Key Client icon on the Service Processor desktop and double-click.
#. Select  Provision  Tokens > Disconnect > Import.
#. Browse your USB device and select the file you downloaded in step 10. You have now deleted the expired tokens on the Service Processor.

Delete Tokens in Credential Manager
-----------------------------------

#. Log in to Central Manager.
#. Select Token Manager > Token Request Queue.
#. Enter the Symmetrix serial number.
#. A list of deleted tokens will be shown with a red X icon to the left of each token. Select each icon to confirm the tokens have been deleted.

Create and Add New Tokens
-------------------------

#. On the Service Processor run the SSC Key Client select Next.
#. Select Provision tokens > Disconnected > Export.
#. Save this file to your portable USB device.
#. On Credential Manager select Token manager > Token Provision Request > Manual Token Provisioning for Disconnected Sites ( SP File Available) > Next.
#. Enter the Symmetrix serial number and select Search.
#. The Service Processor File Upload prompt will appear.
#. Browse your portable USB device and select the file saved in step 2 above and select Upload File.
#. Select the pulldown for the Available Token Type and select the appropriate token type.
#. Select Add to Queue. Repeat this for each token that was removed.
#. When all the new tokens have been added to the Token Transaction Queue select Get Token File.
#. This may take longer than expected. Be patient while the file is generated. Save this file to your local USB device.
#. On the Service Processor select the SSC Key Client > Next > Provision Tokens > Disconnected > Import. The browser window will appear. Select the file you saved from step 10 above on your USB device. (This will load the new token files to the Service Processor.)
#. When prompted for your SSC Manual Password select your SSC password. If prompted for a PIN and/or SDTID Password use the last four digits of the Symmetrix serial number.

Final Steps to Confirm Tokens in Credential Manager
---------------------------------------------------

#. Log in to Credential Manager.
#. Select Token Manager > Token Request Queue.
#. Enter the serial number of the Symmetrix.
#. Listed will be the new tokens that were generated. Select the green Check Marks icon next to each token. This will confirm token addition in Credential Manager. 

Validate Connectivity
---------------------

#. Generate a new credential by logging into Credential Manager.
#. Select Request a Credential.
#. Enter the serial number of the Symmetrix and select search.
#. Select the serial number underlined in the search box.
#. Set the duration to 2 days and select create.
#. Make a note of the Credential.
#. Log off the Service Processor.
#. Enter the Credential generated in step 6.
#. Enter your SSC password and SLC Domain.
#. Once login is verified, log out and close the case.


:download:`Secure-Service-Credential-Secured-by-RSA.pdf <https://app.box.com/s/aiobsyvzu1yl5rydigeigil4wlc2k8vh>`
