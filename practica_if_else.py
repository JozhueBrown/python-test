print("Verificacion de acceso")

edad_usuario=int(input("introduce tu edad: "))

if edad_usuario<18:
	print("No puedes pasar")
elif edad_usuario>100:			#elif es como else if anidados, permite uso continuo de condiciones
	print("Edad Incorrecta")
else:
	print("Puedes pasar!")
print("El programa ha finalizado")


#uso elif
nota_alumno=int(input("Ingrese nota por favor:"))

if nota_alumno<5:
	print("Insuficioente")
elif nota_alumno<6:
	print("Suficiente")
elif nota_alumno<7:
	print("Bien")
elif nota_alumno<9:
	print("Notable")
else:
	print("Sobresaliente")
