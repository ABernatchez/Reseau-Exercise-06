from enum import Enum
from gameState import Save
from jouable import newGame, runGame

class RunState(Enum):
    MENU_PRINCIPAL = 1
    OPTION = 2

def showMenu():
    print("\nFIREWALL: *courte description*")
    print("Membre de l'équipe:")
    print("    - Arnaud Bernatchez\n    - François-Xavier Thibault\n    - Grégoire Gionet\n    - Samuel Rodrigue\n")
    
    print("------------------------------------")
    print("1 - Continuer à jouer")
    print("2 - Commencer une nouvelle partie")
    print("3 - Charger une partie")
    print("4 - Sauvegarder la partie")
    print("5 - Consulter les options")
    print("6 - Quitter")
    print("------------------------------------\n")

def showOptions():
    print("\nFIREWALL: *courte description*")
    print("Membre de l'équipe:")
    print("    - Arnaud Bernatchez\n    - François-Xavier Thibault\n    - Grégoire Gionet\n    - Samuel Rodrigue\n")
    
    print("------------------------------------")
    print("1 - Ajuster le volume")
    print("2 - retour au menu principal")
    print("------------------------------------\n")

def run():
    save = Save()
    run_state = RunState.MENU_PRINCIPAL
    game_info = None
    if (save.game_info != None):
        game_info = save.game_info.copy()

    running = True
    while running:
        match run_state:
            case RunState.MENU_PRINCIPAL:
                showMenu()
                choice = input("\nEntrer votre choix: ")
                match choice:
                    case "1":                        
                        if (game_info != None):
                            runGame(game_info)
                        else:
                            print("\nPas de partie commencé.\n")
                    case "2":
                        game_info = newGame()
                        runGame(game_info)
                    case "3":
                        if (save.game_info != None):
                            game_info = save.game_info.copy()
                            print("\nChargement de la partie...\nFaite\n")
                            runGame(game_info)
                        else:
                            print("\nAucune partie sauvegardé\n")
                    case "4":
                        if (game_info != None):
                            save.game_info = game_info.copy()
                            save.saveData()
                            print("\nSauvegarde de la partie...\nFaite\n")
                        else:
                            print("\nAucune partie à sauvegarder\n")
                    case "5":
                        run_state = RunState.OPTION
                    case "6":
                        running = False
                    case _:
                        print("\nLe choix n'est pas valide\n")
            case RunState.OPTION:
                #Options
                showOptions()
                choice = input("\nEntrer votre choix: ")
                match choice:
                    case "1":
                        NbVolume = input("\nEntrer votre volume choisi: ")
                        save.volume = NbVolume
                    case "2":
                        run_state = RunState.MENU_PRINCIPAL

    save.saveData()
    print("Exiting game...")

if __name__ == "__main__":
    run()