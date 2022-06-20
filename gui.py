from tkinter import *
import tkinter as tk

import passGen
from passGen import Generator


class PassGUI:
    root = Tk()
    main_frame = tk.Frame(root)
    password_label = Label(main_frame)

    def __init__(self):
        self.root.title("Password Generator")
        self.root.eval("tk::PlaceWindow . center" % self.root.winfo_toplevel())
        self.root.resizable(False, False)
        self.build_main()
        self.root.grid_propagate(False)
        self.root.mainloop()

    def build_main(self):
        self.screen_size("main")
        length_label = Label(self.main_frame, text="Enter Password Length", font=("Helvetica", 16))
        length_entry = Entry(self.main_frame)
        length_entry.config(bg="cyan", font=("Helvetica", 14))
        length_entry.place(x=125, y=100)
        length_button = Button(self.main_frame, text="Get Password", command=lambda: self.get_password(length_entry.get()))
        length_label.pack()
        length_entry.pack()
        length_button.pack()
        self.password_label.config(font=("Helvetica", 16))
        self.password_label.pack()
        self.main_frame.pack()

    def screen_size(self, screen):
        w = {"main": 450, }
        h = {"main": 300, }
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w.get(screen) / 2)
        y = (hs / 2) - (h.get(screen) / 2)
        self.root.geometry('%dx%d+%d+%d' % (w.get(screen), h.get(screen), x, y))

    def get_password(self, length):
        if length.isnumeric():
            password = passGen.Generator.basic_gen(int(length))
            self.password_label.config(text=password)
        else:
            self.password_label.config(text="Invalid number")
