import mouse
import keyboard
import time
from tkinter import messagebox


def AttackDirective():
    time.sleep(5)
    trigger = False
    while trigger == False:
        mouse.click()
        time.sleep(.1)
        trigger = keyboard.is_pressed("e")
    messagebox.showinfo(title='Fight Directive', message='The fight directive was completed!')