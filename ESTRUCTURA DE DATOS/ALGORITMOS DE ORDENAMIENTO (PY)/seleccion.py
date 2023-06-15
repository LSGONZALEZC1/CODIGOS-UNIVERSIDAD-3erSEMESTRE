arr = [8,5,2,6,9,3,1,4,0,7]

print (arr)

for i in range (0, len (arr)):
    print(str(arr)+"prueba 0")
    minimo = i
    for j in range (i+1, len(arr)):
        print(str(arr)+"prueba 1")
        if arr[minimo] > arr[j]:
            minimo = j
    temp = arr[i]
    arr[i] = arr[minimo]
    arr[minimo] = temp

print (arr)