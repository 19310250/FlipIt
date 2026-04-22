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
        lblTitle = ttk.Label(self, text="About Us", foreground=Colours.text, font=("Arial", 20))
        lblTitle.pack(pady=20)

        # About us content
        about_text = ("""
        FlipIt is a website designed to help users who are looking to exchange their unwanted items 
        for something they would like to have. 

        We aim to create a community where people can easily 
        swap items without the need for money. 

        This way we can promote sustainability and reduce waste 
        by giving items a second life.

        Our vision is to allow people to easily exchange items they no longer need for something they want, 
        promoting a sense of community and sustainability.
        """
        )
        developer_text = ("""
        This website was developed by a team of 5 students from Oxford Brookes:

        Tim Blokhin, Theo Topham, Soully Traore, Ayman Abdel Hamid, Joey Mulligan.
        """
        )
        lblAbout = ttk.Label(self, text=about_text, wraplength=1400, background=Colours.bg, foreground=Colours.text, font=("Arial", 16))
        lblAbout.pack(pady=10)
        lblAbout2 = ttk.Label(self, text="Our Team", wraplength=1400, background=Colours.bg, foreground=Colours.text, font=("Arial", 20))
        lblAbout2.pack(pady=10)
        lblDevelopers = ttk.Label(self, text=developer_text, wraplength=1400, background=Colours.bg, foreground=Colours.text, font=("Arial", 16))
        lblDevelopers.pack(pady=10)