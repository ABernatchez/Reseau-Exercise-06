import json
class Save ():
    health = 100
    dmg = 5
    speed = 2
    gameMaster = 3
    def saveData(health, dmg, speed, gameMaster):
        data = {
            "Health": health,
            "Damage": dmg,
            "Speed": speed,
            "Game Master": gameMaster
        }
        json_str = json.dumps(data, indent=4)
        with open("Data.json", "w") as f:
            f.write(json_str)


#Source = https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/