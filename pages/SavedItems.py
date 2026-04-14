import tkinter as tk
from tkinter import ttk, messagebox
from Colours import Colours

class SavedItems(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=Colours.bg)

        # Example content for the Saved Items page
        lblTitle = ttk.Label(self, text="Saved Items", background=Colours.bg, foreground=Colours.text, font=("Arial", 20))
        lblTitle.pack(pady=20)

        # This is where you would add the actual saved items content, such as a list or grid of items.
        # For demonstration, we'll just add a placeholder label.
        lblPlaceholder = ttk.Label(self, text="Your saved items will appear here.", background=Colours.bg, foreground=Colours.text, font=("Arial", 14))
        lblPlaceholder.pack(pady=10)