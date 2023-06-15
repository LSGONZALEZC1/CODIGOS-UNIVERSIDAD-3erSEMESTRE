class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, code, letter):
    for char in code:
        if char == ".":
            if not root.left:
                root.left = BinaryTree(None)
            root = root.left
        elif char == "-":
            if not root.right:
                root.right = BinaryTree(None)
            root = root.right
    root.data = letter

def create_tree():
    root = BinaryTree(None)
    insert(root, ".-", "A")
    insert(root, "-...", "B")
    insert(root, "-.-.", "C")
    insert(root, "-..", "D")
    insert(root, ".", "E")
    insert(root, "..-.", "F")
    insert(root, "--.", "G")
    insert(root, "....", "H")
    insert(root, "..", "I")
    insert(root, ".---", "J")
    insert(root, "-.-", "K")
    insert(root, ".-..", "L")
    insert(root, "--", "M")
    insert(root, "-.", "N")
    insert(root, "---", "O")
    insert(root, ".--.", "P")
    insert(root, "--.-", "Q")
    insert(root, ".-.", "R")
    insert(root, "...", "S")
    insert(root, "-", "T")
    insert(root, "..-", "U")
    insert(root, "...-", "V")
    insert(root, ".--", "W")
    insert(root, "-..-", "X")
    insert(root, "-.--", "Y")
    insert(root, "--..", "Z")

    return root

def to_morse(word, root):
    morse = ""
    for char in word:
        try:
            morse += search_morse(root, char)
        except ValueError:
            print(f"No se encontró el carácter '{char}' en el árbol binario.")
    return morse

    
def node_code(node):
    if not node:
        return ""
    else:
        return ("." if not node.left else "-") + node_code(node.left or node.right)

def to_word(morse, root):
    word = ""
    for letter in morse.split(" "):
        if letter == "":
            word += " "
        else:
            node = root
            for char in letter:
                node = node.left if char == "." else node.right
            word += node.data
    return word
