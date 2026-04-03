from tkinter import ttk
import tkinter as tk
from Colours import Colours
from pages import MainPage
from Header import Header

# Login page: handles user login and takes them to the main page
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)

        # centre the login box on screen
        wrapper = tk.Frame(self, bg=Colours.bg)
        wrapper.place(relx=0.5, rely=0.5, anchor="center")

        # title
        tk.Label(wrapper, text="Welcome to FlipIt", font=("Arial", 24, "bold"),
                 bg=Colours.bg, fg=Colours.col4).pack(pady=(0, 30))

        # username field
        tk.Label(wrapper, text="Username", font=("Arial", 12),
                 bg=Colours.bg, fg=Colours.text).pack(anchor="w")
        self.txtUsername = tk.Entry(wrapper, width=35, font=("Arial", 12),
                                    bg=Colours.col2, fg=Colours.text, insertbackground=Colours.text)
        self.txtUsername.pack(pady=(0, 15), ipady=6)

        # password field here we use show="*" to hide the password as it's typed
        tk.Label(wrapper, text="Password", font=("Arial", 12),
                 bg=Colours.bg, fg=Colours.text).pack(anchor="w")
        self.txtPassword = tk.Entry(wrapper, width=35, font=("Arial", 12),
                                     bg=Colours.col2, fg=Colours.text,
                                     insertbackground=Colours.text, show="*")
        self.txtPassword.pack(pady=(0, 25), ipady=6)

        # login button
        tk.Button(wrapper, text="Login", font=("Arial", 12, "bold"),
                  bg=Colours.col3, fg=Colours.text, width=20,
                  command=self.on_login).pack(pady=(0, 10))

        # sign up link for new users (doesn't do anything functionally)
        tk.Label(wrapper, text="Don't have an account? Sign up",
                 font=("Arial", 10), bg=Colours.bg, fg=Colours.col4,
                 cursor="hand2").pack()

    # when login is clicked, grabs the username and it then goes to main page (no actual login functionality implemented) and shows the header buttons
    def on_login(self):
        username = self.txtUsername.get()
        if username:
            self.controller.username = username
        else:
            self.controller.username = "User"
        self.controller.showFrame(MainPage.MainPage)
        Header.ShowButtons(self.controller.header)