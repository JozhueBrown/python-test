from tkinter import *

root=Tk()

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()



#ingresando LAbel de texto
nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10)##con padx y pady se da espacio entre los limites del brafe y el widget

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=0,column=3, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=1,column=0, sticky="e", padx=10, pady=10)

PassLabel=Label(miFrame, text="Password: ")
PassLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10)

ComentariosLabel=Label(miFrame, text="Comentarios: ")
ComentariosLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)

##Ingresando cuadro de texto
minombre=StringVar()##variable que almacena cadenas de texto

cuadroNombre=Entry(miFrame, textvariable=minombre)##aqui se dice que esta sicioado con la variable 
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=0, column=4, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=1, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")#para cambiar los elementos que muestras, se cambia en config

#para agregar un cuadro d texto
textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=3, column=1, padx=10, pady=10)
##si el texto excede, necesita una barra scroll, y esa se debe agregar manualmente
scrollComentarios=Scrollbar(miFrame, command=textoComentario.yview)##en comando se especifia a que widget se implementa, y puede ser x o y view para la oientacion
scrollComentarios.grid(row=3, column=2, sticky="nsew")#con sticky hacemos que se adapte al tamaño del widget
##para que el scroll se quede donde se posiciona el cursor del texto, movemos la config del widget de texto
textoComentario.config(yscrollcommand=scrollComentarios.set)

##funcion para boton
def codigoBoton():
	minombre.set("Juanchito")


##creando un boton
botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()#todo se empaqueta


root.mainloop()