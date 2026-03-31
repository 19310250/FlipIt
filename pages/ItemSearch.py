import tkinter as tk
from tkinter import ttk
from Colours import Colours

class ItemSearch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=Colours.bg)
