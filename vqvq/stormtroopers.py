# Crear dos objetos TablaHash con un tamaño arbitrario (puede variar según el número de elementos)
tabla1 = TablaHash(1000)
tabla2 = TablaHash(100)

# Recorrer la lista de Stormtrooper
for stormtrooper in stormtroopers:
  # Obtener los tres últimos dígitos del código como un número entero
  ultimos_tres = int(stormtrooper[-3:])
  # Obtener las iniciales de la legión como un número entero usando el código ASCII de las letras
  iniciales = ord(stormtrooper[0]) * 100 + ord(stormtrooper[1])
  # Insertar el Stormtrooper en la tabla1 según los tres últimos dígitos como clave y el código como valor
  tabla1.insertar(ultimos_tres, stormtrooper)
  # Insertar el Stormtrooper en la tabla2 según las iniciales de la legión como clave y el código como valor
  tabla2.insertar(iniciales, stormtrooper)

# Mostrar las tablas hash
tabla1.mostrar()
tabla2.mostrar()

# Definir los números de las misiones
mision_asalto = 781
mision_exploracion = 537

# Crear dos listas vacías para almacenar los Stormtrooper asignados a cada misión
asalto = []
exploracion = []

# Recorrer las claves de la tabla1
for clave in tabla1.tabla:
  # Si la clave coincide con el número de la misión de asalto, buscar el valor y agregarlo a la lista de asalto
  if clave == mision_asalto:
    stormtrooper = tabla1.buscar(clave)
    asalto.append(stormtrooper)
  # Si la clave coincide con el número de la misión de exploración, buscar el valor y agregarlo a la lista de exploración
  if clave == mision_exploracion:
    stormtrooper = tabla1.buscar(clave)
    exploracion.append(stormtrooper)

# Mostrar las listas de las misiones
print(f"Los Stormtrooper asignados a la misión de asalto son: {asalto}")
print(f"Los Stormtrooper asignados a la misión de exploración son: {exploracion}")

# Definir las iniciales de las legiones como números enteros usando el código ASCII de las letras
legion_ct = ord("C") * 100 + ord("T")
legion_tf = ord("T") * 100 + ord("F")

# Crear dos listas vacías para almacenar los Stormtrooper asignados a cada misión
custodia = []
exterminacion = []

# Recorrer las claves de la tabla2
for clave in tabla2.tabla:
  # Si la clave coincide con el número de la legión CT, buscar el valor y agregarlo a la lista de custodia
  if clave == legion_ct:
    stormtrooper = tabla2.buscar(clave)
    custodia.append(stormtrooper)
  # Si la clave coincide con el número de la legión TF, buscar el valor y agregarlo a la lista de exterminación
  if clave == legion_tf:
    stormtrooper = tabla2.buscar(clave)
    exterminacion.append(stormtrooper)

# Mostrar las listas de las misiones
print(f"Los Stormtrooper asignados a la misión de custodia son: {custodia}")
print(f"Los Stormtrooper asignados a la misión de exterminación son: {exterminacion}")
