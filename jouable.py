import random

VIRUS = [
    "Bouncy Castle", 
    "Invisible Men", 
    "Like The Dinosaures", 
    "Texture Not Found", 
    "Upside Down All Around", 
    "Black Hole", 
    "Lag Spike"
]
GAMEMODES = ["Zombie", "King of The Hill", "Treasure Hunt", "Race to The Top"]

MAP = ["Coconut Mall", "Mid-City Zoo", "Mega Arch Park"]

OBJETS = ["Boom Box", "Office Chair", "Toy Gun", "Pogo Stick"]

EFFET_OBJETS = [" a jouer une musique explosive!", " a roulé à toute allure loin de son bureau!", " a fais croire aux autres qu'Andy était là!", " a sauté au dessus de tous le chaos!"]

class GameInfo():
    firewall_player = ""
    firewall_score = 0
    survivor1 = ""
    survivor_1_score = 0
    survivor_1_dead = False
    survivor2 = ""
    survivor_2_score = 0
    survivor_2_dead = False
    survivor3 = ""
    survivor_3_score = 0
    survivor_3_dead = False
    nb_kills = 0

    gamemode = ""
    map = ""

    active_virus = []

    def __init__(
        self, 
        firewall = "", 
        firewall_score=0,
        s1 = "", 
        s1_score=0,
        s1_dead=False,
        s2 = "", 
        s2_score=0,
        s2_dead=False,
        s3 = "",
        s3_score=0,
        s3_dead=False,
        nb_kills=0,
        gamemode = "",
        map = "",
        active_virus = []
    ):
        self.firewall_player = firewall
        self.firewall_score = firewall_score
        self.survivor1 = s1
        self.s1_score=s1_score
        self.s1_dead=s1_dead
        self.survivor2 = s2
        self.s2_score=s2_score
        self.s2_dead=s2_dead
        self.survivor3 = s3
        self.s3_score=s3_score
        self.s3_dead=s3_dead
        self.nb_kills=nb_kills
        self.gamemode = gamemode
        self.map = map
        self.active_virus = active_virus

    def reset(self):
        self.firewall_player = ""
        self.firewall_score = 0
        self.survivor1 = ""
        self.s1_score=0
        self.s1_dead=False
        self.survivor2 = ""
        self.s2_score=0
        self.s2_dead=False
        self.survivor3 = ""
        self.s3_score=0
        self.s3_dead=False
        self.nb_kills=0
        self.gamemode = -1
        self.map = ""
        self.active_virus = []

    def addVirus(self, index):
        if (index < 0 or index >= len(VIRUS)):
            raise ValueError(f"Index ({index}) devrait être entre 0 et {len(VIRUS)}")

        #TODO: À place d'utiliser les valeurs, on pourrait utiliser l'index pour mettre dans la liste
        self.active_virus.append(VIRUS[index])

    def getGamemodeString(self):
        return GAMEMODES[int(self.gamemode) - 1]

    def getMapString(self):
        return MAP[int(self.map) - 1]

    def getLastVirus(self):
        return self.active_virus[len(self.active_virus) - 1]

    def getGameDisplay(self):
        str = f"\nFIREWALL\n----------\n"
        str += f"{self.getGamemodeString()} sur la map: {self.getMapString()}\n"
        str += f"Firewall: {self.firewall_player}\n"
        str += f"Survivants: {self.survivor1}, {self.survivor2}, {self.survivor3}\n"
        str += "----------\n"
        return str

    def copy(self):
        return GameInfo(
            self.firewall_player,
            self.firewall_score,
            self.survivor1,
            self.s1_score,
            self.s1_dead,
            self.survivor2,
            self.s2_score,
            self.s2_dead,
            self.survivor3,
            self.s3_score,
            self.s3_dead,
            self.nb_kills,
            self.gamemode,
            self.map,
            self.active_virus.copy(),
        )

    def from_dict(d):
        return GameInfo(
            d["firewall"],
            d["firewall_score"],
            d["survivor1"],
            d["s1_score"],
            d["s1_dead"],
            d["survivor2"],
            d["s2_score"],
            d["s2_dead"],
            d["survivor3"],
            d["s3_score"],
            d["s3_dead"],
            d["nb_kills"],
            d["gamemode"],
            d["map"],
            d["active_virus"],
        )

    #C'est pour la class Save
    def getDict(self):
        return {
            "firewall" : self.firewall_player,
            "firewall_score" : self.firewall_score,
            "survivor1" : self.survivor1,
            "s1_score" : self.survivor_1_score,
            "s1_dead" : self.survivor_1_dead,
            "survivor2" : self.survivor2,
            "s2_score" : self.survivor_2_score,
            "s2_dead" : self.survivor_2_dead,
            "survivor3" : self.survivor3,
            "s3_score" : self.survivor_3_score,
            "s3_dead" : self.survivor_3_dead,
            "nb_kills" : self.nb_kills,
            "gamemode" : self.gamemode,
            "map" : self.map,
            "active_virus" : self.active_virus
        }

def announceVirus(game_info):
    print(f"{game_info.getLastVirus()} is active!")

