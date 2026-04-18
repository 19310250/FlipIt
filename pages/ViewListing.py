from PIL import Image, ImageTk
import tkinter as tk
from Colours import Colours

class ViewListing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=Colours.bg)
        
        
    def view(self, item):
        for widget in self.winfo_children():
            widget.destroy()
        sidebar = tk.Frame(self, background=Colours.bg)

        sidebarWidth= 0.2
        sidebar.place(relx=0, rely=0, relwidth=sidebarWidth, relheight=1)

        body = tk.Frame(self, background=Colours.bg)
        body.place(relx=sidebarWidth, rely=0, relwidth=1-sidebarWidth, relheight=1)

        # Body
        lblName = tk.Label(body, text=item["name"], bg=Colours.bg, fg=Colours.text)
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
        lblImage.pack(fill="x", expand=True, padx=5, pady=5, anchor='n')

        frmSeller = tk.Frame(sidebar, bg=Colours.bg)
        frmSeller.pack(anchor='n')
        lblSeller = tk.Label(frmSeller, bg=Colours.bg, fg=Colours.text)
        lblSeller.grid(column=0, row=0)

        self.imgStarIcon = tk.PhotoImage(file="icons/starS.png")
        for i in range(0, 5):
           tk.Label(frmSeller, image=self.imgStarIcon, background=Colours.bg).grid(row=0, column=i+1)
        
    def buttonSaveItem(self):
        print("save")
    def buttonTradeItem(self):
        print("trade")
