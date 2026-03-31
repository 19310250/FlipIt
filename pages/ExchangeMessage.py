import tkinter as tk
import Colours

### use this new top frame to handle ExchangeMessage as done with the other classes
class ExchangeMessage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("exchange message")
        self.geometry("950x650")
        self.config(bg=Colours.col2)