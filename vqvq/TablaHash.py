# Definir una clase para la tabla hash
class TablaHash:
  # Inicializar la tabla hash con un tamaño fijo
  def __init__(self, tamano):
    # Crear una lista de listas vacías para almacenar los elementos
    self.tabla = [[] for i in range(tamano)]
    # Guardar el tamaño de la tabla
    self.tamano = tamano

  # Definir una función para calcular el índice de un elemento según su clave
  def hash(self, clave):
    # Usar el resto de la división entre la clave y el tamaño de la tabla
    return clave % self.tamano

  # Definir una función para insertar un elemento en la tabla
  def insertar(self, clave, valor):
    # Obtener el índice del elemento según su clave
    indice = self.hash(clave)
    # Insertar el elemento en la lista correspondiente al índice
    self.tabla[indice].append((clave, valor))

  # Definir una función para buscar un elemento en la tabla según su clave
  def buscar(self, clave):
    # Obtener el índice del elemento según su clave
    indice = self.hash(clave)
    # Recorrer la lista correspondiente al índice
    for elemento in self.tabla[indice]:
      # Si la clave del elemento coincide con la buscada, devolver el valor
      if elemento[0] == clave:
        return elemento[1]
    # Si no se encuentra el elemento, devolver None
    return None

  # Definir una función para eliminar un elemento de la tabla según su clave
  def eliminar(self, clave):
    # Obtener el índice del elemento según su clave
    indice = self.hash(clave)
    # Recorrer la lista correspondiente al índice
    for i in range(len(self.tabla[indice])):
      # Si la clave del elemento coincide con la buscada, eliminarlo de la lista
      if self.tabla[indice][i][0] == clave:
        self.tabla[indice].pop(i)
        return
    # Si no se encuentra el elemento, mostrar un mensaje de error
    print(f"No se encontró el elemento con la clave {clave}")

  # Definir una función para mostrar la tabla hash
  def mostrar(self):
    # Recorrer cada lista de la tabla
    for lista in self.tabla:
      # Mostrar cada elemento de la lista
      for elemento in lista:
        print(elemento, end=" ")
      print()
      
# Crear dos objetos TablaHash con un tamaño arbitrario (puede variar según el número de elementos)
tabla1 = TablaHash(1000)
tabla2 = TablaHash(100)
