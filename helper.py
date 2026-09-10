import json
from pathlib import Path
from game_loop import GameInfo

class Save ():
    SAVE_LOCATION = "Data.json"

    volume = 10
    game_info = None

    def __init__(self):
        if Path(self.SAVE_LOCATION).exists():
            with open("Data.json", "r") as f:
                s_dict = json.loads(f.read())

                self.volume = s_dict["volume"]

                if (s_dict["game_info"] != None):
                    self.game_info = GameInfo.from_dict(s_dict["game_info"])

    def saveData(self):
        data = {
            "volume": self.volume,
            "game_info": None if self.game_info == None else self.game_info.get_saveable_state()
        }
        
        with open("Data.json", "w") as f:
            json_str = json.dumps(data, indent=4)
            f.write(json_str)


#Sources = https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
# https://www.w3schools.com/python/python_dictionaries_access.asp