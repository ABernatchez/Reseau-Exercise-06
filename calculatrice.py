def calculatrice():
    print("Bienvenue dans la calculatrice simple!")

    while True:
        print("\nChoisissez une opération:")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")

        choix = input("Entrez le numéro de l'opération (1-5): ")

        if choix == '5':
            print("Exiting...")
            break

        if choix not in ('1', '2', '3', '4'):
            print("Choix invalide!")
            continue

        num1 = 0
        num2 = 0
        try:
            num1 = int(input("Entrez le premier numéro: "))
            num2 = int(input("Entrez le deuxième numéro: "))
        except:
            print("Ce n'est pas une numéro valide.")
            continue
            

        if choix == '1':
            print(f"Voici le résultat: {num1+num2}")
        elif choix == '2':
            print(f"Voici le résultat: {num1-num2}")
        elif choix == '3':
            print(f"Voici le résultat: {num1*num2}")
        elif choix == '4':
            if num2 == 0:
                print("La division par zéro n'est pas possible.")
            else:
                print(f"Voici le résultat: {num1/num2}")

            

if __name__ == "__main__":
    calculatrice()