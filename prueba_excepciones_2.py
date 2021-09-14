def divide():

	try:		#en este ejemplo se hacen dos excepciones consecutivas, que son posibles

		op1=(float(input("Introduce el primer numero: ")))

		op2=(float(input("Introduce el segundo numero: ")))

		print("La division es: " + str(op1/op2))

	except ValueError:

		print("el valor introducido es erroneo")

	except ZeroDivisionError:

		print("No se puede dividir entre 0!")

	finally:		#este se usa para que esas lineas correspondientes se ejecuten si o si

		print("Calculo finalizado")

divide()