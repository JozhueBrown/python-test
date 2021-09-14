nombreUsuario=input("Ingrese nombre usuario: ")

print("El nombre es: ", nombreUsuario.capitalize())

edad=input("Ingrese edad: ")

while(edad.isdigit()==False):
	print("Por favor introduce un valor numerico!")
	edad=input("Ingrese edad: ")

if int(edad)<18:
	print("No puedes pasar")
else:
	print("Puedes pasar")

print("Su edad es: ", edad)

