class Vehiculos():#Se crea la clase padre, como cualquier otra clse
	def __init__(self, marca, modelo):# se hacen las propiedades iniciales itulizando __init__
		self.marca=marca##Se pueden encapsular si asi se desea, pero estos si cambiaran 
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):##Se crean los metodos que realizara la clase
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
		 self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Moto(Vehiculos):#esta es una clase que hereda, metiendo como argumento que recibe, el nombre de la clase padre
	# pass#cuando no se quiere iniciar mas codigo en la clase pero se quiere usar
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo caballito"

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
		 self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

###Se crea otra clase u objeto
class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if self.cargado:
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta no esta cargada"

###Se crea clase vehiculos electricos
class VElectricos(Vehiculos):
	def __init__(self,marca,modelo):

		super().__init__(marca,modelo)
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True
		


# miMoto=Moto("Suzuki", "Ninja")
# miMoto.caballito()
# # print(miMoto.estado())
# miMoto.estado()

# miFurgoneta=Furgoneta("Ford", "Transit")
# miFurgoneta.arrancar()
# miFurgoneta.estado()
# print(miFurgoneta.carga(True))


class BicicletaElectrica(VElectricos,Vehiculos):##se da preferencia a la primera clase que hereda
												#si se quiere ingresar primero los datos, se pone la clase que los pide
	pass

# miBici=BicicletaElectrica("Benotto", "1990")
# miBici.estado()