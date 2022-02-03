import pyautogui


def AppendLocation():
    x, y = pyautogui.position()
    return (x, y)
