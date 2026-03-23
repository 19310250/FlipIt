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
Each page is stored in it's own class. To create a new page copy the first 3 lines of one of these classes and rename it, then add the new name to the for loop in the main class to add it to the list of pages.
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
        def addPlaceholder(entry, text):
            def boxClick(_):
                if entry.get(1.0, "end-1c") == text:
                    entry.delete(1.0, tk.END)
                    entry.config(fg=colours.text)

            def boxFocusLost(_):
                if not entry.get(1.0, "end-1c"):
                    entry.insert(1.0, text)
                    entry.config(fg="grey")

            entry.insert(1.0, text)
            entry.config(fg="grey")
            entry.bind("<Button-1>", boxClick)
            entry.bind("<Leave>", boxFocusLost)
            
        tk.Frame.__init__(self, parent)
        self.config(bg=colours.bg)
        lblName = tk.Label(self, text= "Item Name:", background=colours.bg, foreground=colours.text)
        lblName.pack(anchor="nw")
        txtName = tk.Text(self, height=1, wrap="none", background=colours.col2, foreground=colours.text)
        addPlaceholder(txtName, "What should people search for to find this item....")
        txtName.pack(anchor="nw")

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
