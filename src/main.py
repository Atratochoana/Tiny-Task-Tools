from screen import screenShot
from compareImage import ImageComparer
import Vanguards
from time import sleep
import json
import cv2
import pytesseract

currentCash = 0

#tinyTaskSlots = [(1094, 22),(1364, 22),(1638, 22),(1640, 112),(1362, 112),(1098, 112),(1098, 204)]

with open("src\positions\comparisons.json","r") as f:
    checks = json.load(f)
with open("src\positions\misc.json","r") as f:
    misc = json.load(f)

def run(event):
    if event == "Failed":
        print("Failed is the same")
        Vanguards.retry()
    elif event == "Victory":
        print("Victory is the same")

def mainloop():
    screenShot((misc["yen"][0],misc["yen"][1],misc["yen"][2],misc["yen"][3]),"temp/Yen")
    currentCash = getText("Screenshots/temp/Yen.png")
    for check in checks:
        print(check, end=": ")
        list = checks[check]
        screenShot(list[0],f"temp/{check}")
        if ImageComparer(f"Screenshots/temp/{check}.png",list[1]) >= 0.75:
            run(check)

def getText(image):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    image = cv2.imread(image, 0)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
    return data


for x in range(1):
    mainloop()
