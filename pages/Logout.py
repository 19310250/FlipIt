import tkinter as tk
from Colours import Colours

class Logout(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)

        wrapper = tk.Frame(self, bg=Colours.bg)
        wrapper.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(wrapper, text="You've been logged out", font=("Arial", 24, "bold"),
                 bg=Colours.bg, fg=Colours.col4).pack(pady=(0, 20))

        tk.Label(wrapper, text="See you next time!", font=("Arial", 12),
                 bg=Colours.bg, fg=Colours.text).pack(pady=(0, 30))

        tk.Button(wrapper, text="Back to Login", font=("Arial", 12, "bold"),
                  bg=Colours.col3, fg=Colours.text, width=20,
                  command=self.on_logout).pack()

    def on_logout(self):
        from Header import Header
        self.controller.username = None
        Header.HideButtons(self.controller.header)
        from pages import Login
        self.controller.showFrame(Login.Login)