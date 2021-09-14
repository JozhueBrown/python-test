from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

#se genera el texto
miLabel=Label(miFrame, text="Hola puerk, primer texto")
#miLabel.pack()##todo se debe empaquetar, pero se usa el tamaño que toma el texto
#si se quiere adaptar a el tamaño del frame, se debe usar:
miLabel.place(x=100, y=100)#aqui se especifica en pixeles donde se quere situar

# se puede abrev iar, ya que solo se usara uan vez, y poner lo asi:
miLabel=Label(miFrame, text="Hola puerk, primer texto", fg="red", font=("Comic Sans MS",18)).place(x=50, y=50)

#para usar imagenes en label (apecta png y gif, para otras se deber añadir ams modulos)
miImagen=PhotoImage(file="instagrom.png")
miLabel=Label(miFrame, image=miImagen).place(x=200, y=200)


root.mainloop()