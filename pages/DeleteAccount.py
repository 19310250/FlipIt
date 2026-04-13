import tkinter as tk
from tkinter import messagebox
from Colours import Colours



class DeleteAccount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.get_delete_reason = None
        self.get_password = None
        self.permanent_deletion = None
        self.temporary_deletion = None


        self.config(bg=Colours.col2)
        # nav_frame = tk.Frame(self, bg=Colours.col1)
        # nav_frame.pack(fill="x")
        #
        # tk.Label(
        #     nav_frame,
        #     text="FlipIt",
        #     font=("Arial", 22, "bold"),
        #     bg=Colours.col1,
        #     fg=Colours.text
        # ).pack(side="left", padx=15, pady=15)

        # delete account message
        tk.Label(
            self,
            text="Delete Account",
            font=("Arial", 22),
            bg=Colours.col2,
           # fg="white"
        ).pack(pady=50)

        # reason for the delete#
        reasonable_frame = tk.Frame(self, bg=Colours.col2)
        reasonable_frame.pack(padx=15, pady=8)

        tk.Label(
            reasonable_frame,
            bg=Colours.col2,
           # fg=Colours.col2,
            text="Reason",
            font=("Arial", 15),
        ).pack(side="left", pady=15)

        self.get_delete_reason = tk.Text(reasonable_frame, width=40, height=5, font=("Arial", 12), pady=10, bg="white"
                )
        self.get_delete_reason.pack(side="left", pady=10)

        ## handle password confirmation
        password_frame = tk.Frame(self, bg=Colours.bg)
        password_frame.pack(padx=15, pady=8)


        tk.Label(
            password_frame,
            text="Enter Password",
            font=("Arial", 15),
            bg=Colours.col2,
        ).pack(side="left")

        self.get_password = (tk.Entry(
            password_frame,
            width=30,
            font=("Arial", 12)))
        self.get_password.pack(side="right")

        # Refund or Replacement
        radio_frame = tk.Frame(self, bg=Colours.col2)
        radio_frame.pack(pady=20)


       ## select type of account deletion
        tk.Label(
            radio_frame,
            text="Temporary deletion is an option:",
            font=("Arial", 15),
            bg=Colours.col2
        ).pack()

        self.choice = tk.StringVar(value="Temporary deletion")

        self.permanent_deletion = tk.Radiobutton(
            radio_frame,
            text="Temporary deletion",
            font=("Arial", 12),
            variable=self.choice,
            value="Temporary deletion",
            bg=Colours.col2
        )
        self.permanent_deletion.pack(side="left")

        self.temporary_deletion = tk.Radiobutton(
            radio_frame,
            text="Permanent deletion",
            font=("Arial", 12),
            variable=self.choice,
            value="Permanent deletion",
            bg=Colours.col2
        )

        self.temporary_deletion.pack()

      ##  deletebutton
        tk.Button(
            self,
            font=("Arial", 15),
            text="Delete Account",
            command= lambda : self.submit_Delete()
        ).pack(pady=15)

    def submit_Delete(self):
        reason = self.get_delete_reason.get("1.0", "end-1c")
        password  = self.get_password.get()

        if not reason or not password:
            messagebox.showerror("Error", "password or reason not provided")
            return

        if self.temporary_deletion.select():
            messagebox.showinfo("delete", "Account is  deleted")

        else:
              messagebox.showerror("delete", "Account is temporary deleted")
