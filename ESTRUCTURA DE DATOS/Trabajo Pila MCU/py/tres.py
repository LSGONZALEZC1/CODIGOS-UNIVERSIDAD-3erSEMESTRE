class Pila:
    def __init__(self):
        self.datos = []
        self.tope = -1

    def apilar(self, elemento):
        self.datos.append(elemento)
        self.tope += 1

    def desapilar(self):
        if self.esta_vacia():
            return None
        elemento = self.datos.pop()
        self.tope -= 1
        return elemento

    def tamano(self):
        return len(self.datos)

    def esta_vacia(self):
        return self.tamano() == 0


pila_mcu = Pila()

# se agregan los personajes a la pila
pila_mcu.apilar(('Iron Man', 3))
pila_mcu.apilar(('Thor', 5))
pila_mcu.apilar(('Captain America', 6))
pila_mcu.apilar(('Hulk', 3))
pila_mcu.apilar(('Black Widow', 6))
pila_mcu.apilar(('Hawkeye', 4))
pila_mcu.apilar(('Ant-Man', 2))
pila_mcu.apilar(('Spider-Man', 2))
pila_mcu.apilar(('Doctor Strange', 2))
pila_mcu.apilar(('Black Panther', 2))
pila_mcu.apilar(('Captain Marvel', 1))
pila_mcu.apilar(('Rocket Raccoon', 4))
pila_mcu.apilar(('Groot', 4))

while True:
    print("\n¿Qué actividad desea realizar?")
    print("1. En qué posición se encuentran Rocket Raccoon y Groot?")
    print("2. Cuáles son los personajes que participaron en más de 5 películas?")
    print("3. En que peliculas participó la Viuda Negra (Black Widow)?")
    print("4. Cuáles son los personajes cuyo nombre empieza con C, D y G?")
    print("5. Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        posicion = 1
        while not pila_mcu.esta_vacia():
            personaje = pila_mcu.desapilar()
            if personaje[0] in ("\nRocket Raccoon", "Groot"):
                
                print(f"{personaje[0]} se encuentra en la posición {posicion}")
                break
            posicion += 1
            
    elif opcion == "2":
        print("\nPersonajes que participaron en más de 5 películas:")
        while not pila_mcu.esta_vacia():
            personaje = pila_mcu.desapilar()
            if personaje[1] > 5:
                
                print(f"- {personaje[0]} ({personaje[1]} películas)")
           
    elif opcion == "3":
        while not pila_mcu.esta_vacia():
            personaje = pila_mcu.desapilar()
            if personaje[0] == "Black Widow":
                
                print(f"\nLa Viuda Negra (Black Widow) participó en {personaje[1]} películas")
                break
      
    if opcion == "4":
        personajes_cdg = []
        while not pila_mcu.esta_vacia():
            personaje = pila_mcu.desapilar()
            if personaje[0][0] in ("C", "D", "G"):
                personajes_cdg.append(personaje[0])
        
        print("Los personajes cuyos nombres empiezan con C, D o G son")
        for personaje in personajes_cdg:
            print("\n", personaje)
