import tkinter as tk
from tkinter import messagebox
from Colours import Colours


class ItemsVerification(tk.Frame):
    """
    A Tkinter Frame for verifying high-value items (over £300).
    Provides a scrollable form to collect detailed information about expensive items
    including serial numbers, ownership proof, and purchase details.
    """

    def __init__(self, parent, controller):
        """
        Initialize the ItemsVerification frame.

        Args:
            parent: The parent widget that contains this frame
            controller: The main application controller for managing page navigation
        """
        tk.Frame.__init__(self, parent, bg=Colours.col2)

        # Initialize instance variables
        self.priceInput = None  # Entry widget for price input
        self.prev_main_frame = None  # Reference to previous frame (if needed)

        # Create the main page title label
        tk.Label(self, text="items verification", bg=Colours.col2, font=("Ariel", 30), fg=Colours.text).pack(pady=(20, 0))

        # Dictionary to store all form entry widgets for verification fields
        self.entries = {}

        # ===== SCROLLABLE CONTAINER SETUP =====
        # Create a canvas widget to enable scrolling for long forms
        self.canvas = tk.Canvas(self, bg=Colours.col2, highlightthickness=0)
        # Create a vertical scrollbar linked to the canvas
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        # Configure the canvas to update the scrollbar position
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the scrollbar on the right side
        self.scrollbar.pack(side="right", fill="y")
        # Pack the canvas to fill the remaining space
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create the main frame that will be placed inside the canvas (scrollable content area)
        self.main_frame = tk.Frame(self.canvas, bg=Colours.col2)
        # Create a window inside the canvas to hold the main_frame
        self.canvas_window = self.canvas.create_window((0, 0), window=self.main_frame, anchor="n")

        # Bind events to update scroll region when frame size changes
        self.main_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)

        # Enable mouse wheel scrolling for better user experience
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)        # Windows/macOS
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)    # Linux scroll up
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)    # Linux scroll down

        # Display the initial price input screen
        self.show_price_input()

    # ===== SCROLL HELPER METHODS =====
    def _on_frame_configure(self, event=None):
        """
        Update the canvas scroll region when the main_frame size changes.
        This ensures the scrollbar reflects the actual content size.
        """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        """
        Adjust the inner frame width when the canvas is resized.
        Keeps the inner frame centered and at least as wide as the canvas.

        Args:
            event: The configure event containing the new canvas dimensions
        """
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        """
        Handle mouse wheel scrolling for Windows and macOS.

        Args:
            event: The mouse wheel event containing scroll delta
        """
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _on_mousewheel_linux(self, event):
        """
        Handle mouse wheel scrolling for Linux systems.
        Button-4 is scroll up, Button-5 is scroll down.

        Args:
            event: The mouse button event (4 or 5)
        """
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

    # ===== UI HELPER METHODS =====
    def clear_frame(self):
        """
        Remove all widgets from the main_frame.
        Used when switching between different views (price input vs verification form).
        """
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # ===== INITIAL PRICE INPUT SCREEN =====
    def show_price_input(self):
        """
        Display the initial price input screen where users enter the item price.
        This is the first screen shown when the page loads.
        """
        # Clear any existing widgets from the frame
        self.clear_frame()

        # Create label prompting user to enter the item price
        tk.Label(self.main_frame, text="Enter Item Price (£):", font=("Arial", 12), bg=Colours.col2, fg=Colours.text).pack(pady=10)

        # Create entry field for price input
        self.priceInput = tk.Entry(self.main_frame, width=50)
        self.priceInput.pack(pady=5)

        # Create button to submit and check the price
        tk.Button(self.main_frame, text="Check", command=self.check_prices).pack(pady=10)

    # ===== PRICE VALIDATION LOGIC =====
    def check_prices(self):
        """
        Validate the entered price and determine if verification is needed.
        Items over £300 require additional verification with a detailed form.
        Items under £300 are automatically approved.
        """
        try:
            # Convert the input string to a float
            price = float(self.priceInput.get())

            # If price exceeds £300, show the verification form
            if price > 300:
                self.show_verification_form(price)
            else:
                # Items under £300 don't require verification
                messagebox.showinfo("Approved", "Item approved (under £300).")

        except ValueError:
            # Handle invalid input (non-numeric values)
            messagebox.showerror("Error", "Please enter a valid price.")

    # ===== VERIFICATION FORM DISPLAY =====
    def show_verification_form(self, price):
        """
        Display the detailed verification form for high-value items (over £300).
        Collects comprehensive information about the item including serial number,
        ownership proof, and purchase details.

        Args:
            price: The price of the item requiring verification
        """
        # Clear the existing price input screen
        self.clear_frame()

        # Scroll back to top when showing new form for better user experience
        self.canvas.yview_moveto(0)

        # Display warning label showing the item price in red to emphasize verification requirement
        tk.Label(
            self.main_frame,
            text=f"Item over £300 (£{price})",
            fg="red",
            bg=Colours.col2,
            font=("Arial", 12, "bold")
        ).pack(pady=20)

        # Reset the entries dictionary to store new form fields
        self.entries = {}

        # Define all required fields for item verification
        fields = [
            "Serial Number",
            "Item Description",
            "Brand",
            "Model",
            "Owner Name",
            "Purchase Date",
            "Purchase Location",
            "Proof of Ownership (Ref/Receipt No.)",
            "Reason for Verification"
        ]

        # Create input fields for each verification requirement
        for field in fields:
            self.add_field(field)

        # Create submit button to process the verification form
        tk.Button(
            self.main_frame,
            text="Submit",
            command=self.submit_verification
        ).pack(pady=20)

    # ===== DYNAMIC FIELD CREATION =====
    def add_field(self, label_text):
        """
        Create a labeled entry field and add it to the verification form.
        Each field consists of a bold label and a text entry widget.

        Args:
            label_text: The label text to display above the entry field
        """
        # Create and pack the label for the field
        tk.Label(self.main_frame, text=label_text, font=("Arial", 12, "bold"), bg=Colours.col2, fg=Colours.text).pack()
        # Create the entry widget for user input
        entry = tk.Entry(self.main_frame, width=50)
        entry.pack(pady=8)
        # Store the entry widget in the dictionary using the label as the key
        self.entries[label_text] = entry

    # ===== FORM SUBMISSION =====
    def submit_verification(self):
        """
        Validate and submit the verification form.
        Ensures all fields are filled before accepting the submission.
        Displays a confirmation message upon successful submission.
        """
        # Validate that all fields have been filled in
        for field, entry in self.entries.items():
            value = entry.get().strip()
            if not value:
                # Show error if any field is empty
                messagebox.showerror("Error", f"{field} is required.")
                return

        # All fields are valid, show success message
        messagebox.showinfo("verification complete", "The details will be review within 24 hours")
        ##print("Form submitted successfully")
