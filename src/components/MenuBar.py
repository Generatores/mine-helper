from tkinter import *
from pages.AboutUs import AboutUs


def MenuBar(root):
    WindowMenu = Menu(root)

    FileMenu = Menu(WindowMenu, tearoff=0)
    FileMenu.add_command(label='Exit', command=root.destroy)

    AboutMenu = Menu(WindowMenu, tearoff=0)
    AboutMenu.add_command(label='Information', command=(lambda: AboutUs()))

    WindowMenu.add_cascade(label='File', menu=FileMenu)
    WindowMenu.add_cascade(label='About', menu=AboutMenu)
    return WindowMenu
