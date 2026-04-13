import tkinter as tk
from Colours import Colours
from tkinter import messagebox


class ReturnItem(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=Colours.col2)

        # Title
        page_name_label = tk.Label(
            self,
            text="Item Return Page",
            font=("Arial", 20),
            bg=Colours.col2
        )
        page_name_label.pack(pady=30)


        # Reference Input
        input_reference_frame = tk.Frame(self, bg=Colours.col2)
        input_reference_frame.pack(pady=20)

        tk.Label(
            input_reference_frame,
            text="Item Reference:",
            font=("Arial", 12),
            bg=Colours.col2
        ).grid(row=0, column=0, padx=10)

        self.reference_entry = tk.Entry(input_reference_frame, width=30)
        self.reference_entry.grid(row=0, column=1, padx=10)


        # Reason Input
        input_reasons_frame = tk.Frame(self, bg=Colours.col2)
        input_reasons_frame.pack(pady=20)

        tk.Label(
            input_reasons_frame,
            text="Reason for Return:",
            font=("Arial", 12),
            bg=Colours.col2
        ).grid(row=0, column=0, padx=10)
        tk.Entry()

        #self.reason_entry = tk.Entry(input_reasons_frame, width=30)
        self.reason_text = tk.Text(input_reasons_frame, width=30, height=5, wrap="word")
        self.reason_text.grid(row=0, column=1, padx=10)

        # Evidence (placeholder)
        evidence_pictures_frame = tk.Frame(self, bg=Colours.col2)
        evidence_pictures_frame.pack(pady=20)

        tk.Label(
            evidence_pictures_frame,
            text="Upload Evidence (optional):",
            bg=Colours.col2
        ).pack()

        tk.Button(
            evidence_pictures_frame,
            text="Upload Image"
        ).pack(pady=5)



        # Refund or Replacement
        radio_frame = tk.Frame(self, bg=Colours.col2)
        radio_frame.pack(pady=20)

        tk.Label(
            radio_frame,
            text="Select Option:",
            bg=Colours.col2
        ).pack()

        self.choice = tk.StringVar(value="Refund")

        tk.Radiobutton(
            radio_frame,
            text="Refund",
            variable=self.choice,
            value="Refund",
            bg=Colours.col2
        ).pack()

        tk.Radiobutton(
            radio_frame,
            text="Replacement",
            variable=self.choice,
            value="Replacement",
            bg=Colours.col2
        ).pack()

        # Submit Button
        submit_btn = tk.Button(
            self,
            text="Submit",
            font=("Arial", 12),
            command=self.submit_form
        )
        submit_btn.pack(pady=20)

    # Handle Submission
    def submit_form(self):
        reference = self.reference_entry.get()
        reason = self.reason_text.get("1.0", "end-1c")
        choice = self.choice.get()

        if not reference or not reason:
            messagebox.showerror("Error", "Reference or reason not provided")
            return

            # continue if valid
        print("Reference:", reference)
        print("Reason:", reason)
        print("Choice:", choice)