# Empresa, numero de vuelo, cantidad de asientos del avion, fecha de salida, destino, kms del vuelo.

from tda_lista import Lista,insertar,lista_vacia,eliminar,tamano,buscar,barrido,promedio_temperatura_humedad_mes,insertar2

#Menu prueba :) Miguel.R.C
def menu():

    print("       //BIENVENIDO A AEROPUERTO HERAKLION//        ")

    print("/x/x/-------------------------------------/x/x/")

    print("    1 - MOSTRAR VUELOS CON DESTINO ATENAS, MICONOS y RODAS\n",
          "    2 - MOSTRAR VUELOS CON CLASE TURISTA DISPONIBLE\n",
          "    3 - MOSTRAR TOTAL RECAUDADO POR CADA VUELO (TURISTA Y PRIMERA CLASE)\n"  #SEPARADOS
          "    4 - MOSTRAR VUELOS PROGRAMADOS SEGUN FECHA\n"
          "    5 - VENDER UN PASAJE PARA UN VUELO DETERMINADO\n",
          "    6 - ELIMINAR VUELO, Y CALCULAR DINERO DE REEMBOLSO\n",
          "    7 - MOSTRAR EMPRESAS Y KM DE VUELOS CON DESTINO A TAILANDIA\n",
          "    0 - SALIR")

    opcion = int(input("\n Ingrese una opcion : "))

    if opcion == 0:

        print("OUT")

    elif (opcion == 1):
        # Obtenemos la lista de vuelos que cumplen con los criterios
        vuelos = vuelos_destinos(listaH)
        # Mostramos los vuelos utilizando la función barrido
        if not lista_vacia(vuelos):
            print("Los vuelos con destino a Atenas, Miconos y Rodas son:")
            barrido(vuelos)
        else:
            print("No se encontraron vuelos con destino a Atenas, Miconos y Rodas")

   
        menu()   
    elif (opcion == 2):
        # Recorremos la lista de vuelos
        actual = listaH.inicio
        while actual is not None:
            # Verificamos si hay asientos en clase turista disponibles
            if actual.info['clase turista'] > 0:
                # Mostramos los detalles del vuelo
                print("Vuelo:", actual.info['numero_vuelo'])
                print("Empresa:", actual.info['empresa'])
                print("Destino:", actual.info['destino'])
                print("Fecha de salida:", actual.info['fecha_salida'])
                print("Asientos disponibles en clase turista:", actual.info['clase turista'])
                print("Asientos disponibles en primera clase:", actual.info['primera clase'])
                print("Kilómetros de vuelo:", actual.info['km_vuelo'])
                print()
            # Pasamos al siguiente nodo
            actual = actual.sig
    
        menu()

    elif(opcion ==  3): 
        # Recorremos la lista de vuelos y calculamos el total recaudado por cada uno
        actual = listaH.inicio
        while actual is not None:
            # Calculamos el total recaudado para la clase turista y la primera clase
            recaudado_turista = actual.info['clase turista'] * 75
            recaudado_primera = actual.info['primera clase'] * 203
            # Mostramos el total recaudado para cada vuelo
            print(f"Vuelo {actual.info['numero_vuelo']}:")
            print(f" - Clase turista: {actual.info['clase turista']} pasajeros, total recaudado: ${recaudado_turista}")
            print(f" - Primera clase: {actual.info['primera clase']} pasajeros, total recaudado: ${recaudado_primera}")
            # Pasamos al siguiente nodo
            actual = actual.sig
        # Volvemos al menú principal

        menu()

    elif(opcion == 4):
       
        menu()
    ###################################
    elif(opcion == 5):
        # Recorremos la lista de vuelos y calculamos el total recaudado por cada uno
        actual = listaH.inicio
        vender_asiento(listaH)
        actual = actual.sig
        # Volvemos al menú principal
        menu()
    elif(opcion == 6):
        # Recorremos la lista de vuelos y calculamos el total recaudado por cada uno
        actual = listaH.inicio
        numero_vuelo = input("Ingrese el número de vuelo a eliminar: ")
        eliminar_vuelo(listaH, numero_vuelo)
        actual = actual.sig
        # Volvemos al menú principal
        menu()

listaH = Lista()

