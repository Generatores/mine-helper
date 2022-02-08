from tkinter import *
from tkinter import ttk

from commands.WalkDirective import WalkDirective
from commands.MineDirective import MineDirective
from commands.FightDirective import AttackDirective
from commands.FightDirective import ShootDirective
from components.MenuBar import MenuBar


def Index():
    root = Tk()
    root.title("Mine-Helper")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    WindowMenu = MenuBar(root)

    ttk.Label(frm, text="Welcome to Mine-Helper bot").grid(                                                           row=0, column=0, columnspan=2)

    ttk.Label(frm, text="You will automatically mine").grid(row=1, column=0)
    ttk.Button(frm, text="Mine", command=(
        lambda: MineDirective())).grid(row=1, column=1)

    ttk.Label(frm, text="You will automatically walk").grid(row=2, column=0)
    ttk.Button(frm, text="Walk", command=(
        lambda: WalkDirective())).grid(row=2, column=1)

    ttk.Label(frm, text="You will automatically attack").grid(row=3, column=0)
    ttk.Button(frm, text="Attack", command=(
        lambda: AttackDirective())).grid(row=3, column=1)

    ttk.Label(frm, text="You will automatically shot").grid(row=4, column=0)
    ttk.Button(frm, text="Shoot", command=(
        lambda: ShootDirective())).grid(row=4, column=1)

    ttk.Button(frm, text="Quit", command=root.destroy).grid(
        row=5, column=0, columnspan=2)

    root.config(menu=WindowMenu)

    root.wm_attributes("-topmost", 1)
    root.mainloop()


if __name__ == "__main__":
    Index()
