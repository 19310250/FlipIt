import tkinter as tk
from tkinter import Toplevel, ttk
from colours import colours

class addListing (tk.Frame):
    def __init__(self, parent, controller):
        def addPlaceholder(entry, text):
            def boxClick(_):
                if entry.get(1.0, "end-1c") == text:
                    entry.delete(1.0, tk.END)
                    entry.config(fg=colours.text)

            def boxFocusLost(_):
                if not entry.get(1.0, "end-1c"):
                    entry.insert(1.0, text)
                    entry.config(fg="grey")

            entry.insert(1.0, text)
            entry.config(fg="grey")
            entry.bind("<Button-1>", boxClick)
            entry.bind("<Leave>", boxFocusLost)
            
        tk.Frame.__init__(self, parent)
        self.config(bg=colours.bg)
        lblName = tk.Label(self, text= "Item name:", background=colours.bg, foreground=colours.text)
        lblName.pack(anchor="nw")
        txtName = tk.Text(self, height=1, wrap="none", background=colours.col2, foreground=colours.text)
        addPlaceholder(txtName, "What should people search for to find this item....")
        txtName.pack(anchor="nw")

        lblPhoto = tk.Label(self, text= "Add photo:", background=colours.bg, foreground=colours.text)
        lblPhoto.pack(anchor="nw")
        
