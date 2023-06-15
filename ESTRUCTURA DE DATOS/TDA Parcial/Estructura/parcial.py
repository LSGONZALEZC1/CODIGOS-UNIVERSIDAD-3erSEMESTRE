# """ Se cuenta con los vuelos del aeropuerto de Heraklion en creta, de estos se sabe la siguienrte información: 
# Empresa, numero del vuelo, cantidad de asientos del avion, fecha de salida, destino, kms del vuelo. 
# y ademas se conoce los datos de cantidades de asientos totales y ocupados por clase(primera y turista). 
#  implemente las funciones necesarias que permitan realizar las siguientes actividades:"""
# A) mostrar los vuelos con destino a Atenas (342.1 km), Miconos(283.0 km) y Rodas(425.8 km);
# b) mostrar los vuelos con asientos clase turista disponible;
# C) mostrar el total recaudado por cada vuelo, considerando clase turista($75 por kilometro)(Atenas: 25.657,5 Miconos:21.225 Rodas: 31.935) y primera clase($203 por kilometro);
# D) Mostrar los vuelos programados para una determinada fecha;
# E) Vender un asiento (o ´pasaje) para un determinado de vuelo
# F) Eliminar un vuelo, Tener en cuenta que si tiene pasajes vendidos, se debe indicar la cantidad de dinero a devolver;
# G) Mostrar las empresas y los kilometros de vuelos con destino a Tailandia

# - Se debe crear una clase de Vuelo que contenga como atributos:
#   Empresa : String
#   clase : Clase
#   #vuelo : int
#   Cantidad de asientos: Int
#   Fecha de Salida: String
#   Destino: String
#   Kms del vuelo: Int
#   Distancia: int

# - Se debe crear clase TipoClase:
#    Cantidad de asientos disponibles PrimeraClase:200
#    Cantidad de asientos ocupados PrimeraClase:0
#    Cantidad de asientos disponibles Turista: 400
#    Cantidad de asientos ocupados turista: 0
#    Cantidad de asientos totales: 600

#   def ocuparAsientoTurista(cantAsientosAOcupar):
# 	    Asientos Ocupados Turista += cantAsientosAOcupar
# 	    Asientos Disponibles Turista -= cantAsientoAOcupar

#   def ocuparAsientoPrimeraClase(cantAsientosAOcupar):
# 	    Asientos Ocupados Primera clase += cantAsientosAOcupar
# 	    Asientos Disponibles primera clase -= cantAsientoAOcupar

# - Crear una lista de vuelos

from tda_lista import Lista, insertar, barrido, buscar, eliminar


class Vuelo:
    def __init__(self, empresa, numVuelo, asientosVuelo, fechaSalida,fechaLlegada, destino, distancia,clase):
        self.empresa = empresa
        self.numVuelo = numVuelo
        self.asientosVuelo = asientosVuelo
        self.fechaSalida = fechaSalida
        self.fechaLlegada = fechaLlegada
        self.destino = destino
        self.distancia = distancia
        self.clase = clase
        
class TipoClase:
    def __init__(self, turista, primeraClase):
        self.turista = turista
        self.primeraClase = primeraClase
        self.asientosTurista = 400
        self.asientosPC = 200
        self.asintos_Turista_Ocupados = 0
        self.asientos_PC_Ocupados = 0
        self.asientos_totales = 600
         
vuelois = Li

Vuelos = []