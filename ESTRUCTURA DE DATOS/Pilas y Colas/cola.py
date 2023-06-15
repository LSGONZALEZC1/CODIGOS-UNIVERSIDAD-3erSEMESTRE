from Colas import Cola, arribo, atencion, cola_vacia, tamano, en_frente

cdatos=Cola()
cvocales=Cola()

letra=input('Ingrese un caracter: ')
while(letra !=''):
    arribo(cdatos, letra)
    letra=input('Ingrese un caracter: ')
    
tamanocola = tamano(cdatos)
print('Tamaño de la cola de caractere: '+str(tamanocola))

frentecola = en_frente(cdatos)
print('Valor en el frente: '+str(frentecola))

while(not cola_vacia(cdatos)):
    letra=atencion(cdatos)
    if letra.upper() in ['A', 'E', 'I', 'O', 'U']:
        arribo(cvocales, letra)
        
tamanocola = tamano(cvocales)
print('Tamaño de la cola de las vocales: '+str(tamanocola))
print('Vocales')
while(not cola_vacia(cvocales)):
    dato=atencion(cvocales)
    print(dato)
    