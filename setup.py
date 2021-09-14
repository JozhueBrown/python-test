# creacion de un paquete distribuible, se crea el archivo llamado setup.py 

from setuptools import setup ##con esta llamada se inicia 

setup(    ##en esta instruccion se pondra la informacion que contendra el paquete##
	name="paquetecalculo",
	version="1.0", ##version del paquete, como se quiera
	description="Paquete de redondeo y potencia",
	author="Josue",
	author_email="josue_hdz_barroso@outlook.com",
	url="no existe por el moemnto",
	packages=["calculos", "calculos.redondeo_potencia"]#aqui se usa la direccion del paquete a usar


	)

###para que se cree la carpeta, se abre powershell desde la carpta donde esta el setup
###y se escribe: python setup.py sdist
###crea carpeta dist(contiene un comprimido) y carpeta .egg-info

###para instalarlo, desde consola entas a carpeta dist y escribir:
###pip3 install "nombre de paquete"
###listo

###para desisntalar: pip3 uninstall 'nombre del paquete'