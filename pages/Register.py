import tkinter as tk
import json
import os
import hashlib
from Colours import Colours
from Header import Header

# register page: handles new account creation and saves to users.json
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)

        # centre the register box on screen
        wrapper = tk.Frame(self, bg=Colours.bg)
        wrapper.place(relx=0.5, rely=0.5, anchor="center")

        # title
        tk.Label(wrapper, text="Create an Account", font=("Arial", 24, "bold"),
                 bg=Colours.bg, fg=Colours.col4).pack(pady=(0, 30))

        # username field
        tk.Label(wrapper, text="Username", font=("Arial", 12),
                 bg=Colours.bg, fg=Colours.text).pack(anchor="w")
        self.txtUsername = tk.Entry(wrapper, width=35, font=("Arial", 12),
                                    bg=Colours.col2, fg=Colours.text,
                                    insertbackground=Colours.text)
        self.txtUsername.pack(pady=(0, 15), ipady=6)

        # password field
        tk.Label(wrapper, text="Password", font=("Arial", 12),
                 bg=Colours.bg, fg=Colours.text).pack(anchor="w")
        self.txtPassword = tk.Entry(wrapper, width=35, font=("Arial", 12),
                                    bg=Colours.col2, fg=Colours.text,
                                    insertbackground=Colours.text, show="*")
        self.txtPassword.pack(pady=(0, 15), ipady=6)

        # confirm password field
        tk.Label(wrapper, text="Confirm Password", font=("Arial", 12),
                 bg=Colours.bg, fg=Colours.text).pack(anchor="w")
        self.txtConfirm = tk.Entry(wrapper, width=35, font=("Arial", 12),
                                   bg=Colours.col2, fg=Colours.text,
                                   insertbackground=Colours.text, show="*")
        self.txtConfirm.pack(pady=(0, 25), ipady=6)

        # error label (hidden by default, shows validation messages)
        self.lblError = tk.Label(wrapper, text="", font=("Arial", 10),
                                  bg=Colours.bg, fg="red")
        self.lblError.pack(pady=(0, 5))

        # register button
        tk.Button(wrapper, text="Register", font=("Arial", 12, "bold"),
                  bg=Colours.col3, fg=Colours.text, width=20,
                  command=self.on_register).pack(pady=(0, 10))

        # back to login link
        lbl_login = tk.Label(wrapper, text="Already have an account? Log in",
                             font=("Arial", 10), bg=Colours.bg, fg=Colours.col4,
                             cursor="hand2")
        lbl_login.pack()
        # bind click to go back to login page
        lbl_login.bind("<Button-1>", lambda e: self.go_to_login())

    def hash_password(self, password):
        # hash the password using sha256 before saving - plain text passwords are a security risk
        return hashlib.sha256(password.encode()).hexdigest()

    def on_register(self):
        username = self.txtUsername.get().strip()
        password = self.txtPassword.get().strip()
        confirm = self.txtConfirm.get().strip()

        # basic validation checks
        if not username or not password or not confirm:
            self.lblError.config(text="Please fill in all fields.")
            return

        if password != confirm:
            self.lblError.config(text="Passwords do not match.")
            return

        if len(password) < 6:
            self.lblError.config(text="Password must be at least 6 characters.")
            return

        # load existing users from json, or start fresh if file doesn't exist
        users_file = "users.json"
        if os.path.exists(users_file):
            with open(users_file, "r") as f:
                users = json.load(f)
        else:
            users = {}

        # check if username is already taken
        if username in users:
            self.lblError.config(text="Username already exists.")
            return

        # hash the password before saving - never store plain text passwords
        users[username] = self.hash_password(password)
        with open(users_file, "w") as f:
            json.dump(users, f, indent=4)

        # clear error and go back to login after successful registration
        self.lblError.config(text="")
        self.go_to_login()

    def go_to_login(self):
        # import here to avoid circular import issues
        from pages import Login
        self.controller.showFrame(Login.Login)
