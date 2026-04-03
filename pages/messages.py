import tkinter as tk
from tkinter import ttk
from Colours import Colours
import json
import os

class MessagesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=Colours.bg)
        self.controller = controller
        self.history_file = "chat_history.json" # Where the data lives

        # --- TITLE ---
        tk.Label(self, text="Inbox", font=("Arial", 24, "bold"), 
                 fg=Colours.text, bg=Colours.bg).pack(pady=20)

        # --- MAIN CONTAINER ---
        self.main_container = tk.Frame(self, bg=Colours.bg)
        self.main_container.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # --- SIDEBAR ---
        self.sidebar = tk.Frame(self.main_container, width=200, bg=Colours.col2)
        self.sidebar.pack(side="left", fill="y", padx=(0, 10))
        self.sidebar.pack_propagate(False)

        # --- CHAT INTERFACE ---
        self.chat_interface = tk.Frame(self.main_container, bg="white")
        self.chat_interface.pack(side="right", fill="both", expand=True)

        self.input_frame = tk.Frame(self.chat_interface, bg="white")
        self.input_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        self.entry = tk.Entry(self.input_frame, font=("Arial", 12), relief="solid", borderwidth=1)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=5)
        self.entry.bind("<Return>", lambda event: self.send_message())

        self.send_btn = tk.Button(self.input_frame, text="Send", bg=Colours.col4, fg="white",
                                  command=self.send_message, padx=20)
        self.send_btn.pack(side="right")

        self.display = tk.Text(self.chat_interface, state='disabled', bg="#f8f9fa", 
                               font=("Arial", 11), padx=15, pady=15, borderwidth=0)
        self.display.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        # LOAD EXISTING MESSAGES ON STARTUP
        self.load_chat_history()

    def send_message(self):
        text = self.entry.get()
        if text.strip():
            # Update the UI
            self.update_chat_display(f"You: {text}")
            
            # SAVE TO FILE
            self.save_to_json(text)
            
            self.entry.delete(0, tk.END)

    def update_chat_display(self, message):
        """Helper to push text to the screen"""
        self.display.config(state='normal')
        self.display.insert(tk.END, message + "\n\n")
        self.display.see(tk.END)
        self.display.config(state='disabled')

    def save_to_json(self, message):
        """Writes the message to the JSON file"""
        data = []
        # 1. Read existing data if file exists
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

        # 2. Add new message
        data.append({"sender": "You", "text": message})

        # 3. Write back to file
        with open(self.history_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_chat_history(self):
        """Reads the JSON file and populates the display"""
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as f:
                try:
                    data = json.load(f)
                    for msg in data:
                        self.update_chat_display(f"{msg['sender']}: {msg['text']}")
                except json.JSONDecodeError:
                    pass