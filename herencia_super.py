class Persona():
	def __init__(self, nombre, edad, Lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.Lugar_residencia=Lugar_residencia

	def descripcion(self):

		print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.Lugar_residencia)


class Empleado(Persona):##principio de sustitucion
			#un empleado siemrpe es una persona isinstance()

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
		###Super se usa para tomar los valores y/o metodos que tenga la clase padre y se le manda a llamr como 
		###si fuera una funcion, si recive datos, se deben requerir en la funcion donde se encuentra
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

		self.salario=salario
		self.antiguedad=antiguedad


	def descripcion(self):
		super().descripcion()###igual se usa super, pero no se piden datos porque solo mostrara la informacion ya ingresada
		##ya solo falta imprimir los datos faltantes pertenecientes solo a esta clase
		print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)

Antonio=Empleado(1800, 3, "Antonio", 30, "Mexico")

Antonio.descripcion()

print(isinstance(Antonio, Persona))###nos indica si el objeto creado pertenece a la clase que se menciona
			##devolvera True o False