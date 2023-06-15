# Se tienen los usuarios colaboradores de un repositorio de GitHub y de cada uno de estos se tiene 
# una lista de commit realizados, de los cuales se cuenta con su timestamp (en formato fecha y hora),
# mensaje de commit, nombre de archivo modificado, cantidad de líneas agregadas/eliminadas (puede ser positivo o negativo) 
# -suponga que solo puede modificar un archivo en cada commit que se haga-. Desarrollar un algoritmo que
# permita realizar las siguientes actividades:
# A)Obtener el usuario con mayor cantidad de commits --podría llegar a ser más de uno--
# B)Obtener el usuario que haya agregado en total mayor cantidad de líneas y el que haya eliminado menor 
#   cantidad de líneas
# C)Mostrar los usuarios que realizaron cambios sobre el archivo test.py después de las 19:45 sin importar
#   la fecha;
# D)Indicar los usuarios que hayan realizado al menos un commit con cero lineas agregados o eliminadas;
# E)Determinar el nombre del usuario que realizo el ultimo commit sobre el archivo app.py indicando toda 
#   la información de dicho commit;
# F)Deberá utilizar el TDA lista de lista
from datetime import datetime

class NodoLista(object):
    def __init__(self, info=None, sig=None):
        self.info = info
        self.sig = sig


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamano = 0


def insertar(lista, dato):
    nodo = NodoLista(dato)
    if lista.inicio is None or lista.inicio.info > dato:
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while act is not None and act.info > dato:
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamano += 1


def insertar2(lista, dato):
    nodo = NodoLista(dato)
    if lista.inicio is None or lista.inicio.info['empresa'] > dato['empresa']:
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while act is not None and act.info['empresa'] > dato['empresa']:
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamano += 1


def lista_vacia(lista):
    return lista.inicio is None


def eliminar(lista, clave):
    dato = None
    if lista.inicio.info == clave:
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamano -= 1
    else:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while actual is not None and actual.info != clave:
            anterior = anterior.sig
            actual = actual.sig
        if actual is not None:
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamano -= 1
    return dato


def tamano(lista):
    return lista.tamano


def buscar(lista, buscado):
    aux = lista.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux


def barrido(lista):
    aux = lista.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig

def obtener_usuarios_que_modificaron_test_py_despues_de_las_1945(lista):
    usuarios = set()
    actual = lista.inicio
    while actual is not None:
        commit = actual.info
        if commit['archivo'] == 'test.py' and commit['timestamp'].hour >= 19 and commit['timestamp'].minute >= 45:
            usuarios.add(commit['usuario'])
        actual = actual.sig
    return usuarios
def obtener_usuario_con_mas_commits(lista_commit):
    usuarios_commits = Lista()
    nodo = lista_commit.inicio
    while nodo is not None:
        commit = nodo.info
        usuario = commit['usuario']
        nodo_usuario = buscar(usuarios_commits, usuario)
        if nodo_usuario is None:
            insertar(usuarios_commits, (usuario, 1))
        else:
            nodo_usuario.info = (usuario, nodo_usuario.info[1] + 1)
        nodo = nodo.sig
        
    max_commits = 0
    usuarios_max_commits = []
    nodo = usuarios_commits.inicio
    while nodo is not None:
        usuario, cantidad_commits = nodo.info
        if cantidad_commits > max_commits:
            max_commits = cantidad_commits
            usuarios_max_commits = []
            usuarios_max_commits.append(usuario)
        elif cantidad_commits == max_commits:
            usuarios_max_commits.append(usuario)
        nodo = nodo.sig
    return usuarios_max_commits

def obtener_usuario_con_mas_lineas_agregadas_y_usuario_con_menos_lineas_eliminadas(lista):
    usuarios = {}
    actual = lista.inicio
    while actual is not None:
        commit = actual.info
        usuario = commit['usuario']
        agregadas = commit['agregadas']
        eliminadas = commit['eliminadas']
        if usuario not in usuarios:
            usuarios[usuario] = {'agregadas': 0, 'eliminadas': 0}
        usuarios[usuario]['agregadas'] += agregadas
        usuarios[usuario]['eliminadas'] += eliminadas
        actual = actual.sig
    usuario_con_mas_agregadas = max(usuarios, key=lambda u: usuarios[u]['agregadas'])
    usuario_con_menos_eliminadas = min(usuarios, key=lambda u: usuarios[u]['eliminadas'])
    return usuario_con_mas_agregadas, usuario_con_menos_eliminadas

