import datetime

class EstacionMeteorologica:
    def _init_(self, nombre, pais, latitud, longitud, altitud):
        self.nombre = nombre
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud
        self.registros_diarios = {}

    def agregar_registro_diario(self, fecha, hora, temperatura, presion, humedad):
        if fecha not in self.registros_diarios:
            self.registros_diarios[fecha] = []
        self.registros_diarios[fecha].append({'hora': hora, 'temperatura': temperatura, 'presion': presion, 'humedad': humedad})

def promedio_temperatura_humedad(estaciones, fecha):
    temperatura_total = 0
    humedad_total = 0
    cantidad_registros = 0
    for estacion in estaciones:
        if fecha in estacion.registros_diarios:
            for registro in estacion.registros_diarios[fecha]:
                temperatura_total += registro['temperatura']
                humedad_total += registro['humedad']
                cantidad_registros += 1
    if cantidad_registros > 0:
        promedio_temperatura = round(temperatura_total / cantidad_registros, 2)
        promedio_humedad = round(humedad_total / cantidad_registros, 2)
        return (promedio_temperatura, promedio_humedad)
    else:
        return None
# Creamos algunas estaciones meteorológicas y agregamos algunos registros diarios
estacion1 = EstacionMeteorologica('Estación 1', 'México', 19.4326, -99.1332, 2300)
estacion1.agregar_registro_diario(datetime.date(2023, 4, 15), datetime.time(9, 0), 23.5, 1013, 60)
estacion1.agregar_registro_diario(datetime.date(2023, 4, 16), datetime.time(12, 0), 25.3, 1012, 58)
estacion1.agregar_registro_diario(datetime.date(2023, 5, 1), datetime.time(15, 0), 27.0, 1011, 55)

estacion2 = EstacionMeteorologica('Estación 2', 'Estados Unidos', 37.7749, -122.4194, 10)
estacion2.agregar_registro_diario(datetime.date(2023, 4, 15), datetime.time(9, 0), 18.0, 1010, 70)
estacion2.agregar_registro_diario(datetime.date(2023, 4, 16), datetime.time(12, 0), 20.1, 1012, 68)
estacion2.agregar_registro_diario(datetime.date(2023, 5, 1), datetime.time(15, 0), 22.3, 1014, 65)

estacion3 = EstacionMeteorologica('Estación 3', 'España', 40.4168, -3.7038, 700)
estacion3.agregar_registro_diario(datetime.date(2023, 4, 15), datetime.time(9, 0), 17.5, 1012, 70)
estacion3.agregar_registro_diario(datetime.date(2023, 4, 16), datetime.time(12, 4),15.6,1015,78)

# Calculamos el promedio de la temperatura y la humedad para el mes de mayo
fecha = datetime.date(2023, 5, 1)
promedio = promedio_temperatura_humedad([estacion1, estacion2, estacion3], fecha)
if promedio:
    print(f"El promedio de temperatura en mayo fue de {promedio[0]}°C")
    print(f"El promedio de humedad en mayo fue de {promedio[1]}%")
else:
    print("No hay registros para el mes de mayo")