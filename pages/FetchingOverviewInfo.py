import tkinter as tk
from Colours import Colours


class FetchingOverviewInfo(tk.Frame):
    """
    A Tkinter Frame that displays an overview of purchased items.
    Features a two-panel layout: left panel shows selected item details,
    right panel displays a scrollable list of all items.
    """

    def __init__(self, parent, controller):
        """
        Initialize the FetchingOverviewInfo frame.

        Args:
            parent: The parent widget that contains this frame
            controller: The main application controller for managing page navigation
        """
        tk.Frame.__init__(self, parent)
        #self.title("Overview Items Bought")
       ## self.geometry("800x600")

        # Set the background color for the frame
        self.config(bg=Colours.col2)

        # ===== PAGE TITLE SECTION =====
        # Create a frame to hold the page title
        frame_name = tk.Frame(self, bg=Colours.col2)
        # Display instruction label for the user
        tk.Label(frame_name, text="Click to view bought item", font=("Arial", 20),  bg=Colours.col2).pack(padx=5, pady=20)
        frame_name.pack(fill="x", pady=20)

        # ===== MAIN CONTAINER (TWO-PANEL LAYOUT) =====
        # Create the main frame to hold both left and right panels
        main_frame = tk.Frame(self, bg=Colours.col2)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Configure grid columns with different weights for responsive layout
        main_frame.columnconfigure(0, weight=1)  # Left panel (item details) - takes 1/3 of space
        main_frame.columnconfigure(1, weight=2)  # Right panel (item list) - takes 2/3 of space

        # ===== LEFT PANEL (ITEM DETAILS OVERVIEW) =====
        # Create left panel with white background and border for item details display
        left_frame = tk.Frame(main_frame, bg="white", relief="solid", bd=1)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5)

        # Display the panel title
        tk.Label(left_frame, text="Item Overview", font=("Arial", 16), bg="white").pack(pady=10)

        # Create label to display the selected item's name
        self.name_label = tk.Label(left_frame, text="Name: ", bg="white", anchor="w")
        self.name_label.pack(fill="x", padx=10, pady=5)

        # Create label to display the selected item's reference number
        self.ref_label = tk.Label(left_frame, text="Reference: ", bg="white", anchor="w")
        self.ref_label.pack(fill="x", padx=10, pady=5)

        # Create label to display the selected item's purchase date
        self.date_label = tk.Label(left_frame, text="Date: ", bg="white", anchor="w")
        self.date_label.pack(fill="x", padx=10, pady=5)


        # ===== RIGHT PANEL (SCROLLABLE ITEM LIST) =====
        # Create right panel to display the list of all purchased items
        right_frame = tk.Frame(main_frame, bg=Colours.col2)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=5)

        # Create a vertical scrollbar for the listbox
        scrollbar = tk.Scrollbar(right_frame)
        scrollbar.pack(side="right", fill="y")

        # Create the listbox to display all items with scrollbar support
        self.item_list = tk.Listbox(
            right_frame,
            yscrollcommand=scrollbar.set,  # Link listbox to scrollbar
            font=("Arial", 12)
        )
        self.item_list.pack(fill="both", expand=True)

        # Configure scrollbar to control the listbox view
        scrollbar.config(command=self.item_list.yview)

        # ===== SAMPLE DATA =====
        # List of purchased items - each tuple contains (name, reference, date)
        # In production, this would be fetched from a database
        self.items = [
            ("Iphone 17", "techphone@2025", "01/03/2025"),
            ("Laptop X", "laptop@2025", "12/02/2025"),
            ("Headphone tour pro", "audio@2025", "05/01/2025"),
            ("Monitor XDR", "display@2025", "20/12/2024"),
            ("Keyboard", "input@2025", "15/11/2024"),

            ("Gaming Ryzen pc", "gamepc@2017", "04/09/2017"),
            ("printer 123D ", "techprinter@2017", "22/01/2017"),
            ("Hamlet by WS", "bookws@2016", "10/01/2016"),
            ("combined science", "bookbbc@2025", "20/01/2016"),
            ("bike carrera", "cyclebike@2013", "5/03/2013"),
            ("bulk clothes", "clothexh@2013", "20/01/2013"),
            ("science kits", "sciencekits@2013", "10/05/2010"),
        ]

        # Populate the listbox with item names (numbered list)
        for i, item in enumerate(self.items):
            self.item_list.insert(tk.END, f"{i+1}. {item[0]}")

        # Bind selection event - when user clicks an item, display its details
        self.item_list.bind("<<ListboxSelect>>", self.show_item_details)


    # ===== EVENT HANDLER =====
    def show_item_details(self, event):
        """
        Update the left panel with details of the selected item from the list.
        Called automatically when a user clicks on an item in the listbox.

        Args:
            event: The listbox selection event
        """
        # Get the index of the currently selected item
        selection = self.item_list.curselection()

        # If no item is selected, do nothing
        if not selection:
            return

        # Extract the selected item's index and retrieve its data
        index = selection[0]
        name, ref, date = self.items[index]

        # Update the left panel labels with the selected item's information
        self.name_label.config(text=f"Name: {name}")
        self.ref_label.config(text=f"Reference: {ref}")
        self.date_label.config(text=f"Date: {date}")
