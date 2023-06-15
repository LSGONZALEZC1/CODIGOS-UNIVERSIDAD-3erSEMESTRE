usuarios = ["Ana", "Beto", "Carlos", "Diana"]
commits = [
    [
        # commits de Ana
        ("2021-10-01 10:15", "primer commit", "app.py", 10, -2),
        ("2021-10-02 11:20", "segundo commit", "test.py", 5, -1),
        ("2021-10-03 12:30", "tercer commit", "app.py", 8, -4)
    ],
    [
        # commits de Beto
        ("2021-10-01 13:45", "primer commit", "test.py", 7, -3),
        ("2021-10-02 14:50", "segundo commit", "app.py", 12, -6),
        ("2021-10-03 15:55", "tercer commit", "test.py", 9, -5)
    ],
    [
        # commits de Carlos
        ("2021-10-01 16:00", "primer commit", "app.py", 11, -7),
        ("2021-10-02 17:05", "segundo commit", "test.py", 6, -2),
        ("2021-10-03 18:10", "tercer commit", "app.py", 13, -8)
    ],
    [
        # commits de Diana
        ("2021-10-01 19:15", "primer commit", "test.py", 8, -4),
        ("2021-10-02 20:20", "segundo commit", "app.py", 14, -9),
        ("2021-10-03 21:25", "tercer commit", "test.py", 10, -6)
    ]
]

# lista de listas
lista = [usuarios, commits]

print(lista[1][0][0]) # imprime ('2021-10-01 10:15', 'primer commit', 'app.py', 10, -2)

# inicializar variables
max_commits = 0 # cantidad máxima de commits encontrada
max_users = [] # lista de usuarios con máxima cantidad de commits

# recorrer la lista de usuarios y la lista de commits al mismo tiempo
for user, user_commits in zip(lista[0], lista[1]):
    # obtener la cantidad de commits del usuario actual
    num_commits = len(user_commits)
    # comparar con el máximo encontrado hasta el momento
    if num_commits > max_commits:
        # actualizar el máximo y la lista de usuarios
        max_commits = num_commits
        max_users = [user]
    elif num_commits == max_commits:
        # agregar el usuario a la lista
        max_users.append(user)

# mostrar el resultado
print("El usuario o los usuarios con mayor cantidad de commits son:", max_users)
