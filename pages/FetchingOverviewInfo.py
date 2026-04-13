import tkinter as tk
from Colours import Colours




class FetchingOverviewInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #self.title("Overview Items Bought")
       ## self.geometry("800x600")
        self.config(bg=Colours.col2)

        # TOP BAR
        # top_frame = tk.Frame(self, bg=Colours.col2)
        # top_frame.pack(fill="x")
        #
        # tk.Label(
        #     top_frame,
        #     text="FlipIt",
        #     font=("Arial", 20),
        #     bg=Colours.col2
        # ).pack(anchor="w", padx=5, pady=40)

        frame_name = tk.Frame(self, bg=Colours.col2)
        tk.Label(frame_name, text="Click to view bought item", font=("Arial", 20),  bg=Colours.col2).pack(padx=5, pady=20)
        frame_name.pack(fill="x", pady=20)

        # MAIN CONTAINER (LEFT + RIGHT)
        main_frame = tk.Frame(self, bg=Colours.col2)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Configure grid
        main_frame.columnconfigure(0, weight=1)  # left
        main_frame.columnconfigure(1, weight=2)  # right

        # LEFT PANEL (Overview)
        left_frame = tk.Frame(main_frame, bg="white", relief="solid", bd=1)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5)

        tk.Label(left_frame, text="Item Overview", font=("Arial", 16), bg="white").pack(pady=10)

        self.name_label = tk.Label(left_frame, text="Name: ", bg="white", anchor="w")
        self.name_label.pack(fill="x", padx=10, pady=5)

        self.ref_label = tk.Label(left_frame, text="Reference: ", bg="white", anchor="w")
        self.ref_label.pack(fill="x", padx=10, pady=5)

        self.date_label = tk.Label(left_frame, text="Date: ", bg="white", anchor="w")
        self.date_label.pack(fill="x", padx=10, pady=5)


        # RIGHT PANEL (List + Scrollbar)
        right_frame = tk.Frame(main_frame, bg=Colours.col2)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=5)

        scrollbar = tk.Scrollbar(right_frame)
        scrollbar.pack(side="right", fill="y")

        self.item_list = tk.Listbox(
            right_frame,
            yscrollcommand=scrollbar.set,
            font=("Arial", 12)
        )
        self.item_list.pack(fill="both", expand=True)

        scrollbar.config(command=self.item_list.yview)

        # SAMPLE DATA
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

        # Populate listbox
        for i, item in enumerate(self.items):
            self.item_list.insert(tk.END, f"{i+1}. {item[0]}")

        # EVENT: when item clicked
        self.item_list.bind("<<ListboxSelect>>", self.show_item_details)


    # UPDATE LEFT PANEL
    def show_item_details(self, event):
        selection = self.item_list.curselection()
        if not selection:
            return

        index = selection[0]
        name, ref, date = self.items[index]

        self.name_label.config(text=f"Name: {name}")
        self.ref_label.config(text=f"Reference: {ref}")
        self.date_label.config(text=f"Date: {date}")
