##Serializar: para convertir un fichero o paquete a binario. Asi se hace mas facil su exportacion y distribucion 
import pickle	###la carpeta pickle contiene los metodos necesarios

lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres", "wb")##la variable almacenara  el archivo que se abre con 'wb'(write binary)

#volcado a fichero con dump()
pickle.dump(lista_nombres, fichero_binario)##lsita a volcar y archivo donde se quiere volcar

fichero_binario.close()

del(fichero_binario)

###para cescatar la informacion

fichero=open("lista_nombres", "rb")##leer en binario(rb)

lista=pickle.load(fichero)##se guarda en lista

print(lista)

#y asi serializamos algo listo para si distribucion
#y se recupera la informacion