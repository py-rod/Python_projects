import os
from tkinter import PhotoImage
import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet
import json
from tkinter import messagebox
import subprocess
from new_user import New_User
from admin_manager import interface_window


user_pc  = os.getlogin()

def create_key():
    key = Fernet.generate_key()
    os.mkdir(f"C:\\Users\\{user_pc}\\Crypkey\\key")
    subprocess.call(f"attrib +h C:\\Users\\{user_pc}\\Crypkey\\key",shell=True)
    with open(f"C:\\Users\\{user_pc}\\Crypkey\\key\\filekey.key", "wb")as file:
        return file.write(key)

def load_key():
    return open(f"C:\\Users\\{user_pc}\\Crypkey\\key\\filekey.key", "rb").read()


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.resizable(False, False)
        self.frm = tk.Frame(self.root, bg="#DADADA", padx=10)
        self.frm.grid()
        self.user = tk.StringVar()
        self.password = tk.StringVar()
        self.menu_login()
        
        
    def logo(self):
        self.img = PhotoImage(file="./image/secure.png")
        tk.Label(self.frm, image=self.img, width=150, height=150, bg="#DADADA").grid(column=0, row=0, columnspan=4, sticky="we")
        
    
    def check_info(self):
        user = self.user.get()
        password = self.password.get()
        
        if len(user) == 0:
            messagebox.showinfo(message="User name is empty")
        elif len(password) == 0:
            messagebox.showinfo(message="Password is empty")
        else:
            key = load_key()
            fernet = Fernet(key)
            with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "rb")as file:
                text = file.read()
                decryp = fernet.decrypt(text)
                
                with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "wb")as new_file:
                    new_file.write(decryp)
                

                with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json")as read_json:
                    var1 = json.load(read_json)
                        
                for k, v in var1.items():
                    if user == v["User"]:
                        if user == v["User"] and password == v["Password1"]:
                            with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "rb")as readd:
                                text2 = readd.read()
                            new_encryp = fernet.encrypt(text2)
                            with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "wb")as ff:
                                ff.write(new_encryp)
                                self.root.destroy()
                                interface_window(k)
                        else:
                            messagebox.showerror(message="The user or password is incorrect")
                            with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "rb")as read_:
                                var2 = read_.read()
                            encryp = fernet.encrypt(var2)
                            with open(f"C:\\Users\\{user_pc}\\Crypkey\\data.json", "wb")as new_write:
                                new_write.write(encryp)
                                self.user.set("")
                                self.password.set("")

        
    def menu_login(self):
        #Charge logo 
        self.logo() 
        
        #Camp User
        tk.Label(self.frm, text="User:", font=("Space mono", 12), bg="#DADADA").grid(column=0, row=1, pady=10)
        tk.Entry(self.frm, font=("Space mono", 11), relief="flat", textvariable=self.user).grid(column=1, row=1, pady=10)
        
        #Camp password
        tk.Label(self.frm, text="Password:", font=("Space mono", 12), bg="#DADADA").grid(column=0, row=2, pady=6)
        tk.Entry(self.frm, font=("Space mono", 11), relief="flat", show="*", textvariable=self.password
                ).grid(column=1, row=2, pady=6)
        
        
        #Button login
        tk.Button(self.frm, text="Log in", font=("Space mono", 12), cursor="hand2", command=self.check_info
                  ).grid(column=0, row=3, columnspan=4, sticky="we", pady=15)
        
        #Separator
        ttk.Separator(self.frm, orient="horizontal").grid(column=0, row=4, columnspan=4, sticky="we", pady=10)
        
        #Creat new user
        tk.Button(self.frm, text="Long up", font=("Space mono", 12), cursor="hand2", command=New_User
                ).grid(column=0, row=5, columnspan=5, sticky="we", pady=6)
        
        
        self.root.mainloop()
        

if __name__ == '__main__':
    app = Window()