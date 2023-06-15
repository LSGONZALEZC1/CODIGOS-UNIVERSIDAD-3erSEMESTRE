from collections import deque

# Creamos una pila de personajes de MCU
pila_mcu = deque([
    ('Iron Man', 3),
    ('Thor', 5),
    ('Captain America', 6),
    ('Hulk', 3),
    ('Black Widow', 6),
    ('Hawkeye', 4),
    ('Ant-Man', 2),
    ('Spider-Man', 2),
    ('Doctor Strange', 2),
    ('Black Panther', 2),
    ('Captain Marvel', 1),
    ('Rocket Raccoon', 4),
    ('Groot', 4)
])

def posicion_rocket_y_groot(pila):
    """Determina la posición de Rocket Raccoon y Groot en la pila"""
    rocket_pos = None
    groot_pos = None
    for i, personaje in enumerate(pila):
        if personaje[0] == 'Rocket Raccoon':
            rocket_pos = i+1
        elif personaje[0] == 'Groot':
            groot_pos = i+1
        if rocket_pos is not None and groot_pos is not None:
            break
    return rocket_pos, groot_pos

def personajes_mas_de_5_pelis(pila):
    """Determina los personajes que participaron en más de 5 películas"""
    personajes = []
    for personaje in pila:
        if personaje[1] > 5:
            personajes.append(personaje[0])
    return personajes

def cantidad_pelis_viuda_negra(pila):
    """Determina en cuantas películas participó la Viuda Negra"""
    for personaje in pila:
        if personaje[0] == 'Black Widow':
            return personaje[1]

def personajes_con_iniciales(pila, iniciales):
    """Muestra los personajes cuyo nombre empieza con las iniciales indicadas"""
    personajes = []
    for personaje in pila:
        if personaje[0][0] in iniciales:
            personajes.append(personaje[0])
    return personajes

# Ejemplo de uso de las funciones
print(posicion_rocket_y_groot(pila_mcu))
# Output: (12, 11)

print(personajes_mas_de_5_pelis(pila_mcu))
# Output: ['Captain America', 'Black Widow']

print(cantidad_pelis_viuda_negra(pila_mcu))
# Output: 6

print(personajes_con_iniciales(pila_mcu, ['C', 'D', 'G']))
# Output: ['Captain America', 'Doctor Strange', 'Groot']
