from tkinter import *

ventana = Tk()
ventana.title("Calculator")

ent_texto = Entry(ventana, font = ("Calibri 20"))
ent_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

boton0 = Button(ventana, text = "0",width= 13, height= 2 )
boton1 = Button(ventana, text = "1",width= 5, height= 2 )
boton2 = Button(ventana, text = "2",width= 5, height= 2 )
boton3 = Button(ventana, text = "3",width= 5, height= 2 )
boton4 = Button(ventana, text = "4",width= 5, height= 2 )
boton5 = Button(ventana, text = "5",width= 5, height= 2 )
boton6 = Button(ventana, text = "6",width= 5, height= 2 )
boton7 = Button(ventana, text = "7",width= 5, height= 2 )
boton8 = Button(ventana, text = "8",width= 5, height= 2 )
boton9 = Button(ventana, text = "9",width= 5, height= 2 )

borrar = Button(ventana, text = "AC",width= 5, height= 2 )
parentesis1 = Button(ventana, text = "(",width= 5, height= 2 )
parentesis2 = Button(ventana, text = ")",width= 5, height= 2 )
punto = Button(ventana, text = ".",width= 5, height= 2 )

sum = Button(ventana, text = "+",width= 5, height= 2 )
res = Button(ventana, text = "-",width= 5, height= 2 )
mul = Button(ventana, text = "*",width= 5, height= 2 )
div = Button(ventana, text = "/",width= 5, height= 2 )
igual = Button(ventana, text = "=",width= 5, height= 2 )







#Fila 1
borrar.grid(row = 1, column= 0, padx = "5", pady = "5")
parentesis1.grid(row = 1, column= 1, padx = "5", pady = "5")
parentesis2.grid(row = 1, column= 2, padx = "5", pady = "5")
sum.grid(row = 1, column= 3, padx = "5", pady = "5")


#Fila 2
boton7.grid(row = 2, column= 0, padx = "5", pady = "5")
boton8.grid(row = 2, column= 1, padx = "5", pady = "5")
boton9.grid(row = 2, column= 2, padx = "5", pady = "5")
res.grid(row = 2, column= 3, padx = "5", pady = "5")

#Fila 3
boton4.grid(row = 3, column= 0, padx = "5", pady = "5")
boton5.grid(row = 3, column= 1, padx = "5", pady = "5")
boton6.grid(row = 3, column= 2, padx = "5", pady = "5")
mul.grid(row = 3, column= 3, padx = "5", pady = "5")


#Fila 4
boton1.grid(row = 4, column= 0, padx = "5", pady = "5")
boton2.grid(row = 4, column= 1, padx = "5", pady = "5")
boton3.grid(row = 4, column= 2, padx = "5", pady = "5")
div.grid(row = 4, column= 3, padx = "5", pady = "5")


#Fila 5
boton0.grid(row = 5, column=0, columnspan = 2, padx = "12", pady = "5")
punto.grid(row = 5, column= 2, padx = "5", pady = "5")
igual.grid(row = 5, column=3,  padx = "5", pady = "5")


ventana.mainloop()
