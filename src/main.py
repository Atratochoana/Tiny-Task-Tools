from screen import screenShot
from compareImage import ImageComparer
import Vanguards
from time import sleep
import json
import pyautogui
from webhook import sendMessage

#tinyTaskSlots = [(1094, 22),(1364, 22),(1638, 22),(1640, 112),(1362, 112),(1098, 112),(1098, 204)]
ran = 0
failed = 0

with open("src\positions\comparisons.json","r") as f:
    checks = json.load(f)
with open("src\positions\misc.json","r") as f:
    misc = json.load(f)

def run(event):
    if event == "Failed":
        pyautogui.press("f8")
        pyautogui.press("f8")
        failed += 1

    elif event == "Victory":
        sendMessage(None,ran,failed)
        ran += 1

def mainloop():
    for check in checks:
        print(check, end=": ")
        list = checks[check]
        screenShot(list[0],f"temp/{check}")
        if ImageComparer(f"Screenshots/temp/{check}.png",list[1]) >= 0.75:
            run(check)
    sleep(1)

# def getText(image):
#     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#     image = cv2.imread(image, 0)
#     thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#     data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
#     return data

ended = False
while ended == False:
    mainloop()
