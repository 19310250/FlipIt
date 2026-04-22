import tkinter as tk
from PIL import Image, ImageTk
from Colours import Colours

from pages import ViewListing


class MainPage(tk.Frame):
    """
    The main marketplace page displaying a scrollable grid of item cards.
    Each card shows an item's image, name, price, and action buttons (View and Save).
    Uses a 3-row by 10-column grid layout for item display.
    """

    def __init__(self, parent, controller):
        """
        Initialize the MainPage frame.

        Args:
            parent: The parent widget that contains this frame
            controller: The main application controller for managing navigation and shared data
        """
        # Store reference to controller for accessing shared data and navigation
        self.controller = controller
        tk.Frame.__init__(self, parent)

        # Set the background color for the frame
        self.config(bg=Colours.bg)
        #print("30 max items have been added")

        # Get the list of items to display from the controller
        self.items = controller.items

        # ===== SCROLLABLE AREA SETUP =====
        # Create main container to hold the canvas and scrollbar
        container = tk.Frame(self, bg=Colours.bg)
        container.pack(fill="both", expand=True)

        # Create canvas for scrollable content
        canvas = tk.Canvas(container, bg=Colours.bg, highlightthickness=0)
        # Create vertical scrollbar linked to the canvas
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

        # Create the frame that will contain all item cards (scrollable content)
        scrollable_frame = tk.Frame(canvas, bg=Colours.bg)

        # Update canvas scroll region whenever the scrollable_frame size changes
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Place the scrollable_frame inside the canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Configure canvas to update scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ===== GRID LAYOUT CONFIGURATION =====
        # Define grid dimensions: 3 rows by 10 columns
        rows, cols = 3, 10

        # Configure all columns to have equal weight for responsive layout
        for c in range(cols):
            scrollable_frame.grid_columnconfigure(c, weight=1)

        # Configure all rows to have equal weight for responsive layout
        for r in range(rows):
            scrollable_frame.grid_rowconfigure(r, weight=1)

        # ===== CREATE ITEM CARDS =====
        # List to store PhotoImage references (prevents garbage collection)
        self.images = []

        # Loop through all items and create a card for each
        for index, item in enumerate(self.items):
            # Calculate grid position (row and column) for this card
            r = index // cols  # Row index
            c = index % cols   # Column index

            # Create outer frame for the card with border
            card = tk.Frame(
                scrollable_frame,
                bg=Colours.col2,
                bd=1,
                relief="solid"
            )
            card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")

            # Create inner frame to hold card content
            inner = tk.Frame(card, bg=Colours.col2)
            inner.pack(expand=True, fill="both")

            # Load the item's image from file path
            image = Image.open(item["image"])

            # Resize image to fit card dimensions (120x100 pixels)
            image = image.resize((120, 100))
            # Convert PIL Image to Tkinter-compatible PhotoImage
            photo = ImageTk.PhotoImage(image)

            # Store image reference to prevent garbage collection
            self.images.append(photo)

            # Create label to display the item image
            img = tk.Label(
                inner,
                image=photo,
                bg=Colours.col3
            )
            img.pack(fill="both", expand=True, padx=5, pady=5)

            # Display item name label
            tk.Label(
                inner,
                text=item["name"],
                bg=Colours.col2,
                fg=Colours.text,
                font=("Arial", 8, "bold"),
                wraplength=120,  # Wrap text if it exceeds 120 pixels
                justify="center"
            ).pack(pady=2)

            # Display item price label
            tk.Label(
                inner,
                text=item["price"],
                bg=Colours.col2,
                fg=Colours.col4,
                font=("Arial", 8)
            ).pack()

            # ===== ACTION BUTTONS =====
            # Create frame to hold the View and Save buttons
            button_frame = tk.Frame(inner, bg=Colours.col2)
            button_frame.pack(pady=5)

            # View button - opens detailed view of the item
            # Lambda captures the current item to pass to the viewItem method
            tk.Button(
                button_frame,
                text="View",
                bg=Colours.col3,
                fg=Colours.text,
                command = lambda item=item: self.viewItem(item)
            ).pack(side="left", padx=5)

            # Save button - adds item to user's saved items list
            # Lambda captures the current item to pass to the save_item method
            tk.Button(
                button_frame,
                text="Save",
                bg=Colours.col3,
                fg=Colours.text,
                command = lambda item=item: self.save_item(item)
            ).pack(side="right", padx=5)

    # ===== ITEM ACTION METHODS =====
    def save_item(self, item):
        """
        Add an item to the user's saved items list.
        Prevents duplicate entries and provides user feedback via message boxes.

        Args:
            item: Dictionary containing item details (name, price, image, etc.)
        """
        # Check if item is already in saved items to prevent duplicates
        if item not in self.controller.saved_items:
            # Add item to the saved items list
            self.controller.saved_items.append(item)
            tk.messagebox.showinfo("Saved", f"{item['name']} added to saved items!")
        else:
            # Item already exists in saved items
            tk.messagebox.showwarning("Not Saved", f"{item['name']} is already in saved items!")

    def viewItem(self, item):
        """
        Navigate to the detailed view page for the selected item.
        Updates the ViewListing frame with item details and switches to that page.

        Args:
            item: Dictionary containing item details to display
        """
        # Get reference to the ViewListing frame
        frame = self.controller.frames[ViewListing.ViewListing]
        # Update the ViewListing frame with the selected item's data
        ViewListing.ViewListing.view(frame, item)
        # Switch to the ViewListing page
        self.controller.showFrame(ViewListing.ViewListing)
