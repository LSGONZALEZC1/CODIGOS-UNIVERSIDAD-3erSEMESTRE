class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def create_morse_tree():
        morse_tree = BinaryTree()

        insert(morse_tree, ' ', ' ')
        insert(morse_tree, 'E', '.')
        insert(morse_tree, 'T', '-')
        insert(morse_tree, 'I', '..')
        insert(morse_tree, 'A', '.-')
        insert(morse_tree, 'N', '-.')
        insert(morse_tree, 'M', '--')
        insert(morse_tree, 'S', '...')
        insert(morse_tree, 'U', '..-')
        insert(morse_tree, 'R', '.-.')
        insert(morse_tree, 'W', '.--')
        insert(morse_tree, 'D', '-..')
        insert(morse_tree, 'K', '-.-')
        insert(morse_tree, 'G', '--.')
        insert(morse_tree, 'O', '---')
        insert(morse_tree, 'H', '....')
        insert(morse_tree, 'V', '...-')
        insert(morse_tree, 'F', '..-.')
        insert(morse_tree, 'L', '.-..')
        insert(morse_tree, 'P', '.--.')
        insert(morse_tree, 'J', '.---')
        insert(morse_tree, 'B', '-...')
        insert(morse_tree, 'X', '-..-')
        insert(morse_tree, 'C', '-.-.')
        insert(morse_tree, 'Y', '-.--')
        insert(morse_tree, 'Z', '--..')
        insert(morse_tree, 'Q', '--.-')
        return morse_tree

def insert(tree, letter, code):
    current_node = tree.root
    for symbol in code:
        if symbol == '.':
            if current_node.left_child is None:
                current_node.left_child = Node()
            current_node = current_node.left_child
        elif symbol == '-':
            if current_node.right_child is None:
                current_node.right_child = Node()
            current_node = current_node.right_child
    current_node.value = letter
    
def text_to_morse(text, morse_tree):
    converted = []
    for char in text:
        node = morse_tree.root
        if char != ' ':
            code = ''
            while node is not None and node.value != char:
                if char in node.left_child.value:
                    node = node.left_child
                    code += '.'
                elif char in node.right_child.value:
                    node = node.right_child
                    code += '-'
            converted.append(code)
        else:
            converted.append('')
    return ' '.join(converted)

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