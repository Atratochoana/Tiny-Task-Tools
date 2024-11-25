
from pyautogui import position

def getMousePos():
    currentMouseX, currentMouseY = position()

    return (currentMouseX, currentMouseY)