aviones = [
           {'empresa': 'American Airlines', 
            'numero_vuelo': 'AA101', 
            'clase turista': 10, 
            'primera clase': 90,
            'fecha_salida': '2023-05-01', 
            'fecha_llegada': '2023-05-02', 
            'destino': 'Atenas', 
            'km_vuelo': 7500},

           {'empresa': 'Delta Airlines', 
            'numero_vuelo': 'DL202', 
            'primera clase': 5, 
            'clase turista': 95,
            'fecha_salida': '2023-06-15', 
            'fecha_llegada': '2023-06-16', 
            'destino': 'Tokyo', 
            'km_vuelo': 11000},

           {'empresa': 'Air France', 
            'numero_vuelo': 'AF303', 
            'primera clase': 20, 
            'clase turista': 80,
            'fecha_salida': '2023-07-22', 
            'fecha_llegada': '2023-07-23', 
            'destino': 'Miconos', 
            'km_vuelo': 9000},

           {'empresa': 'British Airways', 
            'numero_vuelo': 'BA404', 
            'primera clase': 15, 
            'clase turista': 85,
            'fecha_salida': '2023-08-10', 
            'fecha_llegada': '2023-08-11', 
            'destino': 'New York', 
            'km_vuelo': 6500},

           {'empresa': 'Lufthansa', 
            'numero_vuelo': 'LH505',
            'primera clase': 10, 
            'clase turista': 90,
            'fecha_salida': '2023-09-05', 
            'fecha_llegada': '2023-09-06', 
            'destino': 'Rodas', 
            'km_vuelo': 12500}
]

for avion in aviones:
    insertar2(listaH,avion)
#----------------------------
def vuelos_destinos(lista):
    # Creamos una lista vacía para almacenar los vuelos que cumplen con los criterios
    vuelos_destino = Lista()
    # Obtenemos el primer nodo de la lista
    actual = lista.inicio
    # Recorremos la lista mientras el nodo actual no sea None
    while actual is not None:
        # Si el destino es Atenas, Miconos o Rodas, lo agregamos a la lista de vuelos_destino
        if actual.info['destino'] in ['Atenas', 'Miconos', 'Rodas']:
            insertar2(vuelos_destino, actual.info)
        # Pasamos al siguiente nodo
        actual = actual.sig
    # Retornamos la lista de vuelos que cumplen con los criterios
    return vuelos_destino
#--------------------------------------
def vender_asiento(lista_vuelos):
    numero_vuelo = input("Ingrese el número de vuelo: ")
    clase = int(input("Ingrese la clase (1 para turista, 2 para primera clase): "))
    cantidad = int(input("Ingrese la cantidad de asientos que desea comprar: "))
    
    actual = lista_vuelos.inicio
    while actual is not None:
        if actual.info['numero_vuelo'] == numero_vuelo:
            if clase == 1:
                if actual.info['clase turista'] >= cantidad:
                    actual.info['clase turista'] -= cantidad
                    print(f"Se han vendido exitosamente {cantidad} asientos en clase turista.")
                else:
                    print("No hay suficientes asientos disponibles en clase turista.")
            elif clase == 2:
                if actual.info['primera clase'] >= cantidad:
                    actual.info['primera clase'] -= cantidad
                    print(f"Se han vendido exitosamente {cantidad} asientos en primera clase.")
                else:
                    print("No hay suficientes asientos disponibles en primera clase.")
            else:
                print("La clase ingresada no es válida.")
            return
        actual = actual.sig
    print("El número de vuelo ingresado no se encuentra en la lista.")

#-----------------------------
def eliminar_vuelo(listaH, numero_vuelo):
    actual = listaH.inicio
    anterior = None
    while actual is not None:
        if actual.info['numero_vuelo'] == numero_vuelo:
            # Calcular devolución si hay asientos vendidos
            asientos_vendidos = actual.info['clase turista'] + actual.info['primera clase']
            if asientos_vendidos > 0:
                total_devolver = actual.info['clase turista'] * 75 + actual.info['primera clase'] * 203
                print(f"Se deben devolver ${total_devolver} por la venta de {asientos_vendidos} asientos.")
            # Eliminar el nodo de la lista
            if anterior is None:
                listaH.inicio = actual.sig
            else:
                anterior.sig = actual.sig
            return
        anterior = actual
        actual = actual.sig
    print(f"No se encontró el vuelo {numero_vuelo} en la lista.")


menu()  