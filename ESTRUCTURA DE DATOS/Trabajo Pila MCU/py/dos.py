class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def tamano(self):
        return len(self.items)

    def imprimir_pila(self):
        for item in reversed(self.items):
            print(item)

def determinar_posicion_rocket_y_groot(pila):
    pos_groot = -1
    pos_rocket = -1

    for i, personaje in enumerate(pila.items):
        if personaje[0] == "Groot":
            pos_groot = i + 1
        elif personaje[0] == "Rocket Raccoon":
            pos_rocket = i + 1

    if pos_groot != -1:
        print(f"Groot está en la posición {pos_groot}")
    else:
        print("Groot no se encuentra en la pila")

    if pos_rocket != -1:
        print(f"Rocket Raccoon está en la posición {pos_rocket}")
    else:
        print("Rocket Raccoon no se encuentra en la pila")

def personajes_mas_de_5_pelis(pila):
    print("Personajes que aparecieron en más de 5 películas:")

    for personaje in pila.items:
        if personaje[1] > 5:
            print(f"{personaje[0]} ({personaje[1]} películas)")

def participacion_black_widow(pila):
    contador = 0

    for personaje in pila.items:
        if personaje[0] == "Black Widow":
            contador += personaje[1]

    print(f"La Viuda Negra participó en {contador} películas")

def mostrar_personajes_con_letras(pila, letras):
    letras = letras.lower()
    print(f"Personajes cuyos nombres empiezan con {letras}:")
    for personaje in pila.items:
        if personaje[0].lower().startswith(letras):
            print(f"{personaje[0]} ({personaje[1]} películas)")

pila_mcu = Pila()

while True:
    print("""
Bienvenido al programa de la pila de personajes del MCU

1. Agregar personaje
2. Determinar posición de Rocket y Groot
3. Personajes que aparecieron en más de 5 películas
4. Determinar en cuántas películas participó la Viuda Negra
5. Mostrar personajes con nombres que empiezan con C, D y G
6. Salir
""")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del personaje: ")
        cant_pelis = int(input("Ingrese la cantidad de películas en las que participó: "))
        pila_mcu.apilar((nombre, cant_pelis))
        print("El personaje ha sido agregado a la pila\n")
    elif opcion == "2":
        determinar_posicion_rocket_y_groot(pila_mcu)
    elif opcion == "3":
        personajes_mas_de_5_pelis(pila_mcu)
    elif opcion == "4":
        participacion_black_widow(pila_mcu)
    elif opcion == "5":
        letras = input("Ingrese las letras para filtrar los personajes
