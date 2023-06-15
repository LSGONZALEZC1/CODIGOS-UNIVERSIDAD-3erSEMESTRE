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
pila_mcu = Pila()
pila_mcu.apilar(('Iron Man', 3))
pila_mcu.apilar(('Capitán América', 4))
pila_mcu.apilar(('Thor', 3))
pila_mcu.apilar(('Hulk', 2))
pila_mcu.apilar(('Viuda Negra', 6))
pila_mcu.apilar(('Ojo de Halcón', 3))
pila_mcu.apilar(('Spider-Man', 2))
pila_mcu.apilar(('Pantera Negra', 1))
pila_mcu.apilar(('Doctor Strange', 2))
pila_mcu.apilar(('Ant-Man', 2))
pila_mcu.apilar(('Capitana Marvel', 1))
pila_mcu.apilar(('Rocket Raccoon', 3))
pila_mcu.apilar(('Groot', 3))
pila_mcu.apilar(('Thanos', 3))



# d. Mostrar todos los personajes cuyos nombre empiezan con C, D y G
personajes_cdg = []
tamano_pila = pila_mcu.tamano()
for i in range(tamano_pila):
    personaje = pila_mcu.desapilar()
    if personaje[0][0] in ['C', 'D', 'G']:
        personajes_cdg.append(personaje[0])
        
print("\n", 'Personajes que empiezan con C, D o G:')
for personaje in personajes_cdg:
    print("\n", personaje)



# b. Determinar los personajes que participaron en más de 5 películas de la saga
personajes_5_pelis = []
tamano_pila = pila_mcu.tamano()
for i in range(tamano_pila):
    personaje = pila_mcu.desapilar()
    if personaje[1] > 5:
        personajes_5_pelis.append(personaje)
        
print('Personajes que participaron en más de 5 películas:')
for personaje in personajes_5_pelis:
    print(f'{personaje[0]} ({personaje[1]} películas)')
