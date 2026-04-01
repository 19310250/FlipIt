from tkinter import ttk
import tkinter as tk
from Colours import Colours
import pages.MainPage

class Login (tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)
        btnLogin = ttk.Button(self, text="Login", command=self.on_login)
        btnLogin.pack()
        
    def on_login(self):
        self.controller.user = "username";
        self.controller.showFrame(pages.MainPage.MainPage)
