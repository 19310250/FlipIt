import tkinter as tk
from tkinter import ttk

from colours import colours
from pages.addListing import addListing

class home (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=colours.bg)
        
        # Placeholder example, can and should be replaced
        label = tk.Label(self, text= "home")
        label.pack(fill=tk.BOTH)
        button1 = ttk.Button(self, text = "add listing", command = lambda : controller.showFrame(addListing))
        button1.pack()
