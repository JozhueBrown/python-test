def devuelve_ciudades(*ciudades): #el a* antes del argumento señala que va a recibir un numero indeterminado de elemento yseran en forma de tupla
	for elemento in ciudades:
		#yield elemento #este se usa para acceder a la tupla completa, o de manera habitual
		#for subElemento in elemento:	#este for es si quisieramos ingresar en los elementos de la tupla
		#	yield subElemento			# junto con el yield
		yield from elemento #de esta forma nos ahorramos el segundo for

ciudades_devueltas=devuelve_ciudades("CDMX", "Guanajuato", "Michoacan", "Guadalajara")#cada cadena, es guardada como una tupla, asi sirve el * anterior

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))