from tkinter import *
from tkinter import ttk

from MineDirective import *
from WalkDirective import *

root = Tk()
root.geometry('300x125')
root.title("Mine-Helper")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Welcome to Mine-Helper bot").grid(column=0, row=0)

ttk.Label(frm, text="You will automatically mine").grid(column=0, row=1)
ttk.Button(frm, text="Mine", command=(
    lambda: MineDirective())).grid(column=1, row=1)

ttk.Label(frm, text="You will automatically walk").grid(column=0, row=2)
ttk.Button(frm, text="Walk", command=(
    lambda: WalkDirective())).grid(column=1, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)

root.mainloop()
