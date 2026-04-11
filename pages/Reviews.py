import tkinter as tk
from tkinter import ttk, PhotoImage
from Colours import Colours

class review():
    def __init__(self, name, rating, text):
        self.name = name
        self.rating = rating
        self.text = text

reviews = []
reviews.append(review("Betty Ball", 5, "Very good If I have a longer review does it change anything?? This is to test if there is line wrapping or not, this review needs to be quite long else it will just go on one line."))
reviews.append(review("Pria Duffy", 4, "I liked this seller very good yes"))
reviews.append(review("Nell Davidson", 3, "Not the worst not the best, would buy again from this seller"))
reviews.append(review("Kye Shaw", 2, "Not a great experience"))

class Reviews(tk.Frame):
    def __init__(self, parent, controller):
        def addPlaceholder(entry, text):
            def boxClick(_):
                if entry.get(1.0, "end-1c") == text:
                    entry.delete(1.0, tk.END)
                    entry.config(fg=Colours.text)

            def boxFocusLost(_):
                if not entry.get(1.0, "end-1c"):
                    entry.insert(1.0, text)
                    entry.config(fg="grey")

            entry.insert(1.0, text)
            entry.config(fg="grey")
            entry.bind("<Button-1>", boxClick)
            entry.bind("<Leave>", boxFocusLost)
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=Colours.bg)
        
        # Create scrollable body
        sidebar = tk.Frame(self, background=Colours.col1)
        sidebar.place(relx=0, rely=0, relwidth=0.16, relheight=1)

        self.canvas = tk.Canvas(self, bg=Colours.bg)

        self.canvas.place(relx=0.16, rely=0,relwidth=0.84, relheight=1)
        self.body = tk.Frame(self.canvas, background=Colours.bg)
        self.canvas.bind(
            "<Configure>",
            lambda _: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window(0, 0, window=self.body)
        scrollbar = tk.Scrollbar(self, command=self.canvas.yview)
        scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
        self.canvas.configure(yscrollcommand=scrollbar.set)

      
        self.body.columnconfigure(0, weight=1)
        # Load sidebar
        lblReviews = tk.Label(sidebar, text="Customer Reviews", anchor="center", background=Colours.col1, foreground=Colours.text)
        lblReviews.pack()
        
        frmStars = tk.Frame(sidebar,background=Colours.col1)
        frmStars.pack()
        self.imgStarIcon = PhotoImage(file="icons/starS.png")
        for i in range(0, 5):
            for j in range(0, 5-i):
               tk.Label(frmStars, image=self.imgStarIcon, background=Colours.col1).grid(row=i, column=j)
            tk.Label(frmStars, text=f"{i*3}",background=Colours.col1, foreground=Colours.text).grid(row=i, column=5-i)
        # Load Add reviews box and button
        self.txtAddReview = tk.Text(self.body, background=Colours.col2, height=20)
        addPlaceholder(self.txtAddReview, "Share your thoughts...")
        self.txtAddReview.grid(row=0, sticky='new', padx=20)
        self.scale = tk.Scale(self.body, from_=5, to=1)
        self.scale.grid(row=0, column=1, sticky='ns')
        btnAddReview = tk.Button(self.body, text="Submit review",background=Colours.col3, command=self.addReviewButton)
        btnAddReview.grid(row=1, sticky='ew', padx=20, pady=20, columnspan=2)
        self.frmReviews = tk.Frame(self.body, background=Colours.bg)
        self.frmReviews.grid(row=2,columnspan=2)
        self.loadReviews()

    def updateScrollRegion(self):
        self.canvas.update_idletasks()
        
    def loadReviews(self):
        for review in reviews:
            self.addReview(review)

    def addReviewButton(self):
        thisReview = review(self.controller.username, self.scale.get(), self.txtAddReview.get('1.0', 'end-1c'))
        reviews.append(thisReview)
        self.addReview(thisReview)
        
    def addReview(self, review):
        frmReview = tk.Frame(self.frmReviews, background=Colours.bg)
        frmReview.pack(anchor="nw")
        frmNameStars = tk.Frame(frmReview,background=Colours.bg)
        frmNameStars.pack(anchor="nw")
        tk.Label(frmNameStars, text=review.name, background=Colours.bg, foreground=Colours.text, font=("Arial", 32)).pack(side="left")
        for i in range(0, review.rating):
            tk.Label(frmNameStars, image=self.imgStarIcon, background=Colours.bg).pack(side="right")
            
        tk.Label(frmReview,text=review.text, pady=10, background=Colours.bg, foreground=Colours.text, wraplength=1000, justify=tk.LEFT, font=("Arial", 20)).pack(side="bottom")
        self.updateScrollRegion()
