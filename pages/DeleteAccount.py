import tkinter as tk
from tkinter import messagebox
from Colours import Colours


class DeleteAccount(tk.Frame):
    """
    A Tkinter Frame for handling account deletion functionality.
    Provides options for temporary or permanent account deletion with reason and password verification.
    """

    def __init__(self, parent, controller):
        """
        Initialize the DeleteAccount frame.

        Args:
            parent: The parent widget that contains this frame
            controller: The main application controller for managing page navigation
        """
        tk.Frame.__init__(self, parent)

        # Initialize instance variables for UI elements
        self.get_delete_reason = None  # Text widget for deletion reason input
        self.get_password = None  # Entry widget for password confirmation
        self.permanent_deletion = None  # Radiobutton for temporary deletion option
        self.temporary_deletion = None  # Radiobutton for permanent deletion option

        # Set the background color for the frame
        self.config(bg=Colours.col2)

        # Create and display the main page title label
        tk.Label(
            self,
            text="Delete Account",
            font=("Arial", 22),
            bg=Colours.col2,
           # fg="white"
        ).pack(pady=50)

        # ===== REASON FOR DELETION SECTION =====
        # Create a frame to hold the reason label and text input
        reasonable_frame = tk.Frame(self, bg=Colours.col2)
        reasonable_frame.pack(padx=15, pady=8)

        # Label for the deletion reason field
        tk.Label(
            reasonable_frame,
            bg=Colours.col2,
           # fg=Colours.col2,
            text="Reason",
            font=("Arial", 15),
        ).pack(side="left", pady=15)

        # Multi-line text widget for users to enter their reason for deleting the account
        self.get_delete_reason = tk.Text(reasonable_frame, width=40, height=5, font=("Arial", 12), pady=10, bg="white"
                )
        self.get_delete_reason.pack(side="left", pady=10)

        # ===== PASSWORD CONFIRMATION SECTION =====
        # Create a frame to hold the password label and entry field
        password_frame = tk.Frame(self, bg=Colours.bg)
        password_frame.pack(padx=15, pady=8)

        # Label for the password confirmation field
        tk.Label(
            password_frame,
            text="Enter Password",
            font=("Arial", 15),
            bg=Colours.col2,
        ).pack(side="left")

        # Password entry field with masked characters (show="*") for security
        self.get_password = (tk.Entry(
            password_frame,
            width=30,
            font=("Arial", 12),
            show="*"))
        self.get_password.pack(side="right")

        # ===== DELETION TYPE SELECTION SECTION =====
        # Create a frame to hold the deletion type radio buttons
        radio_frame = tk.Frame(self, bg=Colours.col2)
        radio_frame.pack(pady=20)

        # Label explaining the deletion options
        tk.Label(
            radio_frame,
            text="Temporary deletion is an option:",
            font=("Arial", 15),
            bg=Colours.col2
        ).pack()

        # String variable to store the selected deletion type (default: "Temporary deletion")
        self.choice = tk.StringVar(value="Temporary deletion")

        # Radio button for temporary deletion option (recoverable)
        self.permanent_deletion = tk.Radiobutton(
            radio_frame,
            text="Temporary deletion",
            font=("Arial", 12),
            variable=self.choice,
            value="Temporary deletion",
            bg=Colours.col2
        )
        self.permanent_deletion.pack(side="left")

        # Radio button for permanent deletion option (non-recoverable)
        self.temporary_deletion = tk.Radiobutton(
            radio_frame,
            text="Permanent deletion",
            font=("Arial", 12),
            variable=self.choice,
            value="Permanent deletion",
            bg=Colours.col2
        )

        self.temporary_deletion.pack()

        # ===== SUBMIT BUTTON =====
        # Button to submit the deletion request
        tk.Button(
            self,
            font=("Arial", 15),
            text="Delete Account",
            command= lambda : self.submit_Delete()
        ).pack(pady=15)

    def submit_Delete(self):
        """
        Handle the account deletion submission.

        Validates that both reason and password are provided, then processes
        the deletion based on the selected deletion type (temporary or permanent).
        Displays appropriate success or error messages to the user.
        """
        # Retrieve the deletion reason from the text widget (from line 1, column 0 to end minus last character)
        reason = self.get_delete_reason.get("1.0", "end-1c")
        # Retrieve the password from the entry field
        password  = self.get_password.get()

        # Validate that both fields are filled
        if not reason or not password:
            messagebox.showerror("Error", "password or reason not provided")
            return

        # Check if temporary deletion option is selected
        if self.temporary_deletion.select():
            messagebox.showinfo("delete", "Account is  deleted")
           ## print("account temporary deleted")

        # Handle permanent deletion
        else:
              messagebox.showerror("delete", "Account is permanently deleted")
             # print("account permanently deleted")
