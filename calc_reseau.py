def decimalToBinary(n):
    binary = bin(int(n))
    print(f"Conversion décimal vers binaire: {n} -> {binary}")

def binaryToDecimal(n):
    num = int(n, 2)
    print(f"Conversion binaire vers décimal: {n} -> {num}")

def decimalToHexadecimal(n):
    print(f"Conversion décimal vers hexadécimale: {n} -> {hex(int(n))}")

def hexadecimalToDecimal(n):
    num = int(n, 16)
    print(f"Conversion hexadécimale vers décimal: {n} -> {num}")

def calculatrice():
    print("Bienvenue dans la calculatrice de conversion simple!")

    while True:
        print("\nChoisissez une conversion:")
        print("1. Décimale vers binaire")
        print("2. Binaire vers décimale")
        print("3. Décimale vers hexadécimale")
        print("4. Hexadécimale vers décimal")
        print("5. Quitter")

        choix = input("Entrez le numéro pour la conversion (1-5): ")

        if choix == '5':
            print("Exiting...")
            break

        if choix not in ('1', '2', '3', '4'):
            print("Choix invalide!")
            continue

        numStr = input("Entrez le premier numéro: ")

        if choix == '1':
            decimalToBinary(numStr)
        elif choix == '2':
            binaryToDecimal(numStr)
        elif choix == '3':
            decimalToHexadecimal(numStr)
        elif choix == '4':
            hexadecimalToDecimal(numStr)

            

if __name__ == "__main__":
    calculatrice()