def obtener_usuarios_que_hicieron_commits_con_cero_lineas(lista):
    usuarios = set()
    actual = lista.inicio
    while actual is not None:
        commit = actual.info
        if commit['agregadas'] == 0 or commit['eliminadas'] == 0:
            usuarios.add(commit['usuario'])
        actual = actual.sig
    return usuarios

def obtener_ultimo_commit_de_app_py(lista):
    ultimo_commit = None
    actual = lista.inicio
    while actual is not None:
        commit = actual.info
        if commit['archivo'] == 'app.py':
            if ultimo_commit is None or commit['timestamp'] > ultimo_commit['timestamp']:
                ultimo_commit = commit
        actual = actual.sig
    return ultimo_commit['usuario'], ultimo_commit

def obtener_lista_commits():
    lista = Lista()
    commits = [
        {'usuario': 'usuario1', 'archivo': 'archivo1', 'agregadas': 10, 'eliminadas': 5, 'empresa': 'empresa1', 'timestamp': datetime.strptime('2022-04-19 14:30:00', '%Y-%m-%d %H:%M:%S')},
        {'usuario': 'usuario2', 'archivo': 'archivo2', 'agregadas': 7, 'eliminadas': 3, 'empresa': 'empresa2', 'timestamp': datetime.strptime('2022-04-18 12:00:00', '%Y-%m-%d %H:%M:%S')},
        {'usuario': 'usuario3', 'archivo': 'archivo3', 'agregadas': 20, 'eliminadas': 15, 'empresa': 'empresa1', 'timestamp': datetime.strptime('2022-04-17 09:15:00', '%Y-%m-%d %H:%M:%S')}
    ]
    for commit in commits:
        insertar2(lista, commit)
    return lista

obtener_lista_commits()

lista2 = obtener_lista_commits() # función que obtiene la lista de commits

while True:
    print("Menu:")
    print("1) Obtener el usuario con mayor cantidad de commits")
    print("2) Obtener el usuario que haya agregado en total mayor cantidad de líneas y el que haya eliminado menor cantidad de líneas")
    print("3) Mostrar los usuarios que realizaron cambios sobre el archivo test.py después de las 19:45 sin importar la fecha")
    print("4) Indicar los usuarios que hayan realizado al menos un commit con cero líneas agregadas o eliminadas")
    print("5) Determinar el nombre del usuario que realizó el último commit sobre el archivo app.py indicando toda la información de dicho commit")
    print("6) Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        usuarios = obtener_usuario_con_mas_commits(lista2)
        print("Usuarios con mayor cantidad de commits: ")
        for usuario in usuarios:
            print("- " + usuario)
            
    elif opcion == "2":
        usuario_max_agregadas, usuario_min_eliminadas = obtener_usuario_con_mas_lineas_agregadas_y_usuario_con_menos_lineas_eliminadas(lista2)
        print("Usuario que agregó mayor cantidad de líneas: " + usuario_max_agregadas)
        print("Usuario que eliminó menor cantidad de líneas: " + usuario_min_eliminadas)
        
    elif opcion == "3":
        usuarios = obtener_usuarios_que_modificaron_test_py_despues_de_las_1945(lista2)
        print("Usuarios que realizaron cambios después de las 19:45 en test.py: ")
        for usuario in usuarios:
            print("- " + usuario)
            
    elif opcion == "4":
        usuarios = obtener_usuarios_que_hicieron_commits_con_cero_lineas(lista2)
        print("Usuarios que realizaron al menos un commit con cero líneas agregadas o eliminadas: ")
        for usuario in usuarios:
            print("- " + usuario)
        
    elif opcion == "5":
        commit = obtener_ultimo_commit_de_app_py(lista2, "app.py")
        print("Información del último commit en app.py: ")
        print("- Autor: " + commit.autor)
        print("- Fecha: " + commit.fecha)
        print("- Mensaje: " + commit.mensaje)
        
    elif opcion == "6":
        break
        
    else:
        print("Opción no válida. Intente nuevamente.")
        