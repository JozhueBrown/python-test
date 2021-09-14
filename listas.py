miLista=["Josue","Elias","Rosa","Vicky"] #agregar *3 para repetir valores

print(miLista[-2])

#porcion
print(miLista[0:3])
print(miLista[2:]) #accede dsde el indice hasta el final

#agregar elemento
miLista.append("Mario")

#agregar elemento intermedio
miLista.insert(2,"mom_Vicky")

#agregar mas elementos
miLista.extend(["uncle_Mario","ount_Diana","Mayin","Dannae","Noah"])
print(miLista[:])

#para indicar el indice de uno en concreto
print(miLista.index("Mario"))

#comprobar si se encuentra
print("Pepe" in miLista)

#eliminar elementos
miLista.remove("Mario")
print(miLista[:])

#eliminar ultimo elemento
miLista.pop()
print(miLista[:])

#sumar listas
miLista2=["Daniela","Daniel"]
miLista3=miLista+miLista2
print(miLista3[:])