@echo off
cls
python write_keenetic.py
cd keenetic
copy /b boot_breed_30000.bin + ENV.bin + eeprom_mod.bin + fw_keenetic.bin full_keenetic.bin
cd ..
python write_keenetic2.py
pause
cls
!Start.bat
