
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	try: 		#se usa try para que intente hacer la accion requerida
		return num1/num2
	except ZeroDivisionError:	#si no se puede hacer, arrojara esta excepcion con algun mensaje o accion que quiera
		print("No se puede dividir entre cero")
		return("Operacion erronea")

#excepcio si se ingresan simbolos en lugar de numeros

while True:	#este bucle es infinito y permite realizar la misma accion mientras el usuario no ingrese valores correctos
	try:
		op1=(int(input("Introduce el primer numero: ")))

		op2=(int(input("Introduce el segundo numero: ")))	

		break #una vez los valores son correctos, el break termina el bucle y continua con la ejecucion del programa
	except ValueError:
		print("Los valores introduciodos no son correctos. Intentalo de nuevo")	
	
operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")