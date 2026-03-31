from tkinter import ttk
import tkinter as tk
from Colours import Colours
 
# based on https://runebook.dev/en/docs/python/library/dialog, slightly jank but seems to work
class Login (tk.Frame):
    def __init__(self, parent, controller):
        self.top = tk.Toplevel(parent)
        self.top.title("Login")
        
        #TODO Add login boxes and buttons that call the login functions
        btnLogin = ttk.Button(self.top, text="Login", command=self.on_login)
        btnLogin.pack()

        # Locks the background window until the user has logged in
        self.top.transient(parent)
        self.top.grab_set()
        parent.wait_window(self.top)

    def on_login(self):
        #todo return data
        self.top.destroy()
