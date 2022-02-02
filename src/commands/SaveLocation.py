import pyautogui


def SaveCoordinate():
    x, y = pyautogui.position()
    return (x, y)
