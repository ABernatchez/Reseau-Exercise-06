import json
from pathlib import Path

class Save ():
    SAVE_LOCATION = "Data.json"

    health = 100
    dmg = 5
    speed = 2
    gameMaster = 3

    def __init__(self):
        if Path(self.SAVE_LOCATION).exists():
            with open("Data.json", "r") as f:
                s_dict = json.loads(f.read())
                self.health = s_dict["health"]
                self.dmg = s_dict["damage"]
                self.speed = s_dict["speed"]
                self.gameMaster = s_dict["game_master"]

    def saveData(self):
        data = {
            "health": self.health,
            "damage": self.dmg,
            "speed": self.speed,
            "game_master": self.gameMaster
        }
        
        with open("Data.json", "w") as f:
            json_str = json.dumps(data, indent=4)
            f.write(json_str)


#Sources = https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
# https://www.w3schools.com/python/python_dictionaries_access.asp