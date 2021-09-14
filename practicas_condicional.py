edad=7

if 0<edad<100:		#se pueden concatenar valores, se deven cumplir ambos o pasa directo al ELSE
	print("edad es correcta")
else:
	print("Edad incorrecta")

#### salarios concatenados
salario_presidente=int(input("Introduce salario presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce salario director: "))
print("Salario director: " + str(salario_director))

salario_administrativo=int(input("Introduce salario administrativo: "))
print("Salario administravito: " + str(salario_administrativo))

salario_jefe_area=int(input("Introduce salario jefe de area: "))
print("Salario jefe de area: " + str(salario_jefe_area))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correcto!!")
else:
	print("Algo no anda bien :(")


#### otro mas (uso de AND y OR)
## beca a superior de 40km, mas de 2 hermanos y salario familiar <=20000
print("Programa de becas 2021")
discancia_escuela=int(input("Introduce la distancia en KM: "))
print(discancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto: "))
print(salario_familiar)

if discancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")

### uso de in
print("Asignaturas optativas año 2017")
print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()  ##con lower() cambias a minusculas, con upper() cambias a mayusculas

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura)
else: 
	print("La asignatura no esta disponible!")