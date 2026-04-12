from tkinter import ttk
import tkinter as tk

from Colours import Colours
from pages import MainPage, AddListing, Login, Logout, ItemSearch, ExchangeMessage, Reviews, messages
class Header (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.col2)
        lblLogo = ttk.Label(self, text="FlipIt",background=Colours.col2, foreground=Colours.col4, font=("Arial", 25))
        lblLogo.pack(side="left")
    
    def ShowButtons(self):
        btn_frame = tk.Frame(self, bg=Colours.col2)
        btn_frame.pack(side="right", padx=10)
        #Search bar
        self.search = tk.Entry(self, font = ("Arial", 12), width=30)
        self.search.pack(side="left", padx=20)

        def open_home():
            print("Home")

        def open_orders():
            print("Orders")

        def open_returns():
            print("Returns")

        def open_account():
            print("Account")

        def open_messages():
            self.controller.showFrame(messages.MessagesPage)
        
        def open_items_search():
            self.controller.showFrame(ItemSearch.ItemSearch)

         # action to each nav page
        actions = {
            "Home": open_home,
            "Orders": open_orders,
            "Returns": open_returns,
            "Account": open_account,
            "Messages": open_messages
        }

        # create buttons and add command
        for text in actions:
            tk.Button(
                btn_frame,
                text=text,
                bg=Colours.col2,
                fg=Colours.text,
                command=actions[text]
            ).pack(side="left", padx=8)


        # MENU BUTTON
        menubutton = tk.Menubutton(
            btn_frame,
            text="Menu",
            bg=Colours.col2,
            fg=Colours.text,
            relief="raised"
        )
        menubutton.pack(side="left", padx=8)

        menu = tk.Menu(menubutton, tearoff=0)

        # Add menu items
        menu.add_command(label="Add Listing", command= lambda : self.controller.showFrame(AddListing.AddListing))
        menu.add_command(label="Message User", command= lambda : self.controller.showFrame(messages.MessagesPage))
        menu.add_command(label="Rate Sellers", command= lambda : self.controller.showFrame(Reviews.Reviews))
        menu.add_separator()
        menu.add_command(label="Logout", command= lambda : self.controller.showFrame(Logout.Logout))

        # Attach menu to button
        menubutton.config(menu=menu)

        
        

