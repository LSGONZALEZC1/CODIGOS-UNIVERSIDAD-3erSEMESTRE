from binary_tree import BinaryTree
from morse_alphabet import MORSE_ALPHABET

# Crear un árbol binario para el código morse a partir del diccionario MORSE_ALPHABET
morse_tree = BinaryTree()
morse_tree.create_from_dict(MORSE_ALPHABET)

def morse_to_text(morse, morse_tree):
    converted = ''
    words = morse.split(' ')
    for word in words:
        node = morse_tree.root
        for char in word:
            if char == '.':
                node = node.left_child
            elif char == '-':
                node = node.right_child
        if node is not None:
            converted += node.value
        else:
            converted += ' '
    return converted

def text_to_morse(text, morse_tree):
    converted = ''
    text = text.upper()
    for char in text:
        if char == ' ':
            converted += ' '
        elif char in MORSE_ALPHABET:
            converted += MORSE_ALPHABET[char] + ' '
        else:
            converted += '? '
    return converted.strip()

def menu():
    print("Seleccione una opción:")
    print("1. Convertir texto normal a código morse")
    print("2. Convertir código morse a texto normal")
    choice = input(">> ")
    return int(choice)

while True:
    choice = menu()

    if choice == 1:
        text = input("Ingrese la palabra a convertir: ")
        morse = text_to_morse(text, morse_tree)
        print(morse)
    elif choice == 2:
        morse = input("Ingrese el código morse a convertir: ")
        text = morse_to_text(morse, morse_tree)
        print(text)
    else:
        print("Opción inválida. Por favor seleccione 1 o 2.")
