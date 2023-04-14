import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview, Scrollbar
import sqlite3
import time



class product:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("550x420")
        self.root.resizable(False, False)
        self.frm = tk.Frame(self.root, padx=5, pady=10)
        self.frm.grid()
        self.db_name = "database.db"
        self.name = tk.StringVar()
        self.price = tk.StringVar()
        self.menu()

    def menu(self):
        #Name
        tk.Label(self.frm, text="Name: ").grid(column=0, row=0)
        self.name_entry = tk.Entry(self.frm, textvariable=self.name)
        self.name_entry.focus()
        self.name_entry.grid(column=1, row=0, columnspan=2, sticky="we")

        
        #Price
        tk.Label(self.frm, text="Price: ").grid(column=0, row=1)
        tk.Entry(self.frm, textvariable=self.price).grid(column=1, row=1, columnspan=2, sticky="we", pady=10)

        #save product
        tk.Button(self.frm, text="Save", cursor="hand2", command=self.add_product).grid(
            column=1, row=2, columnspan=2, sticky="we", pady=5)

        #Delete product
        tk.Button(self.frm, text="Delete", cursor="hand2", command=self.delete_product).grid(
            column=1, row=5,sticky="we")

        #Edit product
        tk.Button(self.frm, text="Edit", cursor="hand2", command=self.edit_product).grid(
            column=2, row=5, sticky="we")

        self.message = tk.Label(self.frm, text="", fg="green")
        self.message.grid(column=1, row=3, columnspan=2, sticky="we")

        #Create table
        self.product_list()

        #Product list
        self.get_products()


        self.root.mainloop()

    #*Creando funcion para visualizar la base de datos
    def product_list(self):
        #Agregando la cantidad de columnas que tendra
        self.table = Treeview(self.frm,column=2, height=10)
        barra = Scrollbar(self.frm, orient="vertical", command=self.table.yview)
        barra.grid(column=3, row=4, sticky="ns", pady=10)
        self.table['yscrollcommand'] = barra.set
        self.table.grid(column=1, row=4, columnspan=2, sticky="we", pady=10, ipadx=30)
        self.table.heading("#0", text="Name")
        self.table.heading("#1", text="Price")


    #!Creando conexion con la base de datos
    def run_table(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    #!Obteniendo datos de la base de datos para mostrarlos en la tabla
    def get_products(self):
        records = self.table.get_children()
        #Limpiando tabla
        for element in records:
            self.table.delete(element)

        #Consultando datos
        query = "SELECT * FROM product ORDER BY Id DESC"
        db_rows = self.run_table(query)
        for row in db_rows:
            self.table.insert("", 0, text= row[1], values= row[2])

    #*Validacion de datos del inicio
    def validation(self):
        if len(self.name.get()) == 0 or len(self.price.get()) == 0:
            messagebox.showerror(message="Falta rellenar un campo")
        else:
            return self.name.get() and self.price.get()

    #!Añadiendo el producto a la base de datos
    def add_product(self):
        if self.validation():
            query = "INSERT INTO product VALUES(NULL, ?, ?)"
            parametros = (self.name.get().capitalize(), float(self.price.get()))
            #*Corriendo la conexion y agregandolos
            self.run_table(query, parametros)
            self.message["text"] = "El producto se ha guardado con exito"
            #Actualizando tabla
            self.get_products()
            self.name.set("")
            self.price.set("")
            self.name_entry.focus()

    def delete_product(self):
        try:
            #*Metodo para saber que item se a seleccionado
            self.table.item(self.table.selection())["text"][0]
        except IndexError as error:
            messagebox.showerror(message="Seleccione un item de la lista")
        else:   
            name = self.table.item(self.table.selection())["text"]
            #Borrando dato seleccionado
            query = "DELETE FROM product WHERE name = ?"
            #Corriendo conexion con la base de datos para borrarlo
            self.run_table(query, (name, ))
            self.message["text"] = "Se elimino correctamente"
            #Actualizando tabla
            self.get_products()

    def edit_product(self):
        try:
            self.table.item(self.table.selection())["values"][0]
        except IndexError as error:
            messagebox.showerror(message="Seleccione un item de la lista")
        else:
            #!Obteniendo nombre y valor del producto
            #!desde la base de datos
            name = self.table.item(self.table.selection())["text"]
            old_price = self.table.item(self.table.selection())["values"][0]
            self.new_name = tk.StringVar()
            self.new_price = tk.StringVar()

                #*Creando ventana de editado
            self.window = tk.Toplevel(padx=10, pady=10)
            self.window.title("Edit product")
            self.window.resizable(False, False)
            self.window.focus_set()
                
                #Mostrando datos antiguos

                #Mostrando el nombre
            tk.Label(self.window, text="Old name: ").grid(column=0,row=0)
            tk.Entry(self.window, textvariable=tk.StringVar(self.window, value= name), state=["readonly"]).grid(
                    column=1, row=0, sticky="we", columnspan=2)

                #Mostrando el precio
            tk.Label(self.window, text="Old price: ").grid(column=0, row=2)
            tk.Entry(self.window, textvariable=tk.StringVar(self.window, value= old_price), state=["readonly"]).grid(
                    column=1, row=2, sticky="we", columnspan=2)

                #Capturando nuevos datos
                #*Capturando nombre nuevo del producto
            tk.Label(self.window, text="New name: ").grid(column=0, row=1)
            tk.Entry(self.window, textvariable=self.new_name).grid(column=1, row=1, sticky="we", columnspan=2)
                

                #*Capturando nuevo precio
            tk.Label(self.window, text="New price: ").grid(column=0, row=3)
            tk.Entry(self.window, textvariable=self.new_price).grid(column=1, row=3, sticky="we", columnspan=2)

                #Cancel
            tk.Button(self.window, text="Cancel", cursor="hand2", command=self.window.destroy
                        ).grid(column=1, row=4, pady=10, sticky="we")
                #Save
            tk.Button(self.window, text="Save", cursor="hand2",
                command=lambda: self.update_product(self.new_name.get().capitalize(),
                                                    name, self.new_price.get(), old_price)).grid(
                                                        column=2, row=4, pady=10, sticky="we")
                
            self.window.grab_set()

    def update_product(self, new_name, name, new_price, old_price):
        new_price = float(new_price)
        query = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
        parametros = (new_name, new_price, name, old_price)
        self.run_table(query, parametros)
        print(new_name, new_price)
        self.window.destroy()
        self.get_products()
        self.name_entry.focus()


            
            

if __name__ == '__main__':
    app = product()