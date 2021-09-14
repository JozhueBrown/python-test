##yield contruye un valor iterable y no ocupa memoria reservada como una funcion normal

def generaPAres(limite):

	num=1
	
	while num<limite:

		yield num*2

		num+=1

devuelvePares=generaPAres(10)	#se crea un objeto en el que almacene el valor a generar

print(next(devuelvePares))

print("codigo aqui...")

print(next(devuelvePares))

print("codigo aqui...")

print(next(devuelvePares))

print("codigo aqui...")

print(next(devuelvePares))

print("codigo aqui...")
