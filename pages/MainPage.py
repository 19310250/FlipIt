import tkinter as tk
from PIL import Image, ImageTk

from Colours import Colours

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=Colours.bg)

        # SCROLLABLE AREA
        container = tk.Frame(self, bg=Colours.bg)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg=Colours.bg, highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

        scrollable_frame = tk.Frame(canvas, bg=Colours.bg)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        ## item names
        item_names = ["air fryer", "chromebook c434", "IKEA's HAMMARN", "iphone 17", "macbook pro", "jbl tour pro", "Monitor XDR",
                      "ryzen pc", "HP envy 123", "Hamlet by WS", "CGP combined science", "carrera bike", "kids scince kits",
                      "exercise book", "exam kits pack", "van rysel helmet", "reading glass", "casio calculator", "jade suitcase",
                      "highbury backpack ", "sony WH-1000XM6", "american freezer", "cost road bed", "office cupboard",
                      "revision desk", "Nvidia rtx 4060", "bundle jeans", "lord of the rink", "nba basketball", "anko toaster" ,
                      ]

        items_path = ["imgs/img/airfryer.gif", "imgs/img/chromebookflip.png", "imgs/img/hammarn.png",
                      "imgs/img/iphone17.png", "imgs/img/macbookpro.png", "imgs/img/jbltourpro.png",
                      "imgs/img/monitorxdr.png",
                      "imgs/img/ryzenpc.png", "imgs/img/hpenvy123.png", "imgs/img/hamletws.png",
                      "imgs/img/cgpscience.png", "imgs/img/carrerabike.png", "imgs/img/kidsscience.png",
                      "imgs/img/exercisebook.png",
                      "imgs/img/examkitpack.png", "imgs/img/halfordhelmet.png", "imgs/img/readingglass.png",
                      "imgs/img/casiocalculator.png", "imgs/img/jadedesignsuitcase.png",
                      "imgs/img/highburyback.png", "imgs/img/sonyheadphone.png", "imgs/img/americanfreezer.png",
                      "imgs/img/costbed.png", "imgs/img/officecupboard.png", "imgs/img/revisiondesk.png",
                      "imgs/img/nvidiartx.png", "imgs/img/bundlejeans.png", "imgs/img/booklordring.png",
                      "imgs/img/basketballnba.png", "imgs/img/ankotoaster.png",

                      ]

        # SAMPLE DATA

        self.items = [
            {"name": f"{item_names[i]}", "price": f"£{(i+1)*10}"}
            for i in range(30)
        ]

        rows, cols = 3, 10


        # GRID CONFIG
        for c in range(cols):
            scrollable_frame.grid_columnconfigure(c, weight=1)

        for r in range(rows):
            scrollable_frame.grid_rowconfigure(r, weight=1)

        # CREATE CARDS
        self.images = []  # store images

        for index, item in enumerate(self.items):
            r = index // cols
            c = index % cols

            card = tk.Frame(
                scrollable_frame,
                bg=Colours.col2,
                bd=1,
                relief="solid"
            )
            card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")

            inner = tk.Frame(card, bg=Colours.col2)
            inner.pack(expand=True, fill="both")


            image = Image.open(items_path[index])


            image = image.resize((120, 100))
            photo = ImageTk.PhotoImage(image)

            # store image reference
            self.images.append(photo)

            img = tk.Label(
                inner,
                image=photo,
                bg=Colours.col3
            )
            img.pack(fill="both", expand=True, padx=5, pady=5)

            # Name
            tk.Label(
                inner,
                text=item["name"],
                bg=Colours.col2,
                fg=Colours.text,
                font=("Arial", 8, "bold"),
                wraplength=120,
                justify="center"
            ).pack(pady=2)

            # Price
            tk.Label(
                inner,
                text=item["price"],
                bg=Colours.col2,
                fg=Colours.col4,
                font=("Arial", 8)
            ).pack()

            # Button
            tk.Button(
                inner,
                text="View",
                bg=Colours.col3,
                fg=Colours.text
            ).pack(pady=5)
