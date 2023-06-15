class Vuelo:
    def __init__(self, empresa, numero_vuelo, asientos, fecha_salida, destino, kms_vuelo):
        self.empresa = empresa
        self.numero_vuelo = numero_vuelo
        self.asientos = asientos
        self.fecha_salida = fecha_salida
        self.destino = destino
        self.kms_vuelo = kms_vuelo
        self.primera_clase_ocupados = 0
        self.turista_ocupados = 0

    def asientos_disponibles_turista(self):
        return self.asientos['turista'] - self.turista_ocupados

    def asientos_disponibles_primera(self):
        return self.asientos['primera'] - self.primera_clase_ocupados

    def vender_asiento(self, clase):
        if clase == 'turista':
            if self.asientos_disponibles_turista() > 0:
                self.turista_ocupados += 1
                return True
            else:
                return False
        elif clase == 'primera':
            if self.asientos_disponibles_primera() > 0:
                self.primera_clase_ocupados += 1
                return True
            else:
                return False
        else:
            return False

    def eliminar_vuelo(self):
        if self.turista_ocupados + self.primera_clase_ocupados == 0:
            return True
        else:
            return False

        def reembolso(self):
            if self.primera_clase_ocupados > 0:
                reembolso_primera = self.primera_clase_ocupados * 203
            else:
                reembolso_primera = 0

            if self.turista_ocupados > 0:
                reembolso_turista = self.turista_ocupados * 75
            else:
                reembolso_turista = 0

            return reembolso_primera + reembolso_turista

    def total_recaudado(self):
        recaudado_turista = self.turista_ocupados * 75 * self.kms_vuelo
        recaudado_primera = self.primera_clase_ocupados * 203 * self.kms_vuelo
        return recaudado_turista + recaudado_primera


class Aeropuerto:
    def __init__(self):
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def mostrar_vuelos_destino(self, *destinos):
        for vuelo in self.vuelos:
            if vuelo.destino in destinos:
                print(f"Vuelo {vuelo.numero_vuelo} con destino a {vuelo.destino} de la empresa {vuelo.empresa}")

    def mostrar_vuelos_turista_disponible(self):
        for vuelo in self.vuelos:
            if vuelo.asientos_disponibles_turista() > 0:
                print(f"Vuelo {vuelo.numero_vuelo} con destino a {vuelo.destino} de la empresa {vuelo.empresa}")

    def mostrar_vuelos_programados_fecha(self, fecha):
        for vuelo in self.vuelos:
            if vuelo.fecha_salida == fecha:
                print(f"Vuelo {vuelo.numero_vuelo} con destino a {vuelo.destino} de la empresa {vuelo.empresa} programado para el {vuelo.fecha_salida}")

    def vender_asiento(self, numero_vuelo, clase):
        for vuelo in self.vuelos:
            if vuelo.numero_vuelo == numero_vuelo:
                if vuelo.vender_asiento(clase):
                    print(f"Se vendió un asiento de clase {clase} en el vuelo {numero_vuelo}")
                else:
                    print(f"No hay asientos disponibles de clase {clase} en el vuelo {numero_vuelo}")

    def eliminar_vuelo(self, numero_vuelo):
        for vuelo in self.vuelos:
            if vuelo.numero_vuelo == numero_vuelo:
                if vuelo.eliminar_vuelo():
                    self.vuelos.remove(vuelo)
                    print(f"El vuelo {numero_vuelo} ha sido eliminado")
                else:
                    print(f"No se puede eliminar el vuelo {numero_vuelo} porque tiene pasajes vendidos")
                    print(f"Se debe devolver un total de ${vuelo.reembolso()}")

    def mostrar_empresas_destino(self, destino):
        empresas = []
        for vuelo in self.vuelos:
            if vuelo.destino == destino:
                if vuelo.empresa not in empresas:
                    empresas.append(vuelo.empresa)
                    kms_vuelo = sum([vuelo.kms_vuelo for vuelo in self.vuelos if vuelo.destino == destino and vuelo.empresa == vuelo.empresa])
                    print(f"La empresa {vuelo.empresa} tiene {kms_vuelo} km de vuelos con destino a {destino}")

