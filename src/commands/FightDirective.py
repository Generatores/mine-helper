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
        trigger = keyboard.is_pressed("x")
    messagebox.showinfo(title='Fight Directive', message='The fight directive was completed!')

def ShootDirective():
    time.sleep(5)
    trigger = False
    while trigger == False:
        mouse.press(button='right')
        time.sleep(1.5)
        mouse.release(button='right')
        trigger = keyboard.is_pressed("x")
    messagebox.showinfo(title='Shoot Directive', message='The shoot directive was completed!')