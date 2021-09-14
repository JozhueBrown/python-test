###Continue

for letra in "Python":
	
	if letra=="h":		##si la instruccion se cumple:
		continue 		##ignora lo que sete por hacerse en la iteracion y pasara a la siguiente vuelta
	print ("Viendo la letra: " +letra)


		###quitar espacios

nombre="Josue Barroso"
contador =0
print(len(nombre))##mostraria que tiene ams valores debido a los espacios
for i in nombre:
	if i==" ":
		continue
	contador+=1

print(contador)##aqui ya mostrara el numero de caracteres sin espacio


###Pass
#while True:		#para crear un bucle infinito
#	pass

##tambien se puede poner dentro de una clase que no quieren habilitar por el momento

###Else
email=input("Introduce un correo plox: ")
for x in email:

	if x=="@":
		arroba=True
		break;		#El break solo sale del bucle conse se encuentra y continua con el resto de codigo
					#no termina con el resto del programa

else:		#este else pertenece al for, cuando termina el ciclo, si no hay cambios entonces toma esa accion
	arroba=False

print(arroba)