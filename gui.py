import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import askyesno
import customtkinter as ct

from passGen import Generator
from encrypt import Encryption
from cleanser import Clean
from saveFile import Save
import pyperclip

class PassGUI:

    root = ct.CTk()
    file_system = None

    #---------------------------- Main Components
    main_dim_w = 330
    main_dim_h = 275
    main_frame = ct.CTkFrame(root, width=main_dim_w, height=main_dim_h)
    main_slider = None
    main_slider_label = None
    logins_button = None
    mode_button = None
    main_password_entry = None
    main_web_entry = None
    main_user_entry = None
    main_gen_button = None
    max_pass_length = 128
    passwordLevel = 1
    file_location = None
    key_location = None
    mode = 2

    #---------------------------- Settings Components
    settings_dim_w = 350
    settings_dim_h = 400
    settings_frame = ct.CTkFrame(root, width=settings_dim_w, height=settings_dim_h)
    progressbar = None

    settings_config = []
    settings_config.append(False)   # symbols
    settings_config.append(True)    # numbers
    settings_config.append(True)    # lowercase
    settings_config.append(True)    # uppercase
    settings_config.append(False)   # punctuation
    settings_config.append(False)   # true 
    security_levels = [30, 20, 10, 20, 20]
    password_length = 64

    #---------------------------- Login Page Components
    logins_dim_w = 500
    logins_dim_h = 200
    logins_frame = ct.CTkFrame(root, width=logins_dim_w, height=logins_dim_h)
    login_combobox = None
    login_combobox2 = None
    login_username_field = None
    login_password_field = None

    def __init__(self):
        self.config()
        self.screen_size("main")
        self.build_main()
        self.build_settings()
        self.build_logins()
        self.root.mainloop()

    def config(self):
        ct.set_appearance_mode("Dark")
        ct.set_default_color_theme("blue")
        self.root.resizable(False, False)
        self.root.title("Password Generator")
        self.root.iconbitmap('./resources/key.ico')

    def build_main(self):
        self.main_web_entry = ct.CTkEntry(master=self.main_frame,
                               placeholder_text="Website",
                               width=150,
                               height=32,
                               border_width=2,
                               corner_radius=10)

        self.main_user_entry = ct.CTkEntry(master=self.main_frame,
                        placeholder_text="Username",
                        width=150,
                        height=32,
                        border_width=2,
                        corner_radius=10)

        self.main_password_entry = ct.CTkEntry(master=self.main_frame,
                placeholder_text="Password",
                width=150,
                height=32,
                border_width=2,
                corner_radius=10,
                show="*")

        self.main_slider = ct.CTkSlider(master=self.main_frame, from_=8, to=self.max_pass_length, number_of_steps=64, command = self.update_slider_label)
        self.main_slider_label = ct.CTkLabel(master=self.main_frame, text=int(self.max_pass_length/2))

        self.main_gen_button = ct.CTkButton(master=self.main_frame,
                                text="Generate Password", 
                                command=lambda: self.get_password(self.main_web_entry.get(), self.main_user_entry.get()))

        settings_button = ct.CTkButton(master=self.main_frame,
                                text="Settings",
                                width=75,
                                corner_radius=10,
                                command=lambda: self.change_screen("main", "settings"))

        self.logins_button = ct.CTkButton(master=self.main_frame,
                                text="Logins",
                                width=75,
                                corner_radius=10,
                                command=lambda: self.change_screen("main", "logins"))

        self.mode_button = ct.CTkButton(master=self.main_frame,
                        text="Mode",
                        width=75,
                        corner_radius=10,
                        command=lambda: self.change_main_mode())

        self.main_web_entry.place(relx=.5, rely=.15, anchor=tk.CENTER)
        self.main_user_entry.place(relx=.5, rely=.35, anchor=tk.CENTER)
        self.main_slider.place(relx=0.5, rely=0.58, anchor=tk.CENTER)
        self.main_slider_label.place(relx=0.5, rely=0.50, anchor=tk.CENTER)
        self.main_gen_button.place(relx=.5, rely=.80, anchor=tk.CENTER)
        self.mode_button.place(relx=.87, rely=.25, anchor=tk.CENTER)
        settings_button.place(relx=.87, rely=.1, anchor=tk.CENTER)

        self.main_frame.pack()

    def change_main_mode(self):
        if self.mode == 1:
            self.mode = 2
            self.main_slider.place(relx=0.5, rely=0.58, anchor=tk.CENTER)
            self.main_slider_label.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

            self.main_password_entry.place_forget()
            self.main_gen_button.config(text="Generate Password", command=lambda: self.get_password(self.main_web_entry.get(), self.main_user_entry.get()))
        else:
            self.mode = 1
            self.main_slider_label.place_forget()
            self.main_slider.place_forget()

            self.main_password_entry.place(relx=.5, rely=.55, anchor=tk.CENTER)
            self.main_gen_button.config(text="Save Password", command=lambda: self.save_custom_password(self.main_web_entry.get(), self.main_user_entry.get(), self.main_password_entry.get()))

    def update_slider_label(self, value):
        self.main_slider_label.config(text=str(int(value)))
        self.password_length = value

    def build_settings(self):
        titles = Clean.left_justify(["Symbols", "Numbers", "Lowercase", "Uppercase", "Punctuation"])
        values = self.settings_config
        boxes = []

        for i in range(len(titles)):
            label = ct.CTkLabel(master=self.settings_frame, text=f"Include {titles[i]}", width=200)
            label.place(relx=.3, rely=0.1 + (i*0.1), anchor=tk.CENTER)

            boxes.append(ct.CTkCheckBox(master=self.settings_frame,
                                      onvalue="on", offvalue="off", text="",))
            if values[i]: boxes[i].select() 
            else: boxes[i].deselect()
            boxes[i].config(command=lambda v=i: self.update_settings(v))
            boxes[i].place(relx=.7, rely=0.1 + (i*0.1), anchor=tk.CENTER)

        label2 = ct.CTkLabel(master=self.settings_frame, text="True Random (Slower)", width=200)
        label2.place(relx=.321, rely=0.6, anchor=tk.CENTER)
        box = ct.CTkCheckBox(master=self.settings_frame, onvalue="on", offvalue="off", text="", command=lambda: self.update_settings(5))
        box.place(relx=.7, rely=0.6, anchor=tk.CENTER)

        back_button = ct.CTkButton(master=self.settings_frame,
                                text="Back",
                                width=10,
                                corner_radius=10,
                                command=lambda: self.change_screen("settings", "main"))

        gen_key_button = ct.CTkButton(master=self.settings_frame,
                                text="Generate Key",
                                width=130,
                                corner_radius=10,
                                command=lambda: self.generate_key())

        sel_key_button = ct.CTkButton(master=self.settings_frame,
                                text="Select Key",
                                width=130,
                                corner_radius=10,
                                command=lambda: self.select_key())

        gen_log_button = ct.CTkButton(master=self.settings_frame,
                                text="Generate Savefile",
                                width=130,
                                corner_radius=10,
                                command=lambda: self.generate_savefile())

        sel_log_button = ct.CTkButton(master=self.settings_frame,
                                text="Select Savefile",
                                width=130,
                                corner_radius=10,
                                command=lambda: self.select_savefile())
        
        self.progressbar = ct.CTkProgressBar(master=self.settings_frame)
        self.update_security_bar()
        self.progressbar.place(relx=.5, rely=.75, anchor=tk.CENTER)
        back_button.place(relx=.87, rely=.1, anchor=tk.CENTER)

        gen_key_button.place(relx=.3, rely=.84, anchor=tk.CENTER)
        sel_key_button.place(relx=.3, rely=.95, anchor=tk.CENTER)
        gen_log_button.place(relx=.7, rely=.84, anchor=tk.CENTER)
        sel_log_button.place(relx=.7, rely=.95, anchor=tk.CENTER)

    def build_logins(self):
        clipboard_image = tk.PhotoImage(file='./resources/clipboard.png')
        self.login_combobox = ct.CTkComboBox(master=self.logins_frame)
        self.login_combobox2 = ct.CTkComboBox(master=self.logins_frame)
        self.login_username_field = ct.CTkEntry(master=self.logins_frame,
                        placeholder_text="Username",
                        width=380,
                        height=32,
                        border_width=2,
                        corner_radius=0,
                        state="readonly",
                        text_color="black")

        self.login_password_field = ct.CTkEntry(master=self.logins_frame,
                        placeholder_text="Password",
                        width=380,
                        height=32,
                        border_width=2,
                        corner_radius=0,
                        state="readonly",
                        text_color="black")

        back_button = ct.CTkButton(master=self.logins_frame,
                        text="Back",
                        width=30,
                        corner_radius=10,
                        command=lambda: self.change_screen("logins", "main"))

        username_button = ct.CTkButton(master=self.logins_frame,
                        image=clipboard_image,
                        text="",
                        width=10,
                        corner_radius=0,
                        command=lambda: self.copy_clipboard(self.login_username_field.get()))

        password_button = ct.CTkButton(master=self.logins_frame,
                        image=clipboard_image,
                        width=10,
                        text="",
                        corner_radius=0,
                        command=lambda: self.copy_clipboard(self.login_password_field.get()))

        self.login_combobox.place(relx=.2, rely=.2, anchor=tk.CENTER)
        self.login_combobox2.place(relx=.5, rely=.2, anchor=tk.CENTER)
        back_button.place(relx=.87, rely=.2, anchor=tk.CENTER)

        self.login_username_field.place(relx=.42, rely=.55, anchor=tk.CENTER)
        self.login_password_field.place(relx=.42, rely=.8, anchor=tk.CENTER)
        username_button.place(relx=.9, rely=.55, anchor=tk.CENTER)
        password_button.place(relx=.9, rely=.8, anchor=tk.CENTER)

    def copy_clipboard(self, text):
        if text != "":
            pyperclip.copy(text)


    def display_login(self, username):
        self.login_username_field.config(state="normal")  # there has to be a better way to insert text to readonly fields
        self.login_password_field.config(state="normal")
        self.clear_login_fields()

        if username != "":
            login = self.file_system.get_login(self.login_combobox.get(), username)
            self.login_username_field.insert(0, login[1])
            self.login_password_field.insert(0, login[2])

        self.login_username_field.config(state="readonly")
        self.login_password_field.config(state="readonly")

    def update_website(self, website):
        if website == "None":
            self.login_combobox2.config(values=[])
            self.login_combobox2.set("")
            self.login_combobox2.config(state="disabled")
            self.clear_login_fields()
        else:
            self.login_combobox2.set("")
            usernames = self.file_system.get_usernames(website)
            self.login_combobox2.config(state="normal")
            self.login_combobox2.config(values=usernames)
            self.clear_login_fields()

    def clear_login_fields(self):
        self.login_username_field.delete(0, END)
        self.login_password_field.delete(0, END)

    def set_login_combobox(self):
        websites = self.file_system.get_websites()
        websites.insert(0, "None")
        self.login_combobox.config(values=websites)
        self.login_combobox.set("None")
        self.login_combobox2.set("")
        self.login_combobox2.config(state="disabled")
        self.login_combobox.config(command=self.update_website)
        self.login_combobox2.config(command=self.display_login)

    def update_settings(self, index):
        self.settings_config[index] = not self.settings_config[index]
        self.update_security_bar()
    
    def update_security_bar(self):
        total_security = 0
        for i in range(len(self.settings_config) - 1):
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

    def generate_key(self):
        direc = filedialog.askdirectory()
        if direc != "":
            path = Encryption.generate_key(direc)
            if not path:
                self.invalid_file_message()
            else:
                self.key_location = path
                self.file_setup()
                self.check_files

    def generate_savefile(self):
        direc = filedialog.askdirectory()
        if direc != "":
            path = Save.create_new(direc)
            if not path:
                self.invalid_file_message()
            else:
                self.file_location = path
                self.file_setup()
                self.check_files()

    def select_key(self):
        file = filedialog.askopenfile(filetypes=[('Key Files', '*.key')])
        if file:
            self.key_location = os.path.abspath(file.name)
            self.check_files()

    def select_savefile(self):
        file = filedialog.askopenfile(filetypes=[('Comma Separated Value Files', '*.csv')])
        if file:
            self.file_location = os.path.abspath(file.name)
            self.check_files()

    def invalid_file_message(self):
        tk.messagebox.showerror(title="Invalid", message="File already exists in this folder!")

    def file_setup(self):
        f = self.file_location
        k = self.key_location
        if f and k:
            Encryption.encrypt(f, k)

    def check_files(self):
        f = self.file_location
        k = self.key_location
        if f and k:
            self.logins_button.place(relx=.87, rely=.40, anchor=tk.CENTER)
            self.file_system = Save(self.file_location, self.key_location)

    def screen_size(self, screen):
        w = {"main": self.main_dim_w, 
            "settings": self.settings_dim_w,
            "logins": self.logins_dim_w,}
        h = {"main": self.main_dim_h, 
            "settings": self.settings_dim_h,
            "logins": self.logins_dim_h,}
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
        elif old_screen == "logins":
            self.logins_frame.forget()
        
        if new_screen == "main":
            self.main_frame.pack()
            self.screen_size("main")
        elif new_screen == "settings":
            self.settings_frame.pack()
            self.screen_size("settings")
        elif new_screen == "logins":
            self.logins_frame.pack()
            self.set_login_combobox()
            self.screen_size("logins")

    def get_password(self, website, username):
        if "" in [website, username]:
            self.gen_error_message("Missing website or username")
        elif all(i == False for i in self.settings_config):
            self.gen_error_message("Must have at least one setting selected")
        elif "," in website or "," in username:
            self.gen_error_message("Invalid character")
        elif not (self.file_location and self.key_location):
            self.gen_error_message("Savefile or key is missing. Locate or generate in settings.")
        else:
            self.disable_main_widgets()
            if self.settings_config[5]:
                password = Generator.generate_true_password(self.settings_config[:5], int(self.password_length))
            else:
                password = Generator.generate_password(self.settings_config[:5], int(self.password_length))
            if not password:
                self.gen_error_message("You must be connected to the internet for true random passwords.")
            elif not self.file_system.save_login(website, username, password): # method returns 0 if fails to save (existing login)
                if askyesno(title="Already Exists", message="Login already exists with the same username. Would you like to overwrite it?"):
                    self.file_system.overwrite_login(website, username, password)
            self.enable_main_widgets()
            self.clear_entries()

    def save_custom_password(self, website, username, password):
        if "" in [website, username, password]:
            self.gen_error_message("Missing website, username, or password")
        elif all(i == False for i in self.settings_config):
            self.gen_error_message("Must have at least one setting selected")
        elif "," in website or "," in username or "," in password:
            self.gen_error_message("Invalid character")
        elif not (self.file_location and self.key_location):
            self.gen_error_message("Savefile or key is missing. Locate or generate in settings.")
        else:
            if not self.file_system.save_login(website, username, password):
                if askyesno(title="Already Exists", message="Login already exists with the same username. Would you like to overwrite it?"):
                    self.file_system.overwrite_login(website, username, password)
            self.clear_entries()

    def clear_entries(self):
        self.main_web_entry.delete(0, tk.END)
        self.main_user_entry.delete(0, tk.END)
        self.main_password_entry.delete(0, tk.END)
            
    def disable_main_widgets(self):
        for widget in self.main_frame.winfo_children():
            widget.config(state="disabled")

    def enable_main_widgets(self):
        for widget in self.main_frame.winfo_children():
            widget.config(state="normal")

    def gen_error_message(self, message):
        tk.messagebox.showerror(title="Invalid", message=message)

