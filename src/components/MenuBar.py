from tkinter import *
from tkinter import ttk

def MenuBar(root):
    WindowMenu = Menu(root)

    FileMenu = Menu(WindowMenu, tearoff=0)
    FileMenu.add_command(label='Exit', command=root.destroy)

    AboutMenu = Menu(WindowMenu, tearoff=0)
    AboutMenu.add_command(label='About us')
    AboutMenu.add_command(label='Contact us')
    
    WindowMenu.add_cascade(label='File', menu=FileMenu)
    WindowMenu.add_cascade(label='About', menu=AboutMenu)
    return WindowMenu