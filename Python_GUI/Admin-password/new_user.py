import os
from tkinter import PhotoImage
import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet
import random
import json
from tkinter import messagebox
import subprocess

user_pc = os.getlogin()

def create_key():
    key = Fernet.generate_key()
    os.mkdir(f"C:\\Users\\{user_pc}\\Crypkey\\key")
    subprocess.call(f"attrib +h C:\\Users\\{user_pc}\\Crypkey\\key",shell=True)
    with open(f"C:\\Users\\{user_pc}\\Crypkey\\key\\filekey.key", "wb")as file:
        return file.write(key)

def load_key():
    return open(f"C:\\Users\\{user_pc}\\Crypkey\\key\\filekey.key", "rb").read()


class New_User:
    def __init__(self):
        self.data = {}
        self.user = tk.StringVar()
        self.email = tk.StringVar()
        self.password1 = tk.StringVar()
        self.register()
    
    
    
    #Gui register
    def register(self):
        self.root = tk.Toplevel(bg="#DADADA", padx=10, pady=10)
        self.root.resizable(False, False)
        self.root.focus_set()
        
        #Email
        tk.Label(self.root, text="Email:", font=("Space mono", 12), bg="#DADADA").grid(column=0,row=0)
        tk.Entry(self.root, font=("Space mono", 11), relief= "flat", textvariable=self.email).grid(column=1, row=0)
        
        #User
        tk.Label(self.root, text="User:", font=("Space mono", 12), bg="#DADADA").grid(column=0, row=1, pady=7)
        tk.Entry(self.root, font=("Space mono", 11), relief="flat", textvariable=self.user).grid(column=1, row=1, pady=7)
        
        #Password
        tk.Label(self.root, text="Password:", font=("Space mono", 12), bg="#DADADA").grid(column=0, row=2)
        tk.Entry(self.root, font=("Space mono", 11), relief="flat", show="*", textvariable=self.password1).grid(column=1, row=2)

        
        #Button
        tk.Button(self.root, text="Create new user", cursor="hand2", font=("Space mono", 12),
                command=self.obtain_data).grid(column=0, row=3, columnspan=4, sticky="we", pady=7)
        
        self.root.grab_set()
        
        
        #Creat id folder and user
    def __ID(self):
        low = "qwertyuiopasdfghjklzxcvbnm"
        number = "1234567890"
        all = low.upper() + low + number
        user_id = "".join(random.sample(all, 15))
        return user_id
    
    
    #Obtain data user
    def obtain_data(self):
        user = self.user.get()
        email = self.email.get()
        password1 = self.password1.get()
        ide = self.__ID()
        
        if len(email) == 0:
            messagebox.showinfo(message="Email empty")
        elif len(user) == 0:
            messagebox.showinfo(message="User name empty")
        elif len(password1) == 0:
            messagebox.showinfo(message="Password empty")
        else:
            #Check exist path
            veri = os.path.exists(f"C:\\Users\\{user_pc}\\Crypkey")
            if veri:
                #Create user if exist data base
                key = load_key()
                fernet = Fernet(key)
                
                #Read data for to decrypt
                with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "rb")as file:
                    read_data = file.read()
                    
                    decry = fernet.decrypt(read_data)
                    
                    #Write data decrypt in data.json
                    with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "wb")as write_fil:
                        write_fil.write(decry)
                    
                    #Prepared data to add to data base
                    with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json")as read:
                        var1 = json.load(read)
                        var1[ide] = {"Email": email,
                                    "User": user,
                                    "Password1": password1}
                        
                        #Create folder with user id for each one
                        os.mkdir(f"C:\\Users\\{user_pc}\\Crypkey\\{ide}")
                        
                        #Add data to data.json
                        with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "w")as new_file:
                            json.dump(var1, new_file,indent=4)
                            
                        #Prepared to encrypt
                        with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "rb")as N:
                            var2 = N.read()
                        
                        new_encryp  = fernet.encrypt(var2)
                        
                        #Write encrypt
                        with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "wb")as encry:
                            encry.write(new_encryp)
                            
                            self.root.destroy()
            else:
                
                #Create firts user in app 
                os.mkdir(f"C:\\Users\\{user_pc}\\Crypkey")
                self.data.setdefault(ide, {"Email": email,
                                           "User": user,
                                           "Password1": password1})
                with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "w") as file:
                    json.dump(self.data,file, indent=4)
                    
                    #Create folder
                    os.mkdir(f"C:\\Users\\{user_pc}\\Crypkey\\{ide}")
                    
                #Create key to encrypt files
                create_key()
                
                #Load key
                key = load_key()
                fernet = Fernet(key)
        
                with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "rb")as file:
                    text = file.read()
                
                    encryp = fernet.encrypt(text)
                
                    with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "wb")as file_write:
                        file_write.write(encryp)
                        
                        self.root.destroy()
