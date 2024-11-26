import pyautogui as auto
from time import sleep

def upgrade():
    auto.press("t")

def retry():
    auto.moveTo((591, 481))
    auto.click()
    auto.click()

def skip():
    auto.moveTo((443, 163))
    auto.click()
    auto.click()

def place(pos,troop):
    auto.press(troop)
    auto.moveTo(pos)
    sleep(0.25)
    auto.click()
    auto.click()