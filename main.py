from src.screen import screenShot
from compareImage import ImageComparer
from time import sleep
import json

checks = {}

with open("src/SSLoc.json","r") as f:
    checks = json.load(f)

def mainloop():
    for check in checks:
        print(check)
        list = checks[check]
        screenShot(list[0],f"temp/{check}")
        if ImageComparer(f"Screenshots/temp/{check}.png",list[1]) >= 0.75:
            print("Same")


for x in range(1):
    mainloop()
