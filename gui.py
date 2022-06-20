from tkinter import *
import tkinter as tk
import customtkinter as ct

import passGen
from passGen import Generator


class PassGUI:

    root = ct.CTk()

    #---------------------------- Main Components
    main_frame = ct.CTkFrame(root)
    main_result_label = None

    def __init__(self):
        self.config()
        self.screen_size("main")
        self.build_main()
        self.root.mainloop()

    def config(self):
        ct.set_appearance_mode("Dark")
        ct.set_default_color_theme("blue")
        self.root.resizable(False, False)
        self.root.title("Password Generator")


    def build_main(self):
        web_entry = ct.CTkEntry(master=self.main_frame,
                               placeholder_text="Website",
                               width=100,
                               height=25,
                               border_width=2,
                               corner_radius=10)

        user_entry = ct.CTkEntry(master=self.main_frame,
                        placeholder_text="Username",
                        width=100,
                        height=25,
                        border_width=2,
                        corner_radius=10)

        gen_button = ct.CTkButton(master=self.main_frame,
                              text="Generate Password", 
                              command=lambda: self.get_password(web_entry.get(), user_entry.get()))

        self.main_result_label = ct.CTkLabel(master=self.main_frame, text="", text_font=("Helvetica", 10))

        web_entry.place(x=50, y=25)
        user_entry.place(x=50, y=60)
        gen_button.place(x=30, y=100)
        self.main_result_label.place(x=-17, y=135)

        self.main_frame.pack()

    def screen_size(self, screen):
        w = {"main": 450, }
        h = {"main": 300, }
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w.get(screen) / 2)
        y = (hs / 2) - (h.get(screen) / 2)
        self.root.geometry('%dx%d+%d+%d' % (w.get(screen), h.get(screen), x, y))

    def get_password(self, website, username, resultLabel=None):
        if "" in [website, username]:
            print("empty")
            self.main_result_label.config(text="Invalid website or username")
            return 0
        print("generating password")

        


