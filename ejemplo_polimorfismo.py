class Coche():

	def desplazamiento(self):## varias clases pueden tener el mismo metodo
		print("Me desplazo utilizando cuatro ruedas")

class Moto():
	
	def desplazamiento(self):## aunque tengan mismo nombre, hacen cosas diferentes
		print("Me desplazo utilizando dos ruedas")


class Camion():

	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")


def desplazamientoVehiculo(vehiculo):#dependiendo el tipo de vehiculo, tomara el metodo correspondiente
	vehiculo.desplazamiento()

miVehiculo=Moto()

desplazamientoVehiculo(Camion())##Se puede poner el objeto creado, o crearlo al momento