.. index:: macos, mac

.. meta::
   :keywords: macos, mac

.. _macos-change-macaddr:

Set a new mac address on startup
================================

1. Open `AppleScript Editor` and paste the following into a new file.

.. code-block:: applescript

   set newMac to "00:00:00:00:00:00"
   set psswrd to "your_password_here"
    
   repeat with counter from 0 to 50
       try
           set currMac to (do shell script "ifconfig en0" & " | grep 'ether '")
           if currMac contains "ether" then
               exit repeat
           end if
       on error
           delay 2
       end try
   end repeat
    
   do shell script "ifconfig en0" & " ether " & newMac password psswrd with administrator privileges

2. Replace ``00:00:00:00:00:00`` and ``your_password_here`` with your own MAC address and password.
3. Save the AppleScript in File Format **Application** and check the **Run Only** box. Name it something descriptive like "SetMacAdd." Save it in Applications or somewhere else where you can find it.
4. Open System Preferences and click on **Accounts**.
5. In Accounts click on the **Login Items** tab and the use the "+" to add your saved AppleScript to the list of login items.
6. Restart to check if it works.