import mouse
import keyboard
import time
from pyautogui import alert


def AttackDirective():
    time.sleep(5)
    print('attack started')
    trigger = False
    while trigger == False:
        mouse.click()
        time.sleep(.01)
        trigger = keyboard.is_pressed("e")
    alert(title="Directive completed",
          text="The attack directive has been executed successfully")


if __name__ == "__main__":
    AttackDirective()
