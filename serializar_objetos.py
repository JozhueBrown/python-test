import pickle ##importamos

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


coche1=Vehiculos("Mazda", "MX5")
coche2=Vehiculos("Bentley", "SuperSport")
coche3=Vehiculos("Mercedes Benz", "Maybach")

coches=[coche1, coche2, coche3]

#abrimos fichero a guardar
fichero=open("losCoches", "wb")
pickle.dump(coches, fichero)

fichero.close()

del(fichero)#para liberar memoria

#recuperamos la info
ficheroApertura=open("losCoches", "rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
	print(c.estado())
