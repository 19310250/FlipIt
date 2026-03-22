import tkinter as tk
from tkinter import Toplevel, ttk

class colours:
    bg = "#1A1F16"
    col1 = "#1E3F20"
    col2 = "#345830"
    col3 = "#4A7856"
    col4 = "#94ECBE"
    text = "#C9D0C6"

'''
This is the main class, it prepairs the window and the ability to switch between different frames. Each page will be put in a different frame.
'''
class FlipITPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("FlipIt")

        # App layout
        self.geometry("1600x1200")
        self.resizable(0, 0)
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
        #TODO finish header
        
        self.frames = {}
        for F in (home, addListing):
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0.05, relwidth=1, relheight=0.95)

        self.showFrame(home)
        login(self,self)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

'''
Each page is stored in it's own class. To create a new page copy the first 3 lines of one of these classes and rename it, then add the new name to the for loop in the main class for it to add it to the list of pages.
Then add items to it like you usually would in tkinter.
'''
class home (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=colours.bg)
        
        # Placeholder example, can and should be replaced
        label = tk.Label(self, text= "home")
        label.pack(fill=tk.BOTH)
        button1 = ttk.Button(self, text = "add listing", command = lambda : controller.showFrame(addListing))
        button1.pack()

class addListing (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "listing")
        label.pack(fill=tk.BOTH)

# based on https://runebook.dev/en/docs/python/library/dialog, slightly jank but seems to work
class login (tk.Frame):
    def __init__(self, parent, controller):
        self.top = tk.Toplevel(parent)
        self.top.title("Login")
        
        #TODO Add login boxes and buttons that call the login functions
        btnLogin = ttk.Button(self.top, text="Login", command=self.on_login)
        btnLogin.pack()

        # Locks the background window untill the user has logged in
        self.top.transient(parent)
        self.top.grab_set()
        parent.wait_window(self.top)

    def on_login(self):
        #todo return data
        self.top.destroy()
    
        
if __name__ == "__main__":
    root = FlipITPage()
    
    root.mainloop()
