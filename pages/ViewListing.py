from tkinter import ttk
import tkinter as tk
from Colours import Colours

class ViewListing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=Colours.bg)
        
    def view(self, item):
        for widget in self.winfo_children():
            widget.destroy()
        lblName = tk.Label(self, text=item["name"])
        lblName.pack()
