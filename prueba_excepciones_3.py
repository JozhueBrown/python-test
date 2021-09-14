import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError ("El numero no puede ser negativo")	#raise es para que podamos lanzar una excepcion nosotors mismos
				#se debe tomar el valor de alguan excepcion existente, o a menos que hayamos creado anteriormente una
				#este excepcion aparecera en el programa y se controlara con try en la linea que aparece
	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un numero: ")))

try:	#aqui se controla la excepcion
	print(calculaRaiz(op1))

except ValueError as ErrorDeNumeroNegativo:#se le puede dar un alias a la excepcion, de otra forma daria dos excepciones
	print(ErrorDeNumeroNegativo)

print("Programa terminado")