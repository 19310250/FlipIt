#!/usr/bin/env python3
from tkinter import ttk
import tkinter as tk

from Colours import Colours
from pages import (MainPage, AddListing, Login, Logout, AboutUs, Help, ExchangeMessage,
Reviews, ViewListing, messages, ReturnItem, FetchingOverviewInfo, ItemsVerification, DeleteAccount, SavedItems, Register)

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

        #Saved Items database
        self.saved_items = []

        #item names
        item_names = ["air fryer", "chromebook c434", "IKEA's HAMMARN", "iphone 17", "macbook pro", "jbl tour pro", "Monitor XDR",
                      "ryzen pc", "HP envy 123", "Hamlet by WS", "CGP combined science", "carrera bike", "kids scince kits",
                      "exercise book", "exam kits pack", "van rysel helmet", "reading glass", "casio calculator", "jade suitcase",
                      "highbury backpack ", "sony WH-1000XM6", "american freezer", "cost road bed", "office cupboard",
                      "revision desk", "Nvidia rtx 4060", "bundle jeans", "lord of the rink", "nba basketball", "anko toaster" ,
                      ]

        items_path = ["imgs/img/airfryer.gif", "imgs/img/chromebookflip.png", "imgs/img/hammarn.png",
                      "imgs/img/iphone17.png", "imgs/img/macbookpro.png", "imgs/img/jbltourpro.png",
                      "imgs/img/monitorxdr.png",
                      "imgs/img/ryzenpc.png", "imgs/img/hpenvy123.png", "imgs/img/hamletws.png",
                      "imgs/img/cgpscience.png", "imgs/img/carrerabike.png", "imgs/img/kidsscience.png",
                      "imgs/img/exercisebook.png",
                      "imgs/img/examkitpack.png", "imgs/img/halfordhelmet.png", "imgs/img/readingglass.png",
                      "imgs/img/casiocalculator.png", "imgs/img/jadedesignsuitcase.png",
                      "imgs/img/highburyback.png", "imgs/img/sonyheadphone.png", "imgs/img/americanfreezer.png",
                      "imgs/img/costbed.png", "imgs/img/officecupboard.png", "imgs/img/revisiondesk.png",
                      "imgs/img/nvidiartx.png", "imgs/img/bundlejeans.png", "imgs/img/booklordring.png",
                      "imgs/img/basketballnba.png", "imgs/img/ankotoaster.png",

                      ]

        seller_names = ["Seller 1", "Seller 2", "Seller 3", "Seller 4", "Seller 5", "Seller 6", "Seller 7", "Seller 8", "Seller 9",
                        "Seller 10", "Seller 11", "Seller 12", "Seller 13", "Seller 14", "Seller 15", "Seller 16", "Seller 17",
                        "Seller 18", "Seller 19", "Seller 20", "Seller 21", "Seller 22", "Seller 23", "Seller 24", "Seller 25",
                        "Seller 26", "Seller 27", "Seller 28", "Seller 29", "Seller 30", "serler 31", "Seller 32",
                        ]

        # SAMPLE DATA

        self.items = [
            {
                "name": f"{item_names[i]}", 
                "price": f"£{(i+1)*10}",
                "image": f"{items_path[i]}",
                "seller": f"{seller_names[i]}",
                "desc": "Ut vel fugiat omnis. Dolor atque qui reprehenderit laudantium. Laborum occaecati corporis facere molestiae."
            }
            for i in range(30)
        ]
        
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
                  Register.Register,
                  Logout.Logout,
                  AboutUs.AboutUs,
                  Help.Help,
                  Reviews.Reviews,
                  ExchangeMessage.ExchangeMessage,
                  messages.MessagesPage,
                  ReturnItem.ReturnItem,
                  FetchingOverviewInfo.FetchingOverviewInfo,
                  ItemsVerification.ItemsVerification,
                  DeleteAccount.DeleteAccount,
                  SavedItems.SavedItems,
                  ViewListing.ViewListing):

            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0.05, relwidth=1, relheight=0.95)

        self.showFrame(Login.Login)

    def showFrame(self, cont):
        frame = self.frames[cont]
        if cont == SavedItems.SavedItems:
            frame.updateSavedItems()
        frame.tkraise()
        self.title("FlipIt.co.uk/" + frame.__class__.__name__)

'''
Each page is stored in it's own class file. To create a new page copy the first 3 lines of one of the classes and rename it, then add the new name to the for loop in the main class to add it to the list of pages, and import it at the top.
Then add items to it like you usually would in tkinter.
'''
        
if __name__ == "__main__":
    root = FlipITPage()
    
    root.mainloop()
