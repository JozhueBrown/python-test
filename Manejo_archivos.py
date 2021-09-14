##en este archivo se trabajara sobre guardar los datos de algun programa ejecutado para que no se pierdan al momento de conluir
#Fases: creacion, apertura, escritura, cierre
##importamos librerias
from io import open##open es para abrir un archivo externo

archivo_texto=open("archivo.txt", "w" )##('nombre archivo', 'modo, lectura, escrituda, append')

frase="Hoy es un buen dia para morir \nmartes bonito"

archivo_texto.write(frase)#en el archivo, con write se escribe dentro del archivo

archivo_texto.close()##terminando se debe cerrar para complir con las fases del archivo


###Para leer el archivo:
archivo_texto=open("archivo.txt", "r" )

#texto=archivo_texto.read()##lo del archivo se almacena en la variable
lineas_texto=archivo_texto.readlines()##se guarda pero en forma de lineas

archivo_texto.close()

# print(texto)

print(lineas_texto[0])

### para agregar mas lineas

archivo_texto=open("archivo.txt", "a" )##la a es de append, que se usa para agregar 

archivo_texto.write("\nLos cambios son buenos :V")

archivo_texto.close()


#para posicionar el puntero en un lugar especifico, usando seek()

# print(archivo_texto.read())#si en read se mete parametro, leera hasta el numero indicado y lo demas no
# archivo_texto.seek(10)##posiciona el puntero en la localidad en el archivo que se lee, para poder volver a leerlo
# print(archivo_texto.read(15))

# archivo_texto.seek(len(archivo_texto.read())/2)##con esto posicionas el puntero a la mitad del archivo de texto
# archivo_texto.seek(len(archivo_texto.readline()))##situa terminando una linea
# print(archivo_texto.read())

#archivo_texto.close()

###para poner el texto en lectura y escritura
archivo_texto=open("archivo.txt", "r+" )#lectura y escritura
#print(archivo_texto.readlines())
lista_texto=archivo_texto.readlines()

lista_texto[1]="Esta linea ha sido incluida desde le exterior\n"#se reemplaza el contenido de la segunda linea

archivo_texto.seek(0)#posiciona puntero donde quiere escribir
archivo_texto.writelines()#se reescribe 

archivo_texto.close()#cierra archivo

