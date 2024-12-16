from ahk import AHK
from time import sleep
#Idea for this is to decompile a txt file into a macro through having it have information based on then action, specific for vanguards

#example input [1-6 for slot][Index of that slot][Action][Sleep time from previous task];
# [Slot] if 0 will mean the action is not character related otherwise is self explainitory
# [Index] this is also self explanatory, if the slot is 0 it doesnt matter
# [Action] this will be one letter such as "u" for upgrade or "r" for restart
# [Sleep] this will just a time from between the last task and this one
# [End] will end in a ; to indicate the difference between the sleep time and slot
# end product could look something like this ;30u15 this means, slot 3 index 0 upgrade after sleeping 15 seconds
# character locations will be at the start and be based on this format: [{slot}:{x coords}:{1 coords}&]=
# example for character location is &2:500:500:&2:600:600:

ahk = AHK()

def find(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]

def find_indices(string, chars):
    return [[i for i, ltr in enumerate(string) if ltr == char] for char in chars]

def decompile(filePath):
    testString = ":3:1412:515::1:1312:615:;30u5;;30u10;;30u0;"
    actions = []
    chars = []
    characters = [[],[],[],[],[],[]]

    indices = find_indices(testString,[":",";"]) #[[0, 2, 7, 11], [12, 17, 18, 24, 25, 30]]
    print(f"Indices = {indices}")
    for x in range(int(len(indices[0])/4)):
        chars.append(testString[indices[0][int(4**(x-1))]:indices[0][(int(4**(x-1))+3)]+1])

    print(chars)
    for c in chars:
        colonIndex = find(c,":")
        print(colonIndex)
        characters[int(c[1])].append([int(c[colonIndex[1]+1:colonIndex[2]]),int(c[colonIndex[2]+1:len(c)-1])])
    print(characters)

    for action in actions:
        ahk.find_window(title="Roblox").activate()
        if int(action[4]) != 0:
            sleep(int(action[4:int(len(action))-1]))
            print("Finished sleeping")
        if int(action[1]) >= 1:
            ahk.click(characters[int(action[1])][int(action[2])][0],characters[int(action[1])][int(action[2])][1])
            print("Clicked on char")
        if action[3] == "u": #U is for upgrade, and assumes that click has happened already
            ahk.key_press("t")
            print("Upgraded")
        if action[3] == "r": #retry for fullscreen, slot should be 0, althought doesnt matter
            for x in range(10):
                ahk.click(x=1175, y=816)
            print("Retried")
        if action[3] == "s": #skip for fullscreen
            ahk.click(x=899, y=192)
        if action[3] == "q": #resets character to spawn
            ahk.click(x=40, y=1004)
            ahk.click(x=1194, y=363)
            ahk.click(x=1287, y=224)
            ahk.click(button="wheeldown")
            ahk.click(button="wheeldown")
            ahk.click(button="wheeldown")
            ahk.click(button="wheeldown")
            ahk.click(button="wheeldown")
            ahk.click(button="wheeldown")
        



decompile(None)