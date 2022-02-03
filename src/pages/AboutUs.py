from tkinter import *
from tkinter import ttk


def AboutUs():
    root = Tk()
    root.title("About us")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    ttk.Label(frm, text="This application was developed by Generatores").grid(
        column=0, row=0)
    ttk.Label(
        frm, text="Visit the repository at https://github.com/Generatores/mine-helper").grid(column=0, row=1)
    ttk.Label(
        frm, text="Contact me at bruno.ruiz@bbrr.solutions").grid(column=0, row=2)
    ttk.Label(
        frm, text="Current version: V1.1.0-alpha").grid(column=0, row=3)

    root.config()

    root.mainloop()
