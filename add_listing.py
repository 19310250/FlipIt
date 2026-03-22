import tkinter as tk
from tkinter import ttk
class add_listing (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "listing")
        label.pack(fill=tk.BOTH)
