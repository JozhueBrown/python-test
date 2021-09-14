##inportamos librerias
from tkinter import *

#para que no lo abra con consola detras, debe ser guardado con extension .pyw

#construimos raiz
raiz=Tk()

raiz.title("Ventana de pruebas")## para darle un nombre

raiz.resizable(1,1)##para evitar redimensionar ventana (width,heigth)

raiz.iconbitmap("favicon.ico")##para cambiar icono 

#raiz.geometry("1360x768")##para que se abra en cierto tamaño, por lo general se da tamaño al frame y no a la raiz

raiz.config(bg="orange")##cambiar propiedades de ventana

#creamos frame
miFrame=Frame()
miFrame.pack(side="bottom", anchor="w")#se empaqueta dentro de la raiz
#dentro se puede sepecificar en que lugar de la raiz se situe

#para ver el frame se le da un fondo
miFrame.config(bg="red")
#se da tamaño al frame y no a la raiz, ya que esta se adapta
miFrame.config(width="800", height="600")

#cambiar caracteristicas del borde
miFrame.config(bd=20)##primero se le da un ancho al borde, por defecto es 0
miFrame.config(relief="groove" )
#agregar un corsor cuando se situe sobre el frame
miFrame.config(cursor="pirate")
miFrame.title("buenas")

raiz.mainloop()##bucle infinito