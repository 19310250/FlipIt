import tkinter as tk
from tkinter import messagebox
from Colours import Colours


class ItemsVerification(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=Colours.col2)

        self.priceInput = None
        self.prev_main_frame = None

        tk.Label(self, text="items verification", bg=Colours.col2, font=("Ariel", 30), fg=Colours.text).pack(pady=(20, 0))

        self.entries = {}

        # SCROLLABLE CONTAINER
        self.canvas = tk.Canvas(self, bg=Colours.col2, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # MAIN FRAME inside canvas
        self.main_frame = tk.Frame(self.canvas, bg=Colours.col2)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.main_frame, anchor="n")

        # Update scroll region when main_frame size changes
        self.main_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)

        # Mouse wheel scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)        # Windows/macOS
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)    # Linux scroll up
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)    # Linux scroll down

        self.show_price_input()

    # SCROLL HELPERS
    def _on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        # Keep the inner frame centered and at least as wide as the canvas
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

    # UI HELPERS
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # INITIAL SCREEN
    def show_price_input(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Enter Item Price (£):", font=("Arial", 12), bg=Colours.col2, fg=Colours.text).pack(pady=10)

        self.priceInput = tk.Entry(self.main_frame, width=50)
        self.priceInput.pack(pady=5)

        tk.Button(self.main_frame, text="Check", command=self.check_prices).pack(pady=10)

    # LOGIC
    def check_prices(self):
        try:
            price = float(self.priceInput.get())

            if price > 300:
                self.show_verification_form(price)
            else:
                messagebox.showinfo("Approved", "Item approved (under £300).")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid price.")

    # VERIFICATION FORM
    def show_verification_form(self, price):
        self.clear_frame()

        # Scroll back to top when showing new form
        self.canvas.yview_moveto(0)

        tk.Label(
            self.main_frame,
            text=f"Item over £300 (£{price})",
            fg="red",
            bg=Colours.col2,
            font=("Arial", 12, "bold")
        ).pack(pady=20)

        self.entries = {}

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

        for field in fields:
            self.add_field(field)

        tk.Button(
            self.main_frame,
            text="Submit",
            command=self.submit_verification
        ).pack(pady=20)

    # FIELD CREATION
    def add_field(self, label_text):
        tk.Label(self.main_frame, text=label_text, font=("Arial", 12, "bold"), bg=Colours.col2, fg=Colours.text).pack()
        entry = tk.Entry(self.main_frame, width=50)
        entry.pack(pady=8)
        self.entries[label_text] = entry

    # SUBMIT
    def submit_verification(self):
        for field, entry in self.entries.items():
            value = entry.get().strip()
            if not value:
                messagebox.showerror("Error", f"{field} is required.")
                return

        messagebox.showinfo("verification complete", "The details will be review within 24 hours")
