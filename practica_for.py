### for variable in elemento a recorrer:

for i in [1,2,3]:
	print("Hola", end=" ") #con end indicas el espacio que quieres dejar y que no de salto de linea

for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
	print(i)

##Uso range()     con range(valor inicio,valor final,saltos de cuanto)
for i in range(5): ##crea un array del tamaño especificado
	#print(i)
	print(f"valor de la variable {i}") ##para concatenar texto con los valores


### verificar un correo
correo=input("Ingrese correo: ")
email=False
for i in correo:
	if(i=="@"):
		email=True

if email==True:
	print("El email es correcto!")
else:
	print("El email es incorrecto")