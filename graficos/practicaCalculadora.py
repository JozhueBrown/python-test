from tkinter import *

raiz=Tk()
raiz.title("Calculadora")
# raiz.config(background="#a25a5e")

miFrame=Frame(raiz)
miFrame.config(background="#292929")
miFrame.pack()
##variables globales
operacion=""##creamos una variable global que almacenara la operacion que se desea realizar
resultado=0



####PAntalla secundaria
numeroPantalla2=StringVar()##declaras que recivira cadena

pantalla2=Entry(miFrame, textvariable=numeroPantalla2)##en el constructor entrara la variable
pantalla2.grid(row=1, column=1, pady=5, padx=10, columnspan=4, sticky="nsew")##columnspan es para expandir una columna el numero de casillas deseado
pantalla2.config(background="#364143", fg="#bfd6e0", justify="right", font=("minecraft",13))

####Pantalla primaria
#se asocia una variable que sera introducida al frame medante opcion textvariable
numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)##en el constructor entrara la variable
pantalla.grid(row=2, column=1, pady=10, padx=10, columnspan=4)##columnspan es para expandir una columna el numero de casillas deseado
pantalla.config(background="#364143", fg="#bfd6e0", justify="right", font=("minecraft",15))

######---------pulsaciones teclado
#se crean funciones para los digitos
# numeroPantalla2.set("5")
def Reset():
	global resultado
	numeroPantalla.set("0")
	numeroPantalla2.set("")
	resultado=0


def Delete():
	borra=len(numeroPantalla.get())
	pantalla.delete(borra -1)
	# print(borra)
	if (borra-1)==0:
		numeroPantalla.set("0")
	# borra.delete(0)
	# numeroPantalla.set(borra)
	

numeroPantalla.set("0")
def numeroPulsado(num):
	global operacion

	# if operacion!="":
	# 	numeroPantalla.set(num)
	# 	operacion=""
	resultado=float(numeroPantalla.get())


	if numeroPantalla.get()=="0" or operacion!="":
		numeroPantalla.set(num)
		operacion=""

	else:
		numeroPantalla.set(numeroPantalla.get() + num)##con get() obtenemos lo que haya en pantalla y agregamos el numero

def pon_pantalla(num):
	global operacion
	global resultado
	numeroPantalla2.set(numeroPantalla2.get() + num + operacion)##pasamos a pantalla secundaria los valores
	numeroPantalla.set(resultado)

####---------funcion suma
def Suma(num):
	global resultado
	global operacion

	resultado+=float(num)
	operacion="+"
	pon_pantalla(num)
	
	print(resultado)

	

####-------Funcion Resta
def Resta(num):
	# pass
	global resultado
	global operacion

	resultado-=float(num)
	operacion="-"
	pon_pantalla(num)

	

####-------Funcion Multiplicacion
def Multiplicacion():
	pass

####-------Funcion diviision
def Division():
	pass


####-------Funcion Resultado
def el_resultado():
	# pass
	global resultado
	numeroPantalla.set(resultado)
	numeroPantalla2.set("")
	resultado=0





####Botones
f1=3
f2=f1+1
f3=f1+2
f4=f1+3
f5=f1+4


###fila 1-------
botonDel=Button(miFrame, text="Del", width=7, height=2, command=Delete)
botonDel.grid(row=f1, column=1)
botonDel.config(background="#505a5e", fg="#bfd6e0")

botonSqrt=Button(miFrame, text="Sqrt", width=7, height=2)
botonSqrt.grid(row=f1, column=2)
botonSqrt.config(background="#505a5e", fg="#bfd6e0")

botonPercent=Button(miFrame, text="%", width=7, height=2)
botonPercent.grid(row=f1, column=3)
botonPercent.config(background="#505a5e", fg="#bfd6e0")

botonDiv=Button(miFrame, text="/", width=7, height=2, command=lambda:Division(numeroPantalla.get()))
botonDiv.grid(row=f1, column=4)
botonDiv.config(background="#505a5e", fg="#bfd6e0")

###fila 2-------
boton7=Button(miFrame, text="7", width=7, height=2, command=lambda:numeroPulsado("7"))
boton7.grid(row=f2, column=1)
boton7.config(background="#1f2b31", fg="#bfd6e0")

boton8=Button(miFrame, text="8", width=7, height=2, command=lambda:numeroPulsado("8"))
boton8.grid(row=f2, column=2)
boton8.config(background="#1f2b31", fg="#bfd6e0")

boton9=Button(miFrame, text="9", width=7, height=2, command=lambda:numeroPulsado("9"))
boton9.grid(row=f2, column=3)
boton9.config(background="#1f2b31", fg="#bfd6e0")

botonMulti=Button(miFrame, text="x", width=7, height=2, command=lambda:Multiplicacion(numeroPantalla.get()))
botonMulti.grid(row=f2, column=4)
botonMulti.config(background="#505a5e", fg="#bfd6e0")

###fila 3-------
boton4=Button(miFrame, text="4", width=7, height=2, command=lambda:numeroPulsado("4"))
boton4.grid(row=f3, column=1)
boton4.config(background="#1f2b31", fg="#bfd6e0")

boton5=Button(miFrame, text="5", width=7, height=2, command=lambda:numeroPulsado("5"))
boton5.grid(row=f3, column=2)
boton5.config(background="#1f2b31", fg="#bfd6e0")

boton6=Button(miFrame, text="6", width=7, height=2, command=lambda:numeroPulsado("6"))
boton6.grid(row=f3, column=3)
boton6.config(background="#1f2b31", fg="#bfd6e0")

botonResta=Button(miFrame, text="-", width=7, height=2, command=lambda:Resta(numeroPantalla.get()))
botonResta.grid(row=f3, column=4)
botonResta.config(background="#505a5e", fg="#bfd6e0")

###fila 4-------
boton1=Button(miFrame, text="1", width=7, height=2, command=lambda:numeroPulsado("1"))
boton1.grid(row=f4, column=1)
boton1.config(background="#1f2b31", fg="#bfd6e0")

boton2=Button(miFrame, text="2", width=7, height=2, command=lambda:numeroPulsado("2"))
boton2.grid(row=f4, column=2)
boton2.config(background="#1f2b31", fg="#bfd6e0")

boton3=Button(miFrame, text="3", width=7, height=2, command=lambda:numeroPulsado("3"))
boton3.grid(row=f4, column=3)
boton3.config(background="#1f2b31", fg="#bfd6e0")

botonSum=Button(miFrame, text="+", width=7, height=2, command=lambda:Suma(numeroPantalla.get()))
botonSum.grid(row=f4, column=4)
botonSum.config(background="#505a5e", fg="#bfd6e0")
###fila 5-------
botonReset=Button(miFrame, text="C", width=7, height=2, command=Reset)
botonReset.grid(row=f5, column=1)
botonReset.config(background="#505a5e", fg="#bfd6e0")

boton0=Button(miFrame, text="0", width=7, height=2, command=lambda:numeroPulsado("0"))
boton0.grid(row=f5, column=2)
boton0.config(background="#1f2b31", fg="#bfd6e0")

botonPunto=Button(miFrame, text=".", width=7, height=2, command=lambda:numeroPulsado("."))
botonPunto.grid(row=f5, column=3)
botonPunto.config(background="#1f2b31", fg="#bfd6e0")

botonIgual=Button(miFrame, text="=", width=7, height=2, command=el_resultado)
botonIgual.grid(row=f5, column=4)
botonIgual.config(background="#a25a5e", fg="#bfd6e0")

raiz.mainloop()