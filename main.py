from tkinter import ttk
import tkinter as tk

from Colours import Colours
from pages.MainPage import MainPage
from pages.AddListing import AddListing
from pages.ItemSearch import ItemSearch
from pages.ExchangeMessage import ExchangeMessage
from pages.RateSellers import RateSellers
from pages.Login import Login
from pages.Logout import Logout

'''
This is the main class, it prepairs the window and the ability to switch between different frames. Each page will be put in a different frame.
'''
class FlipITPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # App layout
        self.geometry("1600x1200")
        self.resizable(False, False)
        self.config(background=Colours.bg)

        mainFrame = tk.Frame(self)
        mainFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Header
        self.header = tk.Frame(self, bg=Colours.bg)
        self.header.place (relx= 0, rely=0, relwidth=1, relheight=0.05)

        lblLogo = ttk.Label(self.header, text="FlipIt",background=Colours.bg, foreground=Colours.col4, font=("Arial", 25))
        lblLogo.pack(side="left")

        btn_frame = tk.Frame(self.header, bg=Colours.col1)
        btn_frame.pack(side="right", padx=10)

        for text in ["Home", "Orders", "Returns", "Account"]:
            tk.Button(
                btn_frame,
                text=text,
                bg=Colours.col2,
                fg=Colours.text
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
        menu.add_command(label="Add Listing", command= lambda : self.showFrame(AddListing))
        menu.add_command(label="Search Item", command= lambda : self.showFrame(ItemSearch))
        menu.add_command(label="Message User", command= lambda : self.showFrame(ExchangeMessage))
        menu.add_command(label="Rate Sellers", command= lambda : self.showFrame(RateSellers))
        menu.add_separator()
        menu.add_command(label="Logout", command= lambda : Logout)

        # Attach menu to button
        menubutton.config(menu=menu)

        # Add all pages to a list which can then be switched between
        self.frames = {}
        for F in (MainPage, AddListing, Login): 
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0.05, relwidth=1, relheight=0.95)

        self.showFrame(Login)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.title("FlipIt.co.uk/" + frame.__class__.__name__)

'''
Each page is stored in it's own class file. To create a new page copy the first 3 lines of one of the classes and rename it, then add the new name to the for loop in the main class to add it to the list of pages, and import it at the top.
Then add items to it like you usually would in tkinter.
'''
        
if __name__ == "__main__":
    root = FlipITPage()
    
    root.mainloop()
