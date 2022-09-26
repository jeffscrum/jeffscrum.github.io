
::
::  for 5876
::  
::  iasynb v 1_9  jul-2015
::
::
::  ==========================================|
::
:: V       V M     M      A      X   X
::  V     V  M M M M     A A      X X
::   V   V   M  M  M    A   A      X 
::    V V    M     M   A A A A    X X
::     V     M     M  A       A  X   X
::
::  ==========================================|
::      How to use
::
::    in SymmWin: Collect: 
::
::  HealthCheck
::  DiskInfo
::  Hardware collection
::
::  script:
::
::  1) copy to o:\emc\29XXXX\
::  2) rename to .BAT 
::  3) cd to o:\emc\29XXXX\ and start BAT
::
::  directory c:\tmp\TMP_2014_11_19  - looks like this - all files will be copyed to one directory
::  all directory content will be ZIPPed to Day_Month_Year.ZIP file
::
::  ==========================================|
:define_vars    
set TMPyear=%date:~10,4%
set TMPyr=%date:~12,2%
set TMPmonth=%date:~4,2%
set TMPday=%date:~7,2%
 
set TMPfilename=%TMPyear%_%TMPmonth%_%TMPday%
set TMPdate=%TMPmonth%-%TMPday%-%TMPyear%
set TMPdt=%TMPmonth%-%TMPday%-%TMPyr%
echo .
echo %TMPfilename%
mkdir c:\tmp\TMP_%TMPfilename%
 
xcopy /s /D:%TMPdate% O:\EMC\CONNECTEMC\*.log c:\tmp\TMP_%TMPfilename%
::xcopy /s /D:%TMPdate% log_zip\*.zip c:\tmp\TMP_%TMPfilename%
xcopy /s /y /D:%TMPdate% SYMMWIN\scripts\HealthCheck* c:\tmp\TMP_%TMPfilename%
xcopy /s /y  SYMMWIN\scripts\sympl_env_health* c:\tmp\TMP_%TMPfilename%
copy logs\symmwin\disk_info.log c:\tmp\TMP_%TMPfilename%
copy logs\symmwin\hardware.log c:\tmp\TMP_%TMPfilename%
copy logs\symmwin\replace_frus_db_*.log c:\tmp\TMP_%TMPfilename%
copy logs\symmwin\HealthCheck_ENV.log c:\tmp\TMP_%TMPfilename%
copy SYMMWIN\data\BadFrusDb.xml c:\tmp\TMP_%TMPfilename%
copy SYMMWIN\data\PartsTable.xml c:\tmp\TMP_%TMPfilename%
copy SYMMWIN\data\ReplacedFrusDb.xml c:\tmp\TMP_%TMPfilename%
copy logs\symmwin\replace_frus_db*.log c:\tmp\TMP_%TMPfilename%
copy logs\symmwin\parts_mon*.log c:\tmp\TMP_%TMPfilename%
c:
cd c:\tmp\TMP_%TMPfilename%
symcfg discover
symcfg list -status > symcfg_list_status.txt
symcfg list -env_data > symcfg_list_env.txt
symdisk list -failed > symdisk_list_failed.txt
symdisk list -hotspares > symdisk_list_HS.txt
pkzip25.exe  -add -rec -path=current ../%TMPdt%  *.*

