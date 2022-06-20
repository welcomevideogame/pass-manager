from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar
import customtkinter as ct
from cleanser import Clean
from functools import partial

import passGen
from passGen import Generator


class PassGUI:

    root = ct.CTk()

    #---------------------------- Main Components
    main_dim_w = 330
    main_dim_h = 275
    main_frame = ct.CTkFrame(root, width=main_dim_w, height=main_dim_h)
    main_slider_label = None
    max_pass_length = 128
    passwordLevel = 1

    #---------------------------- Settings Components
    settings_dim_w = 350
    settings_dim_h = 350
    settings_frame = ct.CTkFrame(root, width=settings_dim_w, height=settings_dim_h)
    progressbar = None

    settings_config = []
    settings_config.append(False)   # symbols
    settings_config.append(True)    # numbers
    settings_config.append(True)    # lowercase
    settings_config.append(True)    # uppercase
    settings_config.append(False)   # punctuation
    security_levels = [30, 20, 10, 20, 20]


    def __init__(self):
        self.config()
        self.screen_size("main")
        self.build_main()
        self.build_settings()
        self.root.mainloop()

    def config(self):
        ct.set_appearance_mode("Dark")
        ct.set_default_color_theme("blue")
        self.root.resizable(False, False)
        self.root.title("Password Generator")


    def build_main(self):
        web_entry = ct.CTkEntry(master=self.main_frame,
                               placeholder_text="Website",
                               width=150,
                               height=32,
                               border_width=2,
                               corner_radius=10)

        user_entry = ct.CTkEntry(master=self.main_frame,
                        placeholder_text="Username",
                        width=150,
                        height=32,
                        border_width=2,
                        corner_radius=10)

        slider = ct.CTkSlider(master=self.main_frame, from_=8, to=self.max_pass_length, number_of_steps=64, command = self.update_slider_label)
        self.main_slider_label = ct.CTkLabel(master=self.main_frame, text=int(self.max_pass_length/2))

        gen_button = ct.CTkButton(master=self.main_frame,
                              text="Generate Password", 
                              command=lambda: self.get_password(web_entry.get(), user_entry.get()))

        settings_button = ct.CTkButton(master=self.main_frame,
                                       text="Settings",
                                       width=10,
                                       corner_radius=10,
                                       command=lambda: self.change_screen("main", "settings"))

        web_entry.place(relx=.5, rely=.15, anchor=tk.CENTER)
        user_entry.place(relx=.5, rely=.35, anchor=tk.CENTER)
        slider.place(relx=0.5, rely=0.58, anchor=tk.CENTER)
        self.main_slider_label.place(relx=0.5, rely=0.50, anchor=tk.CENTER)
        gen_button.place(relx=.5, rely=.80, anchor=tk.CENTER)
        settings_button.place(relx=.87, rely=.1, anchor=tk.CENTER)

        self.main_frame.pack()

    def update_slider_label(self, value):
        self.main_slider_label.config(text=str(int(value)))

    def build_settings(self):
        titles = Clean.left_justify(["Symbols", "Numbers", "Lowercase", "Uppercase", "Punctuation"])
        values = self.settings_config
        boxes = []

        for i in range(len(titles)):
            label = ct.CTkLabel(master=self.settings_frame, text=f"Include {titles[i]}", width=200)
            label.place(relx=.3, rely=0.1 + (i*0.13), anchor=tk.CENTER)

            boxes.append(ct.CTkCheckBox(master=self.settings_frame,
                                      onvalue="on", offvalue="off", text="",))
            if values[i]: boxes[i].select() 
            else: boxes[i].deselect
            boxes[i].config(command=lambda v=i: self.update_settings(v))
            boxes[i].place(relx=.7, rely=0.1 + (i*0.13), anchor=tk.CENTER)

        back_button = ct.CTkButton(master=self.settings_frame,
                                text="Back",
                                width=10,
                                corner_radius=10,
                                command=lambda: self.change_screen("settings", "main"))
        back_button.place(relx=.87, rely=.1, anchor=tk.CENTER)
        
        self.progressbar = ct.CTkProgressBar(master=self.settings_frame)
        self.update_security_bar()
        self.progressbar.place(relx=.5, rely=.8, anchor=tk.CENTER)

    
    def update_settings(self, index):
        self.settings_config[index] = not self.settings_config[index]
        self.update_security_bar()
    
    def update_security_bar(self):
        total_security = 0
        for i in range(len(self.settings_config)):
            if self.settings_config[i]:
                total_security += (self.security_levels[i] / 100) 
        self.progressbar.set(total_security)
        if total_security > 0.75:
            self.progressbar.configure(progress_color="green")
        elif total_security > 0.50:
            self.progressbar.configure(progress_color="yellow")
        elif total_security > 0.35:
            self.progressbar.configure(progress_color="orange")
        else:
            self.progressbar.configure(progress_color="red")
        
            
    def screen_size(self, screen):
        w = {"main": self.main_dim_w, 
            "settings": self.settings_dim_w}
        h = {"main": self.main_dim_h, 
            "settings": self.settings_dim_h}
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w.get(screen) / 2)
        y = (hs / 2) - (h.get(screen) / 2)
        self.root.geometry('%dx%d+%d+%d' % (w.get(screen), h.get(screen), x, y))

    def change_screen(self, old_screen, new_screen):
        if old_screen == "main":
            self.main_frame.forget()
        elif old_screen == "settings":
            self.settings_frame.forget()
        
        if new_screen == "main":
            self.main_frame.pack()
            self.screen_size("main")
        elif new_screen == "settings":
            self.settings_frame.pack()
            self.screen_size("settings")

    def get_password(self, website, username):
        if "" in [website, username]:
            print("empty")
            self.main_result_label.config(text="Invalid website or username")
            return 0
        print("generating password")
