import tkinter as tk
from tkinter import ttk, messagebox
from Colours import Colours
from PIL import Image, ImageTk

class SavedItems(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)

        # Title and the listbox to display saved items
        lblTitle = ttk.Label(self, text="Saved Items", background=Colours.bg, foreground=Colours.text, font=("Arial", 20))
        lblTitle.pack(pady=20)

        #Scrollable area
        container = tk.Frame(self, bg=Colours.bg)
        container.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(container, bg=Colours.bg)
        self.scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=Colours.bg)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.images = []  # Keep references to images
        
    def updateSavedItems(self):
        # Clear previous items
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.images.clear()  # Clear image references

        if not self.controller.saved_items:
            ttk.Label(self.scrollable_frame, text="No saved items yet.", background=Colours.bg, foreground=Colours.text).pack(pady=20)
            return
        for item in self.controller.saved_items:
            card = tk.Frame(
                self.scrollable_frame, 
                bg=Colours.col2, 
                bd=1, 
                relief="solid"
            )
            card.pack(pady=0, padx=0, fill="x")
            inner = tk.Frame(card, bg=Colours.col2)
            inner.pack(expand=True, fill="both")
            # Image
            image = Image.open(item["image"])
            image = image.resize((150, 150))
            photo = ImageTk.PhotoImage(image)
            self.images.append(photo) 

            img = tk.Label(
                inner,
                image=photo,
                bg=Colours.col3
            )
            img.pack(side="left", padx=10, pady=10)
            # Name and price
            info_frame = tk.Frame(inner, bg=Colours.col2)
            info_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            tk.Label(
                info_frame,
                text=item["name"],
                bg=Colours.col2,
                fg=Colours.text,
                font=("Arial", 12, "bold")
            ).pack(anchor="w")
            tk.Label(
                info_frame,
                text=item["price"],
                bg=Colours.col2,
                fg=Colours.col4,
                font=("Arial", 12)
            ).pack(anchor="w", pady=5)
            # Remove button
            tk.Button(
                info_frame,
                text="Remove",
                bg=Colours.col3,
                fg=Colours.text,
                command=lambda item=item: self.remove_item(item)
            ).pack(anchor="e", pady=5)
    def remove_item(self, item):
        if item in self.controller.saved_items:
            self.controller.saved_items.remove(item)
            messagebox.showinfo("Removed", f"{item['name']} removed from saved items!")
            self.updateSavedItems()