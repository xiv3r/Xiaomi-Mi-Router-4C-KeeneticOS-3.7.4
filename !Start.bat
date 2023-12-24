@Echo off
 
:m1
Echo. 
Echo [11] - Connect to router 
Echo.
Echo ------------------------------------------
Echo [22] - Read  backup.bin and eeprom.bin
Echo ------------------------------------------
Echo.
Echo.
Echo ------------------------------------------
Echo [55] - Install Keenetic
Echo ------------------------------------------
Echo. 
Echo.                           
Echo [0] - Exit
Echo. 
echo.
echo. 
echo.
Set /p choice="Select: "
if not defined choice goto m1
if "%choice%"=="11" (1.start_main.bat)
if "%choice%"=="22" (2.start_create_backup.bat)
if "%choice%"=="55" (5.start_write_keenetic.bat)
if "%choice%"=="0" (exit)




Echo.
Echo 
Echo.
Echo.
goto m1
pause >nul