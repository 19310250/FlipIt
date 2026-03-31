import tkinter as tk
import Colours

### use this new top frame to handle logout as done with the other classes
class Logout(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("logout Page")
        self.geometry("950x650")
        self.config(bg=Colours.col2)
