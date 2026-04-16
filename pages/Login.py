from tkinter import ttk
import tkinter as tk
import json
import os
import hashlib
from Colours import Colours
from pages import MainPage
from Header import Header

# login page: handles user login and takes them to the main page
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

        # password field - show="*" hides the password as it's typed
        tk.Label(wrapper, text="Password", font=("Arial", 12),
                 bg=Colours.bg, fg=Colours.text).pack(anchor="w")
        self.txtPassword = tk.Entry(wrapper, width=35, font=("Arial", 12),
                                     bg=Colours.col2, fg=Colours.text,
                                     insertbackground=Colours.text, show="*")
        self.txtPassword.pack(pady=(0, 15), ipady=6)

        # error label (hidden by default, shows if login fails)
        self.lblError = tk.Label(wrapper, text="", font=("Arial", 10),
                                  bg=Colours.bg, fg="red")
        self.lblError.pack(pady=(0, 5))

        # login button
        tk.Button(wrapper, text="Login", font=("Arial", 12, "bold"),
                  bg=Colours.col3, fg=Colours.text, width=20,
                  command=self.on_login).pack(pady=(0, 10))

        # sign up link - now clickable, routes to register page
        lbl_signup = tk.Label(wrapper, text="Don't have an account? Sign up",
                 font=("Arial", 10), bg=Colours.bg, fg=Colours.col4,
                 cursor="hand2")
        lbl_signup.pack()
        lbl_signup.bind("<Button-1>", lambda e: self.go_to_register())

    def on_login(self):
        username = self.txtUsername.get().strip()
        password = self.txtPassword.get().strip()

        # validation - don't let empty fields through
        if not username or not password:
            self.lblError.config(text="Please enter your username and password.")
            return

        # check credentials against users.json
        users_file = "users.json"
        if os.path.exists(users_file):
            with open(users_file, "r") as f:
                users = json.load(f)
            if username in users and users[username] == hashlib.sha256(password.encode()).hexdigest():
                # correct credentials - go to main page
                self.lblError.config(text="")
                self.controller.username = username
                self.controller.showFrame(MainPage.MainPage)
                Header.ShowButtons(self.controller.header)
            else:
                self.lblError.config(text="Incorrect username or password.")
        else:
            # no users file yet - nudge them to register
            self.lblError.config(text="No accounts found. Please sign up first.")

    def go_to_register(self):
        from pages import Register
        self.controller.showFrame(Register.Register)
