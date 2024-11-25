import pyautogui
import time


def getMousePos():
    currentMouseX, currentMouseY = pyautogui.position()

    return (currentMouseX, currentMouseY)





