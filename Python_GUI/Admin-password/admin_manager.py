import os
from tkinter import PhotoImage
import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet
import random
import json
from tkinter import messagebox
import subprocess
from Edit import edit_data

user_pc = os.getlogin()
 
class interface_window:
    def __init__(self, ide):
        self.root = tk.Tk()
        self.ide = ide
        self.root.resizable(False, False)
        self.root.title("Admin password")
        self.frm = tk.Frame(self.root, bg="#DADADA")
        self.frm.grid()
        self.hidden = tk.BooleanVar()
        self.page = tk.StringVar()
        self.user = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.interface()
        

      
    def create_key(self):
        key = Fernet.generate_key()
        os.mkdir(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\key")
        subprocess.call(f"attrib +h C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\key", shell=True)
        with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\key\\filekey.key", "wb")as file:
            return file.write(key)
        
    def load_key(self):
        with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\key\\filekey.key", "rb")as file:
            return file.read()
                    
    #Credits
    def about(self):
        messagebox.showinfo(title="Information", message=f"""
            Application created by py-rod
            
            Thank you for try this app, im appreciate
            one review in github or comment :)
            
            Github:
            (github.com/Prod97/Tkinter-base-de-datos)
            """)
        
    #Menu toolsbar
    def menu(self):
        toolbar = tk.Menu(self.root)
        
        option = tk.Menu(toolbar, tearoff=False)
        option.add_command(label="Exit", command=self.root.destroy)
        
        
        toolbar.add_cascade(label="Option", menu=option)
        toolbar.add_cascade(label="About", command=self.about)
        
        self.root.config(menu=toolbar)

        
    
    #Password configuration to show o hidden
    def show_password(self):
        #Show password
        if self.hidden.get() == False:
            self.p.config(show="")
            self.ico.config(image=self.on)
            self.hidden.set(True)
        else:
            #Hidden password
            self.p.config(show="*")
            self.ico.config(image=self.off)
            self.hidden.set(False)
            
    #id
    def __id(self):
        qwerty = "qwertyuiopasdfghjklzxcvbnm"
        number = "1234567890"
        qwerty_up = qwerty.upper()
        all = qwerty + number + qwerty_up
        new_id = "".join(random.sample(all, 8))
        return new_id
    
    #Data
    def data_table(self):
        self.table = ttk.Treeview(self.frm, column=("Web page", "User", "Email", "Password"))
        self.table.grid(column=0, row=3, columnspan=8, sticky="we")
        ttk.Scrollbar(self.frm, orient="vertical").grid(column=8, row=3 ,sticky="ns")
        self.table.heading("#0", text="ID")
        self.table.heading("#1", text="Web page")
        self.table.heading("#2", text="User")
        self.table.heading("#3", text="Email")
        self.table.heading("#4", text="Password")
        
        veri = os.path.exists(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json")
        
        if veri:
            #Load key
            key = self.load_key()
            fernet = Fernet(key)
            
            #Read json
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "rb")as file:
                text = file.read()
            
            #Desencry json
            decryp = fernet.decrypt(text)
            
            #Write json desencrypte
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "wb")as q_write:
                q_write.write(decryp)
            
            #Read json
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json")as q_read:
                var1 = json.load(q_read)
                
                #Contador
                i = 0
                
            #Charge data 
            for k, v in var1.items():
                #Count data
                for i in str(len(var1)):
                    #Sum data
                    i = i
                    #Insert data in windows
                    self.table.insert("", i, text=f"{k}", values=(v["Page"], v["User"], v["Email"], v["Password"]))
            
            #Read json
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "rb")as w_file:
                text2 = w_file.read()
                
            #Encryp json
            new_encryp = fernet.encrypt(text2)
            
            #Write json encryp
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "wb")as e_file:
                e_file.write(new_encryp)
        else:
            self.table.insert("", 0, text="No hay nada")
    
    #Limpiando campos de entrys
    def clear(self):
        self.page.set("")
        self.user.set("")
        self.email.set("")
        self.password.set("")
    
    #Edit
    def edit(self):
        item = self.table.focus()
        self.id_key = self.table.item(item)["text"]
        self.id_page = self.table.item(item)["values"][0]
        self.id_user = self.table.item(item)["values"][1]
        self.id_email = self.table.item(item)["values"][2]
        self.id_password = self.table.item(item)["values"][3]
        
        if self.id_key == "":
            messagebox.showerror(message="no hay nada que editar")
        else:      
            edit_data(self.ide,self.id_key, self.id_page, self.id_user, self.id_email, self.id_password)
            self.data_table()
                    
    
    #delete information the json
    def delete(self):
        item = self.table.focus()
        key_id = self.table.item(item)["text"]
        
        key = self.load_key()
        fernet = Fernet(key)
        
        with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "rb")as file:
            text = file.read()
            
        decryp = fernet.decrypt(text)
        
        with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "wb")as file2:
            file2.write(decryp)
            
        with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json")as file3:
            var1 = json.load(file3)
            
        var1.pop(key_id)
        
        with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "w")as file4:
            json.dump(var1, file4, indent=4)
        
        with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "rb")as file5:
            text2 = file5.read()
            
        encryp = fernet.encrypt(text2)
        
        with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "wb")as file6:
            file6.write(encryp)
        
        self.data_table()
        
    
    def create_tabele_data(self):
        data = {}
        
        #Obtain data
        page = self.page.get()
        email = self.email.get()
        password = self.password.get()
        
        if  len(page) == 0:
            messagebox.showinfo(message="Empty web page")
        elif len(email) == 0:
            messagebox.showerror(message="Empty email")
        elif len(password) == 0:
            messagebox.showinfo(message="Empty password")
        else:
            check = os.path.exists(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json")
            user = self.user.get()
            if check:
                #Charge key
                key = self.load_key()
                fernet = Fernet(key)

                #Read file 
                with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "rb")as fiile:
                    text2 = fiile.read()
                #Desencriptando
                decry2 = fernet.decrypt(text2)
                
                #Write to json
                with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "wb")as qfile:
                    qfile.write(decry2)
                
                #Read json
                with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json")as read_file:
                    var1 = json.load(read_file)
                    var1[self.__id()] = {"Page": page,
                                        "User": user,
                                        "Email": email,
                                        "Password": password}
                    #Inyectando nuevos valores al json 
                    with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "w")as w:
                            json.dump(var1, w, indent=4)
                            self.page.set("")
                            self.user.set("")
                            self.email.set("")
                            self.password.set("")
                    #Leyendo para empezar a encriptar     
                    with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "rb")as f_file:
                            r = f_file.read()
                            
                    #Encriptando                    
                    new_encryp = fernet.encrypt(r)
                    
                    #Escribiendo la informacion de manera encriptada
                    with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "wb")as r_file:
                        r_file.write(new_encryp)
                
                #Cargando base de datos    
                self.data_table()
                
            else:  
                #Generate key to encryp file
                self.create_key()
                
                #Load key to encryp
                key = self.load_key()
                fernet = Fernet(key)
                
                #Agregando los datos al diccionario para luego hacer dump
                data.setdefault(self.__id(), {"Page": page,
                                            "User": user,
                                            "Email": email,
                                            "Password": password})
                
                with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "w")as file:
                    json.dump(data, file, indent=4)
                    
                    #Read file to encryp
                with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "rb")as f_read:
                    text = f_read.read()
                        
                encryp = fernet.encrypt(text)
                        
                        #write file encryp
                with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "wb")as w_file:
                    w_file.write(encryp)
                            
                    #Limpiando entrys
                    self.page.set("")
                    self.user.set("")
                    self.email.set("")
                    self.password.set("")
                
                #Cargando base de datos
                self.data_table()
            
    #Interface programm
    def interface(self):
        #Toolbar option
        self.menu()
        
        #Data
        self.data_table()
        
        
        #Dominio
        tk.Label(self.frm, text="Web page", font=("Space mono", 12), bg="#DADADA").grid(
            column=0, row=0, columnspan=2, sticky="we")
        tk.Entry(self.frm, relief="flat", font=("Space mono", 11), textvariable=self.page).grid(
            column=0, row=1, columnspan=2,sticky="we", padx=10)
        
        
        #User
        tk.Label(self.frm, text="User", font=("Space mono", 12), bg="#DADADA").grid(
            column=2, row=0, columnspan=2, sticky="we")
        tk.Entry(self.frm, font=("Space mono", 11), relief="flat", textvariable=self.user).grid(
            column=2, row=1, columnspan=2, sticky="we")
        
        #Email
        tk.Label(self.frm, text="Email", font=("Space mono", 12), bg="#DADADA").grid(
            column=4, row=0, columnspan=2, sticky="we")
        tk.Entry(self.frm, font=("Space mono", 11), relief="flat", textvariable=self.email).grid(
            column=4, row=1, columnspan=2, sticky="we", padx=10)
        
        #Password
        tk.Label(self.frm, text="Password", font=("Space mono",12), bg="#DADADA", relief="flat").grid(
            column=6, row=0, columnspan=2, sticky="we")
        self.p = tk.Entry(self.frm, font=("Space mono", 11), show="*", relief="flat", textvariable=self.password)
        self.p.grid(column=6, row=1, columnspan=2, sticky="we")
        
        #Charge image password
        self.on = PhotoImage(file="./image/ojo.png")
        self.off = PhotoImage(file="./image/invisible.png")
        
        #Ico show or hidden password
        self.ico = tk.Button(self.frm, relief="flat", cursor="hand2", bg="#DADADA", image=self.off, command=self.show_password)
        self.ico.grid(column=8, row=1)
        
        
        #Clear data camp
        tk.Button(self.frm, text="Clear", font=("Space mono", 11), relief="flat",command=self.clear).grid(
            column=4, row=2, pady=15, columnspan=2, sticky="we", padx=10)  
        
        #Save data
        tk.Button(self.frm, text="Save", cursor="hand2", font=("Space mono", 11), relief="flat",
                  command=self.create_tabele_data).grid(
            column=6, row=2, pady=15, columnspan=2, sticky="we")
        
        #Edit
        tk.Button(self.frm, text="Edit", font=("Space mono", 11), relief="flat", command=self.edit).grid(
            column=4, columnspan=2,row=4, sticky="we", pady=10, padx=10)
        
        #Delete
        tk.Button(self.frm, text="Delete", font=("Space mono", 11), relief="flat", command=self.delete).grid(
            column=6, columnspan=2, row=4, sticky="we", pady=10)
        
        #Refresh
        tk.Button(self.frm, text="Refresh", font=("Space mono", 11), relief="flat", command=self.data_table).grid(
            column=2, row=4, columnspan=2, sticky="we", padx=10)
        
        
        
        self.root.mainloop()
        
