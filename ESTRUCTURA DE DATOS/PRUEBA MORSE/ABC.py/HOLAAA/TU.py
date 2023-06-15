from YO import MorseTree

# Crear el árbol binario
morse_tree = MorseTree()
morse_tree.agregarCodigo('A', '.-')
morse_tree.agregarCodigo('B', '-...')
morse_tree.agregarCodigo('C', '-.-.')
morse_tree.agregarCodigo('D', '-..')
# Agregue los códigos para todas las letras del alfabeto y los números

def convertir_a_morse(palabra):
    return morse_tree.convertir_a_morse(palabra)

def convertir_a_palabra(morse):
    return morse_tree.convertir_a_palabra(morse)

def mostrar_menu():
    print("Bienvenido al conversor de código Morse")
    print("1. Convertir palabra a código Morse")
    print("2. Convertir código Morse a palabra")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        palabra = input("Ingrese la palabra a convertir: ")
        codigo_morse = convertir_a_morse(palabra.upper())
        print("La palabra en código Morse es: " + codigo_morse)
    elif opcion == "2":
        codigo_morse = input("Ingrese el código Morse a convertir: ")
        palabra = convertir_a_palabra(codigo_morse)
        print("El código Morse en palabras es: " + palabra)
    elif opcion == "3":
        print("Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")