from typing import List, Tuple

# Definición de TDA para vuelos
class Vuelo:
    def _init_(self, empresa: str, numero: str, asientos_totales: int,
                 fecha_salida: str, destino: str, kms: int,
                 asientos_primera: int, asientos_turista: int, vuelo: str):
        self.empresa = empresa
        self.numero = numero
        self.asientos_totales = asientos_totales
        self.fecha_salida = fecha_salida
        self.destino = destino
        self.kms = kms
        self.asientos_primera = asientos_primera
        self.asientos_turista = asientos_turista
        self.vuelos = vuelo
    
    def asientos_turista_disponibles(self) -> bool:
        return self.asientos_turista > 0
 # Definición de TDA para lista de vuelos
class ListaVuelos:
    def _init_(self, vuelos: List[Vuelo]):
        self.vuelos = vuelos
    
    def vuelos_turista_disponibles(self) -> List[Vuelo]:
        return [v for v in self.vuelos if v.asientos_turista_disponibles()]
    
# Crear lista de vuelos
vuelos = [
    Vuelo("Empresa A", "Vuelo 123", 200, "2023-04-18", "Ciudad 1", 500,
          20, 100),
    Vuelo("Empresa B", "Vuelo 456", 150, "2023-04-18", "Ciudad 2", 700,
          30, 50),
    Vuelo("Empresa C", "Vuelo 789", 300, "2023-04-19", "Ciudad 3", 1000,
          40, 0),
    Vuelo("Empresa D", "Vuelo 999", 100, "2023-04-20", "Ciudad 4", 800,
          10, 10)
]

# Crear objeto ListaVuelos
lista_vuelos = ListaVuelos(vuelos)

# Obtener vuelos con asientos de clase turista disponibles
vuelos_turista_disponibles = lista_vuelos.vuelos_turista_disponibles()

# Imprimir información de los vuelos encontrados
for vuelo in vuelos_turista_disponibles:
    print(f"{vuelo.empresa} {vuelo.numero} - {vuelo.destino}")