"""
#Boleteria
vuelos={"HN012":{"ORIGEN":["San Pedro Sula"],"DESTINO":["Roatan"],"cASIENTOS":['A#1', 'A#2', 'A#3', 'A#4', 'A#5', 'A#6', 'A#7', 'A#8'],"PRECIOu":[165.7],"COSTOe":[1200.70]}
        ,"HN013":{"ORIGEN":["Comayagua"],"DESTINO":["Roatan"],"cASIENTOS":['A#1', 'A#2', 'A#3', 'A#4', 'A#5', 'A#6', 'A#7', 'A#8', 'A#9', 'A#10', 'A#11', 'A#12', 'A#13', 'A#14', 'A#15', 'A#16'],"PRECIOu":[278.9 ],"COSTOe":[4500.00]}
        ,"HN016":{"ORIGEN":["Tegucigalpa"],"DESTINO":["San Pedro Sula"],"cASIENTOS":['A#1', 'A#2', 'A#3', 'A#4', 'A#5', 'A#6', 'A#7', 'A#8', 'A#9', 'A#10'],"PRECIOu":[125.8],"COSTOe":[1245.69]}
        ,"HN019":{"ORIGEN":["Ceiba"],"DESTINO":["Roatan"],"cASIENTOS":['A#1', 'A#2', 'A#3', 'A#4', 'A#5', 'A#6', 'A#7', 'A#8', 'A#9', 'A#10', 'A#11', 'A#12', 'A#13', 'A#14', 'A#15', 'A#16', 'A#17', 'A#18', 'A#19', 'A#20'],"PRECIOu":[124.9],"COSTOe":[2550.54]}}

"""

vuelos = [["HN012","San Pedro Sula","Roatan",165.7,{'A#1':1, 'A#2':1, 'A#3':1, 'A#4':1, 'A#5':1, 'A#6':1, 'A#7':1, 'A#8':1, 'A#9':0, 'A#10':0, 'A#11':0, 'A#12':0, 'A#13':0, 'A#14':0, 'A#15':0, 'A#16':0, 'A#17':0, 'A#18':0, 'A#19':0, 'A#20':0}],
          ["HN013","Comayagua","Roatan",278.9, {'A#1':1, 'A#2':1, 'A#3':1, 'A#4':1, 'A#5':1, 'A#6':1, 'A#7':1, 'A#8':1, 'A#9':1, 'A#10':1, 'A#11':1, 'A#12':1, 'A#13':1, 'A#14':1, 'A#15':1, 'A#16':1, 'A#17':0, 'A#18':0, 'A#19':0, 'A#20':0}],
          ["HN016","Tegucigalpa","San Pedro Sula",125.8,{'A#1':1, 'A#2':1, 'A#3':1, 'A#4':1, 'A#5':1, 'A#6':1, 'A#7':1, 'A#8':1, 'A#9':0, 'A#10':1, 'A#11':0, 'A#12':0, 'A#13':0, 'A#14':0, 'A#15':0, 'A#16':0, 'A#17':0, 'A#18':0, 'A#19':0, 'A#20':0}],
          ["HN019","Ceiba","Roatan",124.9,{'A#1':1, 'A#2':1, 'A#3':1, 'A#4':1, 'A#5':1, 'A#6':1, 'A#7':1, 'A#8':1, 'A#9':1, 'A#10':1, 'A#11':1, 'A#12':1, 'A#13':1, 'A#14':1, 'A#15':1, 'A#16':1, 'A#17':1, 'A#18':1, 'A#19':1, 'A#20':1}]]

class Vuelo:

    def __init__(self,codigo_vuelo,origen,destino,precio,asientos):
   
        self.codigo_vuelo = codigo_vuelo
        #self.id_avion = id_avion
        self.origen = origen
        self.destino = destino
        self.precio = precio
        self.asientos = asientos
        self.asientos_disponibles= [k for k in asientos.keys() if asientos[k]==0]
        self.asientos_no_disponibles = [k for k in asientos.keys() if asientos[k]==1]


def carga(conj_vuelos):
    l = []
    for i in range(len(conj_vuelos)):
        l.append(Vuelo(conj_vuelos[i][0],conj_vuelos[i][1],conj_vuelos[i][2],conj_vuelos[i][3],conj_vuelos[i][4]))
       
    return l

def consecuencia(codigo):
    for i in range(len(bbdd)):
        if bbdd[i].codigo_vuelo==codigo:
            return bbdd[i]
   

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]} {opciones[clave][1]} ')


def leer_opcion(opciones,l):
    while (a := input('Opción: ')) not in l:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[1][2](opcion)


def generar_menu(opciones,l, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones,l)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    lista =[i.codigo_vuelo for i in bbdd]
    opciones = {
        1: ['Seleccionar un código de vuelo: ', lista, accion1]
       # '2': ('Salir', salir)
    }

    generar_menu(opciones,lista, '1')
   
bbdd = carga(vuelos)

def mostrar_menu2(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')
       
def leer_opcion2(opciones):
    l = [i for i in opciones.keys()]
    a = int(input('Opción: '))
    while a not in l:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion2(opcion, opciones,vuelo):
    opciones[opcion][1](vuelo)

def generar_menu2(opciones,vuelo):
        mostrar_menu2(opciones)
        opcion = leer_opcion2(opciones)
        ejecutar_opcion2(opcion, opciones,vuelo)
        print()
       
def accion1(o):
    vuelo = consecuencia(o)
    opciones = {
        1: ['Consulta asientos disponibles', consultaDis],
        2: ['Ocupa asiento', ocupa],
        3: ['Consulta precio', consultaP]
    }

    generar_menu2(opciones,vuelo)


def consultaDis(vuelo):
    print(vuelo.asientos_disponibles)
   
def leer_asiento_seleccionado(vuelo):
    a = input('Asiento: ')
    vuelo.asientos[a] = 1
    vuelo.asientos_disponibles.remove(a)
    vuelo.asientos_no_disponibles.append(a)
   

def ocupa(vuelo):
    print("Selecciona un asiento: ",vuelo.asientos_disponibles)
    asiento = leer_asiento_seleccionado(vuelo)
   
def consultaP(vuelo):
    print(vuelos.precio)


if __name__ == '__main__':
    menu_principal()

