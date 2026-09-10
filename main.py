from enum import Enum
from save import Save
from game_loop import newGame, runGame

class RunState(Enum):
    MENU_PRINCIPAL = 1
    OPTION = 2


class Game():
    save = None
    run_state =  RunState.MENU_PRINCIPAL
    game_info = None

    def __init__(self):
        self.save = Save()

        if (self.save.game_info != None):
            self.game_info = self.save.game_info.copy()

    def show_menu():
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

    def show_options():
        print("\nFIREWALL: *courte description*")
        print("Membre de l'équipe:")
        print("    - Arnaud Bernatchez\n    - François-Xavier Thibault\n    - Grégoire Gionet\n    - Samuel Rodrigue\n")

        print("------------------------------------")
        print("1 - Ajuster le volume")
        print("2 - retour au menu principal")
        print("------------------------------------\n")

    def continue_game(self):
        if (self.game_info != None):
            runGame(self.game_info)
        else:
            print("\nPas de partie commencé.\n")

    def load_game(self):
        if (self.save.game_info != None):
            self.game_info = self.save.game_info.copy()
            print("\nChargement de la partie...\nFaite\n")
            runGame(self.game_info)
        else:
            print("\nAucune partie sauvegardé\n")

    def save_game(self):
        if (self.game_info != None):
            self.save.game_info = self.game_info.copy()
            self.save.saveData()
            print("\nSauvegarde de la partie...\nFaite\n")
        else:
            print("\nAucune partie à sauvegarder\n")

    def menu_principal_state(self):
        Game.show_menu()
        choice = input("\nEntrer votre choix: ")
        match choice:
            case "1":                        
                self.continue_game()
            case "2":
                self.game_info = newGame()
                runGame(self.game_info)
            case "3":
                self.load_game()
            case "4":
                self.save_game()
            case "5":
                self.run_state = RunState.OPTION
            case "6":
                return False
            case _:
                print("\nLe choix n'est pas valide\n")
        return True

    def option_state(self):
        Game.show_options()
        choice = input("\nEntrer votre choix: ")
        match choice:
            case "1":
                NbVolume = input("\nEntrer votre volume choisi: ")
                self.save.volume = NbVolume
            case "2":
                self.run_state = RunState.MENU_PRINCIPAL

    def run(self):
        running = True
        while running:
            match self.run_state:
                case RunState.MENU_PRINCIPAL:
                    running = self.menu_principal_state()
                case RunState.OPTION:     
                    self.option_state()
        self.save.saveData()
        print("Exiting game...")
    

if __name__ == "__main__":
    game = Game()
    game.run()