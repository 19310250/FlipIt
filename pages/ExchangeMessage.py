import tkinter as tk
from tkinter import ttk
from Colours import Colours

### use this new top frame to handle ExchangeMessage as done with the other classes
class ExchangeMessage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=Colours.bg)
