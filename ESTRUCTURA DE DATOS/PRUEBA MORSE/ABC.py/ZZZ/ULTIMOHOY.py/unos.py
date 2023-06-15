class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Árbol de código Morse
arbol_morse = Nodo()
arbol_morse.izquierda = Nodo('E')
arbol_morse.izquierda.izquierda = Nodo('I')
arbol_morse.izquierda.izquierda.izquierda = Nodo('S')
arbol_morse.izquierda.izquierda.derecha = Nodo('U')
arbol_morse.izquierda.derecha = Nodo('A')
arbol_morse.izquierda.derecha.izquierda = Nodo('R')
arbol_morse.izquierda.derecha.derecha = Nodo('W')
arbol_morse.derecha = Nodo('T')
arbol_morse.derecha.izquierda = Nodo('N')
arbol_morse.derecha.izquierda.izquierda = Nodo('D')
arbol_morse.derecha.izquierda.derecha = Nodo('K')
arbol_morse.derecha.derecha = Nodo('M')
arbol_morse.derecha.derecha.izquierda = Nodo('G')
arbol_morse.derecha.derecha.derecha = Nodo('O')

def convertir_palabra_a_morse(palabra):
    codigo_morse = []
    for letra in palabra:
        letra = letra.upper()
        # Si la letra está en el árbol Morse, buscar su equivalente
        nodo_actual = arbol_morse
        if letra == ' ':
            codigo_morse.append('/')
            continue
        while nodo_actual and nodo_actual.valor != letra:
            if letra == '.':
                nodo_actual = nodo_actual.izquierda
            elif letra == '-':
                nodo_actual = nodo_actual.derecha
        if nodo_actual:
            codigo_morse.append(letra_nodo_actual(nodo_actual)) # función letra_nodo_actual retornará el equivalente en código Morse del nodo actual
    return ''.join(codigo_morse)

def convertir_morse_a_palabra(codigo_morse):
    letras = codigo_morse.split(' ')
    palabra = ''
    for letra in letras:
        nodo_actual = arbol_morse
        if letra == '/':
            palabra += ' '
            continue
        for simbolo in letra:
            if simbolo == '.':
                nodo_actual = nodo_actual.izquierda
            elif simbolo == '-':
                nodo_actual = nodo_actual.derecha
        if nodo_actual.valor:
            palabra += nodo_actual.valor
    return palabra
