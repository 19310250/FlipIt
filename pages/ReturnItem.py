import tkinter as tk
from Colours import Colours
from tkinter import messagebox


class ReturnItem(tk.Frame):
    """
    A Tkinter Frame for handling item returns.
    Allows users to submit return requests by providing item reference, reason for return,
    optional evidence, and choosing between refund or replacement.
    """

    def __init__(self, parent, controller):
        """
        Initialize the ReturnItem frame.

        Args:
            parent: The parent widget that contains this frame
            controller: The main application controller for managing page navigation
        """
        tk.Frame.__init__(self, parent)

        # Set the background color for the frame
        self.config(bg=Colours.col2)

        # ===== PAGE TITLE =====
        # Display the main page title
        page_name_label = tk.Label(
            self,
            text="Item Return Page",
            font=("Arial", 20),
            bg=Colours.col2
        )
        page_name_label.pack(pady=30)

        # ===== ITEM REFERENCE INPUT SECTION =====
        # Create a frame to hold the reference label and entry field
        input_reference_frame = tk.Frame(self, bg=Colours.col2)
        input_reference_frame.pack(pady=20)

        # Label for item reference field
        tk.Label(
            input_reference_frame,
            text="Item Reference:",
            font=("Arial", 12),
            bg=Colours.col2
        ).grid(row=0, column=0, padx=10)

        # Entry field for users to input the item's reference number
        self.reference_entry = tk.Entry(input_reference_frame, width=30)
        self.reference_entry.grid(row=0, column=1, padx=10)


        # ===== REASON FOR RETURN INPUT SECTION =====
        # Create a frame to hold the reason label and text input
        input_reasons_frame = tk.Frame(self, bg=Colours.col2)
        input_reasons_frame.pack(pady=20)

        # Label for the return reason field
        tk.Label(
            input_reasons_frame,
            text="Reason for Return:",
            font=("Arial", 12),
            bg=Colours.col2
        ).grid(row=0, column=0, padx=10)
        tk.Entry()

        # Multi-line text widget for users to provide detailed return reason
        # Using Text instead of Entry allows for longer explanations
        #self.reason_entry = tk.Entry(input_reasons_frame, width=30)
        self.reason_text = tk.Text(input_reasons_frame, width=30, height=5, wrap="word")
        self.reason_text.grid(row=0, column=1, padx=10)

        # ===== EVIDENCE UPLOAD SECTION =====
        # Create a frame for optional evidence upload (photos of damaged/faulty items)
        evidence_pictures_frame = tk.Frame(self, bg=Colours.col2)
        evidence_pictures_frame.pack(pady=20)

        # Label indicating evidence upload is optional
        tk.Label(
            evidence_pictures_frame,
            text="Upload Evidence (optional):",
            bg=Colours.col2
        ).pack()

        # Button to trigger image upload (functionality to be implemented)
        tk.Button(
            evidence_pictures_frame,
            text="Upload Image"
        ).pack(pady=5)



        # ===== REFUND OR REPLACEMENT SELECTION =====
        # Create a frame to hold the radio button options
        radio_frame = tk.Frame(self, bg=Colours.col2)
        radio_frame.pack(pady=20)

        # Label prompting user to select their preferred resolution
        tk.Label(
            radio_frame,
            text="Select Option:",
            bg=Colours.col2
        ).pack()

        # String variable to store the user's choice (default: "Refund")
        self.choice = tk.StringVar(value="Refund")

        # Radio button for refund option (money back)
        tk.Radiobutton(
            radio_frame,
            text="Refund",
            variable=self.choice,
            value="Refund",
            bg=Colours.col2
        ).pack()

        # Radio button for replacement option (exchange for new item)
        tk.Radiobutton(
            radio_frame,
            text="Replacement",
            variable=self.choice,
            value="Replacement",
            bg=Colours.col2
        ).pack()

        # ===== SUBMIT BUTTON =====
        # Button to submit the return request form
        submit_btn = tk.Button(
            self,
            text="Submit",
            font=("Arial", 12),
            command=self.submit_form
        )
        submit_btn.pack(pady=20)

    # ===== FORM SUBMISSION HANDLER =====
    def submit_form(self):
        """
        Validate and submit the return request form.
        Ensures required fields (reference and reason) are filled before submission.
        Displays success or error messages based on validation results.
        """
        # Retrieve values from form fields
        reference = self.reference_entry.get()
        reason = self.reason_text.get("1.0", "end-1c")  # Get text from line 1, col 0 to end minus last char
        choice = self.choice.get()

        # Validate that both required fields are filled
        if not reference or not reason:
            messagebox.showerror("Error", "Reference or reason not provided")
            return

        # If validation passes, show success message
        messagebox.showinfo("Success", "Form submitted successfully")
        # Debug output (commented out for production)
        #print("Reference:", reference)
        #print("Reason:", reason)
        #print("Choice:", choice)