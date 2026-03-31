import tkinter as tk
import Colours

class ItemSearch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Search items")
        self.geometry("950x650")
        self.config(bg=Colours.col2)