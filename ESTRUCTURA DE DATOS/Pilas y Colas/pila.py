from Pilas import Pila, apilar, desapilar, pila_vacia, tamano, en_cima, barrido

pdatos = Pila()
ppar = Pila()
pimpar = Pila()
dato = int(input('Ingrese un numero - 0 para salir: '))

while(dato !=0):
    apilar(pdatos, dato)
    dato = int(input('Ingrese un numero - 0 para salir: '))
    
tamanopila = tamano(pdatos)
print('Tamaño de la pila: '+str(tamanopila))

cimapila = en_cima(pdatos)
print('Valor en cima de la pila: '+str(cimapila))

barridopila = barrido(pdatos)