def useVirus(game_info):
    virus = []
    for e in range(0, 2):
        virus.append(random.randint(0,6))
    
    print(game_info.firewall_player + ", choisie un virus a injecter: ")
    is_invalid = True
    while is_invalid:
        print("1 : " + VIRUS[virus[0]])
        print("2 : " + VIRUS[virus[1]])
        choix = input("Choix : ")

        if(choix in ("1", "2")):
            is_invalid = False
            game_info.addVirus(virus[int(choix)-1])
    
    announceVirus(game_info)

def chooseGamemode():
    for e in range (0, len(GAMEMODES)):
        number = e + 1
        print(str(number) + ": " + GAMEMODES[e])
    is_invalid = True
    while is_invalid:
        choix = input("Choisissez le gamemode: ")
        if(choix in ("1", "2", "3", "4")):
            is_invalid = False
            return choix
        else:
            print("Entrée invalide. Veuillez réessayer.") 

def chooseMap():
    for e in range (0, len(MAP)):
        number = e + 1
        print(str(number) + ": " + MAP[e])
    is_invalid = True
    while is_invalid:
        choix = input("Choisissez la carte: ")
        if(choix in ("1", "2", "3")):
            is_invalid = False
            return choix
        else:
            print("Entrée invalide. Veuillez réessayer.") 

def roundStart(roundNumber):
    print("-- Round " + str(roundNumber) + " --")
    print("1...")
    print("2...")
    print("3...")
    print("GO!")

def allDead(game_info):
    return(game_info.survivor_1_dead and game_info.survivor_2_dead and game_info.survivor_3_dead)

def endRound(game_info):
    print("Round ended")
    if(allDead):
        game_info.firewall_score += 5
    else :
        while True:
            winner = random.randint(1, 3)
            if(winner == 3 and not game_info.survivor_3_dead):
                game_info.survivor_3_score += 5
                game_info.firewall_score += game_info.nb_kills
                break
            elif(winner == 2 and not game_info.survivor_2_dead):
                game_info.survivor_2_score += 5
                game_info.firewall_score += game_info.nb_kills
                break
            elif(winner == 1 and not game_info.survivor_1_dead):
                game_info.survivor_1_score += 5
                game_info.firewall_score += game_info.nb_kills
                break
    game_info.nb_kills = 0
    game_info.survivor_1_dead = False
    game_info.survivor_2_dead = False
    game_info.survivor_3_dead = False

def killPlayer(game_info, player):
    if(player==1):
        game_info.survivor_1_dead=True
        print(str(game_info.survivor1) + " est mort.")
    elif(player==2):
        game_info.survivor_2_dead=True
        print(str(game_info.survivor2) + " est mort.")
    elif(player==3):
        game_info.survivor_3_dead=True
        print(str(game_info.survivor3) + " est mort.")

def spawnObjet(game_info):
    objet = random.randint(0, 3)
    print("L'objet \"" + OBJETS[objet] + "\" s'est glissé dans le code.")
    pickupperNb = random.randint(1,3)
    if(pickupperNb == 1 and not game_info.survivor_1_dead):
        print(game_info.survivor1 + " a ramassé : " + OBJETS[objet] + ".")
        print(game_info.survivor1 + EFFET_OBJETS[objet])
    elif(pickupperNb == 2 and not game_info.survivor_2_dead):
        print(game_info.survivor2 + " a ramassé : " + OBJETS[objet] + ".")
        print(game_info.survivor2 + EFFET_OBJETS[objet])
    elif(pickupperNb == 3 and not game_info.survivor_3_dead):
        print(game_info.survivor3 + " a ramassé : " + OBJETS[objet] + ".")
        print(game_info.survivor3 + EFFET_OBJETS[objet])
    else:
        print("Le code indésirable a été effacé.")

def eventSimulation(game_info):
    print ("-- Simulateur d'évènement (Admin) --")
    while True:
        print("1: Survivant 1 meurt")
        print("2: Survivant 2 meurt")
        print("3: Survivant 3 meurt")
        print("4: Un objet apparaît")
        print("5: Mettre fin à la simulation")
        choix = input("Que ce passe t'il?: ")
        if(choix == "1" and not game_info.survivor_1_dead):
            killPlayer(game_info, 1)
        elif(choix == "2" and not game_info.survivor_2_dead):
            killPlayer(game_info, 2)
        elif(choix == "3" and not game_info.survivor_3_dead):
            killPlayer(game_info, 3)
        elif(choix == "4"):
            spawnObjet(game_info)
        elif(choix == "5"):
            break
        else:
            print("Entrée invalide. Veuillez réessayer.") 
        if(allDead(game_info)):
            print("Tous les survivants sont morts. La manche est finie.")
            break

def endGame(game_info):
    #TODO Afficher les scores et nommer le grand gagnant.
    pass

def runGame(game_info):
    print(game_info.getGameDisplay())
    for e in range(0, 3):
        roundStart(e + 1)
        useVirus(game_info)
        eventSimulation(game_info)
        endRound(game_info)
    endGame(game_info)

def newGame():
    game_info = GameInfo()
    game_info.firewall_player = input("Qui est le Firewall?: ")
    game_info.survivor1 = input("Qui est le premier survivant?: ")
    game_info.survivor2 = input("Qui est le second survivant?: ")
    game_info.survivor3 = input("Qui est le troisieme survivant?: ")
    game_info.gamemode = chooseGamemode()
    game_info.map = chooseMap()
    return game_info


if __name__ == "__main__":
    game_info = newGame()
    runGame(game_info)