import tkinter as tk
import Colours

class ItemSearch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=Colours.bg)
