##sintaxis
i=1

while i<=10:
	print("Ejecucion " + str(i))
	i=i+1

print("termino la ejecucion")


###con bucle indeterminado
edad=int(input("Introcuzca su edad porfavor: "))

while edad<5 or edad>100:
	print("Edad no valida, Intentelo de nuevo...")
	edad=int(input("Introcuzca su edad porfavor: "))

print("edad del cliente: " + str(edad))
print("Gracias por visitarnos, adelante!!")


##hayar raiz cuadrada de un numero 
import math

print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduzca numero para calcular por favor: "))

intentos=0

while numero<0:
	print("No se puede hallar la raiz de un numero negativo")

	numero=int(input("Introduzca numero para calcular por favor: "))
	if numero<0:
		intentos=intentos+1

	if intentos==2:
		print("Has consumido demasiados intentos. El programa ha finalizado")
		break;

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))