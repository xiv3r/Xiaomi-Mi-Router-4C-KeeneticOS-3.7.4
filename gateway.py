import sys
import os
import subprocess

def get_gateway():
	with open(os.devnull, 'w') as devnull:
		output = subprocess.check_output(["cmd","/c","chcp","437","&","tracert","-d","-h","1","1.1.1.1","&","chcp","866"], stderr=devnull)
	try:
		decode = output.decode("cp437")
	except:
		print ("Ошибка декодирования")
		return
		
	line4 = decode.split("\r\n")[4].strip().split(" ")
	for data in line4:
		if len(data.split(".")) == 4:
			return(data)		
	return

def get_ip_address():
	print("Определяю шлюз по умолчанию")
#	ip_address=get_gateway()
# Не находит роутер закоментируй строчку выше и удали коментарий строкой ниже
	ip_address='192.168.31.1'
	if not ip_address:
		print("Шлюз не найден")
		sys.exit(1)

	print("Шлюз по умолчанию: {ip_address}".format(ip_address=ip_address))
	return ip_address
