import tkinter as tk
import Colours

### use this new top frame to handle RateSellers as done with the other classes
class RateSellers(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Rate Sellers Page")
            self.geometry("950x650")
            self.config(bg=Colours.col2)