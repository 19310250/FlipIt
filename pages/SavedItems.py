import tkinter as tk
from tkinter import ttk, messagebox
from Colours import Colours

class SavedItems(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)

        # Title and the listbox to display saved items
        lblTitle = ttk.Label(self, text="Saved Items", background=Colours.bg, foreground=Colours.text, font=("Arial", 20))
        lblTitle.pack(pady=20)
        self.listbox = tk.Listbox(self, font = ("Arial", 14), width=50, height=20)
        self.listbox.pack(pady=10)

    #Refresh the listbox with the current saved items
    def updateSavedItems(self):
        self.listbox.delete(0, tk.END)  # Clear existing items
        for item in self.controller.saved_items:
            self.listbox.insert(tk.END, item)
        if not self.controller.saved_items:
            self.listbox.insert(tk.END, "No saved items yet.")
