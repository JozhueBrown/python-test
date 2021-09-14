miTupla=("Josue", 25,3,1996)
#convertir tupla en lista
milista=list(miTupla)
#convertir lista en tupla
mitupa=tuple(milista)

print(mitupa)

#comprobar si el valor existe
print("Josue" in mitupa)

#cuantas veces se encuentra un elemento
print(miTupla.count(25))

#longitud
print(len(miTupla))

#desempaquetado de tupla
nombre, dia ,  mes, anio=miTupla
print(nombre)
print(dia)
print(anio)
print(mes)