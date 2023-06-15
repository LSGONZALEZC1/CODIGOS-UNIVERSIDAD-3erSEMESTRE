from TDA_Cola import Cola, arribo, atencion, cola_vacia, tamaño, en_frente, barrido_mover_final, mover_al_final, barrido, total
import random

tipos_vehiculos = ['automóvil', 'camioneta', 'camión', 'colectivo', 'moto']

# hacer referencia directamente al precio del vehiculo
tarifas_vehiculos = {
    'automóvil': 47,
    'camioneta': 59,
    'camión': 71,
    'colectivo': 64,
    'moto': 35
}

cabina1 = Cola()
cabina2 = Cola()
cabina3 = Cola()

# Crear diccionario con los contadores por tipo de vehículo y por cabina
vehiculos_por_cabina_y_tipo = {cabina1: {tipo: 0 for tipo in tipos_vehiculos}, 
                               cabina2: {tipo: 0 for tipo in tipos_vehiculos}, 
                               cabina3: {tipo: 0 for tipo in tipos_vehiculos}}

# Función para agregar un vehículo a una cabina de cobro
def agregar_vehiculo():
    tipo_vehiculo = random.choice(tipos_vehiculos)
    tarifa_vehiculo = tarifas_vehiculos[tipo_vehiculo]
    vehiculo = {
        'tipo': tipo_vehiculo,
        'tarifa': tarifa_vehiculo,
        'tiempo_llegada': random.randint(0, 30),
        'cabina_asignada': None,
    }
    for i in range(30):
        if tamaño(cabina1) <= tamaño(cabina2) and tamaño(cabina1) <= tamaño(cabina3):
            vehiculo['cabina_asignada'] = cabina1
            arribo(cabina1, vehiculo)
            vehiculos_por_cabina_y_tipo[cabina1][tipo_vehiculo] += 1
            break
        elif tamaño(cabina2) <= tamaño(cabina1) and tamaño(cabina2) <= tamaño(cabina3):
            vehiculo['cabina_asignada'] = cabina2
            arribo(cabina2, vehiculo)
            vehiculos_por_cabina_y_tipo[cabina2][tipo_vehiculo] += 1
            break
        else:
            vehiculo['cabina_asignada'] = cabina3
            arribo(cabina3, vehiculo)
            vehiculos_por_cabina_y_tipo[cabina3][tipo_vehiculo] += 1
            break

# Simulación de la cabina de peaje
for i in range(30):
    agregar_vehiculo()

# Atender los vehículos de las cabinas
tiempo_total = 0
while not (cola_vacia(cabina1) and cola_vacia(cabina2) and cola_vacia(cabina3)):
    for cabina in [cabina1, cabina2, cabina3]:
        if not cola_vacia(cabina):
            vehiculo = en_frente(cabina)
            tiempo_total += 2
            total[tipos_vehiculos.index(vehiculo['tipo'])] += vehiculo['tarifa']
            vehiculos_por_cabina_y_tipo[cabina][vehiculo['tipo']] -= 1
            