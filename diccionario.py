miDiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
print(miDiccionario["Alemania"]) #se pueden convinar cadenas con valores numericos

#agregar elemento
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

#corregir
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#eliminar
del miDiccionario["Reino Unido"]
print(miDiccionario)

#poner valores de tupla en diccionario
mitupla=("caca", "qlo", "pdo", "pis")
diccionario={mitupla[0]:1, mitupla[1]:2, mitupla[2]:3, mitupla[3]:4}
print(diccionario)

#diccionario con tupla en lugar de un solo valor
tuxionario={23:"Jordan", "nombre":"Michael", "equipo": "Chicago", "anillos":{"temporadas":(1991,1992,1993,1996,1997,1998)}}#diccionario dentro de otro
print(tuxionario["anillos"])
print(tuxionario.keys()) #imprime las claves
print(tuxionario.values()) #imprime valores
print(len(tuxionario)) #logitud diccionario