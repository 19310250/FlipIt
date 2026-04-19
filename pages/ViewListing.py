from PIL import Image, ImageTk
import tkinter as tk
from Colours import Colours
from pages import Reviews

class ViewListing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)
        
        
    def view(self, item):
        self.item = item
        for widget in self.winfo_children():
            widget.destroy()
        sidebar = tk.Frame(self, background=Colours.bg)

        sidebarWidth= 0.2
        sidebar.place(relx=0, rely=0, relwidth=sidebarWidth, relheight=1)

        body = tk.Frame(self, background=Colours.bg)
        body.place(relx=sidebarWidth, rely=0, relwidth=1-sidebarWidth, relheight=1)

        # Body
        lblName = tk.Label(body, text=item["name"], bg=Colours.bg, fg=Colours.text, font=("Arial", 20, "bold"),)
        lblName.pack(anchor='nw')
        lblCondition = tk.Label(body, text="Condition - New", bg=Colours.bg, fg=Colours.text)
        lblCondition.pack(anchor='nw')
        lblPrice = tk.Label(body, text=item["price"], bg=Colours.bg, fg=Colours.col3)
        lblPrice.pack(anchor='nw')
        lblDesc = tk.Label(body, text=item["desc"], bg=Colours.bg, fg=Colours.text)
        lblDesc.pack(anchor='nw')

        btnSaveItem = tk.Button(body, text="Save Item", background=Colours.col3, command=self.buttonSaveItem)
        btnSaveItem.pack(anchor='nw')
        btnTradeItem = tk.Button(body, text="Trade Item", background=Colours.col3, command=self.buttonTradeItem)
        btnTradeItem.pack(anchor='ne')

        # Sidebar
        self.image = Image.open(item["image"])
        ratio = self.image.size[1] / self.image.size[0]

        self.image = self.image.resize((240, (int)(240 * ratio)))
        self.photo = ImageTk.PhotoImage(self.image)

        lblImage = tk.Label(sidebar, image=self.photo, bg=Colours.bg)
        lblImage.pack(fill="x", padx=5, pady=5, anchor='nw')

        frmSeller = tk.Frame(sidebar, bg=Colours.bg)
        frmSeller.pack(anchor='nw', padx=5, pady=5)
        lblSeller = tk.Label(frmSeller, text="Dave1",bg=Colours.bg, fg=Colours.text)
        lblSeller.grid(column=0, row=0)

        self.imgStarIcon = tk.PhotoImage(file="icons/starS.png")
        for i in range(0, 5):
           tk.Label(frmSeller, image=self.imgStarIcon, background=Colours.bg).grid(row=0, column=i+1)

        lblLocation = tk.Label(sidebar, text="Located - 10 Downing Street, London SW1A 2AA", bg=Colours.bg, fg=Colours.text)
        lblLocation.pack(anchor='nw', padx=5, pady=5)
        btnReadReviews = tk.Button(sidebar, text="Read Reviews", bg=Colours.col3, fg=Colours.text, command=lambda: self.controller.showFrame(Reviews.Reviews))
        btnReadReviews.pack(anchor='nw', padx=5, pady=5)
        
    def buttonSaveItem(self):
        if self.item not in self.controller.saved_items:
            self.controller.saved_items.append(self.item)
            tk.messagebox.showinfo("Saved", f"{self.item['name']} added to saved items!")
        else:
            tk.messagebox.showwarning("Not Saved", f"{self.item['name']} is already in saved items!")

    def buttonTradeItem(self):
        print("trade")
    
