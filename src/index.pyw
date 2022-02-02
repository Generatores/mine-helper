from tkinter import *
from tkinter import ttk

import commands.WalkDirective as walkdir
import commands.MineDirective as minedir
import pages.SaveCoords as savecoords
from components.MenuBar import MenuBar

coordX = 0
coordY = 0


def Index():
    root = Tk()
    root.geometry('400x600')
    root.title("Mine-Helper")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    WindowMenu = MenuBar(root)

    ttk.Label(frm, text="Welcome to Mine-Helper bot").grid(column=0, row=0)

    ttk.Label(frm, text="You will automatically mine").grid(column=0, row=1)
    ttk.Button(frm, text="Mine", command=(
        lambda: minedir.MineDirective())).grid(column=1, row=1)

    ttk.Label(frm, text="You will automatically walk").grid(column=0, row=2)
    ttk.Button(frm, text="Walk", command=(
        lambda: walkdir.WalkDirective())).grid(column=1, row=2)

    ttk.Label(frm, text="You will save a location on screen").grid(
        column=0, row=3)
    ttk.Button(frm, text="Save point", command=(
        lambda: (savecoords.SaveCoords()))).grid(column=1, row=3)

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)

    root.config(menu=WindowMenu)

    root.mainloop()


if __name__ == "__main__":
    Index()
