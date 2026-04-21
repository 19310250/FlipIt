import tkinter as tk
from tkinter import ttk, messagebox
from Colours import Colours
from PIL import Image, ImageTk

class AboutUs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)

        # Title
        lblTitle = ttk.Label(self, text="About Us", background=Colours.bg, foreground=Colours.text, font=("Arial", 20))
        lblTitle.pack(pady=20)

        # About us content
        about_text = ("dsadas"
        )
        lblAbout = ttk.Label(self, text=about_text, wraplength=600, background=Colours.bg, foreground=Colours.text, font=("Arial", 12))
        lblAbout.pack(pady=10)