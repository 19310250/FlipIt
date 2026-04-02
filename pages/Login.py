from tkinter import ttk
import tkinter as tk
from Colours import Colours
from pages import MainPage
from Header import Header

class Login (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)
        btnLogin = ttk.Button(self, text="Login", command=self.on_login)
        btnLogin.pack()
        
    def on_login(self):
        self.controller.username = "username"; # Sets the variable user in the main program for use in other pages
        self.controller.showFrame(MainPage.MainPage)
        Header.ShowButtons(self.controller.header)
