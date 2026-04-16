import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox

from Colours import Colours

from pages import ViewListing

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.config(bg=Colours.bg)

        self.items = controller.items

        # SCROLLABLE AREA
        container = tk.Frame(self, bg=Colours.bg)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg=Colours.bg, highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

        scrollable_frame = tk.Frame(canvas, bg=Colours.bg)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        rows, cols = 3, 10
        # GRID CONFIG
        for c in range(cols):
            scrollable_frame.grid_columnconfigure(c, weight=1)

        for r in range(rows):
            scrollable_frame.grid_rowconfigure(r, weight=1)

        # CREATE CARDS
        self.images = []  # store images

        for index, item in enumerate(self.items):
            r = index // cols
            c = index % cols

            card = tk.Frame(
                scrollable_frame,
                bg=Colours.col2,
                bd=1,
                relief="solid"
            )
            card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")

            inner = tk.Frame(card, bg=Colours.col2)
            inner.pack(expand=True, fill="both")


            image = Image.open(item["image"])


            image = image.resize((120, 100))
            photo = ImageTk.PhotoImage(image)

            # store image reference
            self.images.append(photo)

            img = tk.Label(
                inner,
                image=photo,
                bg=Colours.col3
            )
            img.pack(fill="both", expand=True, padx=5, pady=5)

            # Name
            tk.Label(
                inner,
                text=item["name"],
                bg=Colours.col2,
                fg=Colours.text,
                font=("Arial", 8, "bold"),
                wraplength=120,
                justify="center"
            ).pack(pady=2)

            # Price
            tk.Label(
                inner,
                text=item["price"],
                bg=Colours.col2,
                fg=Colours.col4,
                font=("Arial", 8)
            ).pack()

            # Buttons
            button_frame = tk.Frame(inner, bg=Colours.col2)
            button_frame.pack(pady=5)
            #View button
            tk.Button(
                button_frame,
                text="View",
                bg=Colours.col3,
                fg=Colours.text,
                command = lambda item=item: self.viewItem(item)
            ).pack(side="left", padx=5)

            #Save button
            tk.Button(
                button_frame,
                text="Save",
                bg=Colours.col3,
                fg=Colours.text,
                command = lambda item=item: self.save_item(item)
            ).pack(side="right", padx=5)

    #Function to save item to saved items list
    def save_item(self, item):
        if item not in self.controller.saved_items:
            self.controller.saved_items.append(item)
            messagebox.showinfo("Saved", f"{item['name']} added to saved items!")
        else:
            messagebox.showwarning("Not Saved", f"{item['name']} is already in saved items!")
            
    def viewItem(self, item):
        frame = self.controller.frames[ViewListing.ViewListing]
        ViewListing.ViewListing.view(frame, item)
        self.controller.showFrame(ViewListing.ViewListing)
