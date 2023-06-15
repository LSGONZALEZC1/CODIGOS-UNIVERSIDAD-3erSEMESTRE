class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def construir_arbol(codigo_morse):
    raiz = Nodo(None)
    for letra, codigo in codigo_morse.items():
        nodo_actual = raiz
        for simbolo in codigo:
            if simbolo == ".":
                if not nodo_actual.izquierdo:
                    nodo_actual.izquierdo = Nodo(None)
                nodo_actual = nodo_actual.izquierdo
            elif simbolo == "-":
                if not nodo_actual.derecho:
                    nodo_actual.derecho = Nodo(None)
                nodo_actual = nodo_actual.derecho
        nodo_actual.valor = letra
    return raiz

from graphviz import Digraph

def dibujar_arbol(raiz):
    def dibujar_nodo(nodo, nodo_id, grafo):
        if nodo.valor:
            grafo.node(nodo_id, str(nodo.valor))
        else:
            grafo.node(nodo_id)
        if nodo.izquierdo:
            hijo_izq_id = nodo_id + "0"
            grafo.edge(nodo_id, hijo_izq_id, label=".")
            dibujar_nodo(nodo.izquierdo, hijo_izq_id, grafo)
        if nodo.derecho:
            hijo_der_id = nodo_id + "1"
            grafo.edge(nodo_id, hijo_der_id, label="-")
            dibujar_nodo(nodo.derecho, hijo_der_id, grafo)

    grafo = Digraph()
    dibujar_nodo(raiz, "0", grafo)
    grafo.render("arbol_cod_morse.png", view=True)

def obtener_caracter(raiz, codigo):
    nodo_actual = raiz
    for simbolo in codigo:
        if simbolo == ".":
            nodo_actual = nodo_actual.izquierdo
        elif simbolo == "-":
            nodo_actual = nodo_actual.derecho
    return nodo_actual.valor

def a_morse(frase, codigo_morse):
    codigo_morse_inv = {v: k for k, v in codigo_morse.items()}
    morse = ""
    for caracter in frase:
        if caracter != " ":
            morse += codigo_morse_inv[caracter] + " "
        else:
            morse += "/ "
    return morse.strip()

def a_palabra(morse, codigo_morse):
    codigo_morse_inv = {v: k for k, v in codigo_morse.items()}
    caracteres = morse.split()
    palabra = ""
    for caracter in caracteres:
        if caracter == "/":
            palabra += " "
        else:
            letra = codigo_morse_inv.get(caracter)
            if letra:
                palabra += letra
    return palabra


codigo_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

morse = '- .... . / .-- .. - .... / .- ... / - .... . / -- --- .-. ... . / ..-. --- .-. / -- ..- -. -.-. .... .. -.-. / .--. .-.. .- --. .... - / .. ... / .--. .-.. .- --. .... -'

palabra = a_palabra(morse, codigo_morse)
print(palabra)  # "THE WITH A HORSE FOR MICROPHONE PLAGE IS WALM"
