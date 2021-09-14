#crearemos un archivo donde la informacion se quedara 

import pickle

class Persona():
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad

		print("Se ha creado una persona nueva con el nombre de: ", self.nombre)

	def __str__(self):###convierte en string los datos
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

	personas=[]
	def __init__(self):##desde el constructor podemos indicar que en cuanto se cree el objeto se guarde en la lista
	##
		ListaPersonas=open("fichero_personas", "ab+")##para agregar informacion
		ListaPersonas.seek(0)# desplazamos cursor al comienzo

		##se crea una excepcion si la lista esta vacia
		try:
			self.personas=pickle.load(ListaPersonas)
			print("Se han cargado {} personas del fichero externo...".format(len(self.personas)))

		except:
			print("El fichero esta vacio")

		finally:

			ListaPersonas.close()
			del(ListaPersonas)


	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for c in self.personas:
			print(c)

	##metodo para guardar en fichero
	def guardarPersonasEnFicheroExterno(self):
		ListaPersonas=open("fichero_personas", "wb")
		pickle.dump(self.personas, ListaPersonas )
		ListaPersonas.close()
		del(ListaPersonas)

	def MostrarInfoFicheroExterno(self):
		print("La informacion del fichero externo es la siguiente")
		# ListaPersonas=open("fichero_personas", "rb")
		# infoFichero=pickle.load(ListaPersonas)
		# for c in infoFichero:
		# 	print(c)

		##o tomando la informacion ya leida y almacenada en self.personas
		for c in self.personas:
			print(c)

miLista=ListaPersonas()##creamos objeto para agregar las personas 

p=Persona("Josue", "Masculino", 24)
miLista.agregarPersonas(p)
p=Persona("Elias", "Masculino", 13)
miLista.agregarPersonas(p)
p=Persona("Rosa", "Femenino", 47)
miLista.agregarPersonas(p)

miLista.MostrarInfoFicheroExterno()

