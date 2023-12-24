import sys
import telnetlib
import ftplib
import gateway

router_ip_address=gateway.get_ip_address()
	
try:	
	tn = telnetlib.Telnet(router_ip_address)
except:
	print ("telnet сервер не запущен")
	print ()
	print ("Выполните ещё раз пункт [11] - Connect to router")
	print ()
	sys.exit(1)


tn.read_until(b"XiaoQiang login:")
tn.write(b"root\n")
tn.read_until(b"Password:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
print ()
print ("Создаю полный образ прошивки и eeprom.")
tn.write(b"dd if=/dev/mtd0 of=/tmp/backup.bin\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"dd if=/dev/mtd3 of=/tmp/eeprom.bin\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"exit\n")
print ("Образ прошивки создан")
print ("Файл eeprom.bin создан")
print ("")

ftp=ftplib.FTP(router_ip_address)
file1=open('data/backup.bin', 'wb')
file2=open('data/eeprom.bin', 'wb')
print ("Сохраняю образ прошивки на компьютер")
ftp.retrbinary(f'RETR /tmp/backup.bin', file1.write)
print ("Сохраняю файл eeprom.bin на компьютер")
ftp.retrbinary(f'RETR /tmp/eeprom.bin', file2.write)
file1.close()
file2.close()
ftp.quit()
print ("Выполнено")
print ("")

tn = telnetlib.Telnet(router_ip_address)
tn.read_until(b"XiaoQiang login:")
tn.write(b"root\n")
tn.read_until(b"Password:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
print ()
print ("Удаляю временные файлы")
tn.write(b"rm /tmp/backup.bin\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"exit\n")
print ("Готово.")
print ()
print ()
