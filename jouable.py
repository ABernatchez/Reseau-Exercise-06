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


class Survivor():
    name = ""
    score = 0
    is_dead = False

    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Le nom d'un survivant devrait être un string.")

        self.name = name

    ## Permet de charger un survivant à partir
    def load(name, score, is_dead):
        s = Survivor(name)
        s.score = score
        s.is_dead = is_dead
        return s

    ## Retourne un objet Survivor à partir d'un dictionnaire
    def from_saveable_state(s_state):
        return Survivor.load(s_state["name"], s_state["score"], s_state["is_dead"])

    ## Retourne un dictionnaire (Hashmap) qui permet de sauvegarder ses informations
    def get_saveable_state(self):
        return {"name": self.name, "score": self.score, "is_dead": self.is_dead}


class GameInfo():
    firewall_player = ""
    firewall_score = 0
    survivor_1 = None
    survivor_2 = None
    survivor_3 = None
    nb_kills = 0

    gamemode = ""
    map = ""

    round = 0
    active_virus = []

    def addVirus(self, index):
        if (index < 0 or index >= len(VIRUS)):
            raise ValueError(f"Index ({index}) devrait être entre 0 et {len(VIRUS)}")

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
        str += f"Survivants: {self.survivor_1.name}, {self.survivor_2.name}, {self.survivor_3.name}\n"
        str += "----------\n"
        return str

    def is_survivor_dead(self, index):
        match index:
            case 1:
                return self.survivor_1.is_dead
            case 2:
                return self.survivor_2.is_dead
            case 3:
                return self.survivor_3.is_dead
            case _:
                raise ValueError("Index est hors de la porté.")

    def are_survivors_dead(self):
        return self.survivor_1.is_dead and self.survivor_2.is_dead and self.survivor_3.is_dead

    def points_for_alive_players(self, points):
        if not self.survivor_1.is_dead:
            self.survivor_1.score += points
        if not self.survivor_2.is_dead:
            self.survivor_2.score += points
        if not self.survivor_3.is_dead:
            self.survivor_3.score += points

    def reset_round(self):
        self.survivor_1.is_dead = False
        self.survivor_2.is_dead = False
        self.survivor_3.is_dead = False
        self.nb_kills = 0

    def copy(self):
        state = GameInfo()
        state.firewall_player = self.firewall_player
        state.firewall_score = self.firewall_score
        state.survivor_1 = self.survivor_1
        state.survivor_2 = self.survivor_2
        state.survivor_3 = self.survivor_3
        state.nb_kills = self.nb_kills
        state.gamemode = self.gamemode
        state.map = self.map
        state.round = self.round
        state.active_virus = self.active_virus.copy()
        return state

    def from_dict(d):
        state = GameInfo()
        state.firewall_player = d["firewall_name"]
        state.firewall_score = d["firewall_score"]
        state.survivor_1 = Survivor.from_saveable_state(d["survivor_1"])
        state.survivor_2 = Survivor.from_saveable_state(d["survivor_2"])
        state.survivor_3 = Survivor.from_saveable_state(d["survivor_3"])
        state.nb_kills = d["nb_kills"]
        state.gamemode = d["gamemode"]
        state.map = d["map"]
        state.round = d["round"]
        state.active_virus = d["active_virus"]
        return state

    def get_saveable_state(self):
        return {
            "firewall_name" : self.firewall_player,
            "firewall_score" : self.firewall_score,
            "survivor_1": self.survivor_1.get_saveable_state(),
            "survivor_2": self.survivor_2.get_saveable_state(),
            "survivor_3": self.survivor_3.get_saveable_state(),
            "nb_kills" : self.nb_kills,
            "gamemode" : self.gamemode,
            "map" : self.map,
            "round": self.round,
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


def endRound(game_info):
    print("Round ended")
    if(game_info.are_survivors_dead()):
        game_info.firewall_score += 5
    else :
        game_info.points_for_alive_players(5)
        game_info.firewall_score += game_info.nb_kills
    game_info.reset_round()

def killPlayer(game_info, player):
    if(player==1):
        game_info.survivor_1.is_dead = True
        print(str(game_info.survivor_1.name) + " est mort.")
    elif(player==2):
        game_info.survivor_2.is_dead = True
        print(str(game_info.survivor_2.name) + " est mort.")
    elif(player==3):
        game_info.survivor_3.is_dead = True
        print(str(game_info.survivor_3.name) + " est mort.")

def spawnObjet(game_info):
    objet = random.randint(0, 3)
    print("L'objet \"" + OBJETS[objet] + "\" s'est glissé dans le code.")
    pickupperNb = random.randint(1,3)
    if(pickupperNb == 1 and not game_info.is_survivor_dead(1)):
        print(game_info.survivor_1.name + " a ramassé : " + OBJETS[objet] + ".")
        print(game_info.survivor_1.name + EFFET_OBJETS[objet])
    elif(pickupperNb == 2 and not game_info.is_survivor_dead(2)):
        print(game_info.survivor_2.name + " a ramassé : " + OBJETS[objet] + ".")
        print(game_info.survivor_2.name + EFFET_OBJETS[objet])
    elif(pickupperNb == 3 and not game_info.is_survivor_dead(3)):
        print(game_info.survivor_3.name + " a ramassé : " + OBJETS[objet] + ".")
        print(game_info.survivor_3.name + EFFET_OBJETS[objet])
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
        if(choix == "1" and not game_info.is_survivor_dead(1)):
            killPlayer(game_info, 1)
        elif(choix == "2" and not game_info.is_survivor_dead(2)):
            killPlayer(game_info, 2)
        elif(choix == "3" and not game_info.is_survivor_dead(3)):
            killPlayer(game_info, 3)
        elif(choix == "4"):
            spawnObjet(game_info)
        elif(choix == "5"):
            break
        else:
            print("Entrée invalide. Veuillez réessayer.") 
        if(game_info.are_survivors_dead()):
            print("Tous les survivants sont morts. La manche est finie.")
            break

def endGame(game_info):
    print("Firewall :" + str(game_info.firewall_score))
    print("Survivor 1 :" + str(game_info.survivor_1.score))
    print("Survivor 2 :" + str(game_info.survivor_2.score))
    print("Survivor 3 :" + str(game_info.survivor_3.score))

def round(game_info, round):
    roundStart(round + 1)
    useVirus(game_info)
    eventSimulation(game_info)
    endRound(game_info)

def shouldQuit(round):
    if round == 2:
        return False

    return input("Voulez-vous retourner au menu(y/n)?: ") == 'y'

def runGame(game_info):
    print(game_info.getGameDisplay())
    for e in range(game_info.round, 3):
        round(game_info, e)
        game_info.round = e + 1

        if (shouldQuit(e)):
            return

    endGame(game_info)

def newGame():
    game_info = GameInfo()
    game_info.firewall_player = input("Qui est le Firewall?: ")
    game_info.survivor_1 = Survivor(input("Qui est le premier survivant?: "))
    game_info.survivor_2 = Survivor(input("Qui est le second survivant?: "))
    game_info.survivor_3 = Survivor(input("Qui est le troisieme survivant?: "))
    game_info.gamemode = chooseGamemode()
    game_info.map = chooseMap()
    return game_info


if __name__ == "__main__":
    game_info = newGame()
    runGame(game_info)