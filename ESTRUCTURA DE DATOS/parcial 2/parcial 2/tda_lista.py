class nodoLista(object):
    info, sig = None, None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamano = 0


def insertar(lista, dato):
    nodo = nodoLista()
    nodo.info = dato
    if (lista.inicio is None) or (lista.inicio.info > dato):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while(act is not None and act.info > dato):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamano += 1

def insertar2(lista, dato):
    nodo = nodoLista()
    nodo.info = dato
    if (lista.inicio is None) or (lista.inicio.info['empresa'] > dato['empresa']):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while(act is not None and act.info['empresa'] > dato['empresa']):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamano += 1

def lista_vacia(lista):
    return lista.inicio is None


def eliminar(lista, clave):
    dato = None
    if(lista.inicio.info == clave):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamano -= 1
    else:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while(actual is not None and actual.info != clave):
            anterior = anterior.sig
            actual = actual.sig
        if(actual is not None):
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamano -= 1
    return dato


def tamano(lista):
    return lista.tamano


def buscar(lista, buscado):
    aux = lista.inicio
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux


def barrido(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig


def promedio_temperatura_humedad_mes(lista, estacion):
    """
    Recibe una lista con registros de temperaturas y humedades y una estacion.
    Devuelve un diccionario con los promedios de temperatura y humedad por mes de la estacion.
    """
    meses = {"01": [], "02": [], "03": [], "04": [], "05": [], "06": [], "07": [], "08": [], "09": [], "10": [], "11": [], "12": []}
    actual = lista.inicio
    while actual is not None:
        registro = actual.info
        if registro[0] == estacion:
            mes = registro[5][5:7]
            meses[mes].append((registro[1], registro[3]))
        actual = actual.sig
    promedios = {}
    for mes in meses:
        if len(meses[mes]) > 0:
            sum_temp = 0
            sum_hum = 0
            for registro in meses[mes]:
                sum_temp += registro[0]
                sum_hum += registro[1]
            prom_temp = round(sum_temp / len(meses[mes]), 2)
            prom_hum = round(sum_hum / len(meses[mes]), 2)
            promedios[mes] = (prom_temp, prom_hum)
    return promedios

    