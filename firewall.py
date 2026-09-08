from enum import Enum

class GameState(Enum):
    MENU_PRINCIPAL = 1
    OPTION = 2
    IN_GAME = 3


def showMenu():
    print("FIREWALL: *courte description*")
    print("Membre de l'équipe:")
    print("    - Arnaud Bernatchez\n    - François-Xavier Thibault    - Grégoire Gionet\n    - Samuel Rodrigue")

    print("\n1 - Continuer à jouer")
    print("\n2 - Commencer une nouvelle partie")
    print("\n3 - Charger une partie")
    print("\n4 - Sauvegarder la partie")
    print("\n5 - Consulter les options")
    print("\n6 - Quitter")

def run():
    game_state = GameState.MENU_PRINCIPAL
    running = True

    while running:
        match game_state:
            case GameState.MENU_PRINCIPAL:
                showMenu()
                choice = input("\nEntrer votre choix: ")
                match choice:
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
                    case "4":
                        pass
                    case "5":
                        game_state = GameState.OPTION
                    case "6":
                        running = False
                    case _:
                        print("Le choix n'est pas valide")
            case GameState.OPTION:
                print("Option: retour au menu principal")
                game_state = GameState.MENU_PRINCIPAL

    print("Exiting game...")

    

def load():
    pass

def newGame():
    pass

def save():
    pass

def options():
    pass

def leave():
    pass

if __name__ == "__main__":
    run()