###Clases
class Coche():
	#propiedades
	def __init__(self):			##un constructor le da un estado inicial a una clase
	
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4		#la encapsulacion se realiza poniendo dos guiones bajosantes del nombre
		self.__enmarcha=False

	#comportamiento mediante metodos
	def arrancar(self, arrancamos):
		self.__enmarcha=arrancamos
		if(self.__enmarcha):
			return "El coche esta en marcha"

		else:
			return "El coche esta parado"

	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un largo de ", 
			self.__largoChasis)

		#al final termina con dos metodos o comportameintos

#creando objetos
miCoche=Coche()###instanciar una clase

#print("El largo del coche es: ", miCoche.largoChasis) #esta es una forma de ver las caracteristicas
#print("El coche tiene ", miCoche.__ruedas, " ruedas")
print(miCoche.arrancar(True))
miCoche.estado() #si no se ejecuta el proceso anterior, arroja diferente valor

print("----------A continuacion se crea el seguno objeto-----------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.__ruedas=2
miCoche2.estado()