import tkinter as tk
from tkinter import ttk, messagebox
from Colours import Colours
from PIL import Image, ImageTk

class Help(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)

        # Title
        lblTitle = ttk.Label(self, text="Help", background=Colours.bg, foreground=Colours.text, font=("Arial", 20))
        lblTitle.pack(pady=20)

        # Help content
        help_text = ("dsadas"
        )
        lblAbout = ttk.Label(self, text=help_text, wraplength=600, background=Colours.bg, foreground=Colours.text, font=("Arial", 12))
        lblAbout.pack(pady=10)