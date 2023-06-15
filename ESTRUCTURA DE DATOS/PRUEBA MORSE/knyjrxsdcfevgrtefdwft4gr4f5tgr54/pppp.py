class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
class MorseTree:
    def __init__(self):
        self.root = Node(None)
 
    def insert(self, letter, code):
        node = self.root
        for c in code:
            if c == '.':
                if not node.left:
                    node.left = Node(None)
                node = node.left
            elif c == '-':
                if not node.right:
                    node.right = Node(None)
                node = node.right
        node.val = letter
 
    def search(self, code):
        node = self.root
        for c in code:
            if not node:
                return None
            if c == '.':
                node = node.left
            elif c == '-':
                node = node.right
        return node.val
 
morse_tree = MorseTree()
morse_tree.insert('A', '.-')
morse_tree.insert('B', '-...')
morse_tree.insert('C', '-.-.')
morse_tree.insert('D', '-..')
morse_tree.insert('E', '.')
morse_tree.insert('F', '..-.')
morse_tree.insert('G', '--.')
morse_tree.insert('H', '....')
morse_tree.insert('I', '..')
morse_tree.insert('J', '.---')
morse_tree.insert('K', '-.-')
morse_tree.insert('L', '.-..')
morse_tree.insert('M', '--')
morse_tree.insert('N', '-.')
morse_tree.insert('O', '---')
morse_tree.insert('P', '.--.')
morse_tree.insert('Q', '--.-')
morse_tree.insert('R', '.-.')
morse_tree.insert('S', '...')
morse_tree.insert('T', '-')
morse_tree.insert('U', '..-')
morse_tree.insert('V', '...-')
morse_tree.insert('W', '.--')
morse_tree.insert('X', '-..-')
morse_tree.insert('Y', '-.--')
morse_tree.insert('Z', '--..')
 
def to_morse(word):
    morse = ''
    for letter in word:
        letter = letter.upper()
        code = morse_tree.search(letter)
        morse += code + ' ' if code else ''
    return morse
 
def to_morse(word):
    morse = ''
    for letter in word:
        letter = letter.upper()
        code = morse_tree.search(letter)
        morse += code + ' ' if code else ''
    return morse
 
def from_morse(morse):
    word = ''
    codes = morse.split()
    for code in codes:
        letter = morse_tree.search(code)
        word += letter if letter else ''
    return word

while True:
    print("1. Convertir palabra a código Morse")
    print("2. Convertir código Morse a palabra")
    print("3. Salir")
    choice = input("Elige una opción: ")

    if choice == "1":
        word = input("Introduce una palabra: ")
        morse = to_morse(word)
        print(f"La palabra {word} en código Morse es: {morse}")

    elif choice == "2":
        morse = input("Introduce código Morse: ")
        word = from_morse(morse)
        print(f"El código Morse {morse} corresponde a la palabra: {word}")

    elif choice == "3":
        print("Adios!")
        break

    else:
        print("Opción no válida. Por favor, elige de nuevo.")
