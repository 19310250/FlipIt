#!/usr/bin/env python3
from tkinter import ttk
import tkinter as tk

from Colours import Colours
from pages import MainPage, AddListing, Login, Logout, ItemSearch, ExchangeMessage, Reviews
from Header import Header

'''
This is the main class, it prepairs the window and the ability to switch between different frames. Each page will be put in a different frame.
'''
class FlipITPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # App layout
        self.geometry("1570x700")
        self.resizable(False, False)
        self.config(background=Colours.bg)

        mainFrame = tk.Frame(self)
        mainFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Header
        self.header = Header(self, self)
        self.header.place (relx= 0, rely=0, relwidth=1, relheight=0.05)

        # Add all pages to a list which can then be switched between
        self.frames = {}
        for F in (MainPage.MainPage,
                  AddListing.AddListing,
                  Login.Login,
                  ItemSearch.ItemSearch,
                  Reviews.Reviews,
                  ExchangeMessage.ExchangeMessage): 
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0.05, relwidth=1, relheight=0.95)

        self.showFrame(Login.Login)

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
