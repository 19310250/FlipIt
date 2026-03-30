import tkinter as tk
from tkinter import Toplevel, ttk

from colours import colours
from addListing import addListing
from home import home

'''
This is the main class, it prepairs the window and the ability to switch between different frames. Each page will be put in a different frame.
'''
class FlipITPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # App layout
        self.geometry("1600x1200")
        self.resizable(False, False)
        self.config(background=colours.bg)

        mainFrame = tk.Frame(self)
        mainFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Header
        self.header = tk.Frame(self, bg=colours.bg)
        self.header.place (relx= 0, rely=0, relwidth=1, relheight=0.05)

        lblLogo = ttk.Label(self.header, text="FlipIt",background=colours.bg, foreground=colours.col4, font=("Arial", 25))
        lblLogo.pack(side="left")

        btnAddListing =  ttk.Button(self, text = "Add listing", command = lambda : self.showFrame(addListing))
        btnAddListing.pack(anchor="e")
        #TODO finish header by adding search bar and other buttons
        
        self.frames = {}
        for F in (home, addListing): # Add all pages to a list which can then be switched between
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0.05, relwidth=1, relheight=0.95)

        self.showFrame(home)
        login(self,self)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.title("FlipIt.co.uk/" + frame.__class__.__name__)

'''
Each page is stored in it's own class file. To create a new page copy the first 3 lines of one of the other classes and rename it, then add the new name to the for loop in the main class to add it to the list of pages.
Then add items to it like you usually would in tkinter.
'''

# based on https://runebook.dev/en/docs/python/library/dialog, slightly jank but seems to work
class login (tk.Frame):
    def __init__(self, parent, controller):
        self.top = tk.Toplevel(parent)
        self.top.title("Login")
        
        #TODO Add login boxes and buttons that call the login functions
        btnLogin = ttk.Button(self.top, text="Login", command=self.on_login)
        btnLogin.pack()

        # Locks the background window until the user has logged in
        self.top.transient(parent)
        self.top.grab_set()
        parent.wait_window(self.top)

    def on_login(self):
        #todo return data
        self.top.destroy()
    
        
if __name__ == "__main__":
    root = FlipITPage()
    
    root.mainloop()
