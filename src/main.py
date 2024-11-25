from src.screen import screenShot
from src.compareImage import ImageComparer
from time import sleep
import json

checks = {}

with open("src/SSLoc.json","r") as f:
    checks = json.load(f)

def run(event):
    if event == "Failed":
        print("Failed is the same")
    elif event == "Victory":
        print("Victory is the same")

def mainloop():
    for check in checks:
        print(check, end=": ")
        list = checks[check]
        screenShot(list[0],f"temp/{check}")
        if ImageComparer(f"Screenshots/temp/{check}.png",list[1]) >= 0.75:
            run(check)


for x in range(1):
    mainloop()
