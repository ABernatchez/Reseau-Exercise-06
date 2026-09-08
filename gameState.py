import json
class Save ():
    health = 100
    dmg = 5
    speed = 2
    gameMaster = 3
    def saveData(health, dmg, speed, gameMaster):
        data = {
            "health": health,
            "damage": dmg,
            "speed": speed,
            "game_master": gameMaster
        }
        json_str = json.dumps(data, indent=4)
        with open("Data.json", "w") as f:
            f.write(json_str)
    saveData(health, dmg, speed, gameMaster)
def load ():
    with open("Data.json", "r") as f:
        print(json.loads(f.read())["health"])

#Sources = https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
# https://www.w3schools.com/python/python_dictionaries_access.asp