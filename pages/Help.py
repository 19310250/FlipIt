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
        help_text = ("""
        Welcome to the FlipIt Help Page!

        If you have any questions or need assistance, please feel free to contact us at:

        Phone number: +0123456789

        Email: TestEmail@flipit.com
        """
        )
        verstion_text = ("""
        Version 1.0.0
        
        For updates and more information contact us directly
        """)
        lblHelp = ttk.Label(self, text=help_text, wraplength=1400, background=Colours.bg, foreground=Colours.text, font=("Arial", 16))
        lblHelp.pack(pady=10)
        lblVersion = ttk.Label(self, text="Version", wraplength=1400, background=Colours.bg, foreground=Colours.text, font=("Arial", 20))
        lblVersion.pack(pady=10)
        lblDevelopers = ttk.Label(self, text=verstion_text, wraplength=1400, background=Colours.bg, foreground=Colours.text, font=("Arial", 16))
        lblDevelopers.pack(pady=10)