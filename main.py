import tkinter as tk
from tkinter import ttk

from home import home
from add_listing import add_listing

class FlipITPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("FlipIt")

        # App layout
        self.geometry("1280x1290")
        self.config(background='#1A1F16')

        mainFrame = tk.Frame(self)
        mainFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.frames = {}
        for F in (home, add_listing):
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.showFrame(home)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    
if __name__ == "__main__":
    root = FlipITPage()
    root.mainloop()
