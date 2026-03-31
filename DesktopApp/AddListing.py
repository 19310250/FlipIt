import tkinter as tk
import Colours

### use this new top frame to handle AddListing as done with the other classes
class AddListing(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Add listing Page")
        self.geometry("950x650")
        self.config(bg=Colours.col2)





#
# class AddListing (tk.Toplevel):
#     def __init__(self):
#         def addPlaceholder(entry, text):
#             def boxClick(_):
#                 if entry.get(1.0, "end-1c") == text:
#                     entry.delete(1.0, tk.END)
#                     entry.config(fg=Colours.text)
#
#             def boxFocusLost(_):
#                 if not entry.get(1.0, "end-1c"):
#                     entry.insert(1.0, text)
#                     entry.config(fg="grey")
#
#             entry.insert(1.0, text)
#             entry.config(fg="grey")
#             entry.bind("<Button-1>", boxClick)
#             entry.bind("<Leave>", boxFocusLost)
#
#         tk.Frame.__init__(self)
#         self.config(bg=Colours.bg)
#         lblName = tk.Label(self, text= "Item name:", background=Colours.bg, foreground=Colours.text)
#         lblName.pack(anchor="nw", padx=20)
#         txtName = tk.Text(self, height=1, wrap="none", background=Colours.col2, foreground=Colours.text)
#         addPlaceholder(txtName, "What should people search for to find this item....")
#         txtName.pack(anchor="nw", padx=20)
#
#         lblPhoto = tk.Label(self, text= "Add photo:", background=Colours.bg, foreground=Colours.text)
#         lblPhoto.pack(anchor="nw", padx= 20)
#
#         frmPhotoUpload = tk.Frame(self, height=300, background=Colours.col2)
#         frmPhotoUpload.pack(fill=tk.X, padx=20,pady=20)
#         self.imgPhotoIcon = PhotoImage(file="imgs/icons/photo-icon.png")
#         lblUploadImg = tk.Label(frmPhotoUpload, image=self.imgPhotoIcon, background=Colours.col2)
#         lblUploadImg.pack(fill = "both", expand = True)
#         lblAddPhoto = tk.Label(frmPhotoUpload, text="Click to add photos", foreground=Colours.text, background=Colours.col2)
#         lblAddPhoto.pack(pady=20)
#
#         lblDescription = tk.Label(self, text="Description:", background=Colours.bg, foreground=Colours.text)
#         lblDescription.pack(anchor="nw", padx=20)
#         txtDescription = tk.Text(self, height = 20, background=Colours.bg, foreground=Colours.text)
#         addPlaceholder(txtDescription, "Write about what you are selling, what is included in the box, and any extra information...")
#         txtDescription.pack(fill="x", padx=20)
#
#         lblCondition = tk.Label(self, text="Condition:", background=Colours.bg, foreground=Colours.text)
#         lblCondition.pack(anchor="nw", padx=20)
#         conditions = [ "New", "Used - Like new", "Used - Very good", "Used - Good", "For parts or not working" ]
#         cbConditions = ttk.Combobox(self, background=Colours.bg, values=conditions, foreground= Colours.text, state="readonly")
#         cbConditions.set("Select a condition")
#         cbConditions.pack(fill="x", padx=20)
