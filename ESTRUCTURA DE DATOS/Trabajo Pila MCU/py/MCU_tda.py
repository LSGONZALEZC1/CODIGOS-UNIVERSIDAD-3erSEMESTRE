class Pila:
    def __init__(self):
        self.items = []
        
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, elemento):
        self.items.append(elemento)
        
    def desapilar(self):
        if self.esta_vacia():
            raise Exception('La pila está vacía')
        return self.items.pop()
        
    def tamano(self):
        return len(self.items)

# Creamos la pila con los personajes de Marvel
marvel_pila = Pila()
marvel_pila.apilar(('Iron Man', 3))
marvel_pila.apilar(('Capitán América', 4))
marvel_pila.apilar(('Thor', 3))
marvel_pila.apilar(('Hulk', 2))
marvel_pila.apilar(('Viuda Negra', 6))
marvel_pila.apilar(('Ojo de Halcón', 3))
marvel_pila.apilar(('Spider-Man', 2))
marvel_pila.apilar(('Pantera Negra', 1))
marvel_pila.apilar(('Doctor Strange', 2))
marvel_pila.apilar(('Ant-Man', 2))
marvel_pila.apilar(('Capitana Marvel', 1))
marvel_pila.apilar(('Rocket Raccoon', 3))
marvel_pila.apilar(('Groot', 3))
marvel_pila.apilar(('Thanos', 3))
"""
# a. Determinar en qué posición se encuentran Rocket Raccoon y Groot
posicion_rocket = None
posicion_groot = None
tamano_pila = marvel_pila.tamano()
for i in range(tamano_pila):
    personaje = marvel_pila.desapilar()
    if personaje[0] == 'Rocket Raccoon':
        posicion_rocket = tamano_pila - i
    if personaje[0] == 'Groot':
        posicion_groot = tamano_pila - i
    if posicion_rocket and posicion_groot:
        break
        
print(f'\nRocket Raccoon está en la posición {posicion_rocket} y Groot está en la posición {posicion_groot}')


# b. Determinar los personajes que participaron en más de 5 películas de la saga
personajes_5_pelis = []
tamano_pila = marvel_pila.tamano()
for i in range(tamano_pila):
    personaje = marvel_pila.desapilar()
    if personaje[1] > 5:
        personajes_5_pelis.append(personaje)
        
print('\nPersonajes que participaron en más de 5 películas:')
for personaje in personajes_5_pelis:
    print(f'{personaje[0]} ({personaje[1]} películas)')
"""

# c. Determinar en cuantas películas participó la Viuda Negra
peliculas_viuda_negra = None
tamano_pila = marvel_pila.tamano()
for i in range(tamano_pila):
    personaje = marvel_pila.desapilar()
    if personaje[0] == 'Viuda Negra':
        peliculas_viuda_negra = personaje[1]
        break
        
print(f'\nLa Viuda Negra participó en {peliculas_viuda_negra} películas')

"""
# d. Mostrar todos los personajes cuyos nombre empiezan con C, D y G
personajes_cdg = []
tamano_pila = marvel_pila.tamano()
for i in range(tamano_pila):
    personaje = marvel_pila.desapilar()
    if personaje[0][0] in ['C', 'D', 'G']:
        personajes_cdg.append(personaje[0])
        
print('\nPersonajes que empiezan con C, D o G:')
for personaje in personajes_cdg:
    print("\n", personaje)"""

