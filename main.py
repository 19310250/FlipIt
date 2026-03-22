import tkinter as tk
from tkinter import ttk

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

        label1 = ttk.Label(self.header, text="FlipIt",background=colours.bg, foreground=colours.col4, font=("Arial", 25))
        label1.place(relx=0, rely=0)
        #TODO finish header        
        
        self.frames = {}
        for F in (home, addListing, login):
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0.05, relwidth=1, relheight=0.95)

        self.showFrame(home)

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
        
        # Placeholder, can be replaced
        label = tk.Label(self, text= "home")
        label.pack(fill=tk.BOTH)
        button1 = ttk.Button(self, text = "add listing", command = lambda : controller.showFrame(addListing))
        button1.pack()

class addListing (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "listing")
        label.pack(fill=tk.BOTH)


class login (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        
if __name__ == "__main__":
    root = FlipITPage()
    root.mainloop()
