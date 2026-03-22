import tkinter as tk
from tkinter import ttk


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


class home (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="#1A1F16")
        label = tk.Label(self, text= "home")
        label.pack(fill=tk.BOTH)
        button1 = ttk.Button(self, text = "add listing", command = lambda : controller.showFrame(add_listing))
        button1.pack()

class add_listing (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "listing")
        label.pack(fill=tk.BOTH)
    
if __name__ == "__main__":
    root = FlipITPage()
    root.mainloop()
