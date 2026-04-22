from tkinter import ttk
import tkinter as tk

from Colours import Colours
from pages import (MainPage, AddListing, Login, Logout, AboutUs, Help,
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

    def update_suggestions(self, event=None):
        search_item = self.search.get().strip().lower()
        self.suggestions.delete(0, tk.END)
        self.search_result = []
        # if search box is empty, hide the suggestions listbox
        if search_item == "":
            self.suggestions.place_forget()
            return

        for item in self.controller.items:
            if search_item in item["name"].lower():
                self.search_result.append(item)
        # if no results, hide the suggestions listbox
        if not self.search_result:
            self.suggestions.place_forget()
            return

        for item in self.search_result[:10]:
            self.suggestions.insert(tk.END, item["name"])
        self.update_idletasks()  # Ensure the search entry is updated before calculating positions
        x = self.search.winfo_rootx() - self.winfo_rootx()
        y = (self.search.winfo_rooty() - self.winfo_rooty()) + self.search.winfo_height()
        # Place the suggestions listbox directly below the search entry
        self.suggestions.place(
            x=x,
            y=y,
            width=self.search.winfo_width()
        )
        self.suggestions.lift()

    def ShowButtons(self):
        btn_frame = tk.Frame(self, bg=Colours.col2)
        btn_frame.pack(side="right", padx=10)

        # search bar
        search_frame = tk.Frame(self, bg=Colours.col2)
        search_frame.pack(side="left", fill="x", expand=True, padx=20)
        self.search = tk.Entry(search_frame, font=("Arial", 12), width=30)
        self.search.pack(fill="x", expand=True)
        self.suggestions=tk.Listbox(self, font=("Arial", 12), height=6)
        self.suggestions.place_forget()
        self.search.bind("<KeyRelease>", self.update_suggestions)

        def open_home():
            self.controller.showFrame(MainPage.MainPage)

        def open_orders():
            self.controller.showFrame(FetchingOverviewInfo.FetchingOverviewInfo)

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

        # action to each nav page
        actions = {
            "Home": open_home,
            "Orders": open_orders,
            "Account": open_account,
            "Messages": open_messages
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
        menu.add_command(label="Return item", command=lambda: self.controller.showFrame(ReturnItem.ReturnItem))
        menu.add_command(label="Bought item overview", command=lambda: self.controller.showFrame(FetchingOverviewInfo.FetchingOverviewInfo))
        menu.add_command(label="Verify listed item", command=lambda: self.controller.showFrame(ItemsVerification.ItemsVerification))
        menu.add_command(label="Saved Items", command=lambda: self.controller.showFrame(SavedItems.SavedItems))
        menu.add_command(label="About Us", command=lambda: self.controller.showFrame(AboutUs.AboutUs))
        menu.add_command(label="Help", command=lambda: self.controller.showFrame(Help.Help))
        menu.add_separator()
        menu.add_command(label="Logout", command=lambda: self.controller.showFrame(Logout.Logout))
        menubutton.config(menu=menu)
