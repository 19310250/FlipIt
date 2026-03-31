import tkinter as tk
import MainPage
import Colours


class LoginPage(tk.Tk):

    def __init__(self):
        super().__init__()
        self.main_page_button = None

        self.geometry("1500x800")
        self.title("FlipIt")
        self.config(background=Colours.bg)
       #self.resizable(width=False, height=False)

        # creating top frame
        top_frame = tk.Frame(self, bg=Colours.col1)
        top_frame.pack(fill="x")

        tk.Label(
            top_frame,
            text="Login Page",
            font=("Arial", 22, "bold"),
            bg=Colours.col1,
            fg=Colours.text
        ).pack(side="left", padx=15, pady=10)


    ## open the next page: main page
    def OpenMainPage(self):
        # Button container
        button_frame = tk.Frame(self, bg=Colours.bg)
        button_frame.pack(pady=300)

        # Button
        tk.Button(
            button_frame,
            bg=Colours.col1,
            text="Login",
            font=("Arial", 15),
            command= lambda:MainPage.MainPage()).grid(row=0, column=0, padx=10, pady=10)

if __name__ == "__main__":
    root = LoginPage()
    root.OpenMainPage()
    root.mainloop()

