from tkinter import ttk
from tkinter import *
import sqlite3

i = 0

class box:

    db_name = 'databases.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Calculator')
        
        # Frame container
        frame = LabelFrame(self.wind, text = "Calculator DB" )
        frame.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 5)
        
        #Number input
        self.ent_text = Entry(frame, font = ("Calibri 20"))
        self.ent_text.focus()
        self.ent_text.grid(row = 1, column = 0, columnspan = 4, padx = 5, pady = 5)

        #Numbers buttons
        self.boton0 = Button(frame, text = "0",width= 15, height= 2, command = lambda: self.click_button(0))
        self.boton1 = Button(frame, text = "1",width= 5, height= 2, command = lambda: self.click_button(1))
        self.boton2 = Button(frame, text = "2",width= 5, height= 2, command = lambda: self.click_button(2))
        self.boton3 = Button(frame, text = "3",width= 5, height= 2, command = lambda: self.click_button(3))
        self.boton4 = Button(frame, text = "4",width= 5, height= 2, command = lambda: self.click_button(4))
        self.boton5 = Button(frame, text = "5",width= 5, height= 2, command = lambda: self.click_button(5))
        self.boton6 = Button(frame, text = "6",width= 5, height= 2, command = lambda: self.click_button(6))
        self.boton7 = Button(frame, text = "7",width= 5, height= 2, command = lambda: self.click_button(7))
        self.boton8 = Button(frame, text = "8",width= 5, height= 2, command = lambda: self.click_button(8))
        self.boton9 = Button(frame, text = "9",width= 5, height= 2, command = lambda: self.click_button(9))

        self.borrar = Button(frame, text = "AC",width= 5, height= 2, command = lambda: self.click_delete() )
        self.parentesis1 = Button(frame, text = "(",width= 5, height= 2, command = lambda: self.click_button(")") )
        self.parentesis2 = Button(frame, text = ")",width= 5, height= 2, command = lambda: self.click_button("(") )
        self.punto = Button(frame, text = ".",width= 5, height= 2, command = lambda: self.click_button(".") )

        self.sum = Button(frame, text = "+",width= 5, height= 2, command = lambda: self.click_button("+") )
        self.res = Button(frame, text = "-",width= 5, height= 2, command = lambda: self.click_button("-") )
        self.mul = Button(frame, text = "*",width= 5, height= 2, command = lambda: self.click_button("*") )
        self.div = Button(frame, text = "/",width= 5, height= 2, command = lambda: self.click_button("/") )
        self.igual = Button(frame, text = "=",width= 5, height= 2, command = lambda: self.results())

        #Row 2
        self.borrar.grid(row = 2, column= 0, padx = "5", pady = "5")
        self.parentesis1.grid(row = 2, column= 1, padx = "5", pady = "5")
        self.parentesis2.grid(row = 2, column= 2, padx = "5", pady = "5")
        self.sum.grid(row = 2, column= 3, padx = "5", pady = "5")

        #Row 3
        self.boton7.grid(row = 3, column= 0, padx = "5", pady = "5")
        self.boton8.grid(row = 3, column= 1, padx = "5", pady = "5")
        self.boton9.grid(row = 3, column= 2, padx = "5", pady = "5")
        self.res.grid(row = 3, column= 3, padx = "5", pady = "5")

        #Row 4
        self.boton4.grid(row = 4, column= 0, padx = "5", pady = "5")
        self.boton5.grid(row = 4, column= 1, padx = "5", pady = "5")
        self.boton6.grid(row = 4, column= 2, padx = "5", pady = "5")
        self.mul.grid(row = 4, column= 3, padx = "5", pady = "5")

        #Row 5
        self.boton1.grid(row = 5, column= 0, padx = "5", pady = "5")
        self.boton2.grid(row = 5, column= 1, padx = "5", pady = "5")
        self.boton3.grid(row = 5, column= 2, padx = "5", pady = "5")
        self.div.grid(row = 5, column= 3, padx = "5", pady = "5")

        #Row 6
        self.boton0.grid(row = 6, column=0, columnspan = 2, padx = "5", pady = "5")
        self.punto.grid(row = 6, column= 2, padx = "5", pady = "5")
        self.igual.grid(row = 6, column=3,  padx = "5", pady = "5")

        #history table
        self.tree = ttk.Treeview(height = 14)
        self.tree.grid(row = 0, column = 4, columnspan = 1, padx = 5, pady = 1) 
        #Headder table
        self.tree.heading('#0', text = 'Calculations', anchor = CENTER)
        self.get_products()
    
    def click_button(self, value):
        global i
        self.ent_text.insert(i, value)
        i += 1

    def click_delete(self):
        global i
        self.ent_text.delete(0, END)
        i = 0

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_products(self):
        #Cleanin table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #quering data
        query = 'SELECT * FROM calc'
        db_rows = self.run_query(query)
        #Filling data
        for row in db_rows:
            self.tree.insert('',0, text = row[1])

    def validation(self):
        return len(self.ent_text.get()) != 0 

    def add_calc(self):
        if self.validation():
            query = 'INSERT INTO calc VALUES(NULL,?)'
            parameters = (self.ent_text.get())
            self.run_query(query, [parameters])
        else:
            print('Calculo requerido')
        self.get_products()

    def results(self):
        global i
        calculate = self.ent_text.get()
        result = eval(calculate)
        i += 1
        self.ent_text.insert(i, "=")
        self.ent_text.insert(i,result)
        self.add_calc()

   
if __name__ == '__main__':
    window = Tk()
    application = box(window)
    window.mainloop()