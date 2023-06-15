from pru import BinaryTree, insert, create_tree, search_morse, to_morse, to_word


def menu():
    print("***********")
    print("1. Convertir palabra a código Morse")
    print("2. Convertir código Morse a palabra")
    print("3. Salir")
    print("***********")
    choice = input("Elige una opción (1-3): ")
    return choice

def main():
    root = create_tree()
    while True:
        choice = menu()
        if choice == "1":
            word = input("Escribe una palabra: ")
            morse = to_morse(word, root)
            print(f"El código Morse de {word} es: {morse}")
        elif choice == "2":
            morse = input("Escribe un código Morse: ")
            word = to_word(morse, root)
            print(f"El código Morse {morse} corresponde a la palabra: {word}")
        elif choice == "3":
            break
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    main()
