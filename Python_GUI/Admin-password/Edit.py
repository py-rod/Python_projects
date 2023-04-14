import os
from tkinter import PhotoImage
import tkinter as tk
from cryptography.fernet import Fernet
import json
from tkinter import messagebox

user_pc = os.getlogin()


class edit_data:
    def __init__(self, ide ,id_key, id_page, id_user, id_email, id_password):
        self.ide = ide
        self.id_key = id_key
        self.id_page = id_page
        self.id_user = id_user
        self.id_email = id_email
        self.id_password = id_password
                    
        self.page2 = tk.StringVar()
        self.user2 = tk.StringVar()
        self.email2 = tk.StringVar()
        self.password2 = tk.StringVar()
        self.edit_interface()
                    
    def information(self):
            
        self.page2.set(self.id_page)
        self.user2.set(self.id_user)
        self.email2.set(self.id_email)
        self.password2.set(self.id_password)
        
    def load_key(self):
        with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\key\\filekey.key", "rb")as file:
            return file.read()
        
    def save(self):
        page2 = self.page2.get()
        user2 = self.user2.get()
        email2 = self.email2.get()
        password2 = self.password2.get()
        
        if  len(page2) == 0:
            messagebox.showinfo(message="Empty web page")
        elif len(email2) == 0:
            messagebox.showerror(message="Empty email")
        elif len(password2) == 0:
            messagebox.showinfo(message="Empty password")
        else:
            key = self.load_key()
            fernet = Fernet(key)
            
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "rb")as file:
                text = file.read()
                
            decry = fernet.decrypt(text)
            
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "wb")as file2:
                file2.write(decry)
                
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json")as file3:
                var1 = json.load(file3)
                
            var1[self.id_key] = {"Page": page2,
                                 "User": user2,
                                 "Email": email2,
                                 "Password": password2}
            
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "w")as file4:
                json.dump(var1, file4, indent=4)
            
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "rb")as file5:
                text2 = file5.read()
                
            encryp = fernet.encrypt(text2)
            
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\{self.ide}\\data.json", "wb")as file6:
                file6.write(encryp)
            
            
            self.root.destroy()

                
            
        
                    
    def edit_interface(self):
        self.information()
        self.root = tk.Toplevel(padx=10, pady=10)
        self.root.resizable(False, False)
            
                    
        #Page
        tk.Label(self.root, text="Web page", font=("Space mono", 11)).grid(column=0, row=0)
        tk.Entry(self.root, textvariable=self.page2, font=("Space mono", 10)).grid(column=1, row=0, columnspan=4, sticky="we")
                        
        #User
        tk.Label(self.root, text="User", font=("Space mono", 11)).grid(column=0, row=1)
        tk.Entry(self.root, textvariable=self.user2, font=("Space mono", 10)).grid(column=1, row=1, columnspan=4, sticky="we")
                        
        #Email
        tk.Label(self.root, text="Email", font=("Space mono", 11)).grid(column=0, row=2)
        tk.Entry(self.root, textvariable=self.email2, font=("Space mono", 10)).grid(column=1, row=2, columnspan=4, sticky="we")
                        
        #Password
        tk.Label(self.root, text="Password", font=("Space mono", 11)).grid(column=0, row=3)
        tk.Entry(self.root, textvariable=self.password2, font=("Space mono", 10)).grid(column=1, row=3, columnspan=4, sticky="we")
                        
        #Cancel
        tk.Button(self.root, text="Cancel", font=("Space mono", 10), command=self.root.destroy).grid(column=0, row=4, columnspan=2, sticky="we", padx=5)
                    
                        
        #Save
        tk.Button(self.root, text="Save", font=("Space mono", 10), command=self.save).grid(column=2, row=4, columnspan=3, sticky="we", padx=5)
                        
                    
        self.root.grab_set()