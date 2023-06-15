def vender_pasaje(listaH, numero_vuelo, clase):
    actual = listaH.inicio
    while actual is not None:
        if actual.info['numero_vuelo'] == numero_vuelo:
            if clase == 'turista':
                if actual.info['clase turista'] > 0:
                    actual.info['clase turista'] -= 1
                    print(f"Pasaje vendido en clase turista para el vuelo {numero_vuelo}")
                    return
                else:
                    print("No hay asientos disponibles en clase turista para este vuelo")
                    return
            elif clase == 'primera':
                if actual.info['primera clase'] > 0:
                    actual.info['primera clase'] -= 1
                    print(f"Pasaje vendido en primera clase para el vuelo {numero_vuelo}")
                    return
                else:
                    print("No hay asientos disponibles en primera clase para este vuelo")
                    return
            else:
                print("La clase seleccionada no es válida")
                return
        actual = actual.sig
    print(f"No se encontró el vuelo {numero_vuelo}")
