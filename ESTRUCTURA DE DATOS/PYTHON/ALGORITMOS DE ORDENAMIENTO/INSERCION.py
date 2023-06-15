for i in range(1, len(lista)):
    actual=lista[i]
    indice=i
    
    while indice>0 and lista[indice-1]>actual:
        lista[indice]=lista[indice-1]
        indice=indice-1
    lista[indice]=actual
    
print(lista)


















print(' *binary_counting_sort** \n')


def binary_counting_sort(arr):
  min_val = min([song.año for song in arr])
  max_val = max([song.año for song in arr])
  count_arr = [0] * (max_val - min_val + 1)

  for song in arr:
    count_arr[song.año - min_val] += 1

  for i in range(1, len(count_arr)):
    count_arr[i] += count_arr[i - 1]

  sorted_arr = [None] * len(arr)
  for song in reversed(arr):
    sorted_arr[count_arr[song.año - min_val] - 1] = song
    count_arr[song.año - min_val] -= 1

  return sorted_arr


canciones = binary_counting_sort(canciones)

for cancion in canciones:
  print(f"{cancion.nombre} - {cancion.artista} - {cancion.año}")


def filter_songs_by_year_range(songs, start_year, end_year):
  sorted_songs = binary_counting_sort(songs)

  filtered_songs = []
  for song in sorted_songs:
    if start_year <= song.año <= end_year:
      filtered_songs.append(song)

  return filtered_songs


añoInicio = 1990
añoFinal = 2002

filtered_songs = filter_songs_by_year_range(canciones, añoInicio, añoFinal)

if filtered_songs:
  print('\nCanciones encontradas: entre los años', añoInicio, "y", añoFinal)
  for song in filtered_songs:
    print(song.nombre, song.año)
else:
  print('No se encontraron canciones en el rango de años especificado.')
print("-----------------------------------")