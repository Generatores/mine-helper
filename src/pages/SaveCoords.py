from tkinter import *
from tkinter import ttk
from components.MenuBar import MenuBar


def SaveCoords():
    root = Tk()
    root.geometry('400x200')
    root.title("Mine-Helper")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    WindowMenu = MenuBar(root)

    root.config(menu=WindowMenu)

    root.mainloop()
