from tkinter import ttk
import tkinter as tk

from Colours import Colours
from pages import (MainPage, AddListing, Login, Logout, ItemSearch,
ExchangeMessage, Reviews, messages, ReturnItem, FetchingOverviewInfo, ItemsVerification, DeleteAccount, SavedItems)


class Header(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.col2)
        lblLogo = ttk.Label(self, text="FlipIt", background=Colours.col2, foreground=Colours.col4, font=("Arial", 25))
        lblLogo.pack(side="left")

    def HideButtons(self):
        # destroy all header widgets except the logo
        for widget in self.winfo_children():
            if not isinstance(widget, ttk.Label):
                widget.destroy()

    def ShowButtons(self):
        btn_frame = tk.Frame(self, bg=Colours.col2)
        btn_frame.pack(side="right", padx=10)

        # search bar
        self.search = tk.Entry(self, font=("Arial", 12), width=30)
        self.search.pack(side="left", padx=20)

        def open_home():
            self.controller.showFrame(MainPage.MainPage)

        def open_orders():
            self.controller.showFrame(FetchingOverviewInfo.FetchingOverviewInfo)

        def open_saved_items():
            self.controller.showFrame(SavedItems.SavedItems)

        def open_account():
            accountMenuButton = tk.Menubutton(
                btn_frame,
                text="Account",
                bg=Colours.col2,
                fg=Colours.text,
                relief="raised"
            )
            accountMenuButton.pack(side="left", padx=8)
            accountMenu = tk.Menu(accountMenuButton, tearoff=0)
            accountMenu.add_command(label="Delete Account", command=lambda: self.controller.showFrame(DeleteAccount.DeleteAccount))
            accountMenuButton.config(menu=accountMenu)

        def open_messages():
            self.controller.showFrame(messages.MessagesPage)

        def open_items_search():
            self.controller.showFrame(ItemSearch.ItemSearch)

        # action to each nav page
        actions = {
            "Home": open_home,
            "Orders": open_orders,
            "Account": open_account,
            "Messages": open_messages,
            "Saved Items": open_saved_items,
        }

        # create buttons and add command
        for text in actions:
            if text == "Account":
                actions[text]()
                continue
            tk.Button(
                btn_frame,
                text=text,
                bg=Colours.col2,
                fg=Colours.text,
                command=actions[text]
            ).pack(side="left", padx=8)

        # menu button
        menubutton = tk.Menubutton(
            btn_frame,
            text="Menu",
            bg=Colours.col2,
            fg=Colours.text,
            relief="raised"
        )
        menubutton.pack(side="left", padx=8)

        menu = tk.Menu(menubutton, tearoff=0)
        menu.add_command(label="Add Listing", command=lambda: self.controller.showFrame(AddListing.AddListing))
        menu.add_command(label="Message User", command=lambda: self.controller.showFrame(messages.MessagesPage))
        menu.add_command(label="Rate Sellers", command=lambda: self.controller.showFrame(Reviews.Reviews))
        menu.add_command(label="Return item", command=lambda: self.controller.showFrame(ReturnItem.ReturnItem))
        menu.add_command(label="Bought item overview", command=lambda: self.controller.showFrame(FetchingOverviewInfo.FetchingOverviewInfo))
        menu.add_command(label="verify listed item", command=lambda: self.controller.showFrame(ItemsVerification.ItemsVerification))
        menu.add_separator()
        menu.add_command(label="Logout", command=lambda: self.controller.showFrame(Logout.Logout))
        menubutton.config(menu=menu)