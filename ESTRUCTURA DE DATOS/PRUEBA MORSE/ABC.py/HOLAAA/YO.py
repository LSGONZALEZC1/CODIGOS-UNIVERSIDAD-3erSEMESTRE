class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
 
class MorseTree:
    def __init__(self):
        self.raiz = Nodo(None)
 
    def agregarCodigo(self, letra, codigo):
        nodo_actual = self.raiz
        for simbolo in codigo:
            if simbolo == ".":
                if not nodo_actual.izquierda:
                    nodo_actual.izquierda = Nodo(None)
                nodo_actual = nodo_actual.izquierda
            elif simbolo == "-":
                if not nodo_actual.derecha:
                    nodo_actual.derecha = Nodo(None)
                nodo_actual = nodo_actual.derecha
 
        nodo_actual.valor = letra
 
    def buscarLetra(self, codigo):
        nodo_actual = self.raiz
        for simbolo in codigo:
            if simbolo == ".":
                nodo_actual = nodo_actual.izquierda
            elif simbolo == "-":
                nodo_actual = nodo_actual.derecha
            if not nodo_actual:
                return None
        return nodo_actual.valor

def convertirA_morse(palabra):
    morse = ""
    for letra in palabra:
        if letra in codigo_morse:
            morse += codigo_morse[letra] + " "
        else:
            morse += " "
    return morse

def convertirA_palabra(morse):
    palabra = ""
    codigo = morse.split(" ")
    for c in codigo:
        if c in letra_morse:
            palabra += letra_morse[c]
    return palabra

codigo_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
    ',': '--..--', '?': '..--..', ';': '-.-.-.', ':': '---...', '(': '-.--.', ')': '-.--.-', '-': '-....-', '/': '-..-.',
    '+': '.-.-.', '=': '-...-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '!': '-.-.--', '@': '.--.-.'
}
