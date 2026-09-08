import random

VIRUS = [
    "Bouncy Castle", 
    "Invisible Men", 
    "Like The Dinosaures", 
    "Texture Not Found", 
    "Upside Down All Around", 
    "Black Hole", "Lag Spike"
]
GAMEMODES = ["Zombie", "King of The Hill", "Treasure Hunt", "Race to The Top"]

class GameInfo():
    firewallPlayer = ""
    survivor1 = ""
    survivor2 = ""
    survivor3 = ""

    gamemode = ""
    map = ""

    active_virus = []

    def __init__(
        self, 
        firewall = "", 
        s1 = "", 
        s2 = "", 
        s3 = "",
        gamemode = "",
        map = "",
        active_virus = []
    ):
        self.firewallPlayer = firewall
        self.survivor1 = s1,
        self.survivor2 = s2
        self.survivor3 = s3
        self.gamemode = gamemode
        self.map = map
        self.active_virus = active_virus

    def reset(self):
        self.firewallPlayer = ""
        self.survivor1 = ""
        self.survivor2 = ""
        self.survivor3 = ""
        self.gamemode = -1
        self.map = ""
        self.active_virus = []

    def addVirus(self, index):
        if (index < 0 or index >= len(VIRUS)):
            raise ValueError(f"Index ({index}) devrait être entre 0 et {len(VIRUS)}")

        #TODO: À place d'utiliser les valeurs, on pourrait utiliser l'index pour mettre dans la liste
        self.active_virus.append(VIRUS[index])

    def getGamemodeString(self):
        return GAMEMODES[self.gamemode]

    def getLastVirus(self):
        return self.active_virus[len(self.active_virus) - 1]

    def getGameDisplay(self):
        str = f"\nFIREWALL\n----------\n"
        str += f"{self.gamemode} sur la map {self.map}\n"
        str += f"Firewall: {self.firewallPlayer}\n"
        str += f"Survivants: {self.survivor1}, {self.survivor2}, {self.survivor3}\n"
        str += "----------\n"
        return str

    #C'est pour la class Save
    def getDict(self):
        pass


game_info = GameInfo()

def announceVirus():
    print(f"{game_info.getLastVirus()} is active!")

def useVirus():
    virus = []
    for e in range(0, 2):
        virus.append(random.randint(0,7))
    
    print(game_info.firewallPlayer + ", choisie un virus a injecter: ")
    isInvalid = True
    while isInvalid:
        print("1 : " + VIRUS[virus[0]])
        print("2 : " + VIRUS[virus[1]])
        choix = input("Choix : ")

        if(choix in "1", "2"):
            isInvalid = False
            game_info.addVirus(virus[int(choix)-1])
    
    announceVirus()

def runGame():
    game_info.gamemode = input("Choisissez le gamemode: ")
    game_info.map = input("Quelle est la carte de jeu?: ")

    print(game_info.getGameDisplay())
    useVirus()

def newGame():
    game_info.reset()
    game_info.firewallPlayer = input("Qui est le Firewall?: ")
    game_info.survivor1 = input("Qui est le premier survivant?: ")
    game_info.survivor2 = input("Qui est le second survivant?: ")
    game_info.survivor3 = input("Qui est le troisieme survivant?: ")
    runGame() 

if __name__ == "__main__":
    newGame()