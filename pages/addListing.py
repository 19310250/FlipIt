import tkinter as tk
from tkinter import PhotoImage, Toplevel, ttk
from typing import ReadOnly
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
        lblName.pack(anchor="nw", padx=20)
        txtName = tk.Text(self, height=1, wrap="none", background=colours.col2, foreground=colours.text)
        addPlaceholder(txtName, "What should people search for to find this item....")
        txtName.pack(anchor="nw", padx=20)

        lblPhoto = tk.Label(self, text= "Add photo:", background=colours.bg, foreground=colours.text)
        lblPhoto.pack(anchor="nw", padx= 20)
        
        frmPhotoUpload = tk.Frame(self, height=300, background=colours.col2)
        frmPhotoUpload.pack(fill=tk.X, padx=20,pady=20)
        self.imgPhotoIcon = PhotoImage(file="icons/photo-icon.png")
        lblUploadImg = tk.Label(frmPhotoUpload, image=self.imgPhotoIcon, background=colours.col2)
        lblUploadImg.pack(fill = "both", expand = True)
        lblAddPhoto = tk.Label(frmPhotoUpload, text="Click to add photos", foreground=colours.text, background=colours.col2)
        lblAddPhoto.pack(pady=20)

        lblDescription = tk.Label(self, text="Description:", background=colours.bg, foreground=colours.text)
        lblDescription.pack(anchor="nw", padx=20)
        txtDescription = tk.Text(self, height = 20, background=colours.bg, foreground=colours.text)
        addPlaceholder(txtDescription, "Write about what you are selling, what is included in the box, and any extra information...")
        txtDescription.pack(fill="x", padx=20)
        
        lblCondition = tk.Label(self, text="Condition:", background=colours.bg, foreground=colours.text)
        lblCondition.pack(anchor="nw", padx=20)
        conditions = [ "New", "Used - Like new", "Used - Very good", "Used - Good", "For parts or not working" ]
        cbConditions = ttk.Combobox(self, background=colours.bg, values=conditions, foreground= colours.text, state="readonly")
        cbConditions.set("Select a condition")
        cbConditions.pack(fill="x", padx=20)
        

        
        
