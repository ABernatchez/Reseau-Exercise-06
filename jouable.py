import random

VIRUS = ["Bouncy Castle", "Invisible Men", "Like The Dinosaures", "Texture Not Found", "Upside Down All Around", "Black Hole", "Lag Spike"]
ACTIVE_VIRUS = []
GAMEMODES = ["Zombie", "King of The Hill", "Treasure Hunt", "Race to The Top"]

def announceVirus():
    print (ACTIVE_VIRUS[len(ACTIVE_VIRUS) - 1] + " is active!")

def useVirus(firewall):
    virus = []
    for e in range(0, 2):
        virus.append(random.randint(0,7))
    print(firewall + " choisie un virus a injecter: ")
    isInvalid = True
    while isInvalid:
        print("1 : " + VIRUS[virus[0]])
        print("2 : " + VIRUS[virus[1]])
        choix = input("Choix : ")
        if(choix in "1", "2"):
            isInvalid = False
            ACTIVE_VIRUS.append(VIRUS[virus[int(choix)-1]])
    announceVirus()


def runGame(player1, player2, player3, firewall) :  
    gamemode = input("Choisissez le gamemode: ")  
    isInvalid = True
    while isInvalid:
        print("1 : " + VIRUS[virus[0]])
        print("2 : " + VIRUS[virus[1]])
        choix = input("Choix : ")
        if(choix in "1", "2"):
            isInvalid = False
            ACTIVE_VIRUS.append(VIRUS[virus[int(choix)-1]])
    map = input("Quelle est la carte de jeu?: ")

    useVirus(firewall)



def newGame() :
    firewallPlayer = input("Qui est le Firewall?: ")
    survivor1 = input("Qui est le premier survivant?: ")
    survivor2 = input("Qui est le second survivant?: ")
    survivor3 = input("Qui est le troisieme survivant?: ")
    runGame(firewallPlayer, survivor1, survivor2, survivor3) 

if __name__ == "__main__":
    newGame